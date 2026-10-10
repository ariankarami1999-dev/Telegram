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
<img src="https://cdn1.telesco.pe/file/rAFzer4CSwPf-QO-xfIq6wcqXh5-e_s5-MpdhfeGp_g55gwzs6Lh4Wc_6iwfh53m3eQwBMplb0lcRVWsiFLVMe0900E066Ua0u68-Qe6kzAl9yavl6I_-uZ1kZfqk-KUvv-YJrIuV3Slbom3GvadXny8cHC_e700ok_T-sTvKzpPo4-GWfQjsM4WqLyyZzkBKsQ07UBaYo8cxoRNiDBWWBBwqGjz_ZBsBr76HL-7IIEtccLdtMl18llZ9QNgMJS891As9lv-PTkc-TAXXafdUSkXdk4Kxz35NTZr-olkG2bIH9JZ4Nw5uFLPGwBVySUkOkq69D2cpq2VMHv5-QnYRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 00:25:11</div>
<hr>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oali2aCqu-Jyuicye60Qu25OOXFiztppeNkm35HVKr37m6icpwNMpBY_zCbDSQ_i9yinU_2FqnM9orrGqpT07qW8XslkxLPZvKQrM5aAFmOMHpr14jLuljLsZQ2-ugQjsYU2kG7COubAvoTW3se65SsnYNsyUMUlos_N7iokdx4K6cubHCdc_xPICmdv68YpinFKPAiihoaS74Gbs9v-gpyEoxkkPvJiKBpHzjcX4Vh2puHiQ2otYjSthCsw9L7RGk6iayXe14n5AKRHUCJOAYJR8Qop3yQ-B3HPBY1hRRPidAyOW0nxa89dAwUaC6-PFwwAa6DRQazDj2amNf25Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4TL6B1hhzrcoig4hBPuM7oELSjwLnGZynFml67FfeLPQ8BcgkbNRS5k7M24QFWC-fCanlL5O7nBFdYd3ohc5Yn-mT7OgL2enfN_OMEAHPRz-tyisEScAJAt3m-3j3zXSd-zMNcO3B78J_h5OlqXWsXvceyMco1tnt4528kHaed5Zr8gLVzDjCpt0_axksYSnsSFeC3JVaFcVW7boI7vhaPZssUH9ZniKc6rvWNSbQoSHd17xIiddwu_1mkeHyL-ccKo14knEejfft40M23ZIBMlfRESXRBPIiUTb8lsaHtFbDId5w-iX-_z_SAqgAXEIQ9Bj5lAcvQalwN0B9AsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW8onCA5cGglu5BtM-jxI1TVP4evPuHRQS853ShFuMu49toQ014YnMJSTFfQhxZUj6KIRn4VYBXt-v0Ns4y5PzUaDAt_hCZfYQw5G2xnJnDvc1u98x-JLcqDJ6CInby_JP6PhVo-mZIPIKSgoepNmcbqxaVg2mjYPEJ6vUzmTBoqjpMnq4WZ2FJS_jUanDPYz4o6ZjZYAMtZXEveJrJm8MOY0clrqsx3anj7cUeimHtVxcKTHHHHRLspo7BVBMuL14GicK0lN2xDlHAm-zaeKG1tKkt6xbhJrvZcNaggbFBqBrqOEB0hpcgBHmEJEUh8kAnwjPu-qsnxgquOK7eYOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=eyVGtVoBcgqYm0ycmrkdZBemaqcvac5WOuGstKKMgGiNg17mHwTyTX0lqWzwiiMndJrFxYBQV67lAIXe00dU1KgYRfOkNdVjo2Qt7iCSFVyoKcDN6Wci1bD_VWtDErnFeuEG0F5IH8oBtZmuZ0djtsMx_RqR5qH2uJX3NNVIqo95UQ5Z7wJsVAozqO3XDnj_gnBf00FU-Eib__wMhc0PkYBQ-4Bi20jtQU9oj3kEZmWtP-b5sjFhbAu7JLAjI9G3dElcnlV6j3y0vScvVKQ2yL4kptDCSmwUYk68TZF9awwUMkz-alZfQtuFTt9av-T4je3hpXDlPv5fxdEfzqMONUJV1lx7D79vAUwtb2Ca0c2uA2H4kTS5nfRHd_FgLoyDSV58cAtjIzxUYHSfuPRFle4aAlHPeLgFdCT45uisbe9FxOuTHqfSPexHMhTS-xl2iCDdw87ETqLprdciCw9YDb8uVZAbAwP7Kr2zkXPAn3HF83GrBKQ4GE1vLuws3UNFjI6jFUh3dpLlgSGtMoHPVBX26o9UD6XKMFjQ59G7AqhN-BgAMT0mTbIcUGvsm8aINrTYRsKqbN-JmIwwKa82_TYEY9Z-jSw25gm9lgaeTKs8mapEMNso_CgPKS3t9zziKkRdJ_kUkG3y1OBtcceP_QqA2EPvJvJGoAHzLLk3tlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=eyVGtVoBcgqYm0ycmrkdZBemaqcvac5WOuGstKKMgGiNg17mHwTyTX0lqWzwiiMndJrFxYBQV67lAIXe00dU1KgYRfOkNdVjo2Qt7iCSFVyoKcDN6Wci1bD_VWtDErnFeuEG0F5IH8oBtZmuZ0djtsMx_RqR5qH2uJX3NNVIqo95UQ5Z7wJsVAozqO3XDnj_gnBf00FU-Eib__wMhc0PkYBQ-4Bi20jtQU9oj3kEZmWtP-b5sjFhbAu7JLAjI9G3dElcnlV6j3y0vScvVKQ2yL4kptDCSmwUYk68TZF9awwUMkz-alZfQtuFTt9av-T4je3hpXDlPv5fxdEfzqMONUJV1lx7D79vAUwtb2Ca0c2uA2H4kTS5nfRHd_FgLoyDSV58cAtjIzxUYHSfuPRFle4aAlHPeLgFdCT45uisbe9FxOuTHqfSPexHMhTS-xl2iCDdw87ETqLprdciCw9YDb8uVZAbAwP7Kr2zkXPAn3HF83GrBKQ4GE1vLuws3UNFjI6jFUh3dpLlgSGtMoHPVBX26o9UD6XKMFjQ59G7AqhN-BgAMT0mTbIcUGvsm8aINrTYRsKqbN-JmIwwKa82_TYEY9Z-jSw25gm9lgaeTKs8mapEMNso_CgPKS3t9zziKkRdJ_kUkG3y1OBtcceP_QqA2EPvJvJGoAHzLLk3tlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXwUiUXIeZo8VeaE_4AAQ-WwaSfWPT6aZ70p_qSiewRmTXsloiEFghmzDC_KCvP7iW9A-0tV6VqipbvxZNJlNcVxBvYpEeYdHp0KxkEWbSTPsej1l4PHpzLQEm2VA-ZrxSxShvrIlQdkSy88gwa86tON8-rgCZUtTjRw37h_agOxYt6KAIKidYjdvpsIbv7wSMUy1WMkvd44I3Qvt1FjR2fyFFewpqZHCbrBhjoucf1kyUV2lr49fca732GwIQYnPSGhR2SVcDncXOMyF4BKDp3noUhJ9q1eJjbzekesg34zZpBrNYcdEaAMrGCUtHB5c_M573ZD02j2nRbXBYYD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TT6VJIUeBhR04Aj1VulBG5ITf4Nh7-lv_3JMHn7sVdIf2p10JuVp2aP39WkEojE4ndhpnMTgH_d1fudAOW0hWU-v-spV1dTyE4TdkQUFd8TU6ovGUQ-uD2Ue1aTN05_jLA8iUW1Pa7Vbr4VqCp4yKmXm_We51sBwKtKu7d2pbgwDiig_yJa6g68BqwDHMD2_n_hjROZoOdHimiNWYMkCg6ZzznXfY0bVfe92viBUmXHtMnv5mznje_LIakPRXFqvEY8S4l3aJF8jZa2rXODgK9OlihXjbR4o138q6phm7LEgv6GiVrvQWkuj0PzbGpBiQOq16CqKLXQUf7czCkNJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pSgta-BTKG1I5hMRsECFjd-WYpINvh2I6mU5nFRcuSMH6ucl1omx6GlO4gFPYJfVqULhP9cj9kYpoG9ABCSiV0iOWTn1OlDAspqiSaMNr_FcO3yF2EOL8I9qNX3QWiW-6D7wutm405VwXIzBzzxIUv48m9WLJEiCwSgrAlUuI3yoh-9UkWrYqCEwpb4jS7OcnWDODvKJXYKk81NVNYMAjoJFnJqeXZAqopK7X3J3o1owR7d2SW3z9ncfVLq-1LPkbWRB3xDyIEoNNFhaLLc-hYvQysos0RNvfZPF7hlkNzD_ASd1dy52KcZbAc6cQLmffi4khwNi7xQkxtVcKCWCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OMWFtQ1x4FG25tlsIUy0V3vhV2EEc6zOeBd1VwzLeWGN_aYO6qLcnleNURPVgWuO90tVc3GrMdgjE1wqHquNglqy-3mjKTrlk51egY56PmtpdjaRdTvIrsB8G1w7synX1ZNJB_bCbDnrff_3dOdGQdagCtIj9_7hXHVt0AR92w66j3mD6RySi41n7PJ9oCFgM5tW9G2JW5J7d1NGFxUi1Qa8yUfy2EreNZJYw5SWtnb2liShOsIF1Row7hRL8Q9EgxrgMleS7acK26wARk6oCcFZngTy4tAk0_WTZ94m5iJgkMK2NnlnJplIWJIe9Z3GZFNW6RTHFWYQt2JIPqCxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1v-wJ9RuD_r0Dp9eCOJhZCSQhimqf1vJwaKgIysaKGKjGI8HHDAsUehwerRoBUdgfzCX4i4RXFCm6No-QW06gvcZGs40Uhfrgfp4mzTSJI9_DTWjjEHtHYDhqyZq18jHkP_EP9M-snTiedDUFbmp9sAylzhrrAN59MFvouxnbue7JyKRdDmQ2pKPJ8aAlL420EH_4fAsMLaEla4ejj4SLkbEbizg6pljuIRGtWgWfDxm39x75L_Dv6YUMM31jQXtLNdUJuTKuiiYCvQ9vBaPfpPRt2IQJ626FCiUTILf2ySzkqdeDxbXZ_dB9g5uaXCaL9f8wmGKf5BWjWm7YrE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9_RX175N7RA9Dc7jqVmGup4YTQJrQ91wmd3hh5g87JQn7PMzTVxcVFp8GTfK_KgC3-qo5KAIk_XRubQmHtutELfZWD-WhyLGrf2uQzmt1X4q14v1OMZHw9HpoHRoeQJsxBciNP38X7SMz7ErFOmX7qdn00x0t37BJF7Q8XZTsp6kh4K4-u0RPcbEXTxa0WKEL1cqrQf4_pO9dglG1HcBVak7nvMCX9a3nKlJmGksxppTBU0VsC7G9oecArFeVw-G1tNab1q6ohkFg2Bp2xZqGmWDkBPjGQS9ZtJ-U4Unb7cIK17NgqRQMPAtCvwXUtovv8L1BthRgtU-0Rluy8GwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIKUlWEkmP9JCKKLXxiAE9xhNbXN7XZE52kcA3ClTrl0cd63CfzpotxPzUi3Ix9jKJfS6jdEi7Hn9AM-GbPL8qCuVGwGVfV1AmEbGyudlCM6svsTe7cfnPo1qo3NMb0pMQXY79Evas-KA_3LBYXLLLWCQFGH7jO7E_E187GtNEj7ShZVlup4NgExqVG3Xe0g_bKL1ml-xvxDtAGCxcd1UKRY9A_hAisQJn6MulR5wKMDkF7j5MlS3Ac7mSfvIO0XD6lOcErw7F-ZjBKcW9isj-M9yvZfbboSPkwwt485E6AQJoSobwnGo3efZ9vx5uwVo_hezfzSgx6PgSrQuGxniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nT8cC9xGDmiY88E5Q4iBLZlWYgokvXvIcWa8TytE_z-UbvT2MnppkdFUX-jkyjLV9sIpt1aRO9a-GJMm4wOvl94rwRzPg9FB3-mlZof3nwUEJGyeUiVnMQTuXJQUtQK0kcgmbgE8RMbIYw6mjsVtd4N0p2CiO9YPc5B5YlhnLNsWU4HdUq3nueAw8FLNxq29x6jR3B0HplICJRQzD25ySvjabZbgIMh8XREUlozKNXlUcw1l9OZ1Ot7KXfWzuALHZvK6-4CJ0N8iIqL8P6O7DOoTuxiYtN96gJcWmhBfKr2J_W-ElGwY4ZomsS-yTIimodRIPi_ARXndcC757ZWZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t158DA3WcIAtfnnjP0cX7HFxybBN0eb6gkpW4nymv8AolZAM3z93GAd5pwRUVO2nySN-Xqu-vq7_ygG3xqzzVcTmmDS3r-ifPRDbinH6vHmokb5TKmJDfGBlDj4qCp82cZAC0zDmlLFW9srac_yN26QTIqQ8dgZvuc8EA4HUrgmpkyxBjMm8G084KHB7VAIXJOLPqaL3QMu2O0n-gEb0rAbvokvjNKdjniOCxC0elURg_jjMU-o0BJxeXMj6wAgObqK-tYOAG3BhLAiBZU8ETw6vF4y-ydfOs9DfE0eyP8LVfbqG9384fOWY4QgQQBYizrgjQpXz724QSIS3WowZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JG1laiqnE2ImIJb-7cBK3NH4u7zJ3bz8v08DFbQj8T1zyhMdZ8mzqfg5lAKDSJ6gVGk23iei48qSm8vhtkbVcrzWMQnGqGoVY7lCUUaQ6-X7bgZnuFfzkjISjH8K84Uhf-krfE4nDsse7-_tpCQ4LolaNF_kcn50j3avzM4p6TACekhv8Vtd1zql9-rEIuMl-M4Ob3Ni6snzR5eSPWGFax3H60_VlLwsDfTtwlO7WVVrUQFNQe-BbLLB4DGvizhl3l4xEvBk9wVMdCQ9UmdgwyVxT0GaW1UcgqFE8dkPL_FLOvdegAmhi8zXC-shLK2WJqKunKg_3d9IU8PompKNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d72_yK9nD47kovj33Wu80g1gr-I-Fk6MG6H0cUq3ovttBUKgjmMB7HfZJKCZMnu6_4DJCnN8kDlmsruWOOMxbiUYEJNCl_R0MhMk0fvWm3hiPS3vQ-r3xZRoW3P2NUgzC74qs0VlSdvAOlsR0dS2oUvFlVeoteVCy13SRbpZ38vysMl9U01v1AVkg6Ua3l7LdB5jK6AYoJLcDiQMULvY5KSYrv_X62Tr6_j0EX_PROUU088fYu1f05Wu2bA1UROK2lY9X3WqjEhGTLJfVZWLAMmYGQOGsKmggnHaSkM68h3wNv2mZvxra4KMSqx75YkVgAyiujLAAn57E0OBFuNM0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u65hfaqMHMmJZUw1k8r5zAGkxCG9eExU21kMDMR6eB5-HliQcxzMb-kJ1pmJtlnHANG8hw39sBNgOORCDUy0J8qksDwj2Vq4kXyVJ2HP9kPIT4kZZVRe-5LElOynMcuvUjFB0gGLDlmq9O9QX5tfbHrUrhLw-gwtOAE8Ms_fSlhwoS2IV0V-GS2GqdUOOnrRgE55zp7plHbz5FBJaAStNmthWYY3HV0DTMWGU8qduh9OvohZXhah7v257tNeVNemVfJZ7gFIH-jf_SAu6Ozcp1BYWTphN7tuRBusO7B6JfYB9vWXQFem2hUxAXAIQW0HSRUIsYtbG_PQ4eMX0hiUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4qnKbve_tMTJYH_dc2dmOCC0-PxnoFG4mUd_BFN6-ahde2YoyNr3zvEaJrD6VyJWUMx_oY9ae8JXdSvqL-glOQTBz9eAC8uK51G6C2-qF6S_iWRH0WuTfZcthBQZ1BPnhwz6KCBe6NSQkgsQBcLOis9STEjZ6B1l8ws0myMbYAfC7IAVCnoE6OTK-0jdPUDjuLJcZK4f0CD29pvReJjsFp0Hb4CKvW0Z0u_ck6JKApzr4-L2lKKvQlHrw8mp5-SyFMM3BuyfC_aADDg2lyNFsYisKW2GPwpzgEicsD9eSJ4Z95fKVx7aYhUXGhMYjQQ4oNm_fRgoYHp0R317HPePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iejfom35Az0jhRh95_R-tyEAgSRselF3DWsaYtXQmK0tEM3hGt3LqyrJ57_OyBK8s6wBl_uUrkjUE4A5OS4mOh5cF4gVZrL1r-SHF1GMYquOljhmZWdpxRo1dggyrfHHIAZGTveDHPOshhw-4e0rM8jABopsbDpgoWspG6egqfUe3bUHm2gQ0UzsTa367c_nQXh-P5y5UTl57Jh0NQt_sugSA758rJpH8Hs9dBWsrMFU-w70vL1cmSekD94ff67cOnQbMe6TCkoCtU95Oc9xfnx9QuF5ZWBw6Z4TEKaEuLpzBkZCowwCPIjTd1AYFJz0ikOc5GzxQmNRPeONdOeEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQ_v5vcnz_aveFBKsI8au5nGEtP9_t_RrQHtVD3ZaoRU0KSoDs2mcuKoOiuXWKIE8Y1U_7iqJ4Tt7lL3q_j5DWoYbajF2UlsA04FKEowhOyv4VicWLPQZ7K1n_4LPQpzhMbFjiTdNq1tvWhrqE51Hq7DcZTCY7wXp482AzqdB3K5bj-cLGKIX6zfsOouFi9fwpdup31H6jKPTR2vTN6hIOiDhYS4CWvf8IeFKWMcpyoME6y4WGYko5nkcaexGmJOZ19vlqyQNH8WOSGB0--MGrznAwOysXH1--XM3qrMyk0NdrB69gW9Trn82XN9oJ-7B_dp_f0UhDAPDjK9buSQYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bnhq9cw6a92_eRcRwu7jPlYtA445vuhFkoPz0A8Vqw-8hWfE8jlKqoGZEZ3DiDfLN1HracuK2qwFbKRLxsY0l9tf86Y5gihbM_8pmjB8SEgmyctjCMAz7nHkAaV_zQDZ-q7BRQuBFDk6JFZene1qhm6i2fMc-_QfvKEzYPIXKYSmvnBRtfZTk08izbGicUq3ECplHyLoIwGtHQ_fQGRftkykqIE_8zTgScylO_XwIzPPuYEeGQCJTlGbV3V_nXc_xtmkcuL12Xrp4bE7ktNu42SjhS1OptpZnghSKSTJNUE4wMLdHZMRJmZoMAWyVNXirx2LVTxNGiPalOZ-f6QaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XyrMbIQ5lW80ZJS_UdMu4BCZeFa6a5HDGIRWAv4xMAbvWah4CXpzq0BMXWf1t08Nlm8SAnT18t0c2vZ_W7CdPCwfl91n7_XAAgP9ClTJKAsW4FCNf2sZJJQIKneMpt6D1VvHryUabi53TpA6OltTEVyaPDq8jIpF_Agwjal-CpDXuae_g8hq4KThVi794gBd6i2vUkIIPCZFqF5pGuvOnbfNzYmuDf_5NXDe7YDzBA3eRKVTQkBvOLIa_4S4BQ5mm1VojEtE_QMiu8UzhfudDKcDkKMaMcJW6yuKck1tWKfB8tdn9jZgx_hdvkxcEk70O3_vyxwNHj4E2KY7wHj3lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQo9ehCL0bZ2v_Hnd6I2CobmescqW_IqswNQzkH2mOcFmE1WNb4D9JdgmvICmDg06qOOYwWudkWm7N2O5R3518spIxLKTw_O9t_upcozz_3mzqihwjsa_WrypvABKFNoJl9UfMD19GKsHhIEnkcht7ZRRYpMJW-rkPGUTDXoz8Mep1xkeIXmouKQ34G53EfdJHmFJbN5flr_UTwaP3Ylh_OuRt76yvP5dsUSIbAR4XVM3SfSRfLeZjJYmL6m_8aLmpBgHjAWz7xZfJi5WyuZPBPFT0T4pwqEFEKqtQxOc8cfDto_aS-4nXgZtiXHxP5Ewzjul_52yaUtxNouwkY5mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=X85RAl5_UFJzcF_nKp-eXqI601U8fLbAXRWayFszpZl05FhqHwM9eayDiUGhEfadwB_JNYp7nnaXkAqu3IXaPeO0rJe9z3FHGgr7oEaSKaJ7QiODNXdnwO19UDXPQ6cgMu6SWz3sn1gwBmVDXbnG-LtqeaYHv9UlSS_os8gvnRimbYLtwNnSeT-YLiYQyYggNaqh9ekqg92fcUqUEydQA2CAEQYZjX35-TxCsevUi_NHA14nCctxoU3AmX0ILABBGRC8tkqkV09lk0OwGLYLFDPgf5-xLw0crOciynQa4knEUo7i0hbfX9-QgRixFQvbLsxLtG0DycaqM2yOv75AkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=X85RAl5_UFJzcF_nKp-eXqI601U8fLbAXRWayFszpZl05FhqHwM9eayDiUGhEfadwB_JNYp7nnaXkAqu3IXaPeO0rJe9z3FHGgr7oEaSKaJ7QiODNXdnwO19UDXPQ6cgMu6SWz3sn1gwBmVDXbnG-LtqeaYHv9UlSS_os8gvnRimbYLtwNnSeT-YLiYQyYggNaqh9ekqg92fcUqUEydQA2CAEQYZjX35-TxCsevUi_NHA14nCctxoU3AmX0ILABBGRC8tkqkV09lk0OwGLYLFDPgf5-xLw0crOciynQa4knEUo7i0hbfX9-QgRixFQvbLsxLtG0DycaqM2yOv75AkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YoANzQmxZkkzgqHdpOB4Zb6udgcjB-anHtzZolDifX8Tsjon5byhm9W5RWcoLZF_2H_MfSG1v58oWanP9z9j33Icmyp3akWGLrs8rnnkpP_du_6HbStvTYVXerOTfrhThV03AjKkeHWhtF9-FrXQcdxKWcD_irbIgjhs83gRmBQ7oWtEuEzwDdudZECbcxs4usR5h4d7WzrMdu891kbIUtvEGPe3UqbfB44j7xEjRTySCBzVUuzBa7uHgZKDDx6MXygmeJfUau7Z8kCtDiZ_TZomMzZFxQrale0AEWxAzkADsxzLYnc1jHFzc-e0Lv1PaNmFbl1_jVqx28cn5p8AqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ub4fA3x4s3MtaKwj1fEur-YlY4eZWOKjNXf8AtH7dsNZlrjRruWUocuvbFEd6PJJK2rzu6RtqS6B8n8wQyFP0C8k8J05jNHToJDEuWyHYcb9cvKAL5EfM8ErbR8-KGMVx_rFvHU0UB-jSwbE6BIvfw99-wsavZ2Z7T8XRbxTVaW2pImM73CYgMTth5_6aIkKqHThzRL2xHnFbBmDO7X-vHYsaB5UHE-LAjWrlqRJT_9onAd6mTN58r03cMCs4SzGdGYU_ocIt3aeiOGjDYG1LTj1SzeMU2B8qJ9I0Zz0Prtto-xxaEfA8QyLrZ_P1BG3Ys2ea7XwbvNe4p9nXxHTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DoxkTjsaPEjIG5aSLbjbq1VgJ_KdmpvPk4jJ7FB-2jYNYPzctgjG_Rq2GiIN6EmNV1Z4GEw85YOjEJZiROfA7G-w8HqICatTQpee9MJAJX-hY58GdOV4ZL4UO-GbELuO4alA_KXrvCFgI5RlgL4JDx5SzVpY2cKps0ZT8vWR-PUVnTat5XOhF-Mn_0JuL4wpf9Frb7UGpevkyWw5v_Z63qmgRD-z4au3uiLb9mNO5f-mceIhfaxOODc5W3WURcq_RmCUZjXoBihHyD7dxh_ENeO_fwJDH11DgH-i7UUUE_sC0qJdQ6gcrCzJIHfW8o97Yun_hEGR_IM3rII1Lkb3dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G9G3dIJWOIrbTOt25azavP3oRCWUwBG4CCgfVa3ZEm28_YiPSfMpjtsPdO5sju9R-sXEU4gDYxPCFs13DMs7mMB0ePgEkfEh03J8AZDNhME8R5hrIGOHGzistNrq_6JfslU8NMdUkbr9A68GziL1yJP4J6F054hKfNTF1QeGZnt0RIhj-gZSX9Eq-XdPVcWuH9K9_OxJ13DY2FxDqJmJaz-CWZ1Azeb8_kht4ObFBv5bnjaLdISGqp5hzGpFRZ8E0qScGvpw0I7frI3R9pmfOVFBopLJK0T0k2de2Xn2XCpPQqyNdIcHPnDGWFcBm2wTmmtNy58EKP1S0QF-3jThgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6Nw2jAIRaMcALzvsd8biSt49Z7dAlMVWxqfUhFksh9k2sFflvNmmyMvZdMJCZSbff6voczmR23Xf0n3gXDdM4Gpd6H1yevug_7l4em4vsBFGwlTs6VOgZXYhmxrTMdk0MPXptUvj6k_DwVAuImPdSmf4xCaHF9UTsOaf7uzbv7rYfONZkNARlTp6iDObSvTmFIPgxblOLVkiKkBq2IYcYOp19Xl96kjRUp8Gh4lyMu1tQ1tTGajpF7vmlUigcgsZMgKI4ONs24kwtAMl2M8tiry_ieT0BREgaQSn5M4EvLmYEzxy9aWrlWuFLG3dVv-qXjHmgew26B4zpREPnq2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiEUXq133tQyzWIKJBgXUqQKHdfKxIDBA_T6yobui8ah_Lir6c7uSzzM9-fFoi9JZ_Zgfjo9o9bWY4BGRMhYqDsyWuL0mp_2QRTYSBePH8JBmO3yiuIJ3ukCxrjpbcEaNf2xo2gKWbOxMryFu3jMps6Ji0qegrGOH91oNUtGxvHZMpUSTlR7uE3gzT8VVCi1-XlraZULzbz88MfLQHYgsNXv7M4pArS04xB0VSjHk_HzA_nu9D85vSwSUw77cKndJJIjPNBXD2QQlxAd_PGNIfjdkm_uWUxFH1Fl9lLZhjL3X7FkvjcO3AMDWXu1Cvvkw8lErWwM5ZpIynCDnAXsfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0uF4K0e8oxkG8Em85I6L-HKCZfL5ocC7sbWcla9WIVe1oVSA1JM0EheflpB3ChugoJzOnsehGq6aPuuU0sMdqiLFc8JQnuM5w3qPcz5dKwnIZwxeihsf3wiTe-2YEP6Pqd6Q_iEHNLZ-bfH5h58A6mjJtOXoQ4eBmOW1eaKkYtJ13nfP4MlWmVUc_cyyqa2i4JyUodHsyHl868wHOIV-9_8ABYJca09Wtm-O2avCg-DFUzEoQ7yiUU73X3LOgIHz8l-ZhS4yy5_PEebQrR6CJ6JJdmdEMYzWSl8YUpkJBNpzseJGy_5aDwWqPoakaAWmu88_vLQZ5XHqNRZ5wHBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OVpWBiHUVtOvbF40ZKbjoE8ds2nXUr6kpY0ugP3kQxa_8FWvJYvhWWW35fMpjs8sxldsgZIzW_F5_ywz5i8bscKoKB0es7MptPqDJ40f95hAs7rgQ2gW9aNktN-GFfCtFtIYuWZ_-kPOg19qO3JivPAOp7Lz9IYZ11TxLDSx4_TCElrlq_IGvcm6fdMVG8IVfBkTMbZ_OuPoHr_pMjnn3BrohJz-MhkdP3hhmn9Q8xkr0M_HZomCZB9ZRhjz2778n62Tlx76-FzK7kUkXyzRfihvjAv-_dwjKUTUMIpRFP9ZvqpcejidZjoH5wvsrNZSeZaBNf4YU-IPrQHMZ227pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VRTnsaot7D3txHxTS7FuYlWGJqWhxrLyc3RPGb5PtvVHP0mjxQE1HDh-OsNmy71JT69nio_-BfLCIDZNE8f_ZNhJRkk44otMWlFer1Lo1aizwGgW1B41rDMxrnmH0e6bQEfbJJKl39F7kTJyPPHXOJ92TTisLEWx7Yt5EYtEh1pdLLG8Vj3OGX0OINp4VEH86HrijwUYj1qqHaVa1xS-KzWtWL8VtcJShbfDThUzBqM0pl2tj54EgGVgf3xsqyLZFaScNp2D__JW0XwudnKZ209xJ3dUjCjrteR3ukny_Z2pIxvBtVKCP5QZOF4HnRWVeAPyshdXJ5exm-2LqtIx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/InS90Phnq3WhbCQQCODSJIf0l5O6myuppDyOltBpqgSh6-X8ZtNHaVsbadR-ROefCSgeC_BwmVDlXpTFL5wiEEMYrSgjouSBLn8QKlsCKKrbJ8fYJ-kuJe72XSUj0u9v4DW1oJXIJ14p-V2HS0iJ24BsF0EfbqJbuuezPhMBJZT9QxHI4Mhpqf3KMscJVAP-3AzFNmx5tjCcy29WA_eyS4lBeTrhjdnBSYGhJAzInEJf7eGyfZy1PyKqGeIPi219OBQq2aEIiCBPP2db-MGN9zGgJU27aONB7Ycmblghu2U62hFOppyovitpSbMDATzTiMpc_sAk61uyFDJRRjweTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXmgRj0XXFPHUcGNljQ9I04wtwcnta2XEJVS3_ZYrD3h9iFVWw9xc3WtKpj0a6fY3nh_i8jNbWwwc7Cn8wEZZiPurQqw6vljdSUALIWpZemgIf_dRJfpMZtSEdWX1sZz3Un-xPlfPGS-490EWM88gX13gFsL-cSZlzbK3bGe6VZs8TzkEd1cqyCehf2L6Iu-vZ6voyQmsUJtsEAuEtXLG8jmwzmpwxGDyYAPKnYOm2BJNSRcLkxWmmYw7d_Gl5QISQhXYyZSKB7MciTS1EUlq9Ef_MaOyDuK0HSfLIKoxQggsk-dF594GXa47tVDqmwKUNGeFqyYd3J_6JctEuRKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HblMB-EBXECRgVEuTGDU1d4gCrF7rfEIRalvN5TSH_5ErMx1yzYDUbIB74546csM_p4BTN-qX_vPE3JnZZzUAA4iPCnB_rPQkmUrICCoMpq8cqY4gs2P47AwsM3UDTS9meFFcm12DfSlFSkps2DvQsFo23oO68-nceIp6CiY1iPgzKbIOkkfVkqRhHzXHeJQ9Vs2F_yJNc-Ulmf0qHrqBpYvxjSl9EfGms1NXCja07NvxIdI4gWWNZXKFaWomeQQYuksWqWciiUabXg21FteO5Fv9uxlZyDmblftodp1eelO2PfO09C-DpaSYHLqSRohKUqspRmRIY7s6ifAJwbckw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poBvxd2q6RhI77LZuYyr2WpgBqUpl2m_SWT8pUaxuK1DUT499lUut8lm0C_QCsKIc7zJcKJC-M2pnv-zHvBttmHiVqsMyxmyLX0Jv_Z2wEQ1jWdKR2GARPzgWq6LCLDMlHriKE04nMDWMnBHJ0XbZFS-VTfLqMPW9AwLi1NvOPlDwE77W3Q7omri14-lOLF6OGY2bf0HhC5NGHvAl69smJDc4_jal3MC3G4g2bLd02rpGFmXMtRkWIk5ev-pWFaSZk29KVPCmZn-N50BRsEz1XEI6bcgATqCji1_8iCNIPGrrb4tEwNi0EGQbO8c6l0mnQyKoheGelnNzZq7QMgJZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4XoCsE54XdL1ofIsRi_40b-07MXzVbsvUX9qkAyyO0yLISXbWJ5c9QzmpvfycCxMj4AI0psxR0W7pyRsoLt0viUEcO97LJAQp8871TE6uLOmFHJ90nGs1C9DvCFKBGHtrjQ48uE50KzDvbWOsK2C5Vdy859oWYEeuApdCMkm3Nm3h-QxiZ1xLAEpSqOYU7NrPtViFcIQCAO6eHxbYM7andIbJPttiC4PzEXMkZvn1o9Wiau0M6hdGAX6B9eTV2Yi_yOoERTwLn-qRadL3PYRGW7o9eNiMfPTG9lFHYaqoNACb1XOQ8dL6IB_8nxYYA6O1TCVWHjyO0RxD0z-1hz4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVV3P7s_457spCNRf7C3wNa3sb78AY3UpJhNINyCcUrd6kTYdLOqlvlvFqxaNVyytPuS_5uAyX_-FmucuUIsmI6sCR59LfUCbmV0-QWVW1qYa6xMaBVj2Djs2Kk8Un6T6f8_0Ol-PN9ElT21DaTpBRfwlZaFYn2zarG26r07DZHPd_moDo7fcorZSgEIxk5Vyv_5JCpoXVwBwCDMFc0O30qMGmCa2EXH6zK873PiDpJNroE8SEPjupnLsT-ZfUCY90526eBbQz27arrFGQkYHNvOVOmSCKpyEoUpNOba8uKyGNbGw7Nnyj6l81DXydFqJukg0LCcrM3D-nT_-iRJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJMiTCBNfVwy7C1fHvGoUgS5q72RulaAyyLAMOgx5B-ihI6oTnnh30fYukWCAoyU25gezNvR4JxKHDg1E3FY7P80_aIfADAVu5kZsaJHC45BsQQCg25btKQTiwZvn3IKm90F7ahtEYCmvsNpbfyVQho8BdQMtyCI62qqFvIC57Eqg8dzzOwbgof_dB4Db8cK2hN_JJeeWSDaSEBz_aLPXxC7dZcL069yuvyPElFa7eN6nWgxfj18YMkmlSOUkg_p5MlS3SfJxcBatWzBwGlZ0VnABQXVFm-xaLGLQZpPMLxhJOKdZ6XwUh0NEzkXOgBEhlrzoXFTIu4rn39LwmB4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eU-a3LZV8Y4Suc5SIIAAm1obCPYI7ca3dhXX9_8hgUygaG7ED91Z49NP5DFzPDQuGmFD7jwaT_-LAhKZdfDzx6CwE6uN-a3uVKMH1qORqOeK9VrAYFLewqvb4nFBnjyZpsARfN979UHxjfl-hdJr4obdiHaey5q1qHhGFwgDmmLvQ80pcyGiepIzulGXBgC4gGVQMUusa81ERTV_HZMf_fV7FteoZ88QMoEdm_xmaLeGCmpvAMZhvBS3Vt8HJFcl7wb1K9vRASbOLr2g5T997Iag4Cp90glIbsafESE5dsXk6awkgWaOacfQ9_YO8gs3xtYtfKPXLtV4WSLlEkVtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vLwvbd7gtT96wYT1EahEtodQnOxJBu5Q2e_b5SfgfFlWs2lku8YsgalyWugJE_cGQW9lPSWh6nyMAGPLTn_UrBAtmTDYMsoFLM0gfRmXbQY4ji0XFMrJTQaetZzpGYqenCPc6jfEkqebpfUTx5ESeku-bQs1Cqot_madhUfNgsro9ZnNXJ3kXnpyWZHXkCGutmf7qICys-3nRxtDZrrhAqaYt4az3RjMKeW70C2Y4PiWxWAd5WoqWQU9EHtPcnic8QpsJkDskJ86FDTaCgIfaoRGuS8RUhJvDuKCO4Kxdbl1Q3zmnBoyNCLhP2zlDZagGfNdRpNaB9LzunpA0o948A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mKb5FWgAkZ1ToIkivHbToInLUcPnuCAEYEzdFY9IrXPCY4Fp6sCUrhB-R0w4FQl-NfzxGpm6HBRM_zIKQWUKLISZUMbYDkCZQDhHnGNxfpfu4auiqxMe2scKZ6-SJI2sVmOwAB1k5wey9-zCFqjX7En1GHlquuVAlSEowhuxrHyD0v6xy6OTA2G0l2ZOVg0WQiC_XWJmnwkpBcnTpkTveyzQFBUwuq6CVMPs67ysrxM7H1BLv9wISC8PgcGLoIYtkgMtQv1M0LRzOOJm0HAzeTsgIzNvXv6a9D0Dzfdpack-cNcK2jHdstSu0juXhYQJg0XC9GAvTRrA0Cmz6k9cBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bu9PwEfJBXhgr8UWu_jPmVs1XiGsMToWlG9B2RxA-IJKnrNTAXQ_VP5wVILKVvCqS_G9fSnnhCn08f8q2C3chxzoXns-IaJtzKGzLfUQQj61LpzFpK2RsoegYm2jspn-K36ybl6-x8xkENVNSySpjKbiEnD2oGhCf2HBsaoUDDfJAVNhhoqY67fGxqqx8r9jWpID-rLqEn_h2X1tXT1az56vwXp61fcdCilvSxHuNiaZrxAnXjWyLMYWpgtyQ1dewSXjl7Xa3zf-XJUiPGQTJgvcmKU9BRWLPywHdWv7_yC6iTaoAfoaETBR-fhqwneduBD0KvjKHihkFkRVzM3x1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7sxisoBi803gt_bmljdQCfY64949RqWzmwL3UniZtHPMTfPuAbni6o_YzGsvq2HHqz_QEj9cqjdDf1d-tGxBqUP0snRUXVdGDH1WjNUvWfPrRQ7yFIv1LqiKBCADEa-LmVC8Njhvnbk2HxGpkLWJabyPYwztaoje24j5CRk6NLE2QdVAlD5piaZXWosDztFQlgSeROU4_FEVDD6qf-YD4jFTNjbp7zx4EkHS-z6zfAaiKBWLd1NnbWltbOu7BuHNsbtVzN8AiTCiasqTFjLnnnrw-UgXyyV2swfBhBr6S-smJd5y9Zd4bAfEsnZPKoeQckJ0Iz1bBG8MR6AnzZk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gx15xzl5L5o4aNmJsbrG6jlTHzLDxN2k31lHlpF4VJxhA92dcmBeNkhvZuNDjKaqagDzYnMRw_Fw7mvi_T0e3-ZB5B2H8gSxXeaYuJqNxkc6SHUdmcMgXXhS9FjQhhpZjI4dA56jC30UlFQ55z3_9JSXJE61x_Z7HCn6weQdaA6GyOA2D1rm2MUYY9N-sp1292PAHnojD2RNr5_XPDmlzf6UoSVakIfNfjOG82-2QMcrIC7rgQyQlC23X_g2PAfbphQbX5aEUAX1TBw08p1tE1KS7IOz_6ZSOn4Uj5ZwFr3pY3utEmbGdyKV7UtyQEeW6FkbOlQ6BXK_WzH2zPvBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KavPEOrZ1AqVRBiAlxC_oTMA_8RLnxJmmbvBBIS42bc58w8-g5Avq2l_I62BAiUMbQNBphOLz7cfYbnGjlfPAh7ZIDGtkIM4cbriiTZkHTmn76X7GoSyVQfuEzoDpbdLis_akaKe23JlVb0Q4uwjiwHokV6ol_pwScZ0-xcGaD16vKzKBcFPFIijwL0Zk3pqo_tu9F-OQlCLpmTavND4jov1cmE0oLe-Pp5doTZM1ORDJpuveEr7By0qwT4V1xoRtZYEuUsKTK2L8nn0kRp2XKUM9j83YSKB01TX3uDR_cEzrYQL2Qnl9JiwKWpGbLsLcYjbIBtZoZc7N5fLnPIvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UFoYoiiLA8RZQiBMch9tCS8V1BsjGIuruzA8z-KGG_BXctBhJMX19QK1JLxvV08T16zIsXLCqglZepjGwOTATdPEXrNrN9X5DecUd8Pk7ind6aGoRgxmbZAzdj330pgqW9LzeaxukmRwG4NY_m8Knw51aMNPe3SvyyvYPj6yAqUQHlQccJoiDDiK4imilJU6GkswIh0tpPPJvVhC5jJiZxN5ukfHan5qVYmMwNzlMtx26IqUsIrI0sUg1lepTD98WOEh9km3ajlEx-Cyb8Fl6go2E6_pVrYbGpAI68xw3KetPrjZSNqJPSAqJsvFjlSH-xKkVaP4HGyTasv7-wXbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PmR5IWJCyvLpeW5ZPPc8rUi81U3efJbQwKx4-OYOor4WcRgCRnQia9yeA04E-qf4dhYFeiTG3AuVZWq9JdwyJHh7azhV3uLfEDB7eGmmgf8TB2dKEsBrzkMj4a7rDAQMKLdls4uRTCQXDb-2o71P6ZqaUSMvN-4ghydEtyELdO4jbRoamHXMy6gIthGHncaheiDboAa6rY6Blx9zyAJ10-BMKEGow4JhqFsROU7jkzfvRQBSbmlPnztrv6NB_kv0Kfi2E6uWx625sUA1fRQaw2YhYYI33etNe5wL8CfK1PvogRzIZhyRaDsxabeE6JisXq-fgLzz0NqEQyDTt0IF0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=CXkp0p5jvq7sM1By8ROq17Sz0Q7uxigYsVkfzC5r5nNeI6mZlIq_1pSTTqzL-6IbbuOsX0_GuO3GWkeIn9DaagFL4Nn4B69Z-uLIMKqoHo7R1KNVOWZyHCpxG583kcuAT5VEjvGPtmBbaoEnOCZhcRUNh9hw0iquV0zvwf4ikEjzVsAF5xDoq245b_6Cpg0xs_HnwDTJpeAd3tjy5ouVNhRXEM-sMYEzW-CpC0bs3ZXpDgYTtZXA22IAyktebS12RefayGM8zx_37fb7cLpOKAomOZcMlg8Dz1Otmb7Zi54Ua9kFY9kWYd9Vz10TPxrtFxmXiE4TNeJe99wqJz1NIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=CXkp0p5jvq7sM1By8ROq17Sz0Q7uxigYsVkfzC5r5nNeI6mZlIq_1pSTTqzL-6IbbuOsX0_GuO3GWkeIn9DaagFL4Nn4B69Z-uLIMKqoHo7R1KNVOWZyHCpxG583kcuAT5VEjvGPtmBbaoEnOCZhcRUNh9hw0iquV0zvwf4ikEjzVsAF5xDoq245b_6Cpg0xs_HnwDTJpeAd3tjy5ouVNhRXEM-sMYEzW-CpC0bs3ZXpDgYTtZXA22IAyktebS12RefayGM8zx_37fb7cLpOKAomOZcMlg8Dz1Otmb7Zi54Ua9kFY9kWYd9Vz10TPxrtFxmXiE4TNeJe99wqJz1NIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MUyzzAIxOE3aLdBPhAwep-b_2_8Jj4QdXugDy3LnQPK050gSTL65_d_dCe5rt_oMIWDoqdPbmFmckwQJT3zrFEOc8BQzPSRBQJlHSxXROUE616emJV4Jc4Uq7tRSPJTnGy3ZunygDiLHtupQXn3oquTshL2LDsCiCxWWZ3-vINkyrpfa9Q_iEBf6OF7QIbSHDhwqJmQdemdw4GzznDnSfRWxFYM-zcYjmSdyy6CXDLeT7FNrEZ3NpcKZTSgftkJXSKwkeos2iHdVoA-GlA5IWKdMJo6KJxmiVBPC5yH6u_TthHxf4WL3-B6RCEIZUOqTNxoXXasIya0STdhl85jI5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pt0rUJCUG18JPOKXZX8u5wDWuLU5N1-ZLV3Xhh8_8-is1R7hbzjQdD7j86G41JWZl1YDBntZFWtOEZhQgh1bUmZX2C3zX41GCOU-jaNSxQ_Ge-0-lNTO181sPwxf6tfF-p2RZzQrdO5tk9b5kxjueXGR02Z8z0NPuoGEoOwojAMgZQYtGwBgusbfwDJCMOi8tuJcXBFZocd8_deI8bdMy7ooe3KhJLefkx70yajDuPlkkioJS9SEn8f7VnVicgLSC1UYlLyY9-xVW91LwNnhH3os1e6IOLlu672UdTR4cfs8bYmfpKdMn7DpGWjZbGzMenxAH3k4a8dYkS0_c_go4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/enXe-jXbWIJ81yIQ385rzB7IQrkM6hphQ9kJf5pXZBUt9HxcUqUgMIWLccm9fEQhCqG-V9AFoepQ3-or1yUrhr5-muJxcmmNNP-rjwiMmdSxwcJXoemZOPSd4mz1vSje1zaHRPCIttbUKLV1jznWf09ypu38hbUJAKfFDi_YgUqvNc_g0RIKrY4QgCij5x1CUKouNeFd-vL-VjRkq_S8oqNQxcssaiAoOUDzByKdij8b5aIt9o3EOhrxwTTT7FeximmL6Qp-397xxGRyRbqu_AiDMONnW5GyWzAZ-qVxRoZ_icnfBVH7TlL0qmUrphw33wFy7E1ZOjKJv0bL7Zda2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
