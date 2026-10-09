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
<img src="https://cdn1.telesco.pe/file/RrY3ipNVJazPesBVfjdb6qyxic8q5D3M0UPEDCpBHErTKmCKMxYX4Lmc_qCY96uzub0kBS5NE0oKIuymaP0yfC54NQvMKcnAi1yUTd0VRcLClmAxehcy90vaYh_8Hc8ic2DnCj_Gr-ngJwttRfdUTrMAhP_odn3F4FXv7BT3W29aP8aaCENiqYNSUcSGS_o-UJXMas6RzFKgOeJXo_zWXuyux3H9nwskGTXbvPWW2rCryjHpgT77-p7sNOPgVw3obxMYn89uObh7sDHCjw3Or9EkBUG_dOyjzZx7G3J_F6-0AWIK4edmgvBCIazrPQgTAX2oJ6O4VSx91tLClHqwqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!
آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست، ولی ارزش امتحان کردن رو داره.
🔗
getartcraft.com/apps
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rHvt5J2mNkrlVPwELFmOI7oCkj2NLMSWVaLxnBdHk19aA-Fn1FGr9lYaqkay4vYmngSpsuE0GoSntDdD7rY6lu2vggGjLAn205QPOpU4bipGtc-gpd1x1-UN8u51xs7TfBH-wsbjVVh0GQ2K4UPgUhXjlNMxmx2dLzhN4043b0L0zrB0D4NZLzTLWZRhwaPzUwwMr3FzXgroNJXFsHa6-VP02bY3lgeg1dRWEw4yT3ECNp3N_UIFX6eGsw3na4PpeKn0XNmiy2EPN6FzZ4edUf7n8PYdZz1XVTFAXs3ZIYv1R-WUo97ojkoGGvWkoks-VhNE2Iyn4qYr10UqUwYF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWyav5yP3bvyUaQEcQXQ6VPsgJ5nYyZ2nQWthzQbPCiqUm_xlr3D0pe8hu3Pr8E63gn_BK_cl7zYhngTnM0RK-redimUzRjjhUJuE3YBhjaehaZoKjB6xuyHY9Hy3ni8hP_kQJoUm25oceqOPucqFyJot5r3dPKkSppHmlUiU2kntCFmFvvviYq5UAGX4dfYwe8kF4YL1xRi3bmutlcRotZtM3ss9gRNOI38D0setQTFClsAqoY5VVxUxAlBe2VQFsewyfk66oASJDFkFrIyquJiVvq-syt9t56n3Kz-9-43YaqXAtZp4hZhauQbkkzQJbhSJJo5enS3GVpKh7jkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5543" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBNBmHgp1paoOQ0HV52BiQKVGZ9KkM5hPVB-4EGpbhm110m_fuv85jb1UKmCjfgAQ-RABtkPWZ_Hx52PNLWWNve9YDAIDY7iHhs8t9__iUTncNvV2iw85SkAipsCg-nPcMV-_RQLjhVNLQwDDkBYLxniekLK32Y80oeUmSugW2JGXUBRNAwdybu04IaCSM79Y10Hepe_54oecq6valOEaw_aN1bM3bIvR_sltF4zZXPdRnx-r7u_0Cd8EjKpDLKXddlY4KHjw_wtEU5v_Srrj9Xzn-rbIxOk152Drb8lQObzUXMlgQ67VgN13bPPdgMIKr0HYnmrI-9-vEV6vlSPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=BipNSNmF7DlolUQicN_ANwzUyirgXUeM3C-vtP0qufwYr7YDFDTWd-UYOXAWbEetEbiJ4nxaro_7ELLWtiN6vmJneIWT1KV6uZXz0BLfJT0XGD8mBBe9bfFsI6uMwGvP3RimdIuf2Gz7GhlAYAC4yJ_endqHNYzsKZdmqq931S56Wz_52t5_vbB7UyoW87hS-RisZILXH8z2GCBi9GRueiNnXKiqBzU6oyH0-9GmaPQ5MsESACCSkO56I4DypRqXc510v1HEovyytaLHUaTbmvAMqyAzbF7dhLhoY4mSm47xrgoZpBtQyUeLGFpNss1RplwWiOzT8Jbm6byhBtRAGCSsjPZHuUleP5uTSvt_itYPOylNUyz2J8O0nL919xRYt9IBIOTBG6L76K3gDIQJJ33wZSRNiXgBA7WXDdnhHilOJx-hA-zIJLEdJMCRXet4dRPT7Iu6v-H7EOOo9xj_bGCQT3PzJOMfrdbfJVHdLiSkFITd-4O1I9lB6QO43YIYYt9GWHJdeKjL56xhzv1bNhGb8SDaGWCgometrI0J1uXX0Vb60fmZCMkoRVcVLIXaYhcYHuFVS7eLL1Q99EhHBXi-9A-_7yKse8Sp3BrpZBLkqQh2jJlqxMDi8LAH4ZR1fMgUDBwXK44xMeUfpNBIIKSjVvm5I4KyE_Cu5knjsfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=BipNSNmF7DlolUQicN_ANwzUyirgXUeM3C-vtP0qufwYr7YDFDTWd-UYOXAWbEetEbiJ4nxaro_7ELLWtiN6vmJneIWT1KV6uZXz0BLfJT0XGD8mBBe9bfFsI6uMwGvP3RimdIuf2Gz7GhlAYAC4yJ_endqHNYzsKZdmqq931S56Wz_52t5_vbB7UyoW87hS-RisZILXH8z2GCBi9GRueiNnXKiqBzU6oyH0-9GmaPQ5MsESACCSkO56I4DypRqXc510v1HEovyytaLHUaTbmvAMqyAzbF7dhLhoY4mSm47xrgoZpBtQyUeLGFpNss1RplwWiOzT8Jbm6byhBtRAGCSsjPZHuUleP5uTSvt_itYPOylNUyz2J8O0nL919xRYt9IBIOTBG6L76K3gDIQJJ33wZSRNiXgBA7WXDdnhHilOJx-hA-zIJLEdJMCRXet4dRPT7Iu6v-H7EOOo9xj_bGCQT3PzJOMfrdbfJVHdLiSkFITd-4O1I9lB6QO43YIYYt9GWHJdeKjL56xhzv1bNhGb8SDaGWCgometrI0J1uXX0Vb60fmZCMkoRVcVLIXaYhcYHuFVS7eLL1Q99EhHBXi-9A-_7yKse8Sp3BrpZBLkqQh2jJlqxMDi8LAH4ZR1fMgUDBwXK44xMeUfpNBIIKSjVvm5I4KyE_Cu5knjsfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sPrrnuffeWRj3n6bmt-r9SYaxpJl9_V6L0bSpVOB_Ufsk2_SNc8bKVIOqtGgA51A2kiCuZTaY3w-EGIj4SRLxHX0LJ_8pfkA3CblffGY4_yOmbzSwlemPl3EMm1QC9uBluqfPLqd40PkR70Ak_w7wQubZ-5RRuAtrvzEUtEQdcAgDCaY7P7H32Aca9iDj6nA3cGxEE2GHaIyciwSqPgfoqxVbIJaZVn74AulB1XqEaFLDmClMlJbgURIY2HJyK-_FTy1CRUf15x33K1eipBHEIVn8Udk64O890y790lFt_eglWWDXPdDQrdoGnDOmRFXsNGlBVhe-01PSX15W4-Ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S0ZdIdjhXO856nxOr98ZNehJw0MwVEbB5lQiq6IyPLMet_I1wGQfXJL4nqTWxpusFZNUy1pqmNbkCYFH_dZ-vRYAKITgftVgLM8IuWiTTkoGq2wuRl9EkkYaNDO2RQkVxHidjOZmih1oUpj8VFjNsHfv73M1NlD3Bqz2mid_KMLV5tiGmuZB7YzqQZjnFb98thlVceRhriznnH15zq3Y6M4GIO59_BbpgSVvwa5t2wu5Q9Wo30MTqUbgrHMvhcfbTYmGRCnRkK7Zo5h55pKIpBNqAaSPHP3egzljYT7lPYswwfJgk67qTa9DOwkLbBNuKD7r_MuhFetP-UHiCB2HKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUOO_og9lLkm7i5_6G2zHgYBjKYRmItT-xYV6mDBOhHr2PaO3wjvY6rgp5U_Y_usNN3A6LRp-KcYhq7Hfwy6nrXUEau1rygbF03VkPKzPMuXoIP2VbtGQgkhDm74cEeAGVIh5XXh9pKTPyvlBu5w4RzQMu64JjbarIEGTZ-OQSeMlxBoy4azjJ0_AVBwVttugAKgGZmHb4p0eTlN-U164MRIRpoiRrG2VGQxLjScLqPiPExXBtWsacJYYI2rNBOLQk3vQ4E5DICHD-OS625P1zA0HEAt-7QiDfmPdYxQkvIgDrLeiLM-ZB8VuKyAinqgHwakIH8s4MqEQaT6aKv-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSewvy7UjgXf4ArYCYkwa4Gn_SSZuWiy6kMQolmA30J8KdYgQQPeYZm4I6urmjD5T0ctco4fbKwzbr_QihNrHvqLIPPkpQbn-o9iFIk4E9OEl5B7kTovbBCRgFRys4u4uwPmjOoArYq88_cyzrFzTi8J4TRXI7_sT1ZcBLcqieqppXTX2pxE7zHcLnPL6XAVDGchEXhBDMniXXwVE9rWv43zgrreVdCWi4J8XYV_TP98bmn4Usk7I63lSHA7Z1ldN3CKPWLpxpRNoQ1m8zd4btUgfX5QbjO4D7tGsgfxWX2N6UVt8Oz9qu_ehBOG-ELZn0kTdQnTA-yn5vSe3C0GCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAyBJzg3xScKqZs9JCF0OL1qP7Y_J0eO8Z1yxUCJpjbxKy09RulpNG9aVcx37pW1UyAQTo5SGpV3tYaKbidn3MQB53-CQ1KNEVWoYIBrkpr1W1qDndwt3qGZfSXDey9P2gWwVieyRutrzm6HGd36lJiMV95CXL3HbvxpI1eQpFZmsVHdBBrrIOCP8radasEmkar8NwDveX-78R6jkls7EqozAoTskRDeAurnTID55lmKpe5B-1mz-LOiTj5zjJYangbUgbd5R3sw9OyQkXxjVeRO-8ruY5nBW-yDfZqLu-JbQBVYkcYmAO-00LY8RIfEYWDomVPqdNrxbBZjpiA-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJS2rIVduuAjSNwruJy3JXftiCBuYpdOo-Ei-XEMVbdaMpJEoVqQaXtcSU49zvwaugkN3nHB70ldTB-OeR4D8a0Q3xaLWiymliPuqUXPY8AuuZzY5i5YEBuGgAPSr_w1emdKodci5X1g1sC_Rc1wAHCXsJMyax2ShfjEqGPLC13cbjKpXmsptYqA41b0EOApvE21UTa-uS3pChhAbHc01SCj87oj_-l1xZtScEV2xFE2IVxr2b-CENCXwMyfZC_Ed_rs6z5reHdhXnT2i2K4MjTQV4ppq10Uiy2I93rwNxQ5gbA6Qh9EZmQUP7vqXtnHLwg4TgQET9PF0x8hmN0IzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfWUlAhVluWt5XxgN42pVUVqwr1DC81rqIZMHSD-cZkNT5DD0mER2c-E_4_ZWuLDAOgSb9NKyWOn20vN9H0xl_FdYHQ9rl5OomUeHSf7HLAuLlEYjOBLed9usYDItiOQi9Nb-Z1hM_AH5ITf_a57SAfQ4RaAAwsUFcB7B-xucOwYcBtbt8hwDYl2642iqn5uZEHLPnESlgFGIKGYe2hzgmqZieiK43d5hA2XHl6yeuYBjBsd-SNyZFQy6WtGbUxllseUXuc9AAYT0qonNGt39-LpNWiAAAowZmIi6RqpmI7ZCHHxddIqZhiOJItayL84T6TnPcxGr4JsgVVyIGQrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BrbL8592uBHTJWgTiQKpUXsLnBWbv29oZrRzRUcvWfpFnREcQOs_s0_FbukOkmOV6PTdyyKw7ENqSw3HJGn_dcafk-PqGxS2Aa2vuPCxN1nO6-wSjcXL5cV9JEtiZSGI95sPAuyS4drNSCpy0aowPXO30I3FQvaXh4aQ3BKQ8Uk2zewmYLLqL4nnXiv16NlF1Qp5cbBhw_z5d1Uh-oqfanMLZFGrgLXxEFqJkw0iLHh3RrvhPB-eetZehgxiAKxzFaFkOXyCxrNy1PnsCe2YnXH1anQJWVbMD5JrcoVtc4jOkyTpw7fJ4K9eXogDa7zvAbcS7b2tXkVA-qm3tiz5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F5_HZYYtFPVOaW8YjpPNVKeDjVJySpRv8xRALcIsvVQjAFzkPgo11HfVp4EJj7GMo-iscvaF4qXnO_8ndLpOSuTwoEC6Hm80-zfkxqAKeHtJd8S9gbXzDgSQftXPJdkDzjtpTY9XAS6jfQk0LlipyqJVcT1_yO5B_4fpCoHNwvn9UWpji8gvaKEsIm1fnyazhffM43rZJqg5G8BHXQOMzqu8Lb_sqb-NF4folzkQxGt4gFkOOamvrztAiRGaFloztO99m5X1a44FMf5wC0tor7i-S56pIJlzPa_Bw2tywnU7Bu8l81OCB9h3X1Pof-THiL_ecr_MUuQkI61S3FS-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OcLfdYvqYABvlZQ9JK8CW0mLKEazDitI3AhZ6HZhvZpgqRLyckJOM3eMjZcjXBNihLN6xBsRKtl5yRD8x0KYblTZQcdiC_rszLh8INYe1dABBXe_Hf01eaGoThWEI3-TXKMb7zdjbpC1V7kZXihncMD-OaAkPkuzN0lkhfS_D5qZbviXz9C_9R89jG_7LQuBdxFG0VC7RDqX1TlD4E7X6Rmhc5lbHI56P6i8jQ0fJl81RnW0nE2dwRefDPyTBQrtWrk1CZjQOYnXhdcP5wTT5n09XUEWq9NfDmeMUZgsKZIWkn1T83MOVf6M47cA8JDD__xs5hTO2OmyxWysLF9rQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eYeY616zwWh2URsXSGt0DGhn8bVHWPC7FJ9kYEptSNiZlcGct1foNfGtYHZUWqzb6_n70pEZMHp2VVrP0BIq6zvII4SKuWHztqOiAt4L3LYYCUdrU3DeG1kQsXn0vaFZ9MftRNddjE7YcQsWLFsXuJDlTx4E7xnhBHyDw68bMrW-qUdJykCmS-mYm573H2ZYZrbEPu29nhQQrAH4qOMWuFyZto8sTp2ZTSeIRIk2j9484yBuf6FXooVC9-gNfftFMEndPxHGwwccCIwmtEM1QGAmRE9Uk5wxQCEyrYzBmzW-NxGK8nvtKKhm157Kq8hAlSUdoOHoN_XbNO7n1CENuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2Lwk79XwqqrVipcuNLxmmpChTvDO2SmUWxK7ZKmQBJl7EMGRxifEIQIMsu5sFxtOZKefShb3eQe7kltyIkoHWBoOQmAGzEwe6g28nMzXlCYWNgecR_fQYYlCwgWGA32fE5LlgkJs_jlvW4eDd7G_EyjsjJAVFZPtnr9yiY9UCbcSKqOl7zPz_sV3j2v9pRxrwniXPfg77UUYlcO0iXcRbwaZKzjwNwXKeitOL9V8fSgaJD1iNiFqXQqi7GX9P4jr7yPzrz9pLh4RH8skbCQ-NNtrNlbiz6dWBclVip1pz5oxNg_u6kRuArfcPqCuO95Ht_QtDOXq80ybxOGnRnm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JE5313KZC0OrZP3qP3lzomxW_tC_cw7kj-pdFKL3P5L2yES-7vuDgo7kdY1hSwOZs_sN_U_7vaKzORsbh-yiVJxrhtFMax4i4NUtYV76l8i8JRbktuxFVhyKLpOgb5lTqA1hlubAu2qthQTcqh5XIJ8N6LiJOXRQmbBIOm-1QfmS7yugQdDg_766dQYVlG8wqqMDpB4eli9nhA0niOR-RP7OYl7QD4qA2WjmvcyucRZj2NTtqWeyHnD0Kfnw8FDzB6bZvIprGNjSNvGRQNBPArYJntxY6R9-ufvNkqkJV_NZpX6fBpV1vf_NdCxLBqE9uxvG514ZQx1yruMgMYzBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AE6OBL79GBv7HVYU7d20hH4azvw6gedcGOTh1gxaruZD3P4tuL_B8kzfioe6Ls0dkJKqD3rpRtahfFLwCPs_AMh3EqLJce4X69EzxHTjS0L-ZkYmHqtoPrfrTh_m1VWRUBZ99annVSjiGsM-e2K-o1yKTfsDZEl3aY03_vFvfm0AMIPv0MjmI4xjD1cWSJ5IU3Qn8ZBDJL6RQI_VsRcifBhVwtB_ZGVbIQg1pb1sRKph-yVJpzijF6zVq4nYASf_Jj_3hGzBAauElnxsqPpwmr804rRHq5yf2Xr_DsBKQG4VFSosHepIXhE_QK_q7NSZ_7hBMH5YSBy1tVBAiB4dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vaTRvXjLXY5rDtG2tF8xC9UIrIt6kwB3gX0kYp8qMt3T0yUkX2YOvUZ1SnE_b1jWvmVsqlicpsksWDTCz2CKRrFf6OS-N9hboiT93J303rI9G0TXRwasR-zXFCGrT36L0YV-m6Dd-P5tZbTi-M7mev0cWEr1Th2IQLCyRg7i86l7jgZ6zjfPZcL8x1lTxnSlgxM4mcnwkSjAaC3tl6NhCKK2Ny0zkHhmgzOPGF6SxenRifpuXdL7TdXbCsvDqbVghEwNI_uPyBaxW2ggYEAmCkaasb887xiOvbEWtf9_vQvI3y3FnJyiQeflV_1MfrcEVup0iPveLvnql6tyr1eGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aq_0qSbUtj4TnpYx4IUkTgyZAAc29GBWtRtWVQKE3rqMrmjCM2gbzozWu-v7TNG60zeibgm4AHhu_-gSJeeJBYp1m4oMmwN97mH9mHpMCDG71XxG521sj1wquQiY2HUVi1BreO9K74T6Uua_lMkEU3k231zzGFkIaiNIildB0Z0AB510ufmthoNQxi7bzml68RhMLYxSXeWC5ZwH1hXuY0SPUV3WAG0lRpLlEtqBXIFMUOX1LYYLGcvFsK7_ofFc1C4p1dVZhUatUMi3EuD_o7rvr_97iKi0-azVvT3IIZrq7OCFVP0vF-jiJwttyli_y3M69gMFspVVlmUzQs7RUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wg0pnF838ZmKNHcLwOUtKOnqiK10QN_q5dzKfQDKJwFojzGMgWs-_bm9CARDIs1I5xUeUt1AJyrcY1lDqHvWbFonxpsbs9LlRkelvmHzGLFW-Z1Xrz-TWD2X95J2EuekmySEK_0P5mlS8yMzp_h-LaZ2Qk1wIMOZ5ppCZB4NKr5kc-tPO3g75gJkZRhn2sJOxaXJDOSNxpG75H5M5YQJwKliqg53RGw9oUHo4o0iVweI1dC5pQWtFVB7KUPLBNqtu9iLZLVQX0DjMatdZU71rDBusj_Q3-0DQIww5abBLEWyjb81ZJdDj3wmjD4JA1CUqQ59HMphFFGiavLNsltOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwa5KRq4Df5-Z592TVYwtv-ahms3Zbt4J0GqjJZzVpLPl-MUJMLVTE7eX0ArszgeDD2kfF3SsTwlsih7jICX-S4Zwf2OM_BfEtMnj09m8i0UJT20azz5XjC8JMhqYtNBcAsY-QVD0k1UNLcD9Xb4jNR6hpqoHpGliI4QgrgbS-RkrMcxJHeFzbH3cOd-_0U1G8FN-rmxm7YqZ4BlSPmfRVgLt1iQRR96Bc_TY3rIN-sR84sP8T37PUChElN2on478MtbX1FCd6qS0shX552-2i12Ia6qPY4-C0xC815yjXzZiL693XiqQsRPQybDO7yKsoYP03GEsNTFdN6_u6j9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=V4yNHP8glwImjSAhaVNzFO1igLXRnxeAhXq2tJ0OvrVbCmrAKcxbJc_Cfh672Ca_rqYj-FpwjgauPQSXeiAJ0A-9cTC9LIXakc8P6O6i4c3WaGWOJ6S11vh-xum9tcLSjE-Q11Z69Cf2gxNSSx44Vb-NOHrx8gfhiIPHBUurpMjTTb6g4YkMmo1XIFwsmIckiqLwmtxBX3Oj7IklbyGMWXpqMVrPzYp47OFCGOQPdcN1HI4QkVMEvLyuOzDYQxKS753uEVxfKEk1n5nR2aWnEgQgcxTgXsQrwIze3E54WnT3ZAgoro7DCXjRNcllYDty_LMvgrqN89LCXKS0UV0guQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=V4yNHP8glwImjSAhaVNzFO1igLXRnxeAhXq2tJ0OvrVbCmrAKcxbJc_Cfh672Ca_rqYj-FpwjgauPQSXeiAJ0A-9cTC9LIXakc8P6O6i4c3WaGWOJ6S11vh-xum9tcLSjE-Q11Z69Cf2gxNSSx44Vb-NOHrx8gfhiIPHBUurpMjTTb6g4YkMmo1XIFwsmIckiqLwmtxBX3Oj7IklbyGMWXpqMVrPzYp47OFCGOQPdcN1HI4QkVMEvLyuOzDYQxKS753uEVxfKEk1n5nR2aWnEgQgcxTgXsQrwIze3E54WnT3ZAgoro7DCXjRNcllYDty_LMvgrqN89LCXKS0UV0guQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDmfhJtVE4eJypEntQ01ciIW6YNWBXOZ8i_DgV3DZGghoSJ4yncH6rZ97diihLO7BEHwmDrrWB-6ezK_8F9oa385Fx2bDY239KH_ErubkmawXMn1thM9cJtHc4zGd4iYJg1lTWp1ZZQO1PDr9JzMFS2CXn289bllIb1RWL3UyhILTkOBr1_HArhR2lpPauO9Lh9gz0ZoiAEmFA81eOavy06bb1Itn8G4Qd5Wk6Nw6nEMxZbsUAmOgkSOUpXpJhCPfjlQU81I__Cb10plx_14F9jhpfy_Gun_Q0mOuezIdK-bcaoDKBOE7X4ufw1FH3kCURreaEcEfq7YrFqLiIcstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NvV24TGPpeuV9wq-blYQQPg2_xxGt7oP7TjVBNMgVWg9yOanW1xLVvRmyY65IRwtttaidaGnJMiSHrzhqAG6VyoW7u35uRvzWqbHc8x1XhrR7zIS6ZKJ0ggMeqbJHk-9Dy62swOrIemTcLVGOmj_4yOHDXIuyR8gGRrjxel_Z3KPJC7dLgt4T04v8gRIU31BuFRQIM3B78B-cOOjXeb5Y8c7TFL2UJBAtRtRgKJdi-f2qVl7pwsqsfkGHVajR9sbGH9DwC9iyOtfQlxST9XCLTv1gTQ0ZOiu7F2ngjomSd7MWo7AD8uOJcEIs4BW1nn3o1k5xXB1oFuZftkP5ePfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W6UfVOTUQFyhesVs8LwmiKTCa6w5ATUu2q9ZrWZdTUJy5vjsTvUzLbdDDYUH01PKMIwX6xV-kSsY6O7GwOGviiHlPyyFWmeahUfHa0PK94tntQJ2Jr8ZkzS5ea2t8MXSTU8OCFSjtXzLWOCaDN-TvThoUxIcGyLqUL6eyQEhG8Y8EcFiPHLDN5KBzNzT88u9rXH6RLz7ptymi04b0s6ZIwTydw5gsAXRgRhZckL16x74yAnUX57Gul0zJob2-UuuHFvz_gtDqlbMV_zGfchIwvCyg7On7YNuDc0epVftQjgzeqAhEt7VNrjeCobbBcOKxilCTJptFxyKpwP2wWrylA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EnaCCmLlB3h_lyMv50nNHL1cLMMaQUUnq158RX4BS0JtpHUFSySkX_bCBCHPBVFMag8xkhvyk8kvE97XlgMVVYcaXjtCoA_kelSxX50jvoG9m7Y-NtFHT_RCV8dykV9B8l64y_59dJFIBhEgF-myYRMpGRwVz9MmJnKItVM5wkNqIevMmbrk1ny9hCLT0yrrYBsNvGpJcM52kt_2bsyXv5WAWi_Jzgp7kEBB0Oj5Bnpa9j0XplUwHCqpW9OJuQ7Q3_ZJSfBkPZsRACKKpXvqCQy9SiDjWv8-Bwn91J83Rv-ANucOtS_QgwI3CTAo8CGF3siqoE7RFTGb4cF14RONKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIHWwdmVZp2Bz0OW_N3E1Zcu1-qKNQYq_kpG1d5b3EGjA7UOTNgFrODVrdNHT_hqQ_F70cUXZkD0cBIbdUMYCy-MkzE1S7IevXqTEEDVz_ddat4QtQf0Mh_mAKfJtINzErUMxbCnarXa9VaAcPEuYHPxwBTtwfK7o9ciflgNIZIcgs4MxZlk1QvNLs9AhyPXuCeQCUCEkOz2wbxHuS37xiV7_SMWfsCaegSX3VAG9BgS6ldUS4ruIqqxE4I2QdwDI8Lnpw1SRUUByJdhsXiE9N43vUbhoSrIW11Ch48EULBMz27MF3z8kle_FF_5sATv7ELHTt7ULkoHLnNJSG_Whw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gI0KugqG4wkVU-vfhaoj_7ie1yh7Wx55c63ugiwZjEiq5M8WZCRs3fByGRiCMLY_wiuKWgX95d6Ld9wJH23IyZtW30f1EsOKnc_WH32Mz8hba1_vTGq-93Bqg-Vd-12ysZUFaBWp9keo1getoap7RZH4sOjL2WGLxhRwdFlwuaRC-zTKB6oQOMJrBGk_XzWslmhevpC5SYEmwNXF7UteslCWgSswyciiSAcpcJ3Mv9XV3-5VcCVYVBT76EkiaKw-bfxyHTZUAQyAxnCiI0EKRDBmL71P-LX8NXqNlkgnNNTpqV33sipsVTLqP05WrO5x4JqymAvuNc9_YBu8nQLjOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ9TTqyJTbpyokriIn-BRGn4CN0LiNqGaFpe4mJw3ZcIwBEKgg5QE6lBP2h_f-NdjA0SZJ9M3aEck7NqCwkg0e9hFPdzVjpiWFXa3dxIhu7KRqpGkX0kVcCjdX9RLELaDMSFUhe9msziAmF_hu2WCMQxPaY_TdkPDcz7iNCUyH2nFaHVdDKAFIv06I-IyxzUCJsgfALAqkgSNBVvImftGUCriA0G6rruYTfogtTYhdU-kW2Qm6QP8MhorNEKJwqvwX7cNvCgmA9_C1bLEDnoawEDCtsHnAkYWUrFSZED9PmA6UAjCYHeMkU1BEh9yQNVQgVO9YeBU5T8GXreYzOycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JSQNnyP7tm1wrxihhyEQCQGFY3fQnOZo_n5OtRtXVprvYpilgjE_2-VWU_3MFR8aXE0iJS5gztTRQwdL2hdXD_ueaO7v66EHAPmczWdGq7e8cIm979tdsDogLG6EHGQ9J3opvss3c8dGx9A9zgVGuuj7SdHEXT-2DjuAAmZXhjugE5c0YAj9cr2XdNuUbK642eLg1k_oValu0DMyTBmU7hU2Pv-dJ5h2XN2C-wgh0yoqs-ITUWUzXcus2zmDACcQJz48WUdP6kKIH-zE6crcBcPZyptLJHgCr_HD_0SLfP_u-VSmHwnghOA9BRn5Bx3UcOZj44l9yu9NnSUsITEMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sclls9QUFo2V_4DIGGhFMyY1c_L66yXttkfi_3abXMH9BPCstQulOtrFQXJkgGaVLqizgPIqdSKdVA92vkStItk61P3KyArxt0hlQn_WdhMiXDaNZANVqQJhaskJWsbG2LdVX7hMvwfrrOpGLDJkfwMv2NrvpouHAnBSiULQThmVk8_qJa-Z6NgvBeyKwee_RyBprhDACHGe5DNsZ8WVLSjmIkUSJBXc9kQtgeRqSuhF91AFzl_Z_1sxPKe50UJDLnACRBmBrYlOHywHuXe7pFMUQ6w1lafkHkh_LWMWdC2ABXD0Lzkjhu1ZtCco6HYp3vDCANB-UgR0gAJfJAidpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sWbXsLrfg7vmCXhMZm2udUa2eX1di5Q5STS-5CIRcEy-hGk6HSRXO1aGhwxxyzdfR-3iwkUfqmw60E8gCCKHDcqGpgon03Hyc5aNQfCdglVuENau8ZkCSbLBCazoHgsO8KKram_cFDGvTwuNHV0lv0GCEOmW_huTL1ElrJMooiHi-66XF-2fr85d4zCCEPG5_Ov5fUoN-kmPbBL4_H2h8W4HGTdZFDaAxktvcVJUX4-gXUGICd3ofGfQNXJnrnwbxv1hfAytFTyqOPWvvwpWzxHJlL0WMe5vRr_cNLsfYvuSqYbDIavQ1S172826-kPegP-k8hK1_mqxKB_4BB0y4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lT92-G04QG5dKf199fbbp1ygAV7g_7XfEn-V2fPsS8FcJq_m1gPF7-6RFJEdpNd2Yw85m5zJz8xdBNK4zBniQ1lhwiiDTgWCqfvEWNzAttCQvzBMY6oeWN4mTLDbJXwpDzSpwPJnxZaP7-lTb-QMU5BR95DeCv9ptCCMMP_QJru8FbUw2qURWogC-j2ErtA80AMqWcJq0mEYRiccFEQTC4BUdpSVtiXHNlo7NXYUH9fDdchR3maMbffQTVHffVCnqkTAqNwmK6c1kEPkuzj_xM-dOMiPBg8nDQ2YBwgvIlY4qdJdaZ5I8qhFfHFxFo9gGLicTzO3Oq4uJiGAN30piQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV1Jmrj6IM0gwfiNPlYQ-sONNClcjuSxGkAvb33SrCxbhar_mN7X0hudxf5Fb3SvDCu3Fn2NfnwhKKL0_QgUPvO7XwAYU_8ENAjGUDmSYdjgGKij39n_MPpFzNaq7iKORTTMo7hn6rK6qYKL8RD10kzHQsjwrEq_WKLKHaMWpQqraJDvfKHie1_GOLSXDg0N8EQsF2x-pHSHBIecYCfFic3g9Arr3CZqFcSf3hwNImJpn151Mb9ZrJU5Cb-dMcBU-2-nWWnRfNTDsIpPLt1U9ZO7lNVZVU-3KGSo0_TkgXa6_Tuk51XnXp-00xSR2-cTvM4gwNZGy1x-3rh7-EvQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gVVyPEgzboTJ9Fqg5Rj-0HPDs6WPAxvsXcVZOMVXSqhImbDTkTGtZgvuFMGjZTgyd4MmqF1T_vki6ZPCYRGqxFd2jdhGWUlpBndof4qFJisOAbpxIN_gESLFlokRun0yEK-3rSgwBGr7MU9ZvOMve2yYbw9CVkUsdEsIMts3CcgxE1MM5Z5bbzivrIKNS5W9u0IZ0ShwmQHFWZ-wzrioOln60pKD6aG2uh6GTnFdpfQkKo-pT41N5fYgdQkgkUNtyKbjZpYmTgRitD5T7hFH97hWiQpIE-sDv3m7b4ukDkytoYG_32tIfXb1SGRhxgv5oEmYLzo9-Qf9d9aG6GE8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RogG0wzcaeW2t-MZmwXOAojO2yW3rgGQrMlpfkICoEhZcVlL14NltT6dFgwIYyKHdthbBeizQQ7LRD9VaRqV5imy2NYrq4kO4KeafUHT2If3vIkwDiK3Y69ngnrdNDniVn4QuX2WWFymSbjvX58lnTvsr4_5Ydpyr2MDjdUc-W-gNb1H-ni4H31UR0eHQv5CEorLstxQgsko5q_M0nozAYnFNrkQWDLOEpznXLAXyhLW0GWzXrJenFa_Z4Il-5twupk9D8zgfB_vwz4uT-Z-54STZTLM_T8algDrJKLdOxvmEmd2SRXlTLJGUG02h9bez21X64K28S6D1gU9E2cPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vp0VfTeANHjqgHkC9KSj4RFSkrq5C6AIkBs4xGTodFucmlVBOjEsXoNAWNksw9OhNxqbFCmbLqUZMg22u7qSImAjSVeVHXWusxkdMFYxkStSfsGazf0b4YA5ELdC1xpDykqKQibwxrm2f9LD0Un6SuTGt0YH5z5k6Jtr4QEdgl8Q3ri8R_WDqQF0IO_bbrawwXRuFJyyYb86iQL89a72AnHIagpZwd02XJr7t9zwN3C_0HYjcSvbh3Bq9ipvIszq4ujL33qhDPHjNZ83DhU2Ll-ky7sTbc0WyTJ9ELLHu9VHLO_QzcSh54f_LBAy7zf6s9IGPw0pmgEJrKqutMg5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2tqVfzXtGig6E79hJ7QGAsl2mZd66IEP5U8j2UUjOw6LSlnzHdfJWa9mPdtSM4OrJyATwLpf8J_AJxaOdPUV63PZO5zaJTJvUfOL8NQcukvE9d60VnFE5vR7V_NyzASkMpe2-cGCBEGH2EsZIXzD51FGJXvHXfb5Z3FERpGcRcFBbhhq7lyJDItNt7U7dGb8uAAVc376LHyr9PVSR1DExXEjpz2W5vw0DkplkVh2qcuvBcGPZGPgK5SHpAXU2n-vuQLbOdMbq_GUJ7hB-meHYvrYeTE-U8qsW1ceXsTOg06-yw43O8GbhFQTWpkL9EdK5KTZ3VPW0lV1bWIm6lyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J0C0LlpXeAWXXTtFfNBHeczKvTzyPg-7vNwOmjiOG6NTQhedpQtbyDd0FN5DiUclv6DzMjYeLh3L89BOQ0qAuhXV4uZBiJT_7n9ssV2LtUQ-uka4Q351y8N5lguUgmPjXLKvBC4IsCPaqUnjla9_8cUQUPa5UoX-euV9XsQi2vMkDqJJR1noKbMptMppilL9ieGKPdWnOs5nHieNhFOpOt9EsVpKP1uqThv-JnmAEHDKmxGDSyChsisYqGAvImHhUQcIUVXz5saoAxVDesUWT1XG3E5rx8NwsfR8uJwmhujw3BBi4iniOzeOenie8HYmOYRwf9YB3WgxaSejNPh4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CB9vqqFdFprOocHE_w0BY31ww_IsKav50uKagaLBWS7KMg2vYFRSx-LuGF4FyOG59gyUMtXmjCMW6kCd40Bhbfz1OKkkCmfKxNV8PzYa0hfNPw9lagPWF4fiMsiwnH99BfegXclukKbdMIyiR_Ofg70IlX5pSQLRV3r8eWOzU2ujbaEDCQptb0D7cBydb8zjlwHaK9fYeM5rEzKCaAXgD8Ri96L508qWSZ87TigXo903scyKDGAQM71S4jtQU7wZ9bC-3Xhk1OYwzc_fbH6NYQSVxMNRWYOxwW7xwNWTmVufFXtPtmsHgy6vji6f4idJqBFEaxnE1PTo7kRJKBm0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjboWbTMrZl07MpHm8CFQk44Bux5nbj6S6DBPSXlb1xu0A5ocX7UNhG5A-zT1W1uajEJHzPc1TwrOKBTa1d37Wj-9arqciJ5fJ489v_PpHmRa6zXv31kZc5slzrgtYz2qTYfEOSSyZ2WFmOosGSXQ1XU-r5GpwFxH_wTUu3tbDqtdSnHCLfxyfVDvmwPDBy8XJgxTNb55AZaRMrCRvg5zEdH3CPxFo3yjkETSaYGl5F7s_OL9hkExFkxC6g0aF8C9Nt1e08U5ot2SF2hhafxaL39u83aM-Xh05iDGNVaoEa0qdbElrHBr-0iU_6ozEtPe4GEuKZ20SwBnBipmaO8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_Kg5myFxPQQakWgeMm1o1qrZrh4gVi6Zr7DXWCKEIOLzg6W5eXa1Rz9963WGLr01YUAffH28Uj8sqFme5pTzoSaRB9VYuWjyP7DV2-1SE_7dM05H3bpstk8xRuRqfgR_oivbCZ0FCsWFMDwQuI0x88JpfNPfNEibfTG6Nt2XEJzoQNMsPfJ-izamPG2PG7BIipNmuHXukmdjhtXw0kLgJTZMBadutDPLUtcvZ-urPa2vRzSeLYqEBjVxXfhMZr0Iy-xkKna6TeGHc-YTIeKKnEJfUfz1-7NBoabOV8P23ZHDbtg0bLpLw9hR7p0fnISh31nzfrCpXjUjRu_0Otg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LvNPEiQ26gmiJinCKqs51ejIGuV_5nNy1c3i0nQuBpO40nxBjzyfzb2BOyyL5hok9YbNBVjgH47ztvWmVDiWLKTxv6bvOZ4sBRhu1QSojlA6CMMrJRygzJU5DDkowexwlntNh1gBy5wnuzxFLR0Ae5POJoYT3PaqWHdLNKoieUnC3owrmD8espRngHDq2SlagEBE600Dfy1Lgr1yQ5U7Ntj8Av6dr0ooXDq9xh6rtczFsYGKkmw2gfA_kuu4Ti_4k4hruvOFzf4D8SblP-xwEx-avakcLMC_eI70JtSWl-8ZnNYtTQ93UKauLlK-YPvYX2j_63Y6aqGxTzn1ZB3_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mPJ9lwpC7O2SxCI8oBDyRWx36qadEeCFlZrl0zJF0qnWBqvm_0U8yZV3tCzoeGBuaYtrdCSLzIBpwQ0xnu039tNIN8pDbHso8o3dgaoGvkh-b4YWWVwoCzbO3AQuaKmiKXeh9CkKTFelK7S304g8G1r37P-XnX1uIAtA_A4rcGXAs3VnleafNYY6SWeq8jJNerIgLM8wuSxkj-Axr-S4s-DIJB7HpHhGBYai2S1Kf9xyktZVGLgYtE0x2es7hzC2aVp8KmIa3-6gDdhzCGgGp9XEZRWw-Gn23wYRZFqPO5xInVGK6-SKoGyHnFz9PJYI0ykspXEQucmLe33jVoi6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RT1vxRVAq5c_V6CqdVxkp-gM0zGjFRfud2z8e9M2KIpvOriS1clGHmakF4ikLMUaw7kxcq9yLwI0sGBUf8l_-wrVIFb6WrW60gxBk97Ql0tieJHD9B7ybvgvEmMeo75SwGbbvSc3BSXcUOJ-S-avMA-llsx4_y6AcgcbdsFEaTxPxRw7qVGpKKccXOZm-Ecw03PdTQvFFf62HYYOEeS9H2Qo4I5NCRGLIZfotm9fAYHE58A6td4ZYRtc6CjZ_9DMIL1jG3l0fP_nppkXZnEP_vYxXixAiOrnAp8AVa0aFeRnKSlIFjdjrlqw2UivOyOgn_sKT1fRxruuvr2PHHUXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TrnLBr1LZAabSZ5ppgy0_CBeaMoDgGgd0w0-n_0FfstqaAa1xoWUmhNnW1m8xXf4LkPNMDS1GeyY3w9aIvJMBd-abmDTnrwMtL35ai9DRaKl_FXEOiIZ7OUjNwRJRAaypZQPcXPj8x-NeS2_FPOWQ2vmCdg6kDB2erOSFJR4P3rHOcPZYpjCOhU-LSj5k8mB_kR_I0RnOJrHwuhuBZYbPZAUy7BPaZd0K5BIZl7E_8XLLlpSBUtDfHC4l-bdtH4KOOGdfCDrbyyYcYpyUTieXGwB6EP1vXiYwJulaPtUZEPTakcXT47AKTIk73xkZhEWp8wnzlPiEOB13lJ0TNFdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Frck1Er7sS7EajPObIvgFRy6naCa6NB-enzndjnPs5F2pofUXJISVBtrzPbefD8mOYCY14JCZ2RhMO3ySMNLufCfgB7miyohGvNpTnbUYxth9ZeG_NVIQ7T2zvwJLVxHimE7KrWP5LafFgBMpPkKg5oiBnVfrc3hB1RcG7qm9EQGnCgLVMDcoDLw_fyAiBUydP1CbBXwwb4y0X_HkYdim7ZoH2wApfGXL4IUeUH4T9EXVTSIAUHIehU-R8v_sSmab68AAHw35x_GCvj25_dflTAW1cJNh4738Jw6_Div8fr8uFhHq7D7mgz2wC694jNlrKwQjfZWu-Du5wC1BxYocw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=esaodc6oL_aH6xUOYlmd2wbsjpwA69R88zs4fed6C13cqXGF-M7lMT08sfePj-4FhInqMewpTOxopb65nXe1PI-l7uuM-7jUPud7rr3KhJG2JGfvlLOAXVwdNWD0vxlKGLTBdd2Vdn4qIzZ3vvyDZhtpvP5JJNHXaeOdR1c7Mf960Ezexj5wWAvkn7Sbb3FIwEW2cb8BwGx2546G6F65OXMYWvPaeguUQXzP42Z3d5bvbZg0KaeWzBkI5Ry-OIxV1VVaDzAeFj_GW9yAwHu29R-dmgDFY2XqPq_JZGswJVDZRo_kdkrmzzndMoftjcmWCj0YZjXDy32xTjKGC4z__w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=esaodc6oL_aH6xUOYlmd2wbsjpwA69R88zs4fed6C13cqXGF-M7lMT08sfePj-4FhInqMewpTOxopb65nXe1PI-l7uuM-7jUPud7rr3KhJG2JGfvlLOAXVwdNWD0vxlKGLTBdd2Vdn4qIzZ3vvyDZhtpvP5JJNHXaeOdR1c7Mf960Ezexj5wWAvkn7Sbb3FIwEW2cb8BwGx2546G6F65OXMYWvPaeguUQXzP42Z3d5bvbZg0KaeWzBkI5Ry-OIxV1VVaDzAeFj_GW9yAwHu29R-dmgDFY2XqPq_JZGswJVDZRo_kdkrmzzndMoftjcmWCj0YZjXDy32xTjKGC4z__w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RW6ArShIniYcgfJIBNW14NeXi8uqetTepy2RuVMt26NP80cBmqUL_Aw2uYw4WoBygZ5iAH7Aqq4C9cNqxh4RnEq3T8LOZRpjWeLonAovwmk8r11QlTiCkID0tIuNJmXn9LMoleci8V3a6pg6xQbkoPH4eYypPkEsG0VMD3VeF3pw2Tvpya65C4IGOSmN2CYncsftcwJ2TqyRHVm198MdavtNbcU8cfGXQawLaiKoocMfWveXycdkXPxQ4S3C1EXWfEcyJjuDn01Ia9OJqQTGKCeNjd809Am5mckkqSmLDBQyUANuqKEkq8Nz5Rm0hTs2cOFppgAiOsL-PoIw_p-Ukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUOm_hNy_XluVGvF0VH9Q4jZ2KcmGxq5nT_EqzzaBPkEOiB6V5NWIDDcz5JzdFYM8K3vcoWKu21xVoEInsIgHIHce4PQ4NsfVbtbhMCyVi96iiIqYgEcEJQnxP_gpVUBbFEgAxVWkUni9tZwOWsY25-FFoIBuoKfwt8whZrQEJYPDyMlis49k0i4npH4q0ctmnoMekRtAus1_sl2_soz4NOx-385sPKrqm1KBsQE4EJuijWhDdkNgq4nQOwR6d1FVfdTLL-tL2liIaar2MxyVFs2INXq-QFoJ5fjWEbUhi4nvau85E4mIOja0tIfzFJxuwb-OZ5ZfCRzgeEcC8BUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/peYN-VZ3Y2ayPpvEW4cBpRIMdNZoUZXi9jQdaZ-OoGfgDRoOr26hU31aWmVVbxrBddv1XvS4FMW7CUPcVS55DwmfEebMK2kWjUIMEGXgtZICgguXM5JVqNDXEWl-YLZhs-a4OvoIByUHnF6m6hnHOifPLeWX8M3iPvXz0_uEcuLf3EkaeHRcBQRuoEfrsmbBnRTqYawYunQSVRnobYsH_tV7bUcLowyAJVwcQYteZe-hUMn7k2_FOp0_w48htoCmwYEhA5xvVm_m_uCsbbwM2XsOB5_QVuX10XhQrOn6vydeZ0osxKAVH2MyC4434Tlo324Gio32tVGO5XgWhKQohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
