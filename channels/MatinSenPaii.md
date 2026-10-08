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
<img src="https://cdn1.telesco.pe/file/M2CnXVzWaINJQ6zYh9zq8I4hRIkswaRq3b0BnIzQcUCMZlR6HF5vcPhnq-m4PTBh30n_hCe0pIr9kGQrM1hVVKCfkp9IkFgAoZZ7kp9Ii_147P0kjBdFp0Z9yEhTixGd92dqCcWOvFiRDAgcBT83vMBrO0w1cLXMsi0950azDlbqrCI2Zh8RBftmL5Sv4FAZw0F1VbRE0j0c-D0R8kMKwdkwxkQl2uavtMA8T2wpqe92Pc3eciqSPXTa6Ss3LkSulkvo2EK4SYkvkxOIhbLFgR64bXG8MipqRGOgs3TXTw9Ebmm_3jpmV-dd1FtJJD7DhwvS5G8_3EC_0vYlFY5cpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DF3zu55kyGk-AY7Wj1wO2EVFhNYBmJ-yYQHSUdMezp8CCCEU5155leO1VgvP74V2lZoAjBoDmh_qc7HgBjh_EsjLNkLo9tp16lRHerwGno7EAqjVl238LL6IhQ76qJ_gtd_S4zlUk1IYMZTGl_0MdSfFIzYmWjwCild3dILEdEOQ5-UYFj-RqbfbZk8YhNyqZBavl8rNPhv9vLMW5_MfIgjka1wBzCtH-_r1VfAixHXJGovbDwBCkG_7OzwdPHcRykpuZgInHEmNQz-cOtZbqzoDb35qBQ4zY1f0KK2Rn5aZd-RbP_8MQVNbi-ODjh1LKo48rCt0UIjGshva6IlpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkQOIF1TWbV61DD3pWIUxS40SMna4H_zpO_IJEBK4qtPBhAhpyTnZ3TLpigOBysuC1Yw3fqXZYFroEKrQNkxoIoOXP66bTyIrTarTDIimVY5cvJVF15WJELaNAnbYwUHe6ev5QlLUIgT4hr_x7_-1NBV4MKvvsvHqg6GGZLWE_AQ33QW8cxo9i_hMnjKsoKiZ3LMsJsuiUb7PPK3NZTa7PwSMIWPUzxo-mMvL2alVNHPexUjZByFTV_UrPaa7hPDvuJKD97cCjzF4L9jGOieN3VV8dZ0VCRVY9EHp0f3pQF53y48B3eco5yag9raOViN23Sh925YYh1B_L66YQiMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INN78890bZ2_31-zdsbuHDadkl14ueBILmmPlhW0JkWu9JO5ev_7ZDqYD4g3yyNak-EuxC95110iLZkNkcytVon5HRPTJbitZJnvLOKQ2jar-eBqgxAN-l-Pw9QnHIQ64YDvYOwbDj7luJ7mtXlabVUj0_ozHDDIxHnrKwPob_NiE57ncjAEm3PZ1FMq1XFQDNcitnnthAUKFCKGgqtm4sdGsWg9LGeGw6iiuKSyMQ0gkG3VfXSl4nMkc01fZifdiyC1pU2mapbagsmFeHjBc6ht9sUXx-YvCosY9uRuqj8Vq0q07K-ULU1uoXNYeYyJ_JmM30p1NrbGYDdRBHRGEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=XYc_oJzYd6lLkKhjXKjv58DsN8ZbYs2jZemX6t96Sil-XzKswnq6CfLJpUR0WsffbMAEQ04CKioltMvdPUYbuRu1CUpor1wQ7o8pjA82NTyEPbL8KoAy8UtTdJBv1-LVpPRpU0iI2v7azzl5ULQVSkhc2XIrZC2ekTiym-6whMrqsTxxR-aZd-i9BX301v9KYwX9G_G5YVCEYQoEikd2n8PXcTuiy_-FD5TwhOFL-Ux41_ac6B_QOEeYGpHB0UyLtJTp_U_ryvCNlxXw58vug9VIOY8xaPNXJ2rYarUfXn0bvEzHguQ5Sug3OqhOse63OLiwau3qBiCrE5Stbt9oOwt7QOBwhyR55E-YDZrWyqIKdFmz1zujBtyLyabh9aNVSTDszAiX2Mg5j_h5DorUU_ni0K0XUtpJbJwNC-DXbV-z5gXWNUGY8BHE_slIbF8INEUrJ0QithQ2DiMsC-5game_5YJJE-rtWeDfaeoa8SUF_C7awzlNLGawEjxdUg4HE5Yw2RROjoz2PskbWkNUwTKnYERyiEBO34DaaTY0kmzXQACiwh3xWqDXYJVETONY1xpW50gBx5wBhMkwpWS-aE4LcS3dWOoJxg4DCIzO8rCnOWT-roVg495f4lpDy-V2WwfiLfkgIQP_Bh1SAK_BTzLBIxmN7Qrr7pVJWZ18zB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=XYc_oJzYd6lLkKhjXKjv58DsN8ZbYs2jZemX6t96Sil-XzKswnq6CfLJpUR0WsffbMAEQ04CKioltMvdPUYbuRu1CUpor1wQ7o8pjA82NTyEPbL8KoAy8UtTdJBv1-LVpPRpU0iI2v7azzl5ULQVSkhc2XIrZC2ekTiym-6whMrqsTxxR-aZd-i9BX301v9KYwX9G_G5YVCEYQoEikd2n8PXcTuiy_-FD5TwhOFL-Ux41_ac6B_QOEeYGpHB0UyLtJTp_U_ryvCNlxXw58vug9VIOY8xaPNXJ2rYarUfXn0bvEzHguQ5Sug3OqhOse63OLiwau3qBiCrE5Stbt9oOwt7QOBwhyR55E-YDZrWyqIKdFmz1zujBtyLyabh9aNVSTDszAiX2Mg5j_h5DorUU_ni0K0XUtpJbJwNC-DXbV-z5gXWNUGY8BHE_slIbF8INEUrJ0QithQ2DiMsC-5game_5YJJE-rtWeDfaeoa8SUF_C7awzlNLGawEjxdUg4HE5Yw2RROjoz2PskbWkNUwTKnYERyiEBO34DaaTY0kmzXQACiwh3xWqDXYJVETONY1xpW50gBx5wBhMkwpWS-aE4LcS3dWOoJxg4DCIzO8rCnOWT-roVg495f4lpDy-V2WwfiLfkgIQP_Bh1SAK_BTzLBIxmN7Qrr7pVJWZ18zB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S31dZN8pJreFykj1rCQqTSAAYMRoHdzftDMav2J3CODpEU5rPAZujVAAJ4gHJBTq4rkXM0xEZW87vvQ_4AMU9ac3j8p_hSoYmxRmyNIwpJPi35k86a7PL0gHKPBcx0re_2b8QRsrBai-c7Z_6bR0sV7XbLmInhAnl_reNe0eyNd6m4Kfg4lPBlGrafMvCwChZyvJmGgcwlI_XuCxjfJUL_xoQmvzBgIYwEIiHsJL8gjN75rKe6iGdisDO-IvG-aB868Hf6mwd9IStEwcJu5AmfwbpFLcjyoXlg0a7mKOjmvzKuLIC8iUZlDudZHroR2SsQCyNbgZ4U_TdJHBtErMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WyO6LZ5VPu3Slq7YacGT6FSPzE98FvFiwYxu3p9Q7C8C70L-0In6SBXK4GaWQIpbdAZT8Eg1H3uUODQ50NgLSJe5FGS8XNJdgWZYPtsEf4uqeeAvBbss5KTRIrwRMvEfFTOJUDrkq50HGARKZQPikWX8s0ZOkllMjJX8-clQDZafeu2Xl5vcG9Zb0bTVbUUFkbIzGyuAH5wWsA1yxtTStktuzRBY4QLAYb7NJVXwi_RjtJegSKbGV0HJNNUemzFaSFiaEcGXHEkMH5fuNiO4Q0gu_7si6i7pIKaGJStp4Fr1FsYJd1tHqZWSPyJCglvZid4oW-tgtHyZIKBR6tMCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FkG2hAVLoGw5VFFBaGMEfIYDNsbTstR78QXWZa4H-CWDeCD7nl8fN88-RQEWvJKJAIvyWHOJfUe0on4LhQRsqTPa1FPnqNHkCLikM1v-Kqt8325xBeDkb1CPJvQ0bNoA_9PO76NAMg8EPsUDQbRJ79noRihVyFb4iltVVQD9ulmW9E-OPqmqa86QnBhqiK0DUcqPqAUDwKAId3t-PWjuzpfAd7PQVb1t7HPwMp1n5Xe107ldAu0m6xBmLgAL7CYgtNUhaqmPW6H15FpsjnBQCxJMMOATHivKSsxk13zUERotPMcwUpEpWCv_tdbZ8SbSvefG_osrFJ9ouCrUCu8ejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KV-9bRLD3Ug7IYw07zKKDbyW2CZaYJ2HZlgJ8WChK1gN4Ms7o0K-H_zjZxiyGkH6LVCaDTblMRkSHvBasEIC8pDs2GO3bMJog6_ld9GOTEIRcXqN8otL816HOog77b007XT3juopthbFhW92j2Ka4t5UCmHSJx4v2VbF5E3tTGuwefKWL8gX9iqdqKPa0IpF7FazyGv5LjNgUvtKeCyIrzF7hb0NFdP4sZQpYEIossnTi1qw85ff3dtLITJLJ9ieUYinvOFIMvFAl1p5w3Q4g8TxR3AnEFj4CCgPPvaHTclAPbB7rr-rsZmS6wDdQio2qiQ7387QOXw-lHKLTFKg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nmgUpPyUWE_iGb3jdfJySjl1TSdC8Jm46qFYapvvuUGs9UB_wxzTsRDg2nlzVmY4IPWjZwZ0xvbRNMwwFtzQetzwEXpuMEdT6mWNMTWg9G0KyfQYKgfPYwa_g70XoJq6RvH8WGhqletGdIn19KXdOOu9n5LLTo9nNB3RqkAmvTLrhWP6sIAZoi9mU1SvnLgRrp-9hB3aou6YgiZpPe_p8OekmjjlXfKrrWlbDiAmYU0ci55_UqFccnbBPpLryQYBDUG8hPy2Avxbg8jh7x9W1V91N-DM620uIl7jgQ3U45uRGn1ZcM-RrlRvvNP_uE7JzbyWxezRgsYlXMNgJRS91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlCH3hcVKCtHIyDQXioljIdePt06hyl4quAJxbYVbhG7RptN28fTpWTdUQyrWJ9IyGq13EHmz1AxUsJGBlYRzY8TdWozF6fdFKZnaCMk2HPnkTY8pOIN8gwn0nZ4NoRExJBcEXZjsYNMh6PIoRdlkmEmIUmAO6Vv2r6qRvdU1nqKjXPx7HUBpOC4Ex6mFACgfL82q0XD13RkFclv5xtKNNGIDQF7MayvsmjYHFnOUSrv8rnHSEvDDPqQTtabQH3Mz0RamAVBvipTaEHHsLu8ufAeyxQHgBlDloAcU_DHz3RBr9-vy1CFVl30iol1tyWuSUsM-HE-totJT1randaqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k13EzF7gg3GxcQvjq76ez_LxUG-CK6OE1G9gk3jDCIiW26OqpKKf0bG_ZK4_Dp9sxzxkJl0DJQ1sL4F6wh-honCWw1Jd6gEZbshoVBv5DDM9OO1APINvp9QtLdWpTtM88MHbrV8-UtxMVE8nQuZWUr-vViDHGihzVA_XUAEhhV9qxl4eeOFTxNbJV_q1ebfdByRdpbBYz0A4mhgSKPNmS-LKyJwWHjnYn3Pu68U8ZL0iRT_gP0wBVEw3FNHIJdVeLPE0_6Wdl4QDboYNA-BegLkxor2_vVggBn_7oI12ys-Ue1k23eDRXn4Inryo1OYsr7-yOWvmp5TDT3F9zYR4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyBDrgQNMfpKxif31C9i_ySWLu8VCKK_HJXwuu12bPDY68KapVT6Hf6FgF3DsS-XXsBci2XDoy3ig-3HZyT1U3UOPSXyPRYbUmyZPxgydRbLzQegDV_HYvDcTXXw7kkdCYZrKS2CFGPaEa7_mqKCEWtxPNmTEF0VWorEzILVSqtDSGGLkMnBFDDHfE0I7BKd2eXEyVkfSFPFtJElZ6u4fXpOTT4l4i2OTK3e9aKOJHxcbFek8lY92QIBCjCdFOh2wwtC6H5kZKn916rgxQdz2whgavg3dRSRykjrgwFcBh4b7tjY_4hQr_vnbI936bqEp8de0zhw9s-NqOWn_qt3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i6fhNt_hOLdlhfmmmvf4qMN8NAqXlMjrzzoYtYp7jb4tkNJxHveJGbEPYsK2LQLd6P58GNzO5vgc932l00Y3WYSjTbheqqKEix9jGbG2yNUsERFkGLkOf9svnzEgwhGIanpfciEkBQc37dwvgQ8JP8rb3wEv1talU7v6Qlz9J4b9hcAaD-VcTX60qHZXzPLE3rhTkh0kqp2CJfIL4vfDgapJQoi57bjqMBlpJjDPLEghNRP_YzSY3LrW2HRz-iR87rL8dYU7l-DYiwzavEK__NwsfZ94GZoZEtBUU5NvWmFi249sBzvSP52zWgWAzgl5zbxTa4XteVO4pp7wHBggCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AE_HXthVWa7E-jbge6PitcPMXLUZGvl26hUEJGnBINnSMBL56HBZtk__xp5Xd5duNLbYmAXoqi2ITIM7QznCmRhxk6-z3BI1y4lZnk6A2neT6z64bZLn-jIwn2g-sDrLAz-qq9i8CiPNIWzPqRloWgaTlABxClvJ4UjC1JluZvzLqOXMX5nNaXW-cBkoP7mEyylPEluu249Cqec3NLruqliR9eiI6ZCepCX641WuA_PmG80j120l-Y2R7Rpm8lTr3MPTxGBNPNROxnVT5qNQmC6WLoxbcrxSsfvfsxGHLEhMz2d7NdVRlsgk9vDLdn1x473lmiFuvvAo_WUvPVoAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPLl95oUeBhVzjWLIx6kU281k8KzDYM4-bxYNWh-tU1byk92nzvQvqZ4Qq9xT7YtQWviumh-n8FD2FFhYz_HFQAckVNHrOBXI1J8bpqbq2lj3PLjOviku-e05jTOqfMaKnHgwB-SIBy6f_EQ7NeXbR_jLzncick3VG5KO0olfvb70yH3p5OO4WU7mVYdZwFCPUfcCe7AIr2Tx1kRHjoPA8J5Lk1OptgsczT5ZOWYuymcvrMNRdQnVCQsg_gVvKP8p4-fNBQGUm3l9t9McqwJG2Y3Rw40R_YRj6HWq3ktU0tti0zwjb--Eoa28P-YWTw-IyWhCLcWqz6CGLyv5YkScQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DavYAiX31uv_xmg3HfpycOftDTAAn88ubIcwNXyvGW2wEIEDbowyr_mv_0CQpOKXqzvTlwIQR3GKnbTVfgTcY_1UsPRZcPRrjY9b8DWy-fwcJgBtdkMRXFvHaM8b95JGUqH26fiL4zaKuly_TtlzPfkrX1tSmtHEdo4w3_cn6-o4OCQfYYfLovWjwZsELlPeWX3sbSDg2pdFgxJY-duSlYSXoEE-95aZhqyjxqrjm5jhJZCMzvQIeGp3F9nv7JXZomjcwigt1IKUfziTNFwLSUbn60Ce-atWBJ548vo0KlLqz2-DPepPJBmE02HxIGJPCwE83YoNBADLBcbyHq9F2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/btsuaqXKdZsYB0T3dYXXOzDA1LMU_3h3ZIXWQkiZ_tTaQhWIr0NIgJwrKnL4BYM85XYKYDQJdwpQHadFdiNEKy2aHLHpZ9X70tISTvRw8f28jxwm8LW98bjjgUJcJN-kqtjXwX-LtuNUkZdv6_oU4SiNQGpqhonJ6FWAGDHeQhZLTA8J7qxqQJHgM3y8czKBd2UINydUIXxwYNPkfvIBe0Zsiwtq7Iux0z_AalZTS3eqIT733gcuW7esCPjPO9j6So9ZK8y7BL0wEKy0iV4691mGszbf-EvMm6pfIZ21z-iM1fMZs73b-cl3_VoFl-7sPmDSmkGDT4LzXgwzKoqtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a291O7zkhLiOqJ-0i_uI7gK9LHBu8xYKKQRMzwM7TnzoxezUGHR_ZjwBsm5zneHgjR8ugI95nHrjpriWptCCIkrpfyTfR9eSdJeyFOFebV3zzdiNqU15WKk8B8Q940j_sfIdPghIC1asbhkNPuxMf4v57kV_tkXII-ZXDX2s0mqN-PeBroPT9f_wR0U_X64vol0lW0k5gjXVxMfIowyr5s1Sa70ay12gVq3-LFYLpdaICrFDwQ-NjqtgCVZp6xDXbqg0fRboRRWmZFFMdXrPzvvvopH39PvTjO6PE8HWonZkUk0PtMUWze0b3D3qCStgOBOSqBfDHcu0VvVD5Rur-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j-CyoAi8zK4i7ogsRp7lnAm7eWROMw41mdpsxPbNQ_zM9ElLrfpDdHm5FsS-_g-3PZ2Sc4v_G4iZoJHLSaQm72QQfboVUS836KAo3hlVFIe6Ab2Ct1fYbzyI4SNsIWc6GZliNHQlNPyBfvy5ScRnQttRYVYrv6tHrPxMRHU7FrUW_dwfdUjqSBCQDh_MPD6RJT9dUToVThnRSBw1rV65nvyHuUqHSwVf6UJgHPYFu3hu7h4njsrdk4RCoUa62FmNrHhnrIMBdSppECQ1v_P2VX5M_uYFzRI_1ILH6u3hOP-XX-vMNVJz1Z49mnbni6z72FJXr5aisZUf_Hyjo3oSDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiyiXVZg7CwJ-RGrwFD8sBzrbi2roiG1-mZmfck3vhdNo-hunJ-OivRikSPvgMgM8aNLr7Qrrm7Vr6bP-c1duUxsgTdgJLzHt82zl7WExRW5EzEfGX2QELUcBIP5v6qKzaUrWaXAH0HFOqmWNXHzqZRTy8gbKz9Lt5dBg0g_q15A0uMB6CcPAnElE6skDE7mlCffv0jHY0RP4bwl_pV1TXHv3HQoPh43w0oDgsriwf1EeyHMKtDxyouZlT7b2vgt9EnFCFa4L-4PbtBJXgwwPbyZVIg-4f19Os4Ji5Q4fETdj0XPYSSVXw8XqzEOaXbYWjgywrv7jCb2KTtP_ZAoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVwMMlkx3Iu2vI-yC9qhBEiX30D40FOtrtyzYHFzIJWyGkUHUuoMECnoM9NDCIdQXas-xwwv1girCQm7MEMZoSdPx8fQuzgubdMR6s7mLPOucKpq9XjtL9Oxxnynupooi7-ZymcxCMa4vvEc6ts29FA5H2XH9DbGiSY1fqDB-kkKK9HqpjzOYpmCwlesEAapURsJ6AsqXHkmFKMd3CQWvvlnaqPm5arW2U5SphKHX0kTWj5oL6jLnCjtTEskaj7kaZZOPOpR_aTv-fXw9fBGtQ0EqRqjdcSVs0IhL1LJT5emmVDBDfbncfH3ARTJ909CTLkcgshV3iIw-UabBE4Cdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e6ToJfZD8dW44pZEaH0EMdsmLfi8hQSNVFB5RzTUblx9MIG2g70KcFHcb4-mLdZyHV8sO8OgYoNYMq56m5XJ_LxGtvTyYnPXUIKb7l67pbZO1PJKMPdNRQIK2Qy6fSZt73af28s-_Tv4ENVYMvMr49U27MC9cc8djuV1qsBkmUjtXGQyFVjabufam9PnylGEtnmi7YcAaQ88-gw5nihYXxmLop7G0-x0Pmsik_urypAjugQcN_VaeSB2x4tW93vAKvHuq1R8dLCJpoNOb1rcccskfWhHyjrwcH9xvRq2vVMuzebUbgqXDji4Dy99ub0yZ0_2lS3bzaJBGKEjn5DwxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=W3OguJgQA1mZ575aYtIC7dlT9fpdckIbWSSdJ0IxRIbwaWh2EetIaMk_jznECmVCzEepxjT1qx_CUpunWfs4izzMlOlNZPDocaZE038yezBGWUACsLDefGOEExzxZ9ho4MeVTcI_vKnzGB76a0FqFUevbcVAuVy5j13pdJ7cqlge-f4e87dh1WWuUxrCYNux6CbNqdWf3YB2J2_HhAhga1MRjTmngXJQtwBOPA6-dGKrf2RZNNf0QeBad64b_uYzx90jNuF3juCXFSvcV3UHP6qExKLzfvz2i701uQ16RRw-gRCNut38_DYgd5OYAjymFETeegZGSsL7UJEDlEnCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=W3OguJgQA1mZ575aYtIC7dlT9fpdckIbWSSdJ0IxRIbwaWh2EetIaMk_jznECmVCzEepxjT1qx_CUpunWfs4izzMlOlNZPDocaZE038yezBGWUACsLDefGOEExzxZ9ho4MeVTcI_vKnzGB76a0FqFUevbcVAuVy5j13pdJ7cqlge-f4e87dh1WWuUxrCYNux6CbNqdWf3YB2J2_HhAhga1MRjTmngXJQtwBOPA6-dGKrf2RZNNf0QeBad64b_uYzx90jNuF3juCXFSvcV3UHP6qExKLzfvz2i701uQ16RRw-gRCNut38_DYgd5OYAjymFETeegZGSsL7UJEDlEnCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OXCov-5txskAubVeD9IytKLCOtt8ruwEQ5eBcjfiKdLpZdSl81PUiM5xgdqptnFjH5G6aGLwBaxuC79P5nctMRk6kzGj9I8suZTOqhaNee3HdsWdMk2n8wKTIKfNa3bz5bBEeugnxk0EW8_FnRBevE6FzNKlPrlPUxzmg9ZyM-XcAu3COdyLH91i5klnD3i25k5a4js83nlB-cY3F4buXciyE7wTiATxddTFiRmPB-viy25jfrkiOJTIUZXvcce3OH5z5hfXNJGCbasoe444V0-mwMrRLglSSLQvkFFqgAogI7i_6AuE9zVZzwwZzYl7KCYSAIpzFkDXI46N88XYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d1v7XcCctXvjhxEuNSVbIa9s-VRqkdNEQW9uybLDAafvcT-JZ_pXRwUjJSqA536Z48A4AmC8VNrIwxIA6SYyy0Uap2Ka_QMqHuMtCT3SsetfwsqKYm2PA8XGwXebwxY66x0cJmq6wPfqKbzKGF_Gk_atn0c7BPrM2llmJHQH2m7ESlZRVV4hTJ89jSWi3Rb2HdEx5hoVfu65GfSCpIoIFr4yDzFxdEV9AOVQw5bXDIocayeiO3Q9sjmgkKuEIeL5zOUnf5mCACU0l32OIN1gl0h-Hsj0-jlLD2zZ8Ur8naUyRhevqmuOTmnqjNuuQq1j1upu9J-gUCk7DcTKrnNklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F0aN3kPn189MhoQUJaVYDpfnxEqto_zXeBaCbJ8Vel-8d3DT70tjB45seregSahYRxAT4vNAOaRu2f1G1Dj4ydXGmNt3xwAtDo4wvQzb09fjkWSL7PiQWVsfx6LUDam7DkkQoYc7L3VShLnzqFWrjALPzYcdTvEm7lK3l6T1hpCJyF3o7_8yhWVw1zqokV6bySzbuwTLBUplzsbTa3R9PIvu1xiSn85IeBnCuozfpB9bhSYdq2jp0RhmDo17MjAAbL3GzjcruJbTl59QQlkDvEEEJqBf3Z2cPg7YCXGFKn2XtTYBJwQeS70dZeO9o0BIIjfypzD1dBMyLykGJwD6Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G3IZoIqVyVSOBMd9n80aCee4N-vJ97rk60ROE5vd0hSWJvW5G9IHaSf-39s5GTDuK5l0V0dLMBGYVi5WVYx9uQ9GG4xqRgGRYxwye7fGl9YLojVrnq5QtJVoS1BIEmQ6Emlmp9vD3KKPip5G7jbesvgzNfNbzxdjVoQ1Oz2ICYISwKyTHjmVYc0h1htSE0At_5Wtw4G3hF2zqNpSBdl7TrMciSNn6Oip8Ml_yIXMkHmksQNrsciCe4WS1U4BjuT78FYUv6S-wOgKuI9xfMD5aLjjzJ3mjWnJcqst79hJnu0ENQx1EToLlR1S8maxKqTphJiqQSUKNVZyffp_lD8K3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcdnrTpFdzGZCqtGaVIcKJI0GWLHUH9aqnyfYKJcpT95FCTJe5Cyljcdduav2OyC9lBMMWkzjEc1uNa6ejbX7D7b3YPFv11R3XFo1QWEPt-5oUtt6EQDz0hemvQcP7U5bbWwWPqxvZqMZzVQKW_LlfWKkFB91xirVMAa_MnX36qxcNZgZ77CJ_I4aRURdlAtvJhT31mOMd9imDMtrVtbj_42MJj5fzvZ9l2VeSUwoQ62_o9PfqfXcu7ZVsN-UVj5zHGv8FoU1qOdkXGVi1T1hXFVU_jdPNIgdVGMRsspRtm0GNSKRgz6IESEV67Rm6A61aa_f-kCUTRpEI19fnuacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OKiSdmWPfFfoaYG28r4AVrieal1Mnr-iHPaC9BABqvWjFjMoZgNlru22UC2qNlTQjcjBA9CB59jJk3uq6ODI7-jC03g_Ueh2HF_A8LSNF0Zthkr2ujz_8nlOAECwEi3L0K-vD3s4YORGcua3Q31OLXvrmgyMx_D4-8uMrS-PRUrI8fjxQC6efrMP79O1OkJHbdp9IQHspRp9MWief7y-pSPuue05exGWew6_PeWDcECkAmXGMKxtFeXDGkWSKo_OY0rU262sUiPNjB_rKEoCO4pEdNiIY-tdH3ep7oRcY9c85SUd0h6IwOvD5Tz3HR8rJPQ1NGsM7vmQRe1WfbK1iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-VihJleJfu7NjbPCrkmLLBjfjH-q2bzSWKsrv2RcD6A7kiaFecYnM0q2z3WkrWvoacEj2NqvbS_UG6LTUKxNGw4vkgd-dLqdvsou_pxz1MBvoxUw6NXGCIRasZzGtqWtx-8sJYVNgDIEFFX0hjmjBsLskjCH44-_X8W3C1JhTCYg89Tew6qBS1CNv-SPHDp6am3BKZ_IQxtoIF3kOy9HPsKMzoHm5N9CXhksXZkCq9yRCkkhRBskmd1lqYmvRA41DSy4dUpSHWQzzm3ua6wQNwrC9zDcBIhzoiOiHVB97qcGSDivESf6V3CvZ7B9MROkDlMK639RULlks7oW7O9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UhM2her4CMw31weuuuq4w3XbdqN-fhmGQGCgQhvYabP2NXqtPqz0AShXd6nwtRLj8INFFtZj8bI7dnufRnIHLXaOBwR6TSSu-B5w3wWv1ZLC4Kr1nKFv4ITYxg4beKKSZTwZzqgX12zCMqnRiIWbeW7PJoXWfHUByp2ADV8EMFt9Kkagqud6yncXVmJVSpXZ2lFLMfzW-i0hOtloEQejX_r5g62l8e1pZWJQ2qSrZu2L-5tSaIJiqOgJcyGe_EyEnEXHL5xGOove4jc0AOawxcoCOio2bNJP6i_wC0xQpVwslRQG_nOTQxDRUtjDwtE3YKTPoX3zQNvmhKo9Pvki_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aIPxapOibv1R-17QsDhbJ4-Kl0onIF_VohfaMudhOBl0omUPAOkSZ3wsCLq3GTeEOVcvMAULkmEcgrKwAeN7S2r_Fj25nhiN9iieCmCOUY-hXM4RTRd3-7BkDFnuVs2IV5a2NH1xwVd_FFzq90AVSeKTq0yiCxRksZZ-w__s50A65qK0ZiW__naTSaDH6Y9Ia70WHXS7DDgyHp7ImpqBEsDEWtrQkAI962xv4pLpJ0nO_2LQGkyjO8AqKcsWXtgYOr4cH9InmSpfkMSh62c2k1BFtlrp8GxNHLCJxqtpX0CgOv9KXiYhHU2xK5dyekER-63IFUEGNidAGT8GfKGcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lbwqXldk2YdaeWf3ixPDHO7RDzUwcRL1iQzvf6lfinoDbTcO15dy2Fx3878xNVeOX4QCL6UDFnXxYeBPuQM__lJp5VwH7_BMTjIJ0xueAsarAaLTlAyQDfItGPLfpsFhn4v4Ck7goKNc6T_Vtx25txwf2umO7rZ9II2M0dGaCTKT7n-LMc_aJ6-GE7nKwlf2wiMlJU21eDzSU9I11zWiD779UUtwUHdr0ynFFWSYOCVOsVNzyr3X2LXm3s3ZUKEPNhQvUH18ZH4e31icaEjGElReiHbw9z00GwgiUtj9Xrlb4xRnxUMqbtoyWNChPjBV_Fflp6iY6_3rOreo3bit-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WnErrvrlhqKm6CbWE1gd6LftHXgE-9h8dMuRG-OghyFzEil4FXV2vTG_mR-ZqQ5tcZH-ADH_FBrjWT6IzHxdmv_WGAefT67fIsuexJM6gA4-Unp4QfMsM-ydKtx52E_mQKC7iWm6Uz7dcneryMq3aqJcqxEq1VekPqbHTfYxMGzMw06SJRd7KCUezuBvWm64HMfaK0SaqocTXaTRH-Nqm_ST5P-x0xMzs7wj-unHLkDFyzJrCRhETd1WlzxFNl3d90BbsWHfplDwRGZuj08oZBOEeE-g7oWAAWBUNGGdnwoXq_Mzwsi8qHGWwVspww10T1KkacALrinhNQDf2sWxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3i8IeQFkqjEkQ8bnEGOQs8kbMTfRf5zuvkfBrr_3-3FmQ5Q7OBODeZVib4Ur2KTQY3m1t2GhbmgPo6F8PMFfj5PhWBwkV9-hZBRjBy1GKOQZF4QrRN41axLrPeCHzvDoDV4g91jDUQse6ib3O3T-_cB4RX3lFGcEYSWBKdDyPjN0wi24NSG_ZbOe7owmDY5w9lDH5W3UpyfUJWdu61GEFDXt6deacZ_Mjy8mNs4TSBs3bzPgYqFLviq7snTDL6bnzuW-h1ihc0qusjEzoK8PplzmaSw39CX4aw3IOjSp9MMa9m5QitSav8wJn344KiTwUB89SnMFtmQgSRPyIpjoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gG6qX21muzVHRe9NWDPFSJGjA1mH5bTsIRItYH8BcuxofME_ngfzOHvOM4fBmvzKf-YKFMDiZmYVaYCvboGP7h2JQCyfs_QGoYcC0oShXEEKq5wdLa8bITZk0zdT1Zs--73yoTyOTTHuOvdSM934Dbf3S4eM_PPs6YYwtzg6kf863_GXSaL5lIS5yrJ-FSWcQj7wY_6TISzua2-GdcYoTZooLFw4YzRnbMjd0SXzO06xv3AGJhRGOIAr1W0kYTROQPU-kEEsUeFOtSN8xZ6S34bpnkN5UJxVeSeXSNwF-qZUaxf_Y5Itj3z_oPNA_F-PX43H6sCgUmC-Sz2EaMm--A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTT0Cbpp6HRw1KE6fqWn4cI3QyFx0cOV994DmgQNkmdnCgzyq0Ry-lc04uhgUp_xV309hHa54_DWL91fqjM-wiX5E11qWYZEaUNzvVwtRuNger--pfol2f91lDI68U2JivFUFoJ6IQESEjryb9ZYum8XrBiOFrqqWEqFex3mVgx5Hi9hQ1xLMc_Gf1Ba-QeHh1TlMPIZqSqP6i5HaXqcTvsb-YE4VtdMms__VR3ULeRMbHbLl84__22KgGb30vJ79A9AV8Mlx0lDrLsihVAYziFyVpYKWZIO2N1zfRerp_8seUnH--1jfkopI30XoypB8SUqYARMzxSftZer2n5bJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EU7DTj5LLu5xOIgBaTtLpg206MkAtU5DYE1_Oth3AXOqI-v0kZqUkNCLrT9B_mfA9mtTq2pEurSUrIACoPiSqjy2EdCBqMNpL3MzNhhzwbNXmTJkypGDZNhPmXWAX_w6TlPUK3q03u1JiLQgQCaB2KiPi8QohAxZNseIsmhcn7butZZaT3XSkrI9CS9g3cwmlML6CgOX1vC-QhXI4WH1m2HfXeXeMmr-eASvY8jJnoDI7_DqvSEXT2NbOVE6WKsP_S0oG2YtRKwguU70GMLuG-RNH8g7mTgoGxQHvQNIwWv61GT43rFZLXZNhFtpNVApaDwGuG0O0XG0BTMvPJ4eFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJx3JO4FN4rzjMvk8C9_t8H41qBQ87rVth6qDvemIAUf6JWJQIGC8kVNwyKjRzuGL7XICnBjMgjr4JGRFOph3lOwZfr5Nn573srvWurPXWAt3B7T3mkdea0I43b4HVwpemd5F6mj8sAY8in3B8c_YeCvreuaOdlhmmCucOaxFIpuCPN61kuK2coPT8S1_ihxRmO2PzVGh_eWdACK0DIUys-BVA-xPTCEFdrVQzue5EP3BsH0axjbjGq3QcWCLsyxy_ntxMh8tBpMvXM9tla7L2v6rdPHspN-9Nd1yv9hhxchoLqktwxs2Yxtlk7vk-e7uNxziPTXlavhhZpqPYbsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FE620wR80hv7BDqo8O1N2AyBHGo5vXyIPuuFyqVLLGBsvxCK-VNJXTKOimgVkK77Y8e4KRSIQu1KbN2o3ARP_ugPPv7PAIAQkJdmm7tuxNSniW4AKd-fGi07lgIjDFcXh7BE_1KJefWJBtJPuKy8lfiKHLFn79b4IChug_TXYnB3phFC8yalzhUyfda_ZNpYSZbAWNoEM3TQe7YoT9rz45sSfgxXK3-8k4fu50_4KnIvL9aq0vYwXYKyDUOCtxZM5N0sv7OLq9VWvcVP2Uv4pEebGdSBX4M4PjiRtxJCayDciDrqTkC05Rvl0X-YD3NjvRNE5mNCU_DZJCo8ITQC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vFoK-FciJIAzjbcwfjJqf8RPmpveUNEtK4DlKi5UhcpWCczucr0UjO2vzWXCvm-kr1K0oheA_MRtGbr6yEOM0DxUE1iIMw-vhoZgO9pOiC5okji9_G7YZDfs4wVsABUJcPdfovn7pjA0bXTNC9vbgBoujjQ5mxczi6jtWn-GjUoFZ8IJAvtxkVYbWdXHYLu3okxAbFAxZzVoO4-UoQa-YJJuLnLXfGUFSVpYWISjacfLLc3MUfM3mA-yw7X464Fw9topX396_7SzF3cqds8E6B0zNDx84wVmwJ9kFSYtc2_mq8T2_JZSp2td7wOhFZe0kyNhvnEjMasVTyHKadj-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPuoY-FmBGev3wSvJvxRFWEIHwUceopcm2VXBeAJYsxBvD5W2QZ8qoGEJHCQinAAb46-Kw3LU4hiUiQXJVDihBG-DEus0atSew0FpjXep7zw-qsFnG6rlRvKaehAV2olf9bulzP80OZBtMAZEscuVp-T4OqE7KNvtF13gzQMfhnZVgcbxOa5rKrj8xwJyd2XmfOHyVOJASyQdEtLkzYuX9ipTzH8ejc92wyt7mqGLtH7qW3YVcYPqqtqe5PECA0BIdtpVYIXy4Rnb44C-mXr7l4-XHIUxnuBR8CCmh6hO3Gwpxv7CplyYaiUIB2H8jfRgLLDzrD-lgiEthjuc863Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6rAr1DL84VXwz7XBNtqAfxHS3gZTkvPCHQIXS4r1_jzQkdlQPbnW2r0tdbyXUaTPpgjL560eYiZxgfWGV2Ld2xNkcy_hh2GhuOj48qDYsPKy-jLqc5MrgoNXRQ3QXLn79HCp0XeEiqxHwAUnx2z1kTK5sgJB8N7s_a17sXATiCNrecqaMuOAEHcRYHGHUiAoODAkHfYN5wrVG1pc4jvlE_XV4tEzQyBhrtkgU7s_07f7xnMEDhCT5AT468FxSwSFghgtq1MVQESkMf3ZBVT1M9faU1c2i87UNH1CPf37M4mYt9uzluRuHxqBYkTkIG5Yk4NTiW2USQwoFOb-w5xIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E9TQkX0dbW9BRe3X0wetgPHviBsGu6hO_BG_P7ILNozdl8UD3MdgUIBQgeVANZ6lvwHWMPymXh6EgUCTu_1HVfXgFbZ7bhC8O4_QcqWVAD-IXQl093C9wMJQg9VSEW5iMtbS1MsTHHpbC98k4FiR3DtPNMG2f9YnMkDtVoOlEpXKZfIa2qoJTnbsCAPnJew7R_6XebyOkX6H_3vc0RUq9eM9-6gaUU2ig-s0W9mj-DbIK8sBanc46YqSI3Xl2nAq6ur0clgmJ65Ld5ujWhbRXRBdv_D1ve2eha7SbsrN-6U6G8p6pfFk7XZGpPS545yoG4niD9i8Cy9JpSrVe-zRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KbJexZGapQXerqBwMv1DYCvNGoG730s1jZi7aJFqBcldHHYGc-jdy6pl04dLkPWT-_96J1yW8SbG9gJ1iAxDVNePor-bJ0I7ctQY21Lq-IUF30aNM5MOami04pYsxzDxJXNBLo6P8ReJrRvZCNQYlWW8o6XbX4ZD2YaXZ2UzG0mqm0DJglHkhMxDVB7R9Xn6UoY16jhpmiDpnLp30GlqEL1vUY3CMoCtl6LW1wFIroxFVUk3XP4sDeg76SLKeDJC3rkJTmw-u_InZl1YNvPJr76_CmFeRgOsN-9181YqjidEbXtcrsU6G1u4FAbolWPrwLuX4hysdLI_2WIWwpJz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDlIrRXx29ZRAkQHF2Qe430BG-rlDo-Vq_I4fXoL6qIac4mtuL0SowpPyU4W9MCvaIivb93Qo8rCb7F-yee4-LniUySIY23VdFm-ac3aCBH5OVKa9c3jJgtsNI1LFcbhQ8zOywjTczp0VQQaQKmFB2RBVdHm3udDFf3bwoPKDY6WFkxb8h1QTogH8pcp5JHcmVTfXuBIeLpHYQerkcP6tmuG57Zoh_z3GzkIo99NXYSira3tRBA-4Lm785gOI5GNeC3zfqIz_sWBPXTi52FJzAR91mxgOPaJbstpQFu82-vHerF7--jsD32KHMHvvfW2hB7NVmL-sF4Yj6orXTVkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mB20hYc4MjuUKu-bFkpP4o3IA13LHPEOTpE8nwnX0gsIreX09HPQ_8S3yAzeJpGOQpw-jT4aLzHnrqQ_hS_Z57IEPHmGNSSST8xIQ-V1fgw7ghTyb_xcv34z6hMK6R8EYX6sxXyWW-khvjyUUxOpZ4kWYwVLs1QGYMr8-2k6pwVcr1w7sG5V6ypJbbuxPNCStlDfWDKveg9gNSK-Wzr1sKKkaXemu44gfx9oNDdn5gw0HDSErrmJKLWmiH8VkKtHjWa-REsuJnQtv8eqxEfWVZ8EAs8ks3IZbLyuUYddENp1JMmsrLusXNKySNfo-9_lfBPjit7k9eCtKviFb5nrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CVe-GfEyymRmhMc7Rx99MvG1Jqw8CjNKjq1kkuL_XaRRkwlrqCwVic-bXVo3O35T7yE9Yk-93Kud5GEojDUID0xh0N7wlDuicMe3b_N24t3eFnZpCuQ7RoOzfDNHQnlalZmzG8bJw5CKNz7funERbHGFNAx_KEFcgQV5L38LmNoK5KU0luzgKbBcp7hgZxsowH4fxxlKkhJRF5rPPUUi2XzSdQ_9gMM4nQx-saSIFfk219hNgT08NGOFJqHUgdZMCEv6_wxSjPuWJh3FOyp_Tk3zbUfptmRtFY8jDSmItXgUJkEzsqw_O4ru6x4C6FVQdQNmkruFlrrqOIQ2p91Enw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=AovGTp_jjJL1FOoqDuODBjptbrKjsgCVSEipXhDVGWYdiUw1Iu0KMS2DqqOKbpgSQHsTmAeg1Urjz2VsAwJ0PXDV_4JKq4zXjapDwJDag6bqKnrEpra6xfa_r6Ys99jiKSGZs-giXNqdE9DHuzF9fyordMq-sQQWW8mR74xge82YndEKN2gTd00SaO2v7NWHYfHycAuU3kEwS1INyQU6pUJyJPZZtmaXNKn2B-hXK_hge7gjjyPr0gA-UaiuWa3CXYHecvCG9-CPhfv1X_RM7BBak7p5DtVQ1sPFmDmVyT9l87ZbTMxTszT5yROkLWlN38dP_sbKTJW7xtpYQXqqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=AovGTp_jjJL1FOoqDuODBjptbrKjsgCVSEipXhDVGWYdiUw1Iu0KMS2DqqOKbpgSQHsTmAeg1Urjz2VsAwJ0PXDV_4JKq4zXjapDwJDag6bqKnrEpra6xfa_r6Ys99jiKSGZs-giXNqdE9DHuzF9fyordMq-sQQWW8mR74xge82YndEKN2gTd00SaO2v7NWHYfHycAuU3kEwS1INyQU6pUJyJPZZtmaXNKn2B-hXK_hge7gjjyPr0gA-UaiuWa3CXYHecvCG9-CPhfv1X_RM7BBak7p5DtVQ1sPFmDmVyT9l87ZbTMxTszT5yROkLWlN38dP_sbKTJW7xtpYQXqqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tx8QrJn7a5jiCoBGONfQj1TTGQVTKxcVm6rbbW4GDLygGc2j7zUEOWFF5_7syeh-T7q6NpjwWP4QdsKDLzL6Q8y9OjeinhKaVgy6aFrJITWgRxmw786pmrytcxiSjBV87ov5cFacWop5_ROIxamcvs-4rAZ2hw7s6F5sTemDVqudaPzWMbaJYxaW6CzevzDUZ9jAp88_4BTaPYAJQF-DzPDZs3r8WU9-6S3YuxLEypZMNpCvp5q80bmDxGV6nc-FmzamVYpdDmfgKkWr3mTNL4KpnGyqMyD5tv6UlZjn0zQatAeKITPk2WB6WVStax-Wfw5i_6mr-A_98dYGrsRCsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eWezyrt0aMHvSLA1oIQUDdrQ7D3yEl9PurpkaFRJrx_l1nZ19OaHNpI495ESvO63D7ECBi8lD0kUuAu7cK3BXL8KPwH_1ihmxaQ3A5oGdnAOXKfdrwZw1iaivZJsDZ2_GtFEOPJkeog1wHOnEjnUM02gfiqcqjBxNOmMPm-l4q5r8QDCjUqTMJFzQK8IxatiXF-wvyFnytiI8-l0URGxo85Z_c971sUbrJQD_nDXPpJ0ERrGAdO6FmsKRhUEqfdKnWpkmG3wM84sIyFOa-RpdT_iIvf158gnN3nEVqOMjmNLCNJyevx5zSm4FB0QKz4A6JCIgse1s5pJlSAkV1T32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mT8bxu-D5cQ0muP76zQoqkqpYoDPl6GwwmwwuP_06Iv9kz_IA4Ik5gJjO1Vy-_fUGBAVR2IRf7rZRrdIMzcko6Js3VdjZM1UP3ReTWXFMJMvJno8qetscsnC_9JobpEe1508RwI6DUEnAhpVf9qAIY2XVzSrTHh5dIB3sChQ9M8bc33Tn3jhDKFaDfybcF0IcFHaCmB4rM2ackhkDTNIKGZ4GXITHBcudyyYjYGQuNXwozcMy0QVCLJVpEjb8g-deLTOf4H_RLdDWwDmO5Lu5NsOC_2lWwjXRpSHEUJgppw_HMe8IN_ksIHsMFzSMPsoXBG_8wV7otg4I_aC9T_4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
