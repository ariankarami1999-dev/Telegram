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
<img src="https://cdn4.telesco.pe/file/kAxhl07x-mghkydDyB7JumhiBrlsvaLOp03mbZWlEyDhh_at6lgWVlfUiFGLRLKfaL2CNl8WOK3XOsVFNp0DkXySsUfmyBQJr0Alj8IkoDW3_KvDIxCTBFdzvY8IL1Hj28Pr56YM6YpvTFZEQuS0i4QQctxBQ93Nhc4qAAdwbUKYYnsM9AVxO-II5Vri7OZO9m_84xJxQJ_AiU8xtj-gq1VRBKdL6HTTE8ZcJ1SdGHVzRsTtoHu6CyqKc9MbZC2zmjBKkx-_i_ceGHpoTumf0dNxiYwsWoJlwl_NYocj775J6k-FxYdS6r-4LIHHqPZSFIm4HRTZXY_zil4ZVSMXuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 13:02:44</div>
<hr>

<div class="tg-post" id="msg-138074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👀
رفقای قدیمی فن آخر استاد رو یادتونه یا نه ؟!
👍
فرمایشات ائمه اطهار و مقام معظم رهبری…
🔥
چه آشی بپزم
💦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 369 · <a href="https://t.me/SorkhTimes/138074" target="_blank">📅 13:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#افشاگری
🚫
با توجه به سهمیه لیگ برتری تیم ها، محسن خلیلی با حمایت اینانلو در تلاش است تا به جای جذب محمد قربانی، امیر جعفری را با پرداخت 110 میلیارد رضایت نامه از گلگهر بخرد
.
❌
گویا انتقال قربانی برای آقایان منفعت شخصی ندارد/ویژن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/138073" target="_blank">📅 12:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">چراغی اینو خواستی فور بده
فک میکنم همه هواداری پرسپولیس موافق باشن هیچ مدیری مثل حدادی نمیتونست اینجوری بازیکن جذب کنه خداییش کادر فنی دست روی هرکی گذشت جذب شد ایشالله با جذب قربانی کارنامه خودشو پررنگ تر میکنه
#حمایت_حدادی</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/138072" target="_blank">📅 12:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚠️
⚠️
علی دبیر شده همه کاره….؟! دبیر نفر اصلی هست که دنبال زدن حدادیه و آوردن اینانلوعه  #اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/138071" target="_blank">📅 12:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from꧁༒ᄊﾉÐ刀ﾉムんｲ༒꧂</strong></div>
<div class="tg-text">این دیگه کیه شاخ شده واسه ما برو به کشتی برس پلشت</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/138070" target="_blank">📅 12:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚠️
⚠️
علی دبیر شده همه کاره….؟! دبیر نفر اصلی هست که دنبال زدن حدادیه و آوردن اینانلوعه
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/138069" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138067">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4133fa453.mp4?token=ICluqvlEsmFa7eqxfd1WI_NiYgJCkWyijeciBLAnX7VxwL_aV1AhK9vutxtPWnY71Jz-1XknOmUjshWO0lR7e0m8zArra3itEaHy6aWJ30fJgr7ssLvwJEFWYHWf7IROYTavUbwy_AXF4rLeq4sLJomlPR3E7oSvJIlqfxJ_vaEyli8Lbp_x-BAzBXGZ6uK5D8Vi_BsDA2eUk_uXDSqOoBc9jmpqwMYwxVGMz37a0YJZHlloh2dcQHOAJSoZHn-S31TwJEaaYBIU_FLkpvJm0wYYRdU4ITKvZVJv_0sgMPY4ae_aY2PLFh2fh6OTwd0Z5X-xIIwGxeAdGI7Q55a9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4133fa453.mp4?token=ICluqvlEsmFa7eqxfd1WI_NiYgJCkWyijeciBLAnX7VxwL_aV1AhK9vutxtPWnY71Jz-1XknOmUjshWO0lR7e0m8zArra3itEaHy6aWJ30fJgr7ssLvwJEFWYHWf7IROYTavUbwy_AXF4rLeq4sLJomlPR3E7oSvJIlqfxJ_vaEyli8Lbp_x-BAzBXGZ6uK5D8Vi_BsDA2eUk_uXDSqOoBc9jmpqwMYwxVGMz37a0YJZHlloh2dcQHOAJSoZHn-S31TwJEaaYBIU_FLkpvJm0wYYRdU4ITKvZVJv_0sgMPY4ae_aY2PLFh2fh6OTwd0Z5X-xIIwGxeAdGI7Q55a9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول فصل قبل پرسپولیس رو علیپور زد؛ به نظرت این فصل کی گل اول رو می‌زنه
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/138067" target="_blank">📅 12:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138066">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==  #اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/138066" target="_blank">📅 12:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138065">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/138065" target="_blank">📅 12:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138064">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from. 🌐AB🌐</strong></div>
<div class="tg-text">آقا انجام شد . من یه بیست تایی گذاشتم ولی تنهایی جواب نمیده فقط کانال سرخ تایمز این موضوع رو پوشش داده و بقیه کانال ها بی خبرن . باید همه جمع بشیم مثل قضیه قربانی</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/138064" target="_blank">📅 12:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138063">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخالی خالی</strong></div>
<div class="tg-text">می دونید چرا گرا موند : اینانلو</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/138063" target="_blank">📅 12:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138062">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.f</strong></div>
<div class="tg-text">بهترین مدیرعامل ۲۰ سال اخیر پرسپولیس خدایی تا الان حدادی بوده درویش در این ۴ سال اگر فصل دو بازیکن جوان می‌گرفت تیم جوان می‌شد اما این کارو نکرد الان حدادی این همه بازیکن گرفت باز ضعف داریم بود دنبال دلالی آوردن نبیل سرجوریه و لوکاس سرجوریه که بعد از یک میلیون دلار پولی که از پرسپولیس و و هنر درویش دلالی کردن از فوتبال خداحافظی کرد لوکاس ۳ سال بعد از پرسپولیس یک گل زد و الان حقوقش سالی ۵۰ هزار دلاره نبیل که اصلاً معلوم نیست کجاست امروز اگر هواداران ساکت باشند فردا به گوه خوردن می‌افتیم</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/138062" target="_blank">📅 12:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138061">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">اقا فردا تو ورزشگاه فقط به اینانلو فحش بدیم</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/138061" target="_blank">📅 12:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخالی خالی</strong></div>
<div class="tg-text">حرومزاده ای که نذاشت حسین نژاد بیاد</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/138060" target="_blank">📅 12:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
شنیده میشود که مهدی تارتار قرار است از محمد خدابنده لو به عنوان هافبک بازیساز و فیکس خود بهره ببرد و این بازیکن در بازی برابر شمس آذر نیز در ترکیب فیکس پرسپولیس حضور خواهد داشت
❌
❌
تارتار علاقه زیادی به محمد خدابنده لو دارد و میخواهد این بازیکن را احیا کند…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/138059" target="_blank">📅 12:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.f</strong></div>
<div class="tg-text">خدا درویش را لعنت کنه این‌ها همه نقشه درویشه به ایرانلو می‌گفتند درویش کوچولو یعنی دوران سیاه درویش مدیریت درویش که یادمون نرفت ۴ سال مدیرعامل پرسپولیس بود اگر سالی فقط سه تا بازیکن جوون پدیده لیگ را جذب می‌کرد  اصلاً پیر نمی‌شد بی‌انگیزه نمی‌شد الان هم سوخته که حدادی داره محبوب میشه پرسپولیس انقدر بی‌غیرت و بی‌شرف نشده که پشت پرسپولیس و حدادی را خالی کنه روز شنبه از دقیقه ۱ با خواهر و مادر اینانلو بازی را شروع کنید</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/138058" target="_blank">📅 12:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۔۔۔۔۔باید کهنه سوار بود۔۔۔۔۔۔</strong></div>
<div class="tg-text">هرکی میره ورزشگاه ازدقیقه یک تا اخر بازی برعلیه اینالو احدمیرزایی وخلیلی فقط شعار بدین وخواهان اخراجشون بشین</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/138057" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJahan</strong></div>
<div class="tg-text">داداش من ترکوندم</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/138056" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآقای خاص</strong></div>
<div class="tg-text">ماهم زدیم</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/138055" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعلی رضا</strong></div>
<div class="tg-text">آقا ما هم انجام دادیم ایشالله آزادی پرسپولیس از دست این زالوها</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/138054" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138052">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">چرابقیه چنلا سکوت کردن</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/138052" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138051">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/138051" target="_blank">📅 12:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138050">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🫦
حسین کنعانی گوه خورده با کاسش مطلب سفارشی کون گشاد و ارباب دیوسش رو استوری کرده….
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/138050" target="_blank">📅 12:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138049">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
⛔️
پنجشنبه با اکثر لیدر ها توی یوسف‌اباد جلسه گذاشتن اینانلو و بازگشا که هم تشویقش کنن هم اگر تیم عقب افتاد به حدادی فحش بکشن و فضا رو خراب کنن
⚠️
خار همه تون گ.ا.ی.ی.د.س هوادار ک.و.ن.ت.و.ن پاره میکنه ج.ا.ک.ش.ا.ی دوزاری تو حموم زنونه هم شمارو انگشت میکنن، بی غیرتا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/138049" target="_blank">📅 12:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138048">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💢
💢
💢
💢
باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز یکشنبه هفته آینده بش…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/138048" target="_blank">📅 12:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138047">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHeidar</strong></div>
<div class="tg-text">از بقیه خواهش میکنم اطلاع بدید به دوستان</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/138047" target="_blank">📅 12:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138046">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHeidar</strong></div>
<div class="tg-text">من از دیشب تا الان بالای ۲۰ تا هشتگ اخراج زدم زیر پست باشگاه و بانک شهر</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/138046" target="_blank">📅 12:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138045">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommeysam</strong></div>
<div class="tg-text">اقا ما رفتیم انجام دادیم امیدوارم بقیه هم انجام بدن</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/138045" target="_blank">📅 11:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138044">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">https://www.instagram.com/p/Db3Z8emDcaK/?igsh=MW0zbm5sMHc5Y3UzZw==
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/138044" target="_blank">📅 11:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138043">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
⚠️
بامداد چهارشنبه تا ۵ صبح اینانلو جلسه داشته تا جمعه رسما مدیرعامل بشه
⛔️
چون کودتاش فاش شد،فعلا افتاد عقب.
⛔️
اون اسکل هایی که خوابن بیدار بشن، حیثیت تیم داره به باد میره، کونده خارهایی که فقط تایم نقل و انتقالات عربده کشی میکنید الان خفه خون‌گرفتید پس فردا ادا دلسوز هارو دربیارید ک.ی.ر میزنم به هیکلتون
⛔️
پرسپولیس صندلیش اینقدر کوچیک‌نشده که یه لمپن گوزو بشه مدیرعاملش هوادار پرسپولیس اینقدر بی غیرت و بی چشم رو نشده که پشت تیم و مدیر زحمت کشو خالی بکنه من تا ته این داستان وایمیسم دفاع میکنم خار باعث بانیشم سرویس میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/138043" target="_blank">📅 11:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138042">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🫦
🫦
🫦
🫦
🫦
🫦
🫦
🫦</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/138042" target="_blank">📅 11:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138041">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚽️
دانیال ایری در تمرین امروز پرسپولیس حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/138041" target="_blank">📅 11:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138040">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
تصمیم جدید تراکتور؛ مسیر پرسپولیس برای قربانی هموار می‌شود؟
👀
🔴
🔴
تراکتور شنبه مذاکرات جدیدی با سپاهان برای جذب آرش رضاوند خواهد داشت؛ مذاکراتی که ممکن است باعث شود تراکتور از جذب محمد قربانی کنار بکشد.
🔴
این اتفاق می‌تواند به نفع پرسپولیس تمام شود!
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/138040" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138039">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🫦
کون گشاد و اینانلو ریدن به خودشون… یعنی ریدم تو دهن کسی که رسانه باشگاه رو داد دست یه عضو پخمه جایزه بگیر و نوچش…. امشب
ک
.یر
خیرات میکنم براتون دیوسا اینجا پرسپولیسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/138039" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138038">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvbBt9P0vunmXEJJYaBYyLLFjNfWop7e8Pc8tVqWFJdBL3NQJ6O3wOsKz0gBlbfaILrLCU7WOUfRjaVhpF3zRXZKWTTwldVx9la1Ch-RvrIH5_ouqiFadkIZyXyzJV_YZlsxKDv6spimCtolcrrGOs93HZCIkLlHnFedXDjYrmf3a_WcCCMovfTP4ucuxNRteDgN30XwbSk7owJ8o5Ms0PgrGAsBPpVKyhK-NHd53qR_-rn0yhlu3smzeT94-UKKz6rB5O8JSQZLWIVQFBEGHEhQ5nib4PT0X9FxxBT6GhDWX_uMCMT11pFXyyhODxL6-kdJSO3vBlSw7kAKU5eqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💭
نزدیک 340 هزار کامنت زیر پست اخر باشگاه و همه‌ی هواداران خواهان جذب
#محمدقربانی
هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/138038" target="_blank">📅 11:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138037">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
#اخراج_اینانلو  #اخراج_میرزایی
❌
شما که کلی هشتگ زدین اینارم تو پیج بانک شهر بزنین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/138037" target="_blank">📅 10:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138036">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
هر رسانه پرسپولیسی که الان سکوت بکنه خیانت کاره…. چون یه عده الان آتیش زیر خاکستر رو نمیبینن
❌
اینا دارن زیر پای حدادی رو خالی میکنن هوادار توجه کنن اگه الان کاری نکنیم فردا اینا حرومی ها کاری میکنن تیم نتیجه نگیره تا حدادی اخراج بشه،، تیم به فنا میره پس…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/138036" target="_blank">📅 10:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138035">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
هر رسانه پرسپولیسی که الان سکوت بکنه خیانت کاره…. چون یه عده الان آتیش زیر خاکستر رو نمیبینن
❌
اینا دارن زیر پای حدادی رو خالی میکنن هوادار توجه کنن اگه الان کاری نکنیم فردا اینا حرومی ها کاری میکنن تیم نتیجه نگیره تا حدادی اخراج بشه،، تیم به فنا میره پس…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/138035" target="_blank">📅 10:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
بعد از اینکه حدادی در این پنجره نقل و انتقالاتی عملکرد قابل قبولی داشته اما اینانلو و احد میرزایی با روابطی ک با احمدی مالک باشگاه دارن میخان حدادی رو برکنار کنن تا یکی از خودشون مدیرعامل بشه !!  #اخراج_اینانلو  #اخراج_احد_میرزایی  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/138034" target="_blank">📅 10:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
#شنیده_ها
❌
قربانی با پرسپولیس به توافق رسیده ولی بعضی از اعضای مدیریت (دو نفر ) مخالف این انتقال هستن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/138033" target="_blank">📅 10:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
بعد از اینکه حدادی در این پنجره نقل و انتقالاتی عملکرد قابل قبولی داشته اما اینانلو و احد میرزایی با روابطی ک با احمدی مالک باشگاه دارن میخان حدادی رو برکنار کنن تا یکی از خودشون مدیرعامل بشه !!  #اخراج_اینانلو  #اخراج_احد_میرزایی  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/138032" target="_blank">📅 10:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
علی اینانلو علیه همه کودتا کرده تا خودش مدیرعامل بشه . تا زمانی که اینانلو تو پرسپولیس باشه پرسپولیس رنگ آرامش نمی‌بینه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/138031" target="_blank">📅 10:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePoap0OwTZaYy4J15oOtY1mONzgYWGXF5iA9Ui6EHdFdH_igub_eJgGVOHmMb6JJMPtfcMRJ1h_3VK_4va1TQn5FrFMUtiDv8p_DQ39zfAuaj65BbSEMSvvSS6BnOyFnunwQPLdMylxYjyYC8lYZc_BKGKvcvAzOUV4cArgBHfahenfg4zre98jhKReJjXMCxcf6zVG8L9fAblcSmEioAamxgad03nr9UILs0-OempKfXYV32Yh9Ep9MQr3Fzqqumai3LM9-_6J0-llWiBE0SNXhJ6y8jmw9hj7BRWLp5Os9aPdHo4y-vPEeesHrSYCx5zhypUJ3gxsApXYHdBxszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی اینانلو علیه همه کودتا کرده تا خودش مدیرعامل بشه . تا زمانی که اینانلو تو پرسپولیس باشه پرسپولیس رنگ آرامش نمی‌بینه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/138030" target="_blank">📅 10:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
هر رسانه پرسپولیسی که الان سکوت بکنه خیانت کاره…. چون یه عده الان آتیش زیر خاکستر رو نمیبینن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/138029" target="_blank">📅 10:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚜
علیرضا بیرانوند در تلاش برای حضور در تیم ملی امید ایران برای ۳ سهمیه بزرگسالان میباشد تا با کسب مقام احتمالی در مسابقات آسیایی از خدمت سربازی معاف شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/138028" target="_blank">📅 10:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_xtdQJ4s23A33BrZbrgTwMFJC5Cif4cDGe2iIR-LBgyP6cv2PPMR8X0EXYF1NiK9FJ-AErniC48DdzmnwGZ0zqufvQnpmKlgzfIxPlJM1qJXX9BOK27y1OzS8_tAAvNOaPtgREI8EErrvy7ZEWmJlP9jCQLpKqrPCfLuj4zs7ewa2T99qR7KZPzmZesvxUrVp9nOIZTErfoW-oKX-EfMUgp7osfbcl3BBhDThh07LPmn3MHEEDgqh7OMl1VnJSnIAOP61yGIu3wHh2lWBLhXQ-5ZBMFz0KX6pG_Uc6eVKpOFexS8wDTUmOhVTMgzJ3QT05ZA9fhkkkClwFXu-dokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علت ماندن تیوی بیفوما در پرسپولیس، کاهش وزن، آمادگی جسمانی مطلوب و همچنین تغییر نگرش او و اصلاح سبک زندگی شخصی‌اش بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/138027" target="_blank">📅 10:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138026">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
میلاد محمدی تو اولین بازی تیم جدیدش امشب تیمش تو پلی‌آف لیگ کنفرانس تو عرض کمتر از ۱۵ دقیقه ۲ تا کارت زرد گرفت و اخراج شد :)))
😄
😄
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/138026" target="_blank">📅 09:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
شنیده میشود که مهدی تارتار قرار است از محمد خدابنده لو به عنوان هافبک بازیساز و فیکس خود بهره ببرد و این بازیکن در بازی برابر شمس آذر نیز در ترکیب فیکس پرسپولیس حضور خواهد داشت
❌
❌
تارتار علاقه زیادی به محمد خدابنده لو دارد و میخواهد این بازیکن را احیا کند…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/138025" target="_blank">📅 09:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMHWxPoTk6qREE-RIl8HpRTIzUTRjtbflE4B-88KsYH2d6B7-9yqhTPrq65TZVs9HlOiLbodY8N8Wr9KWQMl03WVo3wNh_3te0Cz_4RLnnQcA47WmNQ2EU7pZZNK-Mm5pKZmWAdQv2ffAwyZKmPc6b607R1zSNsZvwuErDY3nMdX8I0T-3W_9zuAYuTOLjQszxEo5bpaCt2KiUM95eDcLwSIeP7X9eVhiKGnsUimeyQLZMlLTpb295AzTPd3l_ometlLARghm__M_UQaJT55uovE5Whbnd7Po5bM1-55okKIBn7ucrCb_JjY_rdmVm3d1MbIq6m9PkEJh77S-RGyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/138024" target="_blank">📅 09:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3g6v3F2CT0izRFlqPie82VOfcq_9bzFsoK-hCl4dcfzdIWGkdJ5NCgL-toITP07fnz5W6lOiIsElYY7Jf4gQJKxQBsB9rgEPPRdT-eMxfRoeFuJFymQEOMQz_Oix9Jtkc0p22PJc18uBjv3509XvQ9j2PxvDhkrzhkb3bdW5HaIFihIotY-OKFcFCeNL0X5aLNjllllzAfSQY4j-AmamqGeLz6ERIiXh0ioIvnWifTcXP_SXgU_9kLBtd8mx90MvuY_0_jiP2etz3DI7apQ4g9iL3ny7Mc0qvsIDsAXXB5SaOhRDn47o_GydnVLIEqJ-N5UQ77obOZVFhcUzenXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد نسل جدید آمریکا؛ شلتون مقابل ناکاشیما، کدام‌ یک حرف آخر را در فینال مونترال می‌زند؟
🎾
Ben Shelton -
🎾
Nakashima
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
📌
مسابقه را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138023" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب احتمالی پرسپولیس مقابل شمس آذر:
🔴
پیام نیازمند
🔴
مجید عیدی
🔴
حسین کنعانی
🔴
محمدمهدی زارع
🔴
ابوالفضل جلالی
🔴
پوریا لطیفی فر
🔴
مارکو باکیچ
🔴
اوستون ارونوف
🔴
مهدی تیکدری
🔴
علی علیپور
🔴
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138022" target="_blank">📅 01:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
هر رسانه پرسپولیسی که الان سکوت بکنه خیانت کاره…. چون یه عده الان آتیش زیر خاکستر رو نمیبینن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138021" target="_blank">📅 01:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آقای هوادار الان سکوت بکنی پای کار نباشی فردا نیای بگی فلان شد بهمان شد از ما گفتن من گلوم پاره شد، اینا اگر بمونن اینقدر علیه بازیکنا هم کارشکنی میکنن تا تیم نتیجه نگیره و خودشون کارو دست بگیرن
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138020" target="_blank">📅 01:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#نظر_شخصی
🤩
روزی که حدادی اومد عده زیادی گفتن جونه سابقه مدیریتی نداره، ولی من گفتم زمان بدید این آدم خودش هواداره انگیزه داره، برنامه داره…. این ادم موقعی که تیم دست بورس بود وارد هئیت مدیره شد و تمامی موارد اقتصادی و اسپانسری و پرداختی ها دست این ادم بوده.
🗣
آقا و خانوم هوادار؟! ما در طی این چند سال بدهکار بودیم؟ بازیکن ها اعتصاب میکردن ؟ اسپانسر چوسکی داشتیم؟! از زمانی که ایشون اومده بالاترین عدد های اسپانسرینگ برای پرسپولیس بوده با کلی طرح اقتصادی با طبیعت الانم که از نئو بانک پرسپولیس رونمایی شده، این ادم سبقه ورزشی نداشت ولی ثابت شد تو زمینه اقتصادی عالی عمل کرده و با توجه به نقل و انتقالات تا این جای کار میشه گفت نمره قبولی گرفته….قطعا اشتباهات زیادی هم داشته اول کار و تصمیمات بدی گرفته همه هم آگاه هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138019" target="_blank">📅 01:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💯
تو همه دوره های مدیریتی فساد بوده هم مدیر فاسد بوده هم سرمربی
خود برانکو سر خارجی ها میخورد اما قهرمانی میاوردن، اینا دیگه شورشو در آوردن فقط فکر خودشون هستن اینجا پرسپولیسه این تیم هوادار داره
مردم به عشق اخبار پرسپولیس با شور شوق سر کار تو خونه نصف شد اخبار رو دنبال میکنن و با هر خبر شادو غمگین میشن اون موقع به عده بی پدر مادر روح روان مارو بهم میریزن
#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138018" target="_blank">📅 00:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/138017" target="_blank">📅 00:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏆
🔴
اگر این دیوس و نوچش نبودن نیم فصل پارسال تیم با کله تو دیوار نمیرفت چقدر بال بال زدم، الان فرمون دست حدادی بود هرچی تو مارکت بود رو به قول قمیا آب تاراش کردیم کلی هم بانک شهر هزینه کرده تنها تیمی هم بودیم اردو خارجی رفتیم اینا حاصل مدیریت حدادی و احمدیه…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138015" target="_blank">📅 00:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ببین اینا دیگه چکار کردن که چراغی اینجوری عصبی شده ازشون</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138014" target="_blank">📅 00:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">چراغی که اهل مماشات بود همیشه</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/138013" target="_blank">📅 00:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">ببین اینا دیگه چکار کردن که چراغی اینجوری عصبی شده ازشون</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/138012" target="_blank">📅 00:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⛔️
آقای احمدی فورا این کون طاقار و نوچش رو سیک کن وگرنه هوادار بزنه سفید و سیاه باهم از خجالت شون در میاد خشک و تر باهم میسوزن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138011" target="_blank">📅 00:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🫦
یه مشت سگ بغل کنه گربه زیر سر بزار آدم شدن ریدم فرق سر آقا دیوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138010" target="_blank">📅 00:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚠️
جوری بگای
.
یم شما ج
.
اک
.
شا رو که مقنی ها کونتونو به عنوان نمونه کار نشون کارفرما بدن….اوکی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138009" target="_blank">📅 00:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
علی شیخ الاسلامی آنالیزور ساپینتو در استقلال بعنوان آنالیزور جدید مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/138008" target="_blank">📅 00:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
شنیده میشود که باشگاه گل‌گهر با توجه به جذب پدرام قاضی پور بی میل به فروش امیر جعفری با قیمت خوب به پرسپولیس نیست و ممکن است لحظه‌ آخری این بازیکن پرسپولیسی شود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138007" target="_blank">📅 00:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب احتمالی پرسپولیس مقابل شمس آذر:
🔴
پیام نیازمند
🔴
مجید عیدی
🔴
حسین کنعانی
🔴
محمدمهدی زارع
🔴
ابوالفضل جلالی
🔴
پوریا لطیفی فر
🔴
مارکو باکیچ
🔴
اوستون ارونوف
🔴
مهدی تیکدری
🔴
علی علیپور
🔴
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138006" target="_blank">📅 00:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#اخراج_اینانلو
❌
#اخراج_احد_میرزایی
❌
#اخراج_بازگشا
❌
#اخراج_خلیلی
❌</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138005" target="_blank">📅 00:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💥
از نسلی که ساخت، برای نسلی که ادامه می‌دهد...  پیراهن جدید پرسپولیس؛ با امضای تاریخ
🙌
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138004" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138003">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💥
از نسلی که ساخت، برای نسلی که ادامه می‌دهد...  پیراهن جدید پرسپولیس؛ با امضای تاریخ
🙌
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138003" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
یکی از خبرنگاران فرهیختگان مدعی شده؛ که پرسپولیس به جذب امیر جعفری خیلی نزدیکه و احتمالا با ایری همزمان رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138002" target="_blank">📅 23:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💥
از نسلی که ساخت،
برای نسلی که ادامه می‌دهد...
پیراهن جدید پرسپولیس؛
با امضای تاریخ
🙌
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138001" target="_blank">📅 23:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
فارس: کوروش اژدهاکش با قراداد قرضی از پرسپولیس به نساجی پیوست و بزودی رسمی میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138000" target="_blank">📅 23:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxe_8KZR-tvRgP-oocw9ZPkTgcxAh7eWgGSvXZeV0qx0pM_gZurCAP3eNpckcH9Wg74nA2Ij2d5VP1V5W5S6_62zrifwJfmtJphZxMcPttblrHG7eyolEtW-K3l_wEzeL3V1zlTd0PyICKp5dN9LrxQT9tDxhfeMEJuELZSc_c6iMgZ9NL3lLHOxKOn0HVMQadYcLVCW7Psq9yFyziKA-extbcv0QuO5t7CyJsV48pT2SRsXsXj493u-QXaJtRexd8lAChmVwgUxEDRlxOmolZMT6iDnr9ZDt-QpnVTK4Py-3LXhgeLqtGfVwtOeQMLETf4kOaw-xI_Hp6NnMOVXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ارسالی_هوادار
⛔️
بدون شرح…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137999" target="_blank">📅 23:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137998">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚽️
دانیال ایری در تمرین امروز پرسپولیس حضور یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/137998" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137997">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚠️
از روزی که این کون گشاد اومده تمام رسانه ها با پرسپولیس بد شدن چرا ؟! چون‌ ایشونو از شهرداری آوردن و گوز بارش نیست برمیداره زنگ میزنه به خبرنگار ها و تهدید شون میکنه مدیر روابط عمومی که روابط عمومی بلد نیست…..
❌
اینانلو با دخالت هاش و گرفتن رسانه هم تیمو…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/137997" target="_blank">📅 23:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137996">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Nkhz</strong></div>
<div class="tg-text">اینانلو اگه عاشق مدیریته
میتونه مدیریت دسشویی درفشی فر رو بگیره دستش</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137996" target="_blank">📅 23:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🫦
کون گشاد و اینانلو ریدن به خودشون… یعنی ریدم تو دهن کسی که رسانه باشگاه رو داد دست یه عضو پخمه جایزه بگیر و نوچش…. امشب
ک
.یر
خیرات میکنم براتون دیوسا اینجا پرسپولیسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137995" target="_blank">📅 23:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137994">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXsrnlRAtfr0aVsD7eoUS0tPR6Sh1YSP0iL48i0pznwtzH7srhIbHFayot2D6fC0f9REF2akiBD514BxT9RMkQOUi25EOXQWmCdWyswbrarPjip6okkIi7Hhbsf66FF8hciqQUitD52VITG-sqR14Sr4O7mA8W9kn0AMsDRlv3JexJpxTSPIX5oKwpPo9dcdjsj-smDU8M1SGgAZQuQApu27ReiTJ0hMkFkELR--3byznqliv7wRBRQXaBeWiyPMGqCkwHuH1w-i87IqBX6YixIYZpSBjLk5WQJn2tHvw9IrfNeT_CIuXCuM0pbcAGTKgy3t3UERXkj4VawEV0o_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫦
کون گشاد و اینانلو ریدن به خودشون… یعنی ریدم تو دهن کسی که رسانه باشگاه رو داد دست یه عضو پخمه جایزه بگیر و نوچش…. امشب
ک
.
یر
خیرات میکنم براتون دیوسا اینجا پرسپولیسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/137994" target="_blank">📅 23:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137993">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✖️
✖️
محمد قربانی صبح امروز از طریق نماینده‌ رسمی‌خود به‌ مدیریت‌ باشگاه پرسپولیس اعلام کرده درصورتی‌که تا روزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قید توافق‌ شخصی با تراکتور رو می‌زنم با پرسپولیس قرارداد امضا خواهد کرد.//خرمی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137993" target="_blank">📅 23:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137992">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TghFIu0hAyGg0rcbrxgGtxZrp-pe9wE0KzvESedc418Rn0cpHCmF_dGvNsfufNY5SH2hUPQ8hEfu_YZHI_DWqMKq6XHIU9p4SFTTbRJeVIq0Hurt3lHDqAJtqmSEYeESMf3_AyOKiR-o7-EzNTbnzdkbVY1cmOddZNyKl1k4xSjhjyDN0bHBFKjKSm0T0baLt8fTx554rBkaqtKSNBpznJtBsD2fUmILy3JY6n9EanVKl3ev893zdIwPvU92HYtMQ3ZiBUEyDp1YJjoZngH0sbJw3bjSRmih5U2K9ed8-HovdGMxqkEJPMY7VmpLrbrk4g56Lw8W8qFYPvJvLwSZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دانیال ایری در تمرین امروز پرسپولیس حضور یافت
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137992" target="_blank">📅 23:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137991">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
🤩
محرم نویدکیا در مورد کسری طاهری :
❌
دو باشگاه در حال صحبت هستند. یک‌سری مسائل وجود دارد و باید همان قراردادی که میان روبین کازان و نساجی بسته شده، در انتقال به سپاهان هم در نظر گرفته شود. در غیر این صورت او باید تا نیم‌فصل همان نساجی بماند. اگر شکل قرارداد متفاوت باشد، ممکن است مشکلاتی ایجاد شود و بازیکن تا نیم‌فصل نتواند شرایط لازم را داشته باشد. شاید تا یکی دو روز آینده به جمع‌بندی برسند در غیر این صورت هم این بازیکن به ما اضافه نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/137991" target="_blank">📅 23:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137990">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
تصاویری از تمرینات امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137990" target="_blank">📅 22:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137989">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
فوری :سر مسائل امنیتی گرون شدن قیمت بنزین کنسل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137989" target="_blank">📅 22:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚠️
حدادی تکون بخوره هوادار تو ورزشگاه خار مادرتون میده هوا…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137988" target="_blank">📅 22:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⛔️
🫦
کودتای اینانلو و کون گشاد علیه حدادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137987" target="_blank">📅 22:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🏅
🏧
هشدار به هواداران پرسپولیس و بانک شهر
🚫
زمزمه‌هایی درباره تحرکات پشت‌پرده برخی اعضای هیئت‌مدیره و نزدیکانشان برای تغییر معادلات مدیریتی باشگاه به گوش می‌رسد؛ تحرکاتی که اگر واقعیت داشته باشد، نمی‌توان ساده از کنار آن گذشت.
🚫
سؤال روشن است: آیا عده‌ای از…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137986" target="_blank">📅 21:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🏅
🏧
هشدار به هواداران پرسپولیس و بانک شهر
🚫
زمزمه‌هایی درباره تحرکات پشت‌پرده برخی اعضای هیئت‌مدیره و نزدیکانشان برای تغییر معادلات مدیریتی باشگاه به گوش می‌رسد؛ تحرکاتی که اگر واقعیت داشته باشد، نمی‌توان ساده از کنار آن گذشت.
🚫
سؤال روشن است: آیا عده‌ای از…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137985" target="_blank">📅 21:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137984" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/137983" target="_blank">📅 21:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137981">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpQXxY0KR-GDy4vwrkhj_KaRoptfYnLREDEkvaueMi-lOuwgSJrizSsgn6BfIDj14XXfoHuAaX93FcM24SwX2jOuzC163_niECLJv5CDKEDLmIV4CFQ09-fj8bTG0amzdAHM5i9BEh9LUNECCzhVwk7EeY4fkpNBgqKHxyaaQYaPaqky4kaSu7KWc1BpbDhLdI2HHxgy2fXAf1dNuU4_kBIuhF_4Yatv8YBs9vwwWe708pNY5Kct008BQGzBLffnnyknovJMaSavFV8ZvWlsNbn8VfIYjtlvv50Rzn_TQtMl90lEZUZrGnLL5xavB5xZEj0t8hB1orYbf6PzenLtoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کیت‌های پرسپولیس در 4 فصل گذشته؛ کیت جدید ارتش‌سرخ فردا رونمایی خواهد شد.ببینیم چه جوریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137981" target="_blank">📅 21:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137980">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
پرسپولیس نوین؛ این بار باید حمایت کنیم
🔴
🤩
اگر منصف باشیم، باید به پیمان حدادی و مدیریت فعلی پرسپولیس بابت کاری که در نقل‌وانتقالات انجام داده‌اند خسته‌نباشید بگوییم.
🔴
جذب بازیکنان جدید، تغییر نسل، هزینه کردن برای تقویت تیم و ساختن یک ترکیب تازه، نشان می‌دهد پرسپولیس وارد مسیر جدیدی شده؛ مسیری که می‌شود اسمش را گذاشت: پرسپولیس نوین.
🔴
نباید فراموش کنیم مدیران قبلی آن‌قدر به تیم آسیب زدند و آن را از نظر بازیکن و ساختار تضعیف کردند که امروز حتی با این همه خرید و هزینه، باز هم جای تقویت داریم.
🔴
اما همین که امروز برای پرسپولیس هزینه می‌شود و برای ساختن تیم جدید بازیکن جذب می‌کنند، خودش یک اتفاق مثبت و قابل حمایت است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137980" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137979">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🏅
برنامه بازی ها فردا لیگ برتر؛
🏅
تراکتور _
🏅
پیکان 18:00
🏅
استقلال_
🥇
مس شهر بابک 19:30
🏅
خیبر_
🏅
فجر سپاسی 19:30
🏅
استقلال،خ_
🏅
آلمینیوم 20:00
🏅
سپاهان_
🏅
چادرملو 20:00
🏅
گل گهر_
🥇
نساجی 20:15
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/137979" target="_blank">📅 21:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137978">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
بدون حضور خرید جدید پرسپولیس
🔻
رونمایی باشگاه نساجی از کیت‌جدیدش که اثری از دانیال ایری ستاره جدید و خرید احتمالی پرسپولیس دیده نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137978" target="_blank">📅 21:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137977">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
دانیال ایری نام نساجی از بیو و پروفایل خودشو با لباس نساجی حذف و تغییر داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137977" target="_blank">📅 21:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137976">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJS4AkGE_mbrpeNZQpat82306URVGdckjq_hnyUcsjFBpPzCVHaZSHqdCySUbYeWU3lUu2SHvvnYla2jqhVDmMMvJCsJ8lPslVndx21IgomUsLhwtc2EBcijARj2ii9iePeLfqJcDSpMOAydvi_tGbs5du60lIz9cAruAay93hdicUajqU9eJoSnJQq-zhPxGTlgTgHrWMIt53wdNOPjsWFjTfbBo3b63C8206Vx_ci8jquxpI9i-FHAqtQuzHw4m6YZiOM6MAMU2PBCPXJFv4T7qIjkn_kbbm0Jti8ZumjQYkVdo6x4xEGitJq1KW6CiokimjRAt57ZnyRfHQDSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دانیال ایری نام نساجی از بیو و پروفایل خودشو با لباس نساجی حذف و تغییر داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137976" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137975">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVS4bwZOgMQVEeK5nftQsuZ9Afqvtu961q24v13HZ5D2GpXGpQChX20GjnIjL1Y3UrJg7wFA8DHQ9m_4VYyuWhacFNsyahp-_sN_HYYtgdYSM2tS_RpqZSbwpH-ccVrpCm5nU-iE0HDZfHyXnwrOQlBRMWeQs-i977hg8LT6933YMjuEdfjiHOfWyAi-wUD9fMx9XhCG2cxW-nEv0NhQ-gcOjkJw0K4_fL8DujfrhLgNkOSs9M5uEtRg6PqhPxhyRaL1t7GKc3cM8R98D2Sg-u099vAUaLqpZ3VX5Xi8wjqiZmdm3IuTZ4c0TLozUTMQJS66TKUmtseTYbi7ejv9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرینات امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137975" target="_blank">📅 21:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137973">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
شرکت یوسف جامه اسپانسر جدید پرسپولیس شد و قراره ۵۵۰ میلیارد تومان در سه مرحله به حساب باشگاه واریز کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137973" target="_blank">📅 20:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137972">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137972" target="_blank">📅 20:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137971">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
رامین رضاییان که هیچ تیمی گردن نگرفتش امشب با کمک میثاقی میاد فوتبال برتر تا از سگ دو زدن هاش تو اسپانیا تعریف ‌کنه که شاید یه تیمی گردن بگیرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137971" target="_blank">📅 20:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137970">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137970" target="_blank">📅 20:21 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
