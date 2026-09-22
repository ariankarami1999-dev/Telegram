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
<img src="https://cdn4.telesco.pe/file/vISDtCftnA20Twf5uc23E5YWsvus-NX9Fl1XBt3IuaK-lCAyQgU9itzXAsoZqITAjpCq3hsOexpKSyiQdKV6MTsenEBVnx8t-UMMh3Wr3oE_umV3hyotWM-ImHVDLGsIl7GPpLhrTTgQ6y-Eg3KZ7HQgKnwKruupHC6tyx8Rz03_sh5PHzyofSh2ZpCJazCXOp7Z_OdE40_n0DmoPnQhPCoF8B34YhHA-VsuseOBcn_V2I0P330I1C4lZcQ36KxgmlYmoHeAlQ3jGttBK_SwWoXoTHWtiQrvX2KB8d6lFts4QdUZzQeIM3QAluiRdDKu1laWRP4WPY_uuvaQLdSIvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 993K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-148711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8adae7aeaa.mp4?token=sB1g4LEtDkPbbyyLwSsXBEP-emu2wlQ_oYM09jtLeE5RMh4tQZo7LfAsgvoURUcvbUkZmVH3trV2zrVb9sac_F1SZm5dzDICb80Po8Hr8RWmf3T0Gs8KhXdO1IvOaOOC80LPG5aQkBzSy6UnuNkykxEXLCoVuJfRMHhLitGX0kfoYyidHoyROhpIx6TrT0xbhtgX_Ed2NoYe6Um8Yq_UDyx7gsc1gi0QCRKDUjaq3j3p9e5yAR3QkQQduzih3vjS-_on75WAq0LQe3_8dwdJmkRUAo7xwMhJazdNxyCieoSolMo8TL6yDS7FpjifMhUdzPWTSx7jnBi3_If1qIQGN3rFbtz95uxnz5Z3ygNR9zk2XVf7s8W8bPuXSNYw5a5pB7cf0v1P3fS0qoVJz-LzN-HIf2OXocME5-0SxjVzPhtr56oebzWv_O4LtGit6xG-xXraSDCp6izzcpgAWbOempD6GD0vkdkvaWYIhh-vViSOhDHkgfNGX9NukZKpYcjznqAnr9xGc2n6PAtWeO0XQ6j9JHBItG_OKy_1P3UQhJHOsgMD3Iuz4o_8newy00hyJlU8dtwNEKHQcxty5MUQPnLrvtIfjJJHKjUE_tBmUmmA41ZmUCNel0bpX8VB5fy9-JvGwo8hpv-RkamdGJQUBij-x4vVzpEieG7FJ85ioUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8adae7aeaa.mp4?token=sB1g4LEtDkPbbyyLwSsXBEP-emu2wlQ_oYM09jtLeE5RMh4tQZo7LfAsgvoURUcvbUkZmVH3trV2zrVb9sac_F1SZm5dzDICb80Po8Hr8RWmf3T0Gs8KhXdO1IvOaOOC80LPG5aQkBzSy6UnuNkykxEXLCoVuJfRMHhLitGX0kfoYyidHoyROhpIx6TrT0xbhtgX_Ed2NoYe6Um8Yq_UDyx7gsc1gi0QCRKDUjaq3j3p9e5yAR3QkQQduzih3vjS-_on75WAq0LQe3_8dwdJmkRUAo7xwMhJazdNxyCieoSolMo8TL6yDS7FpjifMhUdzPWTSx7jnBi3_If1qIQGN3rFbtz95uxnz5Z3ygNR9zk2XVf7s8W8bPuXSNYw5a5pB7cf0v1P3fS0qoVJz-LzN-HIf2OXocME5-0SxjVzPhtr56oebzWv_O4LtGit6xG-xXraSDCp6izzcpgAWbOempD6GD0vkdkvaWYIhh-vViSOhDHkgfNGX9NukZKpYcjznqAnr9xGc2n6PAtWeO0XQ6j9JHBItG_OKy_1P3UQhJHOsgMD3Iuz4o_8newy00hyJlU8dtwNEKHQcxty5MUQPnLrvtIfjJJHKjUE_tBmUmmA41ZmUCNel0bpX8VB5fy9-JvGwo8hpv-RkamdGJQUBij-x4vVzpEieG7FJ85ioUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی جانفداها از گرانی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/148711" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ایران‌ایر: هیچ ابلاغیه رسمی برای توقف پروازهای استانبول، باکو و نجف دریافت نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/148710" target="_blank">📅 13:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رویترز به نقل از مقام ایرانی: هیئت ایرانی حاضر در نیویورک، اختیارات کامل برای از سرگیری روابط دیپلماتیک با ایالات متحده را دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/148709" target="_blank">📅 13:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / عربستان سعودی فعالیت خط لوله نفت شرق-غرب را از سر گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/148708" target="_blank">📅 13:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روانبخش، نماینده مجلس: ما در جنگ با آمریکا هستیم، ممکنه پزشکیان رو تو نیویورک دستگیر کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/148707" target="_blank">📅 13:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الجزیره:ایران آماده هست که تنگه هرمز رو در عرض ۷ روز باز کنه اگه فشار نظامی آمریکا و متحدانش کم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148706" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الجزیره:ایران آماده هست که تنگه هرمز رو در عرض ۷ روز باز کنه اگه فشار نظامی آمریکا و متحدانش کم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148705" target="_blank">📅 13:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رویترز: چین میخواد در ازای توقف فروش سلاح آمریکا به تایوان برای فشار بر ایران کمک کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148704" target="_blank">📅 13:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبرگزاری ژاپنی کیودو به نقل از یک مقام ایرانی: ایران اعلام کرد در صورت اقدام آمریکا برای کاهش فشار نظامی، تنگه هرمز را ظرف ۷ روز باز می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148703" target="_blank">📅 13:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148702">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148702" target="_blank">📅 13:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148701">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">در روستایی کوچک، کدخدایی زندگی می‌کرد که بیشتر مردم از رفتار و تصمیم‌هایش ناراضی بودند. او مردی لجباز بود و اگر از کسی کینه‌ای به دل می‌گرفت، حتی به قیمت ضرر مردم هم کوتاه نمی‌آمد.
روزی یکی از اهالی پیشنهاد کرد برای نجات زمین‌های روستا، مسیر آب را تغییر دهند. کدخدا فقط به خاطر اختلاف قدیمی با او، پیشنهادش را رد کرد.
چند ماه بعد، خشکسالی آمد. زمین‌ها خشک شدند، دام‌ها از بین رفتند و خانواده‌های زیادی مجبور شدند روستا را ترک کنند.
مردم می‌گفتند: «خشکسالی بلای روستا بود، اما کینه‌ی کدخدا آن را به فاجعه تبدیل کرد.»
کدخدا سال‌ها بعد فهمید که گاهی یک آدم، وقتی قدرتش را با کینه و لجاجت همراه کند، می‌تواند تاوان اشتباهاتش را به جای خودش، از مردم بگیرد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148701" target="_blank">📅 13:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
منابع ایتایی: تا ته تو ماتحت دو کشور کمونیست کافر چین و روسیه فرو رفتیم و دمشون گرم و عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148700" target="_blank">📅 13:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مجری صداسیما: مردم میگن میدونیم گرونیا بخاطر جنگ و محاصره هست و مقاومت میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148699" target="_blank">📅 12:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وال‌استریت ژورنال: عربستان سعودی طی ماه‌ها تلاش کرده بود با تغییر مسیر محموله‌های نفتی، از عبور از تنگه هرمز اجتناب کند؛ اما اکنون ناچار شده است مجدداً محموله‌های نفتی خود را از همین مسیر عبور دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/148698" target="_blank">📅 12:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز: چین میخواد در ازای توقف فروش سلاح آمریکا به تایوان برای فشار بر ایران کمک کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/148697" target="_blank">📅 12:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
خبر لغو پروازهای ترکیش ایرلاین به ایران تکذیب شد؛ ترکیش ایرلاین ۸ ماه است به ایران پرواز ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148696" target="_blank">📅 12:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: آمریکا به‌دنبال ایجاد صندوق ۱۰ میلیارد دلاری برای زیرساخت‌های انرژی منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/148695" target="_blank">📅 12:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
زهران ممدانی: ترامپ تنها کسی است که می‌تواند نیویورک را درست کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148694" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cc58cbb1.mp4?token=XZSSPr3hVthpfTUbjdLYQwIJnNTu-dpoTxPABlbjsy0pTLqSNLlf6yI1jG-rD_5HDcZewtgs0SF6msUKcQlQPt70O8lKycLpbrBSVPAIwb2LXiGjS_PW_GWNqNODAH9OXCvTcof1njmrGpquzo2HjNdvZlJBC0ClS4396bAhKERFaupsTzFDJ93fhCCjbBpyc09lAeKacGN1K00nc0NKb19xBfRpS4h52403c4VFC5_tviYiBRVWJoyzTGYV1cHlMP3mw6sIEqcnip5Rh4c52G1UmfYCes039LHCar2vknETkdFJh4HthXLVDJCPD91B2KHzCHTdGOdVR1sbO_RRnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cc58cbb1.mp4?token=XZSSPr3hVthpfTUbjdLYQwIJnNTu-dpoTxPABlbjsy0pTLqSNLlf6yI1jG-rD_5HDcZewtgs0SF6msUKcQlQPt70O8lKycLpbrBSVPAIwb2LXiGjS_PW_GWNqNODAH9OXCvTcof1njmrGpquzo2HjNdvZlJBC0ClS4396bAhKERFaupsTzFDJ93fhCCjbBpyc09lAeKacGN1K00nc0NKb19xBfRpS4h52403c4VFC5_tviYiBRVWJoyzTGYV1cHlMP3mw6sIEqcnip5Rh4c52G1UmfYCes039LHCar2vknETkdFJh4HthXLVDJCPD91B2KHzCHTdGOdVR1sbO_RRnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز صبح تو محمدشهر کرج شوهر سابق یه زنه میاد تو مغازه زنه که کافه داشته با کلت به زنه و خودش شلیک میکنه زنه مُرده خودشم
فوت کرده.
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148693" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ec0706b8.mp4?token=RLI54TbIFsZxerIosZPV_WZFnirXsHX4m1JD_lcBIBe994GdnKjafyotubCoV0etn9vY3t2yoDLy2-AUHZj4AVKLqeyHw2jWS9y8ebj6wZoyAMohkdm45hHMVko4AQYPCf6WadMKPPZAwkVpiDCVTE7YAjzqf9bxrQUS3e_oYx6ZWzI-LDUG9UxXO2-mjNTKycdZ34mTHMCIbLEXm8S9laAkZ4fXHyEtnVPKamfsQOW8Z1KYNZPButZjxIWtWRikiH-yJQw6rnfNDkakdv88ZFTt5rGuANpovinS7QWw6lGLCSqEGGfyq8XI7J-uvhJeLZgD0FaeRGFLXkc9A7nbkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ec0706b8.mp4?token=RLI54TbIFsZxerIosZPV_WZFnirXsHX4m1JD_lcBIBe994GdnKjafyotubCoV0etn9vY3t2yoDLy2-AUHZj4AVKLqeyHw2jWS9y8ebj6wZoyAMohkdm45hHMVko4AQYPCf6WadMKPPZAwkVpiDCVTE7YAjzqf9bxrQUS3e_oYx6ZWzI-LDUG9UxXO2-mjNTKycdZ34mTHMCIbLEXm8S9laAkZ4fXHyEtnVPKamfsQOW8Z1KYNZPButZjxIWtWRikiH-yJQw6rnfNDkakdv88ZFTt5rGuANpovinS7QWw6lGLCSqEGGfyq8XI7J-uvhJeLZgD0FaeRGFLXkc9A7nbkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو جدید کاوه آهنگر زمان در راه پاسارگاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148692" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اردوغان خواستار لغو حق وتو در شورای امنیت سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148691" target="_blank">📅 12:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نخست‌وزیر قطر: خاورمیانه به یک «چارچوب امنیتی منطقه‌ای جدید» نیاز دارد که ایران را هم شامل شود
🔴
جنگ ایران باید برای منطقه به منزله یک «زنگ بیدار باش» باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148690" target="_blank">📅 12:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCX2XLg9Q9gEZNsEzKBngfp_CvDFLUG9Sn_rKAcWHsvMpe8ruUVSOAGK0n8d6sp6yZkmxpvCNMgiivLkBBcugi1OiTe4rvxC0gCnHh3FZ7AdQo69KwcIXFD4wgfPZwwKWo_19GaJbzoNLOoLK_ZV-SY3MsYyF26OYw2meQHsXP-Ds5jUEoQivSb0AqgxaRiCygMC34xdbUQYiugW3PhEZsEixnZX8O9Gzjq-E7Eiy--gQh7UytTcrs_EEhqvCe-ly5UodvVnUCZ8XCbf1DthKoyqgRch6SZt5zUZQBpUSa4mSNjADvzMcN9wOnK4EQjPpAkzFElwuUH-FdmDj6oPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق زیبا کلام: مشکل ما با تندروهای خودمان است که ۳۶سال همه قدرت را بدست آورده بودند و حالا سرسوزنی حاضر به ازدست دادن آن نیستند ولو به قیمت به خاک سیاه نشستن نود میلیون ایرانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148689" target="_blank">📅 11:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر نیرو: صنعت برق از نقاط قوت ماست، قطعیا و مشکلات بخاطر جنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148688" target="_blank">📅 11:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75ab8b39a.mp4?token=Ij3vfXTG5hbsYQ-dCFXhyptrEntwERFOc4m8kRDKUJu6ncTa5Sx1Y4154yuFHXjELizP2bpMo2IXQ2VOGCKj2sKbKyMI1xw1VwaR5j84pi18p-agnq5T7i9W2GTDqTx7AIK19A8SotZZ8FHrJ5NOCeSl9dgq98NILNPkuaUnJQwRgUPIVM4ARATn55V8EbLqWg9grmCE4gJsOYORdWSkFvQlQkRPqxQQr1n1ZWu-_YMhYWwdO8oKg13In6d0u0p8IYVcTwRz7KDLtWS-PxVcDAYZw0Dvu1WZs-6dfv6JzxzGqyGG1fPcLend_OjhH3hmdDMJO9qeSQBGXefBbThGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75ab8b39a.mp4?token=Ij3vfXTG5hbsYQ-dCFXhyptrEntwERFOc4m8kRDKUJu6ncTa5Sx1Y4154yuFHXjELizP2bpMo2IXQ2VOGCKj2sKbKyMI1xw1VwaR5j84pi18p-agnq5T7i9W2GTDqTx7AIK19A8SotZZ8FHrJ5NOCeSl9dgq98NILNPkuaUnJQwRgUPIVM4ARATn55V8EbLqWg9grmCE4gJsOYORdWSkFvQlQkRPqxQQr1n1ZWu-_YMhYWwdO8oKg13In6d0u0p8IYVcTwRz7KDLtWS-PxVcDAYZw0Dvu1WZs-6dfv6JzxzGqyGG1fPcLend_OjhH3hmdDMJO9qeSQBGXefBbThGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت موبایل یک پاکبان در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148687" target="_blank">📅 11:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e76cebe8.mp4?token=mXe-Mrjp1E_IDFsoHjOZUaDy8TTusPVZecamrBg-g9FOZlp4Q99kwrA6n5nXXPfxfymq1XOkK8VgJjdWLw6Ki5Fst5C7vBTcnILKBALOuJaQr8gg9az8GqajUPMljYJ9cHKpWpk-_S-AbEcB4HsznYlV4LEpLWi-OZJjm60zkBDVip-uzXcCdu0d_MZngSjip_4X3m20VaejvtWlV_9NxUzgS-XLRPaYInCDMatfY-WPUrvjPG4tlfgXCp1ZPrmpE07f7sVQh4QIT7yWib7YmoDrDlN7TynEFHHI_tqtMFBviBVPUD4eWaiA7phEZ9Am-xBRsyIaage5EbHZL0PTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e76cebe8.mp4?token=mXe-Mrjp1E_IDFsoHjOZUaDy8TTusPVZecamrBg-g9FOZlp4Q99kwrA6n5nXXPfxfymq1XOkK8VgJjdWLw6Ki5Fst5C7vBTcnILKBALOuJaQr8gg9az8GqajUPMljYJ9cHKpWpk-_S-AbEcB4HsznYlV4LEpLWi-OZJjm60zkBDVip-uzXcCdu0d_MZngSjip_4X3m20VaejvtWlV_9NxUzgS-XLRPaYInCDMatfY-WPUrvjPG4tlfgXCp1ZPrmpE07f7sVQh4QIT7yWib7YmoDrDlN7TynEFHHI_tqtMFBviBVPUD4eWaiA7phEZ9Am-xBRsyIaage5EbHZL0PTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی پالایشگاه نفتی بزرگ روسیه در حمله پهپادی اوکراین
🔴
رسانه‌های اوکراینی در پی حمله پهپادی اوکراین به روسیه، تصاویر و فیلم‌هایی از پالایشگاه نفتی بزرگ در شهر «سامارا» واقع در جنوب شرقی روسیه منتشر کردند که در آتش می‌سوزد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148685" target="_blank">📅 11:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هم اکنون ، پرواز جنگنده‌ها در آسمان بغداد و چند استان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/148684" target="_blank">📅 11:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxWOxgYDUkgJRFaqPT0T-7vP_NRO0XAgRnlQHHY_hFa9-TJR4-nRU4czt4OCP9itevn3BlMdWqXxfkSVsGmuZBpPO5owVP6La1VAuzypjHKf443O6hKQOq-KAnDl-raCig42dCJjItMiG83ZHn6dBUTrbC3uuYsbsJCu09iDd_aHuP51ZkgGuSuilYvJDM2_wzPZwphTRMTrgk_5chT5sLnFlk9gAdWcypip1Yft7-HRJZFqr8kKARKyPsCkQFYDi03egOXVfrYY1kfW4vwxvVCaKfMVDUbYSRuELCfDZvvN5a39CL9wdWSQ4Eh3buy5s8Hq64dc-yQAyuyyOOGz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای امور خارجه ترکیه، عربستان سعودی، مصر و پاکستان در نیویورک با یکدیگر دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148683" target="_blank">📅 11:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
چین: با تحریم‌های آمریکا علیه شرکت‌های هواپیمایی ایران مخالفت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148682" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148681" target="_blank">📅 10:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148680">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148680" target="_blank">📅 10:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148679" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پزشکیان: دشمن در تلاش است تا تمام راه‌های هوایی‌ و زمینی را بر ایران ببندد تا ما را مجبور به تسلیم کند ولی نمی‌داند ما تسلیم زورگویی دشمنان نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/148678" target="_blank">📅 10:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8gUqwQ_GEsZ2Nr1_RJEuRwteHUmf4lJbnRRj1__KZCFbQzP3AXJorOlGkQsDitZk9amUU0CuC32ft5l_GpfEIMsoJrLWEnh3OmLo7ZhGPa5PHu1OGg-bTw6jwTKWfyHhAr12qgipC7HHCHUDcZZX_bwTpPI_U7pOSL6a5qeuUFcH_0Gal_OYI4aUgHcCQ1diqId8kvsa6_KCOSIMUHpKY9we5hUS1gX0UEPyg74hqsMloopam6tX3299IAQilRtb-MRC3HhnUQgPVhSMOZah5yQxZ2-wAB5eG7qO0FMPkFa2k7GO3QjNxXJE2-WKbYU09bZnQJwL3te-77hY7PRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان
:
هم‌پیمانان ترامپ از کشورهای حوزه خلیج فارس، روز سه‌شنبه در نیویورک با او دیدار خواهند کرد.
🔴
نگرانی‌های آن‌ها دوگانه است: اول، ترس از تشدید تنش‌ها؛ و دوم، ناتوانی در محافظت از شهروندان آمریکایی.
🔴
آن‌ها قبلاً ترامپ را متقاعد کردند که از یک اقدام نظامی بزرگ خودداری کند، و این بار، از اینکه به یک جنگ عمیق‌تر کشیده شوند، در حالی که واشنگتن به دنبال راهی برای خروج از این وضعیت است، نگران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148677" target="_blank">📅 10:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
‏ ۴ ایراد شورای نگهبان به طرح مهریه
🔴
‏ سخنگوی شورای نگهبان در گزارش جدید خود ۴ ایراد و ابهام اصلی این شورا به طرح اصلاح قانون مهریه را تشریح کرد.
🔴
‏۱. صرفاً نظارت الکترونیکی برای بدهکاران کافی نیست؛ ممکن است بدهکار توان پرداخت داشته باشد اما از پرداخت خودداری کند.
🔴
‏ ۲. تعیین سقف ۱۴ سکه برای ضمانت اجرای وصول مهریه محل ایراد شرعی شورا قرار گرفته؛ معیار باید توانایی یا ناتوانی واقعی بدهکار باشد، نه تعداد سکه.
🔴
‏ ۳. ضوابط نظارت الکترونیکی، محدوده رفت‌وآمد و نحوه برخورد با تخلفات و عذرهای موجه باید دقیق‌تر مشخص شود.
🔴
‏ ۴. درباره امکان بازگرداندن حقوق مالی، اموال و هدایای دریافت‌شده از سوی زوجه نیز ابهاماتی وجود دارد.
🔴
‏ شورای نگهبان مصوبه را برای رفع ایرادات شرعی و ابهامات حقوقی به مجلس بازگردانده و تأکید کرده ضمانت اجرای مهریه باید بر مبنای توانایی واقعی پرداخت بدهکار تنظیم شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148676" target="_blank">📅 10:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7950eaf4f4.mp4?token=DsjWr6dArOlvl9X4b15ClBKxmPB2e_12kQlgzFE4bPjTrS9N8mC7jnuHUds_sGakqPnstPcktizcSJNLMXlqlb2Uho-A-0x3cr2c4XyEcF66LdAkGaTJLdUCkVgpwIz5pcLZEzU0pXnHnZoStDlm7gMkOg13pAqWHXnr5jBQqQqo5QUkdzjLuPmhtOmlJgX61iydScZ1Z6LhsD_2Wk9Ld0eAGazOZyOR6cw6zjsuGdT0XsSok8b-MewC-eZ7O3EC8tgBsPIxC7g4mywPmMf77MzWFczbLPmL3Y5QvXXbq1xK6N6ihSoSqAt3wD9ukXMjHN8YoHgNErgJ-FSVZJ1bWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7950eaf4f4.mp4?token=DsjWr6dArOlvl9X4b15ClBKxmPB2e_12kQlgzFE4bPjTrS9N8mC7jnuHUds_sGakqPnstPcktizcSJNLMXlqlb2Uho-A-0x3cr2c4XyEcF66LdAkGaTJLdUCkVgpwIz5pcLZEzU0pXnHnZoStDlm7gMkOg13pAqWHXnr5jBQqQqo5QUkdzjLuPmhtOmlJgX61iydScZ1Z6LhsD_2Wk9Ld0eAGazOZyOR6cw6zjsuGdT0XsSok8b-MewC-eZ7O3EC8tgBsPIxC7g4mywPmMf77MzWFczbLPmL3Y5QvXXbq1xK6N6ihSoSqAt3wD9ukXMjHN8YoHgNErgJ-FSVZJ1bWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ در مراسم افتتاحیه محل فرود بالگرد  جدید کاخ سفید ،محل فرود را افتتاح کرد  اما سخنان او به دلیل صدای بلند هلیکوپتر کاملاً نامفهوم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148675" target="_blank">📅 10:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b46fd9e5.mp4?token=MIUEoGQRepvaHrmkdgfOeNzM16dctt0vP_e8iLXxC-vvqpkWVh65bzqeEGCPKzimqq8SgAHXEmBZaNtWmC3y9J3_Ho6ZecC_PbT_asa8_P8KBt9SjQ3L4gFdq518VOt59TxtnN8lse_z8C8RW-5MlBSKS-bjAVe0Tw6SahTYmP_hGTJw-WGKKsThAxUV0fy5agC8W6CKiR6QcGQmrvx31HIB1Tg_vFS9IKHBfOdX6nsI1Kay6fgfNEsUH03ysWRj6ETtt_wAoewCLjTO8HuDg-M1VqayGsibcpF77VyntRrx1JuuFyx3-obkfIrPbqq3IJ9rgnedf3X7AquZsu9pFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b46fd9e5.mp4?token=MIUEoGQRepvaHrmkdgfOeNzM16dctt0vP_e8iLXxC-vvqpkWVh65bzqeEGCPKzimqq8SgAHXEmBZaNtWmC3y9J3_Ho6ZecC_PbT_asa8_P8KBt9SjQ3L4gFdq518VOt59TxtnN8lse_z8C8RW-5MlBSKS-bjAVe0Tw6SahTYmP_hGTJw-WGKKsThAxUV0fy5agC8W6CKiR6QcGQmrvx31HIB1Tg_vFS9IKHBfOdX6nsI1Kay6fgfNEsUH03ysWRj6ETtt_wAoewCLjTO8HuDg-M1VqayGsibcpF77VyntRrx1JuuFyx3-obkfIrPbqq3IJ9rgnedf3X7AquZsu9pFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پنتاگون ۶ فایل جدید مربوط به اشیای ناشناس پرنده(UFO) را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148674" target="_blank">📅 10:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2pFolFRwmAq9BRRB2k5tPaMGcZYJCTDC4SNmyYXip3CdGQvXgs27ENx7rv-5mTYFwnvR1OnDu1E0FqEfSKYasoZMSKTjthsJPPUeFVvzPgA8fvfbXCQuI4e5t_1leP2xaRw23fO3f_-y1yBDjZveAsF5aseM42MSydz7F6Ikldlgu1Q6y79XkHjjJOixi8d6QJyT4Gmqp5aOuPcepkKPLelYH58XC5OtfSZlLKg1PgO6rYiBgWK8NuLn2_eJ9XrEYFDXDN-zTmUCqEbJ0Bm3jKmabq-7JLT-TwrEubDd9AaYp5_nnUrTtn62ZlAHsfeH5CR-oZw9BsuNMrzf_tR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بریتانیا مجوز عملیات سوخت‌رسانی هوایی برای حمایت از عربستان در یمن را صادر کرد
‏
🔴
اندی برنهام، نخست‌وزیر بریتانیا، به نشریه «پولیتیکو» اعلام کرد مجوز انجام یک مأموریت سوخت‌رسانی هوایی توسط نیروی هوایی سلطنتی این کشور صادر شده است.
‏
🔴
بر اساس این گزارش، هدف از این عملیات، پشتیبانی از هواپیماهای نیروی هوایی عربستان سعودی در انجام «اقدامات دفاعی» علیه جنبش انصارالله در یمن عنوان شده است.
‏
🔴
این مأموریت با استفاده از یک فروند هواپیمای سوخت‌رسان «وویجر» متعلق به نیروی هوایی سلطنتی بریتانیا انجام خواهد شد و قرار است در روزهای آینده آغاز شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148673" target="_blank">📅 10:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVAoKCd7VgGuzXQ2adC54bD5bSyhdakbnRqSujaoGG7e6UdeHvBmBNwxjSlKFvrnjraXHuardY5pYvaOZkhUNYogoN7UGFxzrr_HdD9jd-dbbzRkbtO-lZbV4RirF7dUG1c-cUMteMAsewmJwOGg6SCtKYpHPpjGNc596KaGflKvE7zpvZL_moydLDHLs7pU97OeP3clOdDyHXoSZcxpu4BdqxHhR188IbrBEDSLWJY-luwlJ0u0Wu_0ozbZjVodWIMjfJygA8WSZIRmWBwwFTK6J-hEi7rIeZNRrTKvG_-x8uEzAeLpWrQZkMv4KzcIYw7qBPwGFnTSsg1xOkvyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی نفت برنت 102 دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148672" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزرای خارجه گروه G7 حملات حوثی‌ها در یمن و علیه عربستان سعودی را محکوم کردند و از ایران خواستند ارسال سلاح برای این گروه را متوقف کند.
🔴
«ما حملات مستمر شورشیان حوثی در یمن و علیه عربستان سعودی را به‌شدت محکوم می‌کنیم.»
🔴
«این الگوی خطرناک تشدید تنش می‌تواند تجارت بین‌المللی را تضعیف کرده و موجب بی‌ثباتی جهانی شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148671" target="_blank">📅 10:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گروه هفت: اقدامات ايران که قابل اعتراض هستند، یک الگوی خطرناک از تشدید تنش را نشان می‌دهند و هشداری برای وخیم‌تر شدن بیشتر درگیری‌ها هستند
🔴
اقدامات ايران تهدیدی برای تضعیف تجارت بین‌المللی و ایجاد بی‌ثباتی اقتصادی جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148670" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
طبق گزارش رویترز، ایالات متحده قصد دارد یک پایگاه نظامی متعلق به دوران جنگ سرد را در منطقه نارزارسوآک در جنوب گرینلند مجدداً احیا کند و همچنین یک پایگاه دیگر را در منطقه مسترسویک در سواحل شرقی، در چارچوب توافق آتی با دانمارک و گرینلند، ایجاد کند.
🔴
نارزارسوآک در گذشته محل پایگاه نظامی "بلویی وست وان" متعلق به ایالات متحده بود که در دهه 1950 تعطیل شد. در حال حاضر، منطقه مسترسویک توسط گروه ویژه "سیروس" متعلق به ارتش دانمارک، که متشکل از واحدهای نیروهای ویژه است، مورد استفاده قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148669" target="_blank">📅 09:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qz8V56PNoAu1LV5N8pilRk0b1RsXlhOCgjjNzCAfwVgwF0f7eDTfqRs9Dtlsenz3gr7iNYhdqdlGOsv2XXEKedCjvzF6wTd4BGIRq5AI4ZCy8Axx-BE5M_LQWPS6ufIJm_6u2NAEsbRR6Z31rMJohnVTnHUXWoQb5Wfb6k6PugaEs645aMw2zMAM5kX5LDwTvjpxTj7d-Lt0hV404-j2w-nwOOZtXmnA969mz66KxvVhMign73bMvqOUaJomsXUG1EFnnyj_q6FOjfuYV_exLFFCxovZVHOxEgp866zGnb17TUHZ2QG-iKDJAQectPTRJWQInHm4rTMjYZDMEBs22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت ترامپ طبق نظرسنجی NBC NEWS:
🔴
۵۶ درصد مخالف
🔴
۴۱ درصد موافق
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148668" target="_blank">📅 09:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee843d670d.mp4?token=VEd3mFLueRMlq9p8Nd1F3TAfRsyIgLwUIFlYv15iXBpuo7cK4AIxOY048BO3QzTk9LOLZhKqcxXltQd0xnlZOGEFf7Pz0-BEJbugc9uPXFXR4H9WOt76MmqGaZnl4iHU8DEROCBg7aIw8bcwIT_l1w43SZeDkjrx-u71hhU1wClZWxgrePlqr0Da042JTg5WApcAgeTNabcmGTJtDZhDmkaQQLf_-EnFGCezA1lqYfDpTOL62CWE1MVC0q1uzM1fa31iwN_vmgrBt8Gf-78OxwxNNN-qLQvPpY5POGgPEnBcmbITig5qJvwojSndp7oKaXiPi02taEk3VJm39t5ozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee843d670d.mp4?token=VEd3mFLueRMlq9p8Nd1F3TAfRsyIgLwUIFlYv15iXBpuo7cK4AIxOY048BO3QzTk9LOLZhKqcxXltQd0xnlZOGEFf7Pz0-BEJbugc9uPXFXR4H9WOt76MmqGaZnl4iHU8DEROCBg7aIw8bcwIT_l1w43SZeDkjrx-u71hhU1wClZWxgrePlqr0Da042JTg5WApcAgeTNabcmGTJtDZhDmkaQQLf_-EnFGCezA1lqYfDpTOL62CWE1MVC0q1uzM1fa31iwN_vmgrBt8Gf-78OxwxNNN-qLQvPpY5POGgPEnBcmbITig5qJvwojSndp7oKaXiPi02taEk3VJm39t5ozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد کشتی فله‌بر با پرچم پاناما با  کشتی ماهیگیری چینی  در سواحل سنگاپور
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148667" target="_blank">📅 09:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03301281f.mp4?token=MiTPfMtDNPVuAdZUZEee_y2n7fAHhoSCTloUNUqzJyRZ6D4mbyQ-8Cj5ZIepsf2xF1mg3PsEm5Vv24SnbXmXhjgdUelYpCU4gyYw7R25Jb4vCBj0HHOeEXUw04-YMfuS5mkuhwwW64YC1zFb-Mr3wSNylkoiXqzsk3Wm-Lraw2M6cKZlF5hx9DXRI0Nzg6UnOdd6uinNwc6MCsX_eDRSWqGshTiQd9X8vyJ4KtZFBrCa6XvHOC9AFyuOeCAreFXifN6cg-nV59KF2nN67whSbIUWWYbYn-g2k8kHlVrAkLte0CotES16DCqwjKNYnrpUe7pSF8UhiA_hpt8Fjk_LjHYcSrlXPcJdt8RqQc9k2637Fg4_lz7B1nnLNg2JDZ9O89VaGmwNtWotnP81BDYTQl8jl8MOIwMhdRTyHGraarIX2LmWj7j1NBkglOJZ9q3_QSTTf3TKvfHQMYwqTLKPWAY0kJyQoJq4DRgRGteUNHotBOSQRK-C-IKO67MGBzPcYnUtXAjsPcMSnHXhaUD-ySJeFAQ9RtEb6JE3BmytNjkRfeDTQw8PS-EINPhJYrHWZs5Cgg33rApKhKb77u6k9bNRI48TQqZ2keTiOTUtwDS48fwA_yD1pOrHGb5RD4BtMN5T1TzVqQBGnVV3lWEg9cv8OqaCtnheG_zELoxSBJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03301281f.mp4?token=MiTPfMtDNPVuAdZUZEee_y2n7fAHhoSCTloUNUqzJyRZ6D4mbyQ-8Cj5ZIepsf2xF1mg3PsEm5Vv24SnbXmXhjgdUelYpCU4gyYw7R25Jb4vCBj0HHOeEXUw04-YMfuS5mkuhwwW64YC1zFb-Mr3wSNylkoiXqzsk3Wm-Lraw2M6cKZlF5hx9DXRI0Nzg6UnOdd6uinNwc6MCsX_eDRSWqGshTiQd9X8vyJ4KtZFBrCa6XvHOC9AFyuOeCAreFXifN6cg-nV59KF2nN67whSbIUWWYbYn-g2k8kHlVrAkLte0CotES16DCqwjKNYnrpUe7pSF8UhiA_hpt8Fjk_LjHYcSrlXPcJdt8RqQc9k2637Fg4_lz7B1nnLNg2JDZ9O89VaGmwNtWotnP81BDYTQl8jl8MOIwMhdRTyHGraarIX2LmWj7j1NBkglOJZ9q3_QSTTf3TKvfHQMYwqTLKPWAY0kJyQoJq4DRgRGteUNHotBOSQRK-C-IKO67MGBzPcYnUtXAjsPcMSnHXhaUD-ySJeFAQ9RtEb6JE3BmytNjkRfeDTQw8PS-EINPhJYrHWZs5Cgg33rApKhKb77u6k9bNRI48TQqZ2keTiOTUtwDS48fwA_yD1pOrHGb5RD4BtMN5T1TzVqQBGnVV3lWEg9cv8OqaCtnheG_zELoxSBJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: «من از آن دسته افرادی هستم که واقعاً معتقدم رسانه‌های خبری باید صادق باشند.
🔴
مشکل برخی از این رسانه‌ها — نمی‌گویم بیشترشان، بلکه برخی از رسانه‌های بزرگ‌تر — این است که واقعاً سازمان خبری نیستند.
🔴
مشکل این نیست که آنها گرایش لیبرال دارند. من این موضوع را نمی‌پسندم، اما با آن کنار می‌آمدم.
🔴
مشکل این است که آنها عملاً به بازوی تبلیغاتی جریان چپ تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148666" target="_blank">📅 09:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a410023fe.mp4?token=Qa-c-lVhqcn7YyxQ4o8WmMf5sc-pnfyhQ39TG2s_1Ui53Frba_Gl_xf6KW8sW-ND7PVJqxn8mqJ4sG7rBfGp_aS0v7A9OOckVJJNVVwYE6mL02bj3z_NuynZKOSIqhWN91jVQHJCI3BUhKygNE7RW43MemVr0BSM-0FQuu80TPnRNMBzgF-Frqv459qOVaMV649sp-aaNNdpqmjZeCij69uDsLWCAcDqvIa4KsnqsJNzJSZDQMUIQn-j6P3OLextO0fUoCeFBTnkDUBv-0_i7vI7gefgDYmdplzZOtJ7GyxyLlrOr3ooZMm6MQ1kyb_YzTcOXxakL2yxFqGg9ehEOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a410023fe.mp4?token=Qa-c-lVhqcn7YyxQ4o8WmMf5sc-pnfyhQ39TG2s_1Ui53Frba_Gl_xf6KW8sW-ND7PVJqxn8mqJ4sG7rBfGp_aS0v7A9OOckVJJNVVwYE6mL02bj3z_NuynZKOSIqhWN91jVQHJCI3BUhKygNE7RW43MemVr0BSM-0FQuu80TPnRNMBzgF-Frqv459qOVaMV649sp-aaNNdpqmjZeCij69uDsLWCAcDqvIa4KsnqsJNzJSZDQMUIQn-j6P3OLextO0fUoCeFBTnkDUBv-0_i7vI7gefgDYmdplzZOtJ7GyxyLlrOr3ooZMm6MQ1kyb_YzTcOXxakL2yxFqGg9ehEOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : «من معمولاً برای سخنرانی‌هایم از قبل آماده نمی‌شوم. ترجیح می‌دهم از صمیم قلب صحبت کنم.
🔴
به نظرم وقتی حرف‌ها را با کلمات خودتان بیان می‌کنید و واقعاً از صمیم قلب صحبت می‌کنید، صحبت‌ها خیلی بهتر منتقل می‌شوند تا اینکه اجازه دهید شخص دیگری سعی کند کلمات را در دهان شما بگذارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148665" target="_blank">📅 09:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af891e99e.mp4?token=TSAZHOCKwrN5uuTr1T0g46ggi4Zwm45rypMxapt6ZwUh56Mtqiv73voDXi5kzfSaVxNjOPR7Az-cOjibzNyMb_P-VrdqqI3IlXWf6lQQlsDQdbB5dUqZ1r5BbU2uTzR7ZULVovOmg7XxZmxoTvhc7d4vVMuU-J6TiZtJDuFN_pgBvksHyfe1IgfqWkyPvTMsP8ecrXjAfYsFRfEHjNes5LwHpLyCvprsC5eO4Rls-tFS5dn4rMsnl_U4vZr5IY7xQv22Jp4mtrxi7zZMmiStO6ygcz2KhKl-dXyUTCHUbseeM53xSAtTxQPkbz25rjrjm65NRkzaiwWkbfL0irrNnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af891e99e.mp4?token=TSAZHOCKwrN5uuTr1T0g46ggi4Zwm45rypMxapt6ZwUh56Mtqiv73voDXi5kzfSaVxNjOPR7Az-cOjibzNyMb_P-VrdqqI3IlXWf6lQQlsDQdbB5dUqZ1r5BbU2uTzR7ZULVovOmg7XxZmxoTvhc7d4vVMuU-J6TiZtJDuFN_pgBvksHyfe1IgfqWkyPvTMsP8ecrXjAfYsFRfEHjNes5LwHpLyCvprsC5eO4Rls-tFS5dn4rMsnl_U4vZr5IY7xQv22Jp4mtrxi7zZMmiStO6ygcz2KhKl-dXyUTCHUbseeM53xSAtTxQPkbz25rjrjm65NRkzaiwWkbfL0irrNnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، جولانی، برای شرکت در مجمع عمومی سازمان ملل در شهر نیویورک حضور دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148664" target="_blank">📅 08:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ماکرون: کاهش تنش در بازارهای انرژی را با ترامپ بررسی کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148663" target="_blank">📅 08:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148662">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی عراقچی و دبیرکل سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148662" target="_blank">📅 08:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148661">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پزشکیان دقایقی پیش تهران را به مقصد نیویورک ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/148661" target="_blank">📅 08:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148660">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اردوغان: روابط ترکیه و آمریکا با ترامپ شتاب تازه‌ای گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/148660" target="_blank">📅 08:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148659">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d971e74d.mp4?token=EnjGJt6xA83lrScgJZLNQmw3MvSST58fhcRtdfZebjVvGlW4nnfMRcTr-cQP1mlszQN2P3KreSyclK1c69Hn-WDr5bCJA7KXjSZKijGNG3wIbTRkE1wvM0Tl8eh76nJf772ekFDJNX97j-qG6le3q1d2RAi9BapJD2OYWNxpPvAjnJrf06Xhrh7tgFpHH9WrZn55a86H9Ec4zN61RCvdL9asgcBbLsZOwTYOH5MhS-Ll0T1ivn-zNx6QH7paW5Az7WzGbRnaGQOEi6z0IF6Ei2fc2I0eTQEmxzZyO384XGdiRR_fcrMPVmAWk0YvolydyMyB28GjZClOvrcZUvj84A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d971e74d.mp4?token=EnjGJt6xA83lrScgJZLNQmw3MvSST58fhcRtdfZebjVvGlW4nnfMRcTr-cQP1mlszQN2P3KreSyclK1c69Hn-WDr5bCJA7KXjSZKijGNG3wIbTRkE1wvM0Tl8eh76nJf772ekFDJNX97j-qG6le3q1d2RAi9BapJD2OYWNxpPvAjnJrf06Xhrh7tgFpHH9WrZn55a86H9Ec4zN61RCvdL9asgcBbLsZOwTYOH5MhS-Ll0T1ivn-zNx6QH7paW5Az7WzGbRnaGQOEi6z0IF6Ei2fc2I0eTQEmxzZyO384XGdiRR_fcrMPVmAWk0YvolydyMyB28GjZClOvrcZUvj84A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز آزمایشی جنگنده نسل ششم چین
🔴
‏جنگنده نسل ششم جی۳۶ چین دوباره در پروازهای آزمایشی در روشنایی روز مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/148659" target="_blank">📅 08:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148658">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
👈
تیتر جدید روزنامه تلگراف:
ترامپ در حال برسی منفجر کردن کل ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/148658" target="_blank">📅 07:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148657">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJnL8PiiNi5pT1X9voHIHU4QyMfZZ8ofCufKicUYLEaPuiO97tygqqyBvhLrHD7r49JG1TOjWtdXr-nHaOUqs52A9OJ1COLbs2feOHCLzNM7q9wWhneZ6ncSjLszFUFkvdmXksD3cFIjCMlmfgjqxMgzhAyKG37hKqRnt4Z7ZQB0agGIgPFJkq1yEnm9CK2SjoniWQ_dI7eBcJPwdeOF_6Rm7P-UAT4k12FzL9tPyxVPlinTOr_BaxhKdqS8YTZnd03z_NBIRUSUtMO9PlDbViII3zw9E6vexCWMDtsvHgVRCCvr1QQ2ph4KWl0W4lMF1TW9ZBe8WZX3OuCxphMA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید از راه‌اندازی «Trump TV» خبر داد و اعلام کرد این شبکه به‌صورت ۲۴ ساعته و ۷ روز هفته پخش خواهد داشت؛ جزئیات بیشتری ارائه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/148657" target="_blank">📅 07:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148656">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طلا و دلار فردا منفجر میشه
⁉️
همین حالا چک کنید
👇
https://t.me/+WWnSixAo9FA4MDZk
https://t.me/+WWnSixAo9FA4MDZk
تحلیل آتنا
:طلا و دلار از فردا با صعود شدید مواجه میشه
⚠️
‌‌</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/148656" target="_blank">📅 01:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148655">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmeZn6m4Pqx_C2_UtFZEhWGosjQztEJKX5FEZs0bOnDRVf8l2RRns0NWutjXiSn2lxyK307mZ6hL8QydkBmQ9TUhvWmqv8pyZiDYe1zvJcEbJyJhYbmu-9K00hCIWx6BgIMHlEh05rTJOuSUk0SN3LJBW-_jO-EtB91sevzWL02RtWcDpqiIXox4Wi7ualhYQyKFJwVFC_N80vdToW8IJW75L7myKbck23vCybhsyNyWQiQ2LZ0XyUXVnDAB7qcEZYWt_aPqvMthdsqiQzMiOTlQviDdXrXmnYOR_ChJgUUN05xIjrMmmAREMgoV1lpL0nDv4ZZnB7qS3jkcxoko0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت 99 دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/148655" target="_blank">📅 01:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148654">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff8dd60b7.mp4?token=UkNwLfb0l_EQUzxbRwMRVSCxc9b0sVKWmzhqxCQbmtY4dK1c4l-8nzr1JtKfTugXvNwVu_gI7CJ5ylgSwKpiZE0UE9TvWaQafxcagAY9qHm8JEjxm0CMNStBQW8RwxS1t0UOVcE9t2F9bKvK6VT6yCpZnkfLcgcwfJdgz87BLQ8M7i7sB-r_Cdcoiaz6PePqYO_r-S3Pd1besEJR-VqT9YmJjymSGtMIcrR5eT4c5Pf-b_IfAFvCxCpnfr-138UslJCKvAWiqKvWFBcLr6UKKMgbnXS_5SSIb_D_2K7RaoijrdPwmXYuNS02_cl13gctshlPmp28ed-xn8H8Jx0b_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff8dd60b7.mp4?token=UkNwLfb0l_EQUzxbRwMRVSCxc9b0sVKWmzhqxCQbmtY4dK1c4l-8nzr1JtKfTugXvNwVu_gI7CJ5ylgSwKpiZE0UE9TvWaQafxcagAY9qHm8JEjxm0CMNStBQW8RwxS1t0UOVcE9t2F9bKvK6VT6yCpZnkfLcgcwfJdgz87BLQ8M7i7sB-r_Cdcoiaz6PePqYO_r-S3Pd1besEJR-VqT9YmJjymSGtMIcrR5eT4c5Pf-b_IfAFvCxCpnfr-138UslJCKvAWiqKvWFBcLr6UKKMgbnXS_5SSIb_D_2K7RaoijrdPwmXYuNS02_cl13gctshlPmp28ed-xn8H8Jx0b_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت وزیر خزانه‌داری آمریکا: ما می‌دونیم پول‌ها و دارایی‌های شبکه حکومت ایران کجاست؛ حتی حساب‌های خارج از کشور و خونه‌های خیلی گرونشون رو هم شناسایی کردیم. می‌خوایم فشار اقتصادی رو شدیدتر کنیم، حساب‌ها و دارایی‌های مرتبط رو مسدود کنیم و سراغ شبکه‌های مالی سپاه هم بریم.
🔴
در مورد چین هم میگه با وجود اختلافات آمریکا و چین، سر موضوعاتی مثل جلوگیری از هسته‌ای شدن ایران و باز بودن تنگه هرمز نقاط مشترکی دارن.
🔴
یعنی پیام اصلیش اینه: «می‌دونیم پول و دارایی‌هاتون کجاست و می‌خوایم از نظر مالی بهتون فشار جدی وارد کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/148654" target="_blank">📅 01:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا:
با چین درباره ایران مذاکرات پشت‌پرده داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/148653" target="_blank">📅 01:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
هم اکنون قدرت‌نمایی جنگنده های ارتش بر فراز آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/148652" target="_blank">📅 01:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: از دست ایران بسیار عصبانی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/148651" target="_blank">📅 01:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: ایران سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/148650" target="_blank">📅 01:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: ایران اوضاع بسیار بدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/148649" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6810089eb9.mp4?token=TcdPoLoB90y8ihFJ0iDafGLKTx3iEfs-wGYI9Et2XUgfnCrS0xkL1-v3i7-CUkzuPMRFnbjA2Gs2ZWQVTE1yNUyqARwrlbWzDqVzI2nIHZtfeJiNVcVuH8WCHuArVkQpMuiZEJBsrwbUPUYS0PaV-6r9Ap9p_YUTxIV2CNZIQ8yyKyrZeZwwLODak_SZb8nB5JZOTk4Uof6rnUpDBft-bcEVp1jwkPJU0pywG3M3fKzwQ3dUb7wtuaTKRj6S479iDDg_SiUYKsT2fXBeincEeUZJBL0Xz9zscWynooSnjTJ-huNNmOlW1g8A48aXGoD5CocuMxsj7Fkc539h6ssUJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6810089eb9.mp4?token=TcdPoLoB90y8ihFJ0iDafGLKTx3iEfs-wGYI9Et2XUgfnCrS0xkL1-v3i7-CUkzuPMRFnbjA2Gs2ZWQVTE1yNUyqARwrlbWzDqVzI2nIHZtfeJiNVcVuH8WCHuArVkQpMuiZEJBsrwbUPUYS0PaV-6r9Ap9p_YUTxIV2CNZIQ8yyKyrZeZwwLODak_SZb8nB5JZOTk4Uof6rnUpDBft-bcEVp1jwkPJU0pywG3M3fKzwQ3dUb7wtuaTKRj6S479iDDg_SiUYKsT2fXBeincEeUZJBL0Xz9zscWynooSnjTJ-huNNmOlW1g8A48aXGoD5CocuMxsj7Fkc539h6ssUJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
«گفتند قرار است من را تحریم و بایکوت کنند، اما هیچ‌وقت این کار را نکردند.
🔴
به این همه پوشش رسانه‌ای الونیوز نگاه کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/148648" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: امروز جلساتی درباره ایران برگزار خواهم کرد، و اوضاع به خوبی پیش نمی‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/148647" target="_blank">📅 00:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRDL3NuU_2BJVERvA-y1xGzvcYTQiH9QasbKy_wOSHPc_jPmmzcOc9csH9MnGnT8cS_KQhvhS8hL6z_CvolmhnUKYZdvY8RS_OGKrd50bVRkV_nisXSrewIi4zQlaBcIV7XmxoVcJhzwT2usdlD-_IY4KMi4BudJTDjNgcwDxaO0lIJFZYt6rL-RtcaMYd2upkoEm7ASl7PmW1_R7aqJcos9w7Si3oFddPHzf75CnXQ3muZbmpRWSjkQqLXj252BWez4kmY7ZiBOJZekLEpOoDnGY9OtrRJjWe0XA26X6t8mkIOVNy6im5Af75Bh-xEddXxv_tdUl9rEtEC1Wccjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: از تاریخ ۲۱ سپتامبر تاکنون، ۱۱۰ فروند شناور در چارچوب محاصره تغییر مسیر داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/148646" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوووووووووووووووووری</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/148645" target="_blank">📅 00:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوووووووووووووووووری</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/148644" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
👈
کانال 12 عبری:
ارتش اسرائیل برای تشدید تنش‌ها با ایران در حال آماده‌سازی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/148643" target="_blank">📅 00:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pigq1IBqdXdaDaUwT190uCErtD8rFR_Kt50Uk_pBDw9ILRCiRfaP6MLeJPCS-t2XvUEGHwemFIG2cAwtrX36l2qwB64-CIFecKFMpAaKLGqhOF1C46AvOIpNwlCzy6yygxeB39xUS8e8S6Pbh4AYHWO9uvzPdwMSG6qvVRZbGmmGSV15egFGPPmaTF1I6PIfJw16tOHiT1n3lrCn7XuKnCxVUte9hExNd1J0JiL-9AhSKxKG3G6JQUMRuB6CC7MTcF5p11QutUo9p2-QYeTdLrf6rERhnTCLoSdlattqCP4lStE3sYpvEVCn-nh5fG4Wm_rQyJK9kaDJ5r3axn-OoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز امنیت دولت لهستان برای ساکنان چند منطقه در استان لوبلین، در نزدیکی مرز اوکراین، هشدار صادر کرد و درباره حمله هوایی روسیه به خاک اوکراین هشدار داد.
🔴
نیروهای هوایی لهستان نیز از ساکنان خواستند هوشیار باشند و منتظر اطلاعیه‌های بعدی بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/148642" target="_blank">📅 00:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgEx1LZWhneuAtMfbMHAFY091wBjtHaS-Yf85E_mm7mok_wSWRxPBstMqmQ5maQ_lJ-CkRuA3KIqgKhgjOr3VLLoazasXPs8QOXp5pBZTPbulf-H6QC9rnGdGIo7fsdIlxOqSnX2qGFeXP2JrNV8lpugSyFj-aWZnQ0v6Dn-QEbxYt6sonUQhDi4afTg4ic6mg3qHfL_VmpRVx71bCOHokGHqIhq4f626u3vs7jxt9zZM70WYEkqLbom4T3RmLxE-WvXwyeLRDD6ceBIsWHafp0h_QaRcmNEGadXEmCgCnwNkc7yZH1byAePudwkss9Ym3Cn5woh_kr3sZyXjDqYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه نگار اماراتی: اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه.
🔴
آماده باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/148641" target="_blank">📅 00:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نخست وزیر عراق در گفت‌وگو با نیویورک تایمز: گروه‌های مسلح عراقی، تحویل سلاح‌های خود را آغاز خواهند کرد و انتظار می‌رود این روند تا 30 ژوئن 2027 به پایان برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/148640" target="_blank">📅 23:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پراندلی، تحلیلگر بازار جهانی: ترامپ با یه مصاحبه و جمله احتمال توافق، قیمت نفت رو از ۱۰۷ به ۹۷ دلار رسوند. عربستان هم به دنبال بازگشایی خط لوله شرق-غربه و با این تفاسیر دیگه نیازی به تنگه هرمز نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/148639" target="_blank">📅 23:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عراقچی برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/148638" target="_blank">📅 23:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b889a0ca.mp4?token=tsLpL5Nt26GPpBeqt9npygJgBxecFONR1VnCVz6qT1KX4hcKA_5U4-ZogT3Ycme13cOjbrsUFFZeuTHDXsPFv1CaeXF4FAZhD3i_q4sYkqckvu6C2mwiLyr89fFltVseXFvbTd3ntQJx-juvU4rLW_JtT4jas7xMZvPvRGU-o7ZlapbtvQf23C0OzKOhr0KDwsDkjuA0-NxDgkF-81UAZL3O-KNQ0lPV8L9GYQPr04G8hvRFr7Gtua-0lCTrTzfYMAEeXk6OwNR1DBeCYHiCmgMzMEwIguM6dzcJJk36yrxdfXyHvfvOZWkRVucxLOw-qA777Slvl9FdrAu33vUJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b889a0ca.mp4?token=tsLpL5Nt26GPpBeqt9npygJgBxecFONR1VnCVz6qT1KX4hcKA_5U4-ZogT3Ycme13cOjbrsUFFZeuTHDXsPFv1CaeXF4FAZhD3i_q4sYkqckvu6C2mwiLyr89fFltVseXFvbTd3ntQJx-juvU4rLW_JtT4jas7xMZvPvRGU-o7ZlapbtvQf23C0OzKOhr0KDwsDkjuA0-NxDgkF-81UAZL3O-KNQ0lPV8L9GYQPr04G8hvRFr7Gtua-0lCTrTzfYMAEeXk6OwNR1DBeCYHiCmgMzMEwIguM6dzcJJk36yrxdfXyHvfvOZWkRVucxLOw-qA777Slvl9FdrAu33vUJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عربستان در مرز با عراق بالون جاسوسی مستقر کرد
‏
🔴
گارد مرزی عربستان اقدام به نصب و به پرواز درآوردن یک بالون ویژه رصد و جاسوسی در نزدیکی مرزهای عراق کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/148637" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MneblKTDBj78--QGByNe39AROiupPJ2Amwx-_pZVBMqW9ZUQ9Diei2m-uDsRlrQCeg7z5dnTRF2LOuXK3J6Md9HPp3V_PaqJg5gGDvDFLiCqq7hl1-zvRatGor5k0TPwkrcJ98_69-kPeoIqbvbZ0kN8GgSyMnuY-JvLivik7S-QP62ipBS8wuuOO_PABdEiLr1muCV3NMqkKViSXO3ucSojtWhJB7BHQGoWaVSQH521SbvwYVH7niPJ64PE5lBMWC-u-fmcVRuD8__vGiQ4nMJHP6II3kDJdKcMQRUQMjjyW6o4LVz6gn73qTQsC8u8NQ275Azr2OLE-KyZNxpdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : در حال حاضر که در شهر نیویورک هستم، در راه یکی از مکان‌های مورد علاقه من در جهان، یعنی کاخ گریسی (Gracie Mansion) هستم. من سال‌ها در آنجا وقت گذرانده‌ام، با شهردارهای عالی، شهردارهای متوسط و شهردارهای نامناسب.
🔴
دیدن اینکه اکنون چه شکلی شده، جالب خواهد بود. من توسط شهردار مامدانی دعوت شده‌ام. مشتاقانه منتظر آن هستم. بیایید دوباره شهر نیویورک را عالی کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/148636" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟡
طلای ۱۸ عیار: 23,707,200  تومان
🔻
حباب طلا ۱۸ عیار: -1.78% ______________________
🟡
طلای دست دوم: 23,391,128  تومان
🟡
تتر: 228,800  تومان
🟡
یورو: 265,010  تومان
🟡
هر گرم نقره: 511,230  تومان
🟡
سکه بهار آزادی: 230,130,000  تومان
🟡
سکه امامی: 233,980,000  تومان
🟡
نیم…</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/148635" target="_blank">📅 23:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5YWaaQ-vNZLi4MRssbChAp-vypSM57q_eNs8FQA_K7d_dac3KucZKxQdghNG9zYh4ryF8WbKEVgAMgPnvPY-JZWMwZveNtOz0SU5Gb3Fof4YTUV0050kWb7rmETrmHFjO-76u7B6wGrGQLbfgFGeNb_MSQOLgp6cKv_ITcxhyGE3hQTxXkifBeDQDFjMHhWsD-nVvRISEvizF_8Xwf4Z37dOFARuykgbiSnZM2gIVsSKPXKWjOpM_uaF6mqa64NWj9OF20Ow0ytansnR1MY5VEy3snC_SMVbBRZEknXj-csfYZejVrTBwgMahW_rrNxUzxcKd6WDIId2pzv1_VpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی خبرنگار نزدیک به حکومت: ونس اخیرا در جلسه‌ای گفته که وضعیت ترامپ در انتخابات آتی آمریکا خوب نیست؛ باید کاری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/148634" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROTeq89gkNCTH4JqD3wwf86vffU9FergJ5nPOnSHUGvFAWx3orQMusJaxowoMf3-VAG7tbCnRs5jiEsc1CEezXuENWo5MZ1rW4ASe-x6rSn6ost2ShvE-0tnrscJ-uJwDpj7JGSGtgE2LmsaTfZvmUW88_s_MB_KYYi8yTvegsRUqrlCJV07hGbU2Gq8ksnUg623zgXRYz4fWp7U4Wa6KTRHv1dacbIDlfFE4eiK8T9MmPG_TWWvd9qfgB1Xu47oHWcDv2i-B1OSzaU1Nt2oGyRG4HiXmEhAZ67gc1Lmka3v-lgElvgK4Pum-530Y2QaCruGxRQTyC8SY2Jo3BwjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همانطور که انتظار می‌رفت، شبکه خبری جعلی CNN، نشریه Politico (که باید ۸ میلیون دلار کمک مالی که دولت آمریکا برای زنده ماندن آن‌ها پرداخت کرده است را پس بدهد!) و MSNOW (که قبلاً با نام MSDNC شناخته می‌شد)، شکایت کرده‌اند تا به کاخ سفید و به من، رئیس جمهورتان، دسترسی پیدا کنند.
🔴
آن‌ها یک قاضی بسیار خوب (از نظر خودشان) انتخاب کرده‌اند، مردی که در گذشته به نفع جیم آکوستا حکم صادر کرد، که اکنون به نظر می‌رسد از سطح زمین ناپدید شده است. نام این قاضی، تیم کلی است، و متاسفانه، او توسط "ترامپ" منصوب شده است
🔴
به عبارت دیگر، تقریباً بدون شک و، همانطور که معمول است، ما به این حکم اعتراض خواهیم کرد، زیرا رسانه‌های خبری جعلی و نشریاتی که فقط مطالب منفی منتشر می‌کنند و با انتشار داستان‌های دروغین و افتراآمیز، امنیت ملی ما را به خطر می‌اندازند، نباید به مهم‌ترین دفتر در سراسر جهان، یعنی دفتر بیضی (Oval Office)، دسترسی داشته باشند. این دفتر باید با احترام، وقار و منزلت رفتار شود، نه اینکه توسط افراد بی‌ارزش و درجه سه، آلوده شود، افرادی که عمداً مطالب را تحریف، دستکاری و تخریب می‌کنند.
🔴
تقریباً هر داستانی که درباره من یا هر چیزی که به من مربوط می‌شود، منفی، نادرست و در بسیاری از موارد، خطرناک برای کشور ما است. مهم نیست که دستاوردهای من چقدر بزرگ باشند، آن‌ها آن‌ها را بی‌اهمیت جلوه می‌دهند و تحقیر می‌کنند.
🔴
حقیقت این است که من در هفت ایالت کلیدی، در رای عمومی، در کالج انتخاباتی (۳۱۲ به ۲۲۶) و در اکثر شهرستان‌های آمریکا با ۸۶ درصد آرا پیروز شدم، و با این وجود، گزارش می‌شود که ۹۴ درصد تبلیغات درباره من منفی است. با وجود چنین رسانه‌های کج‌رو و فاسد، چگونه من می‌توانستم با این اختلاف فاحش پیروز شوم؟ زیرا رسانه‌ها هیچ اعتبار ندارند، و این یک چیز بسیار بد برای کشور ما است. چرا من باید به چنین افرادی "دسترسی" بدهم؟ شاید قاضی کلی بتواند این موضوع را توضیح دهد.
🔴
در هر صورت، من وظیفه دارم برای موفقیت و امنیت کشورمان مبارزه کنم. اخبار جعلی یک تهدید برای دموکراسی است، و من هر کاری را که لازم باشد انجام خواهم داد تا اطمینان حاصل کنم که ایالات متحده آمریکا شکوفا شود. "آمریکا را دوباره بزرگ کنیم!
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/148633" target="_blank">📅 23:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArXQOyW8MPYUmUVvrHYy9btr3ESHMJF5hgbQi8vGI3pyIy3xNqd3wT7GBC1ih2v8tQwaqhAEfTS4qEC4yR-6Pqr9_lJFZNTEXytRQ6jfsfbf85_gHkYVnoT8LGA0MDuMPs7JrEArSuby11c5_TS-vZ4R2v7FptkfGL7Zx6QXYTok4_qpwBXvPWs89kdDDLH19wQzmk1VznfEQS4LDd7Tz-GyWCWDgG2kWXh6muKKKJrMTH72wrxmQvdO-I2qHndAjLynWFWHXPdStPSwRkjjOMmeLJbmR5HfjtbtnuyADcnCvxsm_BmqA_KNDahIiZMogMi83-Bhmdvp3sGaJ1ybCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/148632" target="_blank">📅 23:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه چین راجب ایران: چین فقط اقداماتی رو انجام میده که به صلح کمک کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/148631" target="_blank">📅 23:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تیراندازی در لس آنجلس از پشت بام به سمت مردم
🔴
یک مظنون پس از تیراندازی به سمت مردم از پشت بام ساختمانی در جنوب لس آنجلس، در ایالت کالیفرنیا در کشور آمریکا  توسط پلیس بازداشت شد.
🔴
نیروهای امدادی سه مصدوم را به بیمارستان انتقال دادند.
🔴
پلیس چندین خیابان اطراف منطقه را بسته است و از ساکنان خواست از این منطقه دوری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/148630" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fan7UNzIIUgwtfCqzFrvnz7VisBAcTMufcOUllF7LkTwFhN3rxyFMtL8it-38i6_9OBXMbb6MZOl-kYkD0BCDRULzDLNlimzD43mmqCQ-IkG-vx7-Fml2CVk0uqfWpTetNT-WLvmY7yW1iYJLI_LnDBEqAexKRR24yW6oINDLGYnXlCwux4_YLHVu1img3dRHh63YVZjtLTNJGhduk63Ac65SIa9Gty664l6JaMje4TbVxDwp3WNdRDyQ07HBVYl1BFjZAZDfL4O0OsMOt3F1hcTEkp2IvrZSqY5qOvwEKRcFu3rccImPiezdZuKeJ6B3QFgVnNN90f7F-6h0GmSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعتراف یک زن ۲۷ ساله مشهدی به قتل شوهرش:
بهم محبت نمیکرد منم با همکاری دوست پسرم کشتمش و تو حاشیه روستا جسدشو مخفی کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/148629" target="_blank">📅 23:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPsPAcZer6H2IG6quUsSARuSWuv7F7tHLHJ9IF8DEZ9hb-rJQWf50mRo-r0hoGFWzDsMhD8mTzZv-aU_nYQgXSru-UPbKH3vCOTq4QsKsfdhg7rnlKrFWHhPhvA_TcS6pMpANgviTbfWYWEFzgnTWVNeIQpCzc21aYHRt5HI-x76DnYw1vBZp7-yUbYTDkQwf0NoyjDZt8P4ZPqNh6Z1Gx4AfnezADSeVBHGiZjJ80jVOrw5SpKXvvUuHWfigvC6g0WrhW7ZIAheQQ8jtFouf26DiobZJ-9fMuhbhr8qoUx4-eM4db1aT8WinrxmbM5ZfR8YTwmly9zi7cxP6al9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDZclSXi3Wr-_E-qN1PtEWEw6A14AXvLZGyXWPSfPFZ1IDR-X-fnI8MuOaEYONVlwhfdBxA5hLhe4FZbc6kaijuunJNdVG2zKXoYFg2tnTfkVSeaK6wetI9tYWlfDyK87I-YOWMk7BIxaqS5xB9v8DZYFP5tHlI-yD99IMqjRTyqcJxLyhpTYwzHjyYiyk7drDbYOuTIIn0BzHrJ11TRDEhsvGqkSuTbBdCdZIE3T0Rgu8SlqEI2vzNWHVkzE2xYpYB1wycpiIp8vevmjVb7GEPJxoDcuaRCkYIdilguPZa2XAIO7LYlui78H7Dv3VrMRlTt4a8dn1P6w3GzGk0e3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل دقایقی پیش حملاتی را علیه مناطق شرقی شهر غزه انجام دادند
🔴
این اقدام پس از آن صورت گرفت که یک خودروی مهندسی متعلق به نیروهای دفاعی اسرائیل در شمال غزه مورد اصابت یک دستگاه انفجاری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/148627" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه چین و آلمان درباره وضعیت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/148626" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148625">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/525f2c026e.mp4?token=nxCz3-Pzm-pYizLN_5tNG5Lb_n7FjNR2djlYU37CtJ89JJzCGH-CJKwPZEtFukMFxyzW2c7ic7FHgRwAX9SqrfEv-9Ygc7iJUGCUkwXew3dqg5GXslTNr_3E-V9B2PKmqBrUKKAIQZwmlfypRu9mvVdeyJavT8riYHfOXR-Fy2AJu7b0fO5UDRVm09_KPn9PiXwZEUzuz4-Ul09GoG8pgLPPN8EoZeguG5oZD-m-f4LPFW4gplU6ByxlGocaWA39gXcXb_ODGEEw0IwRv7rg3iaLcjByENFpus0qbobvHj9MP_5B9u2nrFi-3218e9wvpqCAXXEXYkFeYQLqfpvEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/525f2c026e.mp4?token=nxCz3-Pzm-pYizLN_5tNG5Lb_n7FjNR2djlYU37CtJ89JJzCGH-CJKwPZEtFukMFxyzW2c7ic7FHgRwAX9SqrfEv-9Ygc7iJUGCUkwXew3dqg5GXslTNr_3E-V9B2PKmqBrUKKAIQZwmlfypRu9mvVdeyJavT8riYHfOXR-Fy2AJu7b0fO5UDRVm09_KPn9PiXwZEUzuz4-Ul09GoG8pgLPPN8EoZeguG5oZD-m-f4LPFW4gplU6ByxlGocaWA39gXcXb_ODGEEw0IwRv7rg3iaLcjByENFpus0qbobvHj9MP_5B9u2nrFi-3218e9wvpqCAXXEXYkFeYQLqfpvEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/148625" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148624">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bafb25ee5e.mp4?token=tjzfW9kAhNlqLba3NAFqn-4Ztx27cGP_05ZieGLJG13JwlI8r0RZ1y-T0eqZlLix7J9Wxg4tvvCc3kap6s5isst7aS5VA4NQqfhxyuFcOxhGNhg2QeiFSt9ognCIkFHvGatPzt0V3f2paQyhsdOPE5gmTqE6UNhOdnhrt-r1QfHnR7xLRYEnv63_tMZoaHRLWMq7QWmnSAKw2uYkAodvaN5tGkff3VhO7jGY98hYfQw3f1ItyVRC4FlTnUzL0fcd2HXcMV62aiij0FwSSlTGHBsDTZDMlAB6B8iH9fDzG31vE1MhY5zYJ25cnmCFU14-JmkoXUCZp0y5o_4JLIdOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bafb25ee5e.mp4?token=tjzfW9kAhNlqLba3NAFqn-4Ztx27cGP_05ZieGLJG13JwlI8r0RZ1y-T0eqZlLix7J9Wxg4tvvCc3kap6s5isst7aS5VA4NQqfhxyuFcOxhGNhg2QeiFSt9ognCIkFHvGatPzt0V3f2paQyhsdOPE5gmTqE6UNhOdnhrt-r1QfHnR7xLRYEnv63_tMZoaHRLWMq7QWmnSAKw2uYkAodvaN5tGkff3VhO7jGY98hYfQw3f1ItyVRC4FlTnUzL0fcd2HXcMV62aiij0FwSSlTGHBsDTZDMlAB6B8iH9fDzG31vE1MhY5zYJ25cnmCFU14-JmkoXUCZp0y5o_4JLIdOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو جدید استاد گودرزی در راه پاسارگاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/148624" target="_blank">📅 22:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148623">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💢
قیمت بیتکوین ترکید</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/148623" target="_blank">📅 22:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148622">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RM5dEoX9QbdsvNlJHySMMhRPxzpjX9_8397bCW151cFvYcMpcGFtS6xwypLped0_3_RRF9GPElo4JYG89cACdxRVcAgzFtDNJo_xu1d-J4Wn7Xgke4ISZhiL3F9yZS9wMWy08psfgGdMMXIV2xoNKg-2mHFw4-PcUv1Y2OedRwk5w9jbIZQXE52Z8y2Xr6vL-_zZ03yCWxWiDSbZr2N9YYcEMom2XP1fgXfA15swKWenICcZ3DTkbAqlJSCnIwTMXWMKwMvIqufU0btKw_A0EKRyrD95LjhZat93V2lgqPADi7IpGPiOTXlgkO9ti3I4sBhbr_FwQXjvN-KVDc-H1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام ستاد امر به معروف و نهی از منکر استان تهران، ورود مایعات(الکل تو قوطی آبمیوه مثلا) به سالن کنسرت ها ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/148622" target="_blank">📅 22:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148621">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElDMjX-mT8NKqamPRc3ZvFAg-B5aStwL08ILXWZrR82XadIgpDlJq7uLed7ICfqkSYMMdAFWSXzPdV-YUKZJhk6_L52X_JTti4Wcdoazy_9ftgMRe16icrFShhSmxLkemyfsDHlhkkZr4jdVupTFxZ5w0RG3hAkmYctQb0O8PVM6TpGZ83EPDx2Zv4HE3RsDlBVHOcoJvWlf8vOw16lVKG01YDHKbhOPWTtOsT1izLMmSBvGwDbzbbsbR3q8drnACPFFUtGqeayF45ozMwkHAv23Tjl2JeJ2PGNvst16tqICIvlyzTu8iXd-ZnhpocsBulPlpsXA0rKogiPwQfDExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید کاخ سفید: اتفاقی در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/148621" target="_blank">📅 22:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148620">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: در حال حاضر بی‌اعتمادی بزرگی میان واشنگتن و تهران وجود دارد و هر یک از آن‌ها منتظر تسلیم دیگری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/148620" target="_blank">📅 22:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148619">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6bQhjC_FkhdbcbivUAEI3lCy0P5p5pJdzlJO3EhnSiJjwzotR9ufTcOA_4CLLKJzJzszH9Mvn_f_HBSGaEMR4ij-f4-lIdqVq9HierGfOwNwLZB65WR6XdSCXSHnKyIqb78OHpwG9hEUZLJMAhVWogzzDSVf0dJKWoccqVv64BTOmklehcd-TVqa-h4ojb8ApKdhyk1PDZBpDlXs_x9hz2UDrujX_vzi65KPV6BfN_Sw1k6Occw41LyVxy2lq2ReT7YZPXPkHcHprDuZ_7t4WCDCv0HrJinG-ZQYobgEC9KYG4mU37uMCgyxRnEy8SdYSQC_U1OUKZnof38ZszJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استاد گودرزی: هموطن راه در جهان یکیست و آن راه راستیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/148619" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترکیش ایرلاین اعلام کرد پرواز های ایران و ترکیه خود را دست کم تا پایان سال متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/148618" target="_blank">📅 22:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148617">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394c3bbc47.mp4?token=u8lVHPZNiz2HgyC98TFhakDk4nqhWSmtVH9aa1bPlpauqJnhx1CS3w_DvvHvLZ3x-mxWM085Y6_jR2YOEd93tCdBXMtnLZ_4ofVxsEMQFjiz9YoCviiOU_EsZanU4zI87C9tg9DySWktKRJPRdwD7gtsA_xLGPNObLmsExDD2v89gV4JDHbom8UndyL0TJTVsJyKwSwBW68GXFUTbkyNgyBHyCgE14Wkesk5T_4_lHnlFQVDMcbHrEb7q3w41H36Sm3sGdqrh046ebzBpuvWaObSFzhI7cWO02JzEED3lPGuBbeZ2-3mKc8hJcYhc7ZypDERpwDPJ5QEaxqmrRP4tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394c3bbc47.mp4?token=u8lVHPZNiz2HgyC98TFhakDk4nqhWSmtVH9aa1bPlpauqJnhx1CS3w_DvvHvLZ3x-mxWM085Y6_jR2YOEd93tCdBXMtnLZ_4ofVxsEMQFjiz9YoCviiOU_EsZanU4zI87C9tg9DySWktKRJPRdwD7gtsA_xLGPNObLmsExDD2v89gV4JDHbom8UndyL0TJTVsJyKwSwBW68GXFUTbkyNgyBHyCgE14Wkesk5T_4_lHnlFQVDMcbHrEb7q3w41H36Sm3sGdqrh046ebzBpuvWaObSFzhI7cWO02JzEED3lPGuBbeZ2-3mKc8hJcYhc7ZypDERpwDPJ5QEaxqmrRP4tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متقی، استاد دانشگاه: آمریکا طی ۴۵ روز آینده جنگ بعدی با ایران را آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/148617" target="_blank">📅 22:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148616">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
روزنامه همشهری : به دلیل شرایط جنگی رژه نیروهای مسلح امسال برگزار نمیشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/148616" target="_blank">📅 21:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
اولین ربات تحلیل اقتصادی رایگان
‼️
🔴
اگه نمیدونی کجا سرمایه‌ گذاری کنی یه سر به اینجا بزن
👇
@Sygnl_bot
@Sygnl_bot</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/148615" target="_blank">📅 21:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0c34f5f8.mp4?token=ZyX2ZnC0zyryCZ7c9gFFEtXGk4wVcwnhBEmH4YudNBJzGy1MNz6Tk7jc2GNQwiFRD-Vy3rJN46RAgVgSshO232keox09tf4K8WJ5wi612r5GpB1P0lhlFT2ZqrrhX7tNgMO_1DoX7Xp7r9kqN1mlS9SEkwII4c-VgtRN-6fF73G0RL0Q_wKJYPVokqjH_2aIdUIqjbofNFxXjxj-62fpnLrKYNjs0xp4bcjYSuM-CRpQTUaJ3VBCaiNoKOvwsX0anwir_pUN_-JWgLX9PmFh6E9DLeKI1c5GawVZLP7CLnyS1KnBMVgrZRY5Y0nO7BDgcOEGbGCiiDL9cJTBPAy5ZiyFU67afpJf-PO-DzotZGtyajaVOxHhVtXZxTeYwyTQg4lDTa4vHGdByXxOgDt6MUrGFyA8DhU028bSkVdmXY6ZxnNEFHjOifndxiHSL8tYvQcdDnBRNINVtBZ_rkr0h0oonFwfHsfqSh9NV4Wwx6iXXgJzOvpHUzFlIpgqYebTkTkbF7hV2vlbbBHQ66AkOiQuQIFbprUUKV8cI0LJ2VXq8jn3soQq6oktBphbc2CsTkcGSjqMoX6RqrlOyStRPVktcOD0AhhCsABXU7aG2vkC9-4x4F4KaK8_sRFVaKiu0vBA76-AXJYSqVh4o-G9zLu8jgArq_L5rG3V-A5WEHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0c34f5f8.mp4?token=ZyX2ZnC0zyryCZ7c9gFFEtXGk4wVcwnhBEmH4YudNBJzGy1MNz6Tk7jc2GNQwiFRD-Vy3rJN46RAgVgSshO232keox09tf4K8WJ5wi612r5GpB1P0lhlFT2ZqrrhX7tNgMO_1DoX7Xp7r9kqN1mlS9SEkwII4c-VgtRN-6fF73G0RL0Q_wKJYPVokqjH_2aIdUIqjbofNFxXjxj-62fpnLrKYNjs0xp4bcjYSuM-CRpQTUaJ3VBCaiNoKOvwsX0anwir_pUN_-JWgLX9PmFh6E9DLeKI1c5GawVZLP7CLnyS1KnBMVgrZRY5Y0nO7BDgcOEGbGCiiDL9cJTBPAy5ZiyFU67afpJf-PO-DzotZGtyajaVOxHhVtXZxTeYwyTQg4lDTa4vHGdByXxOgDt6MUrGFyA8DhU028bSkVdmXY6ZxnNEFHjOifndxiHSL8tYvQcdDnBRNINVtBZ_rkr0h0oonFwfHsfqSh9NV4Wwx6iXXgJzOvpHUzFlIpgqYebTkTkbF7hV2vlbbBHQ66AkOiQuQIFbprUUKV8cI0LJ2VXq8jn3soQq6oktBphbc2CsTkcGSjqMoX6RqrlOyStRPVktcOD0AhhCsABXU7aG2vkC9-4x4F4KaK8_sRFVaKiu0vBA76-AXJYSqVh4o-G9zLu8jgArq_L5rG3V-A5WEHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای اولین بار از طریق هلیکوپتر "مترین وان" از محوطه جنوبی کاخ سفید به سمت مقصد خود عزیمت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/148614" target="_blank">📅 21:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سپاه: آمریکا و اسرائیل دیر یا زود باید به خروج از منطقه تن بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/148613" target="_blank">📅 21:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148612">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
حمله هوایی سعودی‌ها به الجوف یمن
🔴
جنگنده‌های سعودی در جدیدترین حملات خود، شهرستان «الحزم» در استان الجوف را هدف حمله هوایی قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/148612" target="_blank">📅 21:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148611">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بلومبرگ: ایران به یک محموله دیگر LNG قطر برای عبور به پاکستان مجوز داد
🔴
بلومبرگ گزارش داده پاکستان مجوز عبور یک محموله دیگر گاز طبیعی مایع‌شده قطر از تنگه هرمز را از ایران دریافت کرده است.
🔴
براساس این گزارش، یک محموله دیگر LNG قطر نیز در همین ماه با مجوز ایران از تنگه هرمز عبور کرده و به پاکستان رسیده بود.
🔴
کشتی حامل محموله جدید قرار است فردا به پایانه واردات پاکستان برسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/148611" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148610">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
جی دی ونس: این انتخابات میان‌دوره‌ای میان کسانی است که معتقدند این کشور باید آینده‌ای داشته باشد و کسانی که ترجیح می‌دهند آن را ویران کرده و از نو بسازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/148610" target="_blank">📅 21:16 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
