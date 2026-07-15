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
<img src="https://cdn1.telesco.pe/file/AhyDjRcMrJHi5PIDi85840oPbdXn-aCpMbQsU3yKK5WL0hJ5XnEtr4WFV36u6ARtQEBurSUMYjPftuyYMM5oyDlLjxwUCTzxnMuWZQd8LzKKICHs7TdcmDgkS1aUbqitt2W-7Fl1EyjHIHGofkYcCIoDaSpF6mvsjdw6UwToZWuPshrofECKY1SVYvMWUa98w3WXiO7QG2sJoFYcUntjkcBqxsvW9JPiAA71JnHjSNVS-4U-LdQNrR9ZhmnFoYpIAt2CD9Tphb_QkTPrMc2VsbqpZX6kXBxDavZ1yvP8Zr-Lc-8T7zZ0eYJAmICqkDuhCsPMnE1duqXc1GkdTUSbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-4507">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نسخه‌ی اندروید هم دوستم زحمتشو کشید نوشت:
https://github.com/ZethRise/Aethery
البته هنوز باید کاملترش کنه
😀</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/MatinSenPaii/4507" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4506">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GpQm6_fjLasMNHt9XVCaGzlNXQLN7CuIV9cc0yLSlBc8YjlfeZxGf9Pz0FB4CK6yGD4ZoOAvPqyHPljKrCIq70v6CIk16NQiQNdgt-E1dRC4PynmrztPmfJ2X5Xv-gw-crT2UB6eYnWnv708Lfapo0WUlDxRM7UL3XtOZdUCs1RIk-WwQIsPynGHNYAcTCDvyp-YBLMtgLU2medayKSGakfE_Z_2ST2urDw7STAdRpXrHVKZ1wraZSECKbDBQ_8zTQB8iP8xKoZaDRomvAKoUGuJz5BUdct6xO6i20R_wUWhzEneOzksRx0s8YxULV-35wGiBF5uPH94jwRB4KVmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن Aether-GUI آپدیت شد به ورژن 0.3.0
تغییراتی که توی این ورژن دادم:
الف) آپدیت به هسته‌ی 1.1.1 خود Aether که سه تا قابلیت داره:
1- دیگه وقتی می‌نویسه Connected، یعنی واقعا Connected! تونل الان به‌ صورت سرتاسری اعتبارسنجی می‌شه تا مشکلی که توی اون برنامه متصل نشون داده می‌شد اما هیچ ترافیکی جریان نداشت، برطرف بشه.
2- خودترمیمی MASQUE — در صورت قطع شدن تونل یا شکست توی اعتبارسنجی، Aether به‌طور خودکار مجددا اتصال رو برقرار می‌کنه.
3- اتصال مجدد سریع — آخرین تنظیماتی که باهاش تونستید وصل بشید به حافظه سپرده میشه تا سری بعدی خیلی سریعتر وصل بشید.
ب) مشکل ارور setup prompts برطرف شد کامل
ج) مشکل بافر نامحدودی که باعث افزایش تدریجی و مداوم مصرف پردازنده توی حین مسیر اتصال و توی تمام سیستم‌ها می‌شد، برطرف شد. الان مصرف CPU نزدیک به 0 هست.
د) تمامی کتابخونه‌های غیرضروری و سنگین، حذف شدن
از اینجا دانلود کنید:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/MatinSenPaii/4506" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4505">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش ساخت کانفیگ bepass uoosef
1. از یکی از لینک های زیر پلاگین bepass رو دانلود کنید
✅
•
https://github.com/bepass-org/nekobepass/releases
2. پلاگین رو داخل برنامه نکوباکس فعال کنید.
3. وارد لینک زیر بشید و فایل worker رو دانلود کنید
•
https://github.com/bepass-org/bepass-worker
4. به کلودفلر برید و یک ورکر بسازید وفایل رو داخلش اپلود کنید
5. ورکر خودتون رو در فرمت زیر قرار دهید
https://name.workers.dev/dns-query
• /dns-query
6. فایل خامی که باید در اخر ادرس worker خودتونو داخلش قرار بدید  داخل لینک زیر هستش
https://rentry.co/bepass
💡
خلاصه و نکته:اگر حوصله ساخت این کانفیگ رو ندارید میتونید از کانفیگ اماده زیر استفاده کنید و از نسخه ۱.۳.۴ برنامه رو بریزید:
#کانفیگ
های آماده بدون نیاز به ساخت:
👇
https://rentry.co/bepass
(این کانفیگ هیچ ربطی به پنل هایی مثل نهان یا bpb نداره و کاملا متفاوت و نتیجه دیگه ای داره به خاطر وجود پلاگین یوسف د نکوباکس)
#یوسف_قبادی
@xsfilterrnet
👑
@Paradise_Of_Freedom
⚡️</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/MatinSenPaii/4505" target="_blank">📅 23:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4504">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/4504" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4503">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">این‌روزا تماما بغضم. از دیدن این وضع زندگی و اینهمه فشاری که به مردمم میاد
از اینکه حتی نمیتونن یه زندگی معمولی داشته باشن
از اینکه نه نونی هست برای خوردن، نه آینده ای برای امیدوار بودن..
هر روز میبینم که قطعی برق چه ضرر‌هایی داره به مردم جنوب میزنه..یکی رو خودش بنزین خالی میکنه، یکی از شدت فشار جلوی دوربین گریه میکنه..یکی گوسفند مرده رو میذاره رو کولش که ببره برای زن و بچه‌ای که دوساله گوشت نخوردن..
چی میتونم بگم، فقط اینکه پا به پاشون من هم غمگینم..</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/4503" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4502">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4502" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4501">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی: https://github.com/CluvexStudio/Aether لینک پروژه GUI من: https://github.com/MatinSenPai/Aether-GUI دستور نصب از ترموکس:  curl -fsSL https://raw.githubusercontent.co…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4501" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4500">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خیلیا سر ویدئوها از من می‌پرسید که کدوم روش برای نت ملی جوابه؟ و آیا «اینم زمان نت ملی قطع میشه»؟
جوابش اینجاست که کامل توضیح دادم:
https://t.me/MatinSenPaii/3680
اما خلاصه بخوام بهتون بگم نه این متد ویدئوی آخری نه پنل‌های کلودفلر هیچکدوم وصل نمی‌مونن طبیعتا. اگه اینا وصل می‌موند که دنیا گلستان می‌شد. قطعی اینترنت معنایی نداشت دیگه.
با بسته شدن
cloudflare.com
و آیپی‌هاش، اکثرا از کار میفتن(sni کمی سختتر)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4500" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مشکل گیر کردن روی answering setup prompts رو هم برق برگشت سعی می‌کنم برطرف کنم
🎨</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4499" target="_blank">📅 11:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">و رفقا در مورد ویدئوی قبل و اسکنر، من مشغول کار کردن روش هستم که اسکنر رو خیلی خیلی قوی‌تر و پایدار تر بکنم روی اینترنت‌های محدودتر مخصوصا نت همراه، و به زودی ورژن جدید SenPai Scanner همراه با نسخه‌ی اندرویدش قرار داده میشه روی گیتهاب
تا اون موقع با تعداد ورکر پایین(50 یا زیر 50) و با کانفیگ‌های BPB یا Edge یا پنل Nahan تست بگیرید. با خود Cfnew تست نگیرید</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4498" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4497">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تمام تلاشم این بود تا قبل از ساعت 12 که برق بره ویدئو رو بذارم
🦆</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4497" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n7_lz8RRLb9wtiUIBN74csPDiMcEl83XmDQgVaBJ1oiEAbYpZeiFx4KWjfl8ql9dqdCW5ckPmRDMC-VvxfF7asjC_mzQUvDIrG_173CS0t8CQ2u3W6blxZvWbgOVF2qaRRc4WfuHF1N54MIeBfSXqHA2cNdYdtEHYOLC2U7XYYHaOeuLAT9HRHq2QpP4JMC5-OQfxcMPBOD0iIjF8Yu3qIqJrg7-yaOqBWrom002Zowd-kuH3KKMMBlqSNMMwjisq5xQqAuB2wbA_Jn2exGTGcGZTQZHuMVeZxB7fbHtLbCRnoPBFFW6IG8_oWH-dy7HtuuXzcymDL_Vb7rHaQtHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4496" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نفر اول:
دوست ممد
🥳</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4495" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آموزش رو ضبط کردم. قرار میدم واستون کمی دیگه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4494" target="_blank">📅 10:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متشکرم از همه‌ی دوستان بابت فیدبک
روی ایرانسل و مبین نت اختلال بیشتره، مخابرات و آسیاتک و همراه اول جواب بهتری گرفته بودن همه
برای گیم هم Wireguard بزنید. نه warp on warp</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4493" target="_blank">📅 08:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4492" target="_blank">📅 08:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگر سؤالی دارید، توی کانال سازنده‌ی اصلی هسته‌ی پروژه بپرسید:
https://t.me/CluvexStudio</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4491" target="_blank">📅 08:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CzuNTN4U2AqDOL4STq14Kh-Q679C3-86y955PoejeId4yN_22NTnMUzIjlk4yyeSfYOnT5Y-DTyRfBHVu2HfDMdGif0SJ7xTdDCfc-Q2XPdof5CxR-ENLBoKvoCUj8d-VQEEu9rDqztRDsyGHRwLBef6Iq2AUv4ie1-M7msmxnLzPTlLdL4GRnZOis96-ALyW3do7y8JwptI4Gl67iNX3UtWfNJqRzZXUXL2L21Y7CgmCmQ477Oufe66oKJpFg-WB8uIjw73GeulcvJou5-IiTi1GJNlB5_YwdudVY9O5TC6TqhqP-3getbldi08ZGVaP_UFrGY_R2eEsXN82woarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که Wireguard آیپی ایران نشون میده(نه آیپی خودتونو)  ولی Warp on Warp آلمانه اصولا بعد از کانکت شدن هم خیلی راحت روی V2rayN بزنید و وصل بشید: socks://Og@127.0.0.1:1819#Aether-GUI</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4490" target="_blank">📅 08:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هنوز کسی سر گیم فیدبک نداده
👀</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4489" target="_blank">📅 08:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sknl_i6LaVivZoYigq5mEYY_R1Ghf_ihGKbdVLSDnE7KH61zIEgXshgInV1eYp2rSlxMbHNZSaEZrCQBkas18PZXyq5AEjEdx4TEcurZX-AaVWlqV5mrYGrdnr990GTup-4K0-T-BRuZDyyP4vKxxu4-vmuivw3I1Fc6Y7j6TxZtbz99KDFBX2Rldqnt1QnWNQc_ko0O7fm3XXPNT5X-kKNzc6dBFrzDQfao4FmV6VhIlMzm7AUQ8dYJ-y5v3AhG-6IJZ_0hxkKC6UIe1hZ9gDxzmWx_wgl2dLSY6CPmRbOI4gREdLqfz941hyQR1TdT5LQd9YqbxHpkFeterOz3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو مثل دوستمون می‌گیرید، پروتکل‌های wireguard و warp on warp رو امتحان کنید و همچنین scan mode رو هرچی از چپ به راست ببرید، سختگیرانه‌تر جستجو می‌کنه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/4488" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">موقتا نیاز دارم بچه‌های گیمر سر این متد Aether بهم فیدبک بدن، ببینم تا چه حد پاسخگو بوده براشون هر پروتکل(یا اصلا نبوده)
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4487" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4486" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به همین راحتی</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/4485" target="_blank">📅 08:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خوبیش نسبت به Worker کلودفلر اینه که محدودیتی در کار نیست و همچنین دردسر اضافی هم نداره.
سازنده هم لطف کرد اسکریپت راحتتر واسه ترموکس نوشت:
https://t.me/CluvexStudio/254</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4484" target="_blank">📅 07:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بفرمایید دانلود کنید. قبلش با سازنده‌ی پروژه مشورت کوتاهی داشتم و اجازه گرفتم که روی یه پروژه‌ی مجزا GUI رو بنویسم دنبال راهی هستم که همچنان اتصال راحتتر بشه. فایل Setup رو دانلود و نصب کنید https://github.com/MatinSenPai/Aether-GUI</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/MatinSenPaii/4483" target="_blank">📅 07:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه ‌GUI راحتتر واسش نوشتم روی ویندوز</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4482" target="_blank">📅 07:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روی گوشی درست نمایش داده نمیشه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4481" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خیلی خلاصه بگم:
فیلترینگ به‌طور معمول دو راه داره برای شناسایی:
(الف) دیدن امضای مشخص پروتکل در هندشیک،
(ب) بلاک‌کردن آدرس‌های شناخته‌شده یا کل ترافیک UDP.
حالا  Aether راه (الف) رو با تقلید از HTTPS معمولی + نویز خنثی می‌کنه، و راه (ب) رو با اسکن دائمی آدرس‌ها + قابلیت سوییچ به TCP (h2) دور می‌زنه.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4480" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PMzFtcZf53rmg5KqMPy52a-xYrlFjo1UVWBNvuKG-_E23EQdw1o2ne_QQ8boFOiahFcwjgq9bHBbUpZ7-QkejisjrmyR_lbMkdXvunV5tsyFUsyvX7DTeyeawJPrl9UQFpyY5pbIzwX39O-1MCDZxziy5CSk322T3BbIl1ngDLhUP402pT8jp08d7r9HseOkXovAsrYuyeI2MlcDzD2agbftP3XTonoNzKpjDoVhfr04_qxb1GaGydx8MJ53bQUtwrKzgh081TgI-f8Ay7eWy_xb0YHvqfJbFdFE273U5njpUokVi-ZNezQJlzEXBv5zMk-IdLBzuFNN2lVI5nLybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4479" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4478" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به زودی آموزشش رو می‌ذارم. هم دسکتاپ هم اندروید</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4477" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
خلاصه از متن و ساده کردن برای دوستان مبتدی:
شما فیلترشکن oblivion یا وارپ(
1.1.1.1
) قطعا میشناسید.
این فیلترشکن ها تا قبل از دی ماه خونین متصل بود و شما با تنها وارد کردن یه مقداری مثل ip شیر و خورشید متصل میشدید ولی بعد از اون ماجرا ها از کار افتاد و هسته عملا بروز نشده بود تا الان.
حالا یعنی چی یعنی واسه
#اندروید
و
#ios
قراره هسته اپلیکیشن هایی که مربوط به این روش بودن بروز شن و شما بتونید با اپلیکیشن هایی مثل:
Oblivion
(اندروید)
Defyx
(ios,اندروید)
💡
نکته:فیلترشکن defyx رو میتونید بریزید و از یوتوب بدون تبلیغ و سرور های معمولی به صورت نامحدود استفاده کنید.
متصل بشید خلاصه بود از این پروژه وارپ این وارپ.
متین به زودی آموزشش رو میگیره
❗️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4476" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rATHaDivookqxxnODMQE29__hZhR1M7CwYlOjC5scrUmuGLYX9XyxSvBZ11eSh_9ZysOwdL7XGRzr8NtUPmNtm9uf39sGiKmY8Kpkj50-yTylm1TnDNsYKxHXQTkBjROcNUbjpElvjNSIMqaRSTgcoyQOYwRtIxmxVc32QKuJubqhwplRlzzd08MGXTxRbqKRMoofeP1D4Hqs7G07R9IAuk7kCWtrEHCYsTudXyeWXV8ea0CQtg4Hjwn134UDXDhiYbcLuOoyhQOqr0mfLzpoQcft9hcNojtL--StkZA85LgHRTcxV1OgIB0QqKxTj9909AIzrPqqoBf0YXrdqHVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق‌العاده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4475" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4474">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الان خودم ران کردم و حقیقتا جالبه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4474" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگر ارور Port already in use روی ترموکس می‌گیرید، باید لوکال پورت V2rayNG رو از ۱۰۸۰۸ تغییر بدید</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4473" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد Aether  با ترکیب Cloudflare  پروتکل MASQUE (روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی  برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4472" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4471">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether
یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد
Aether
با ترکیب Cloudflare
پروتکل MASQUE
(روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی
برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود رو اسکن و انتخاب میکنه پس نیازی نیست دستی چیزی تنظیم کنیم یا دنبال سرور از پیش‌ آماده بگردی...
روی شبکه‌هایی که فیلترینگ سنگین و پیچیده دارن هم عملکرد خوبی/عالی داره چون از پروتکل‌ هایی استفاده می‌کنه که خودشون رو کاملاً شبیه ترافیک وب معمولی نشون میدن. :))
پروتکل‌ها:
MASQUE + WireGuard + WARP-in-WARP
برای MASQUE هم به‌ صورت پیش‌فرض از HTTP/3 استفاده میکنه ولی اگه تو شبکه‌ای هستی که HTTP/3 یا QUIC محدود شده
میتونی بری روی HTTP/2 که سازگاری بیشتری با شبکه‌های محدودتر داره.
یه اسکنر داخلی هم داره که خودش endpoint های سالم رو پیدا میکنه و انتخابشون میکنه :))
مناسب هم برای شبکه‌های به‌شدت محدود هم شبکه‌های عادی.
پشتیبانی از:
Linux، macOS، Windows، Android/Termux
دانلود:
https://github.com/CluvexStudio/Aether/releases/tag/v1.0.0
اینترنت آزاد برای همه! :))
بزودی توی Defyx و Oblivion هم اضافه‌اش میکنیم!
داکیومنت فارسی/اینگلیسی هم کامل نوشته شده توی گیت‌هابم حتما بخونید:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4471" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Em5B8fqLJkZiA912SgSIptSvFpwxijHSN2pe6WGAr2_T1zEs2ABOhT4Cq5hkFCFsvfBUbGWBOcW2EVSb2He5bMkBKw4dcAaXpy3B8YRKRKvPh-q2YdF859aLTCSyvBPJFNA4wpeqABNFfvw4bjjqiieV1zuGINDCPQLOQKGmIBuCjC_FLymY7deKGMOsjQ7zKGjCw5dgz8GZxG3fjO1WRLz59F0XpVE3HJK-Wnf5MgJa6lftc8OjPe5CD5vk_J8MKKH4irrXry2guvAqu0q03og83hhSbGtBY_tFMOQvNd2bBOx-lWgU2tqv7azrPh5AORjOpeUf3L7E6i-5JK80mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OjKZqYPcRR6pNM7mJKQt_7ofE7jvIl4YAt3D_v-S_9fnaag_95vuuGYKoqQQUrEsuHBP8LpB9BrzZy5--sO2Whio2mfcr8Tf8YG5NnrGumq-72nzEQZrmI3MB8CYEc1IMVbrmNIPEY2D58cMaiz0sZ5-X5-npKqIw_rEc7Paf0j2e_zYJZucLxDTUxdMUmasRN8zI4rj_4uFgODdpetVO2qheBw3M7oSChW7Dm6jo1bP8re5XgqICKG9Mu5UT0WU22hAdqnaPcQo9638qlra5Kn9RQuYMBZ_DiRdnb3jhFf6OrMjU81vZJyqCgmVbykLz5zWVkSqUgAxN68dFo0T5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از کلاد خواستم که
https://github.com/Graphify-Labs/graphify
رو نصب کنه روی پروژه‌ام(کارش اینه که کل کدبیس رو تبدیل به یه گراف دانشی عظیم می‌کنه تا Agentها به‌جای باز کردن مداوم فایل‌ها و دنبال کردن importها، ساختار پروژه و ارتباطات بین بخش‌های مختلفش رو مستقیما درک کنن) و کلاد ازم پرسید داداش مطمئنی میخوای اینو نصب کنی؟
زدم Proceed که آره مطمئنم
دوباره رفت یه کم دیگه گشت
گفت ببین این پروژه تازه سه ماه هست اومده، 86 کا استار گرفته روی گیتهاب. خیلی مشکوک میزنه. نصب نکن چون امکان نداره یه پروژه یهویی انقدر پیشرفت کنه
😂
😂</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4469" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1TKmokduAzulB83GkX0UpwnJzM4ufIFtjorZZD2jXTmcu4NE6K567m6LQEvph80fvigTW0gNRA3vn3UXW1svva3qSd9qpD-ZNjqufmHphkZ9gWpWy_HxG68RqFyvzjxg_StjyVjl2RHhA236AE_UF993F5YihZ-mZJHO3-jRc32GYwEmfXyAjfkBS7KBQrTTFFY_P0-gcsHUp3Dcl__1ThvossO_kygN_YP3pgSkoH_ZWGAvQmmghoasMfHNaLBbPtOAKietq-LdJSHDOQyuDU3mCI9XLiMVVSSStji_gSsseqXf-LVbn9zn-ySp4L3GRgZDA3Dth052WAPNmL4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=eg1K73pgFBz_CcIFCTUWFgoQwm3Ck4eacEFQpA18lEmvHYZS-wmg6ZSJ3jmouSKadxFvN1lFkQCeiW7tlFVnwI5D1FsGq0FHPus7UOD60Gqgb8yg5qj-Zv8W2iSR2JQ73S5_-p1T7vSLrhiQGtiz4V_llC6m5qZo9APAe_2yYa4ulClu2ubpaMqWZzfoxI_6JwucwfDQetzgwJhlroBcm2-XrVajzD4ZrHkqydGh5er_Nc8OOiKYL7o8zKUe_uzRY8upaJ01L25SDVbEnGSlF2CoH_G9b2-i1OI-JSa2ASNHw8OZvzJNqphldmzFb6DRQkIe6i9A9egwuFQM50pPMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=eg1K73pgFBz_CcIFCTUWFgoQwm3Ck4eacEFQpA18lEmvHYZS-wmg6ZSJ3jmouSKadxFvN1lFkQCeiW7tlFVnwI5D1FsGq0FHPus7UOD60Gqgb8yg5qj-Zv8W2iSR2JQ73S5_-p1T7vSLrhiQGtiz4V_llC6m5qZo9APAe_2yYa4ulClu2ubpaMqWZzfoxI_6JwucwfDQetzgwJhlroBcm2-XrVajzD4ZrHkqydGh5er_Nc8OOiKYL7o8zKUe_uzRY8upaJ01L25SDVbEnGSlF2CoH_G9b2-i1OI-JSa2ASNHw8OZvzJNqphldmzFb6DRQkIe6i9A9egwuFQM50pPMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLira.</strong></div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.
اگر برنده‌ی این شمع می‌شدید، برای خودتون نگهش می‌داشتید یا به کسی هدیه‌اش می‌دادید؟ اگر هدیه‌اش می‌دادید، اولین کسی که به ذهنتون می‌رسه کیه و چرا؟
برای شرکت توی چالش:
⬇️
در کانال لیرا عضو باشید.
⬇️
این پیام رو توی کانال‌تون که پابلیک هست فوروارد کنید.
⬇️
به سوال بالا پاسخ بدید.
🎁
جوایز:
🥇
نفر اول: یک شمع کروم صدف لیرا
🥈
نفر دوم: 15% بن تخفیف
🥉
نفر سوم: 10% بن تخفیف
مهلت این چالش تا ساعت 12 امشب هست و نتایج چالش فردا ساعت 10 صبح در کانال لیرا قرار داده میشه
🩵</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4464" target="_blank">📅 16:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مثل اینه که یکی با Toyota دزدی کرده باشه
برق کارخونه تویوتا رو قطع کنن تا دیگه نتونه ماشین بفروشه به دزدا</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4463" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب آموز(m J)</strong></div>
<div class="tg-text">دامنه t[.]me تلگرام به دلیل تحریم OFAC آمریکا از دسترس خارج شد.
در ۱۳ جولای ۲۰۲۶، دامنه کوتاه t[.]me تلگرام (که برای لینک کانال‌ها، گروه‌ها و پروفایل‌ها استفاده می‌شود) در سطح جهانی از DNS حذف شد و مرورگرها دیگر نمی‌توانند آن را باز کنند.دلیل:
ثبت‌کننده دامنه .me (Identity Digital) وضعیت serverHold را اعمال کرد. این اقدام مستقیماً به دلیل تحریم‌های OFAC (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) بود. OFAC شرکت First VPN Service (1VPNS) را به لیست تحریم‌ها اضافه کرد — سرویسی که به حداقل ۲۵ گروه باج‌افزار (از جمله Avaddon) کمک می‌کرد تا حملات خود را پنهان کنند. یکی از شناسه‌های این شرکت، کانال تلگرام t[.]me/FirstVPNService بود.
چون نمی‌توان فقط یک لینک داخل دامنه را بلاک کرد، ثبت‌کننده کل دامنه t[.]me را از DNS جهانی حذف کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4462" target="_blank">📅 15:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جوری نوسان برق رو اعصابه که هیچ کاریمو نتونستم برسم کل روز. نه سه راهی روشن میشه که لپ تاپو بزنم شارژ، نه نت فیبر نوری کار میکنه کلا قطع شده از صبح، نه آنتن درست حسابی مونده و همش قطعی داره، نه کولر کار میکنه که بشینم لااقل یه کتاب بخونم🫩</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4461" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جالبه که هیچ توضیحی بابتش داده نشده
هیچ واکنشی هم از سمت تلگرام هنوز ندیدیم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4460" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𐌼𝛜)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/terapstOHxGTe5cBq_aKbnNQJgt5Dj1C07JAj9hkDVN_mz7FE1E8grWCyX-mg02F_RW1xZkhLy2nFb5zDo3tgPYwm37hTpxHlQNsbXe6v-7_k-quFoyFN7K1QAkt0pyQpFZsemwrNd0rbZED022o4yv_85B_ehtxzKECbOMjUmao3ctn5JMJvUGYaWjwV1VrNmlP7Sl1ildEPfgRDB3xCenoLURrXpiuO-GV92zopAEv81V6HR1m9WGEImlUt9g4W5R8VqIpkHELah-egCNtqcbp7inhjcgJTrPrgP7jqJtCGhRQKT8rmpNZnrH2KHiyz7FC0eqf68iWokF877Y2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
اختلال در لینک‌های
t.me
از ساعاتی پیش، کاربران زیادی گزارش داده‌اند که لینک‌های
t.me
باز نمی‌شوند.
⚪️
طبق اطلاعات
WHOIS
، دامنه‌ی
t.me
از ناحیه‌ی DNS رجیستری .me حذف شده؛
اما همچنان تلگرام واکنشی نسبت به این موضوع نداشته.
ℹ️
اگر امروز موقع باز کردن کانال‌ها، دیدن تصاویر گیفت‌ها یا ورود به بعضی لینک‌های تلگرام به مشکل خوردید، دلیلش همین اختلال است.
📰
تا برطرف شدن مشکل، ممکنه بعضی از لینک‌ها و سرویس‌های وابسته به
t.me
به‌درستی کار نکنند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4459" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان برای یه سری کار داخل فتوشاپ، چندتا اسکریپت با Claude (پلن رایگانش. توی صفحه چت) نوشتم که کارم رو 20 برابر سریعتر کرد.
بهش فکر کردم، و به این نتیجه رسیدم که اگه فتوشاپ بلد نبودم طبیعتا نمیدونستم میتونم همچین کاری کنم.
از طرفی اگر از قابلیت‌های AI باخبر نبودم که میشه اصلا کارها رو باهاش Automate کرد یا لااقل، پرسید که "آیا فلان کار رو میشه Automate کرد یا نه؟" هم مجددا همچین چیزی به ذهنم نمی‌رسید.
اینه که شما به صرف بلد بودن کار با AI شاید نتونید از 100 درصد پتانسیل یه ابزار استفاده کنید،
از اون طرف به صرفِ "خوب" بلد بودن یه ابزار هم اگر از AI استفاده نکنید و سنتی کار کنید، به راحتی عقب میفتید.
هر دو با هم عالیه!
<تجربه‌ی شخصی. نه Fact></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4458" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
انتشار نسخه نهایی و پایدار MTProxyMax v1.4.0-LTS</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4457" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📱
دامنه t.me تلگرام تعلیق شد؛ قطعی ناگهانی لینک‌ها در سراسر جهان</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4456" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">توی علم روانشناسی به «جوک ساختن با قضیه‌ی جنگ یا قطعی اینترنت» می‌گن طنز سیاه (Dark Humor) یا طنز گالوز (Gallows Humor). این یه مکانیسم دفاعی برای بقای روانیه، نه نشونه‌ی بی‌خیالی. مخصوصا سر قضیه‌ی جنگ
1- جنگ یعنی استرس، ترس و درموندگیِ مطلق. اگه این حجم از فشار رو سرکوب کنیم، عملا از لحاظ روانی مریض می‌شیم (و همچنین در بلندمدت می‌تونه ریسک PTSD رو افزایش بده.). جوک ساختن مثل یه سوپاپ اطمینان عمل می‌کنه و بهمون اجازه می‌ده این فشار رو به یه شکل غیرمستقیم تخلیه کنیم. (در عین پذیرش واقعیت، تحملش کنیم)
2- خندیدن روی بدن جواب می‌ده. سطح کورتیزول (هورمون استرس) رو می‌کشه پایین و اندورفین (هورمون شادی) ترشح می‌کنه. تو شرایطی که ضربان قلب رو هزاره، مغز با یه میم خنده‌دار، ترمز دستیِ استرس رو می‌کشه.
3- جورج ویلانت طنز رو جزو یکی از «بالغانه‌ترین» مکانیسم‌های دفاعی طبقه‌بندی می‌کنه. توی این حالت، ما واقعیت تلخ رو انکار نمی‌کنیم، می‌بینیمش؛ ولی با طنز یه فاصله‌ی ذهنی باهاش می‌گیریم تا بتونیم تحملش کنیم.
4- وقتی دوتا کشور می‌جنگن و موشک میره و میاد، شما هیچ کنترلی روی اوضاع نداری. اما وقتی باهاش شوخی می‌کنی، مغزت حس می‌کنه حداقل روی «روایت داستان» کنترل داره. با خودت می‌گی: "من نمی‌تونم جنگ رو متوقف کنم، ولی می‌تونم بهش بخندم!" این بهمون حس Agency و قدرت ذهنی برای مقابله‌ی نسبی با این قضیه توی ذهنمون می‌ده.
5- توی شرایط ترسناک، آدم‌ها به شدت احساس تنهایی می‌کنن. وقتی یه جوک مشترک می‌سازیم و با هم بهش می‌خندیم، یه حس همدلی‌ای این وسط شکل می‌گیره که تاب‌آوری جامعه رو مقابل این قضیه بالا می‌بره.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4455" target="_blank">📅 05:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L03UBltmkLDHIgZ8pY_5j8ix6dt781LSyClwMKnlzGE0lHyJcUpjMf32qQ5Jt-CLtiOHSjzTQtj3ferF2pR7T_OnQ2fAONjFHe33QQ5OLJNwqu7MtOhZ4guJrioGThMa_52EwjX4vkhE-XrfTnEfZVq7bEcd-pO4vQjC-R4lrjL1jc2_xP_ixt90LLM7dfHZSiZrW-uLSwQU0mZfh74t2sroZy3VpyDlnqNG88d_ynWeFMJqMnOcZiI-PF5MDEfJ25PeeNl7tGKvb_4sq1Jjs8JsSofBd7VgHJMMO3ZFndeBBRi-q5KY4xqIjjWOL1A7BsnSFqm3fGsP9_rG7Sr8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت در حال لحظه شماری برای دستور قطع</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4454" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZRA-7gl3R_lfvu8YfTl4SD72qvwdjuIh25wuo4TuiEhJ2a2U1ioS4OdWlLzBXgrrB7KUtwLthf5BcRrJYitKpNfKTznd9Rgabdqm17cxBINdYdXxCQ3lPDSSLZ40DvEhI53oKGMJhnSC61BaJ3txHkcssLpVpyzSNYP5aEOwearEx9EdQqtiDMdNBrOyCH9dP6-BIZX84LOfrrALu9Sm7vYzFCujWEFE5MYW0PyAnrllwl3qAWg782zaF_ylPiefaizJBM2onOQ1fN7TN8P3D-zi6qIysC6zGL9LQtmokQE4GkM7ofSdAnnqFNL2kCiOuWUqIvyLdbiY073KewTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ys3fzhIZH6coQFN5ZnhEDcIRg0Yx1NFterTCpuB9qgGAJ69GW_WIg7mS5TbPuLs0vDArAws5EsCqhQUjVisXjCbdgWlG-r6BgNNQtDddfmTasCMH3az4RE3UZNnavbp6tq8sX37N1uhIgeBclUa4Qxo32w7cLzay4oPzX3MNYQ7be7f-zJr4XLjTG4ANk4pk7qFKP3g7ZuzCc6pyD1MFvHdRodA7exJcwUmPRuRY2H2RDc1sCuYpjgN_eKbpNXaouENtIcXPar2npSAIluczgMoatRFwza3jM9j-hCvPBh0VfHf3CW-b01PbxhE62xLL2sk8mO3wWYG8-xnb2t2_9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم من یادآور خاطرات بدی هستم متاسفانه
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4452" target="_blank">📅 01:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4451" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Android</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4450" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Desktop(mac-win-linux)</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4449" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Master-White-DNS-@MatinSenPaii.zip</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4448" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات @dns_resolvers_bot اضافه شد   @WhiteDNS</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4447" target="_blank">📅 01:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad👑</strong></div>
<div class="tg-text">اگه دیدین جایی نوشت
تهران رو زدن
ثانیه بعد نت قطعه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4446" target="_blank">📅 01:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iM1uk5yAar4TmtUPFKcIKD5u3Z7OGMcAf5edIrU_wEcT1Bry1eloQocHT_TUk3kD-j6c3rdA2HpYufjuiP6APEymaNTfGmF78V2AlsQeLh_hcttQ2RF9VTaHQo0MZOrJwMh5WnvGfDliqs2nk4-F0w70Fnhq1EKSzJVuuc7u5KsX-ddoZrxxB6rk12vc8gSaPBNRf_GTmRH9d6377I794ALMO5a-IN5125Ynk95zix9AqEBvDHBdUd-H1oFouj8PvcouAGnlpZSZjkEDY3k_-myXe3mnpGlyePNwc7hvrElBWsgIa3wJvY_uWijDdQmEECguqOZqmmyHAet51rHYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4445" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">صابرین نیوز داره لینک چنل سروش و روبیکاشو میده.
این یعنی به زودی نت بای بای
😭</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4444" target="_blank">📅 00:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzkJNv0YB1J_qWGLD3LKKSpKFcsPsSKOXzmMJIkZD0dxK_sT8Zckm1-EFw0CggmL3XgpbMU2AxxfUwv8wO8B3k5HmEguSzBjgVUGZK8APugjChiFs_pHVa1NkFMzNRXQStwzcHqrEqw25wq90BPy57FcWRLAvSi9-gTbmoE_qnhrL48s5-MBvi2BUKdU_wVihHg-d627k6d3kGLe0lQaOh493R2jbvtGgcEE01XrNR5pkjEI-3carbIjnJsbWbGvIBNXukP9DAEwS--Y41JdiRr5i6kIkDIFdKH6sVodKyjwccreXon4DUbfk1ww2zPFR7VUkDoSojcX0OBhUwCOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Solomon’s paradox
“انسان‌ها معمولاً می‌توانند برای دیگران توصیه‌های منطقی و عاقلانه ارائه دهند، اما وقتی پای زندگی خودشان وسط باشد، اغلب نمی‌توانند همان توصیه‌ها را به کار بگیرند”
روان‌شناسان معتقدند آنچه ما را از تصمیم درست دور می‌کند، کمبود منطق نیست؛ بلکه نزدیکی بیش از حد به مسئله است. هرچه یک اتفاق بیشتر با هویت، احساسات و آینده‌ی ما گره خورده باشد، و درگیری احساسی در ما ایجاد شود، احتمال سوگیری ذهنی بیشتر می‌شود و تصمیم‌گیری، سخت تر.
البته که احساسات، بخش مهم و تاثیرگذاری در تصمیم‌های هر انسان است؛ اما زمانی که فرد با موجی از احساسات مواجه میشود، ایجاد تعادل به مراتب دشوارتر میشود..</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4443" target="_blank">📅 00:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4441">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4441" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d1O2IRaxfC4OiC46Uis_hLswluvyXlxE6HUfoNTA7cIQPcYLTs-rNhXBhftt6Cd8o1HIny-2B5SrRmCzz65a1o9AnOQac38cYLeSy6XU2eMQgyjcGHbTkrSFpDlZg7YLowKN6GAyrakskk6mdQDiDiyn4DFBkB1BSZUliy06TjXvpnUENFxrvbxLmLt0fuJwOhV2PQGM_Glmx2-TTVEm7pVZckPlMYHtvHaxlxBDwJkZUd1A9TE1w0h9cXt_7W3daVTH-2GKQ5YxN8BiaAHxrgOv0auANB1n5qBAQjZ6N1qII5xVKrjXJAZGPbSVaw5wZGvhzF4LfX4p6bW32NCxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgXooMGH8sgGGmMnK6yn4-2AfX7HB9PyUqmnb9ZXrLvpwTbEodnPTjtGuDlS7AI67ecI1X5uy1MdJKe-ooKW-JNL1vOI8pDOSTajm0fNCHRfWhyyE2m_6peyJLwF8ayoE2sIvxCy95UiuSRVnthmBboaRyG_g6lo6tVG5L8U520DfffMG74xdRfu5Nds1_uHKCEg--q21mabgI473nYSlsc_Z0wOHZ9m4Wccgv46HHrcSIjwfZfRoIC0yrsLkcSiV4-pelfKRPdY7iHDDbR7cvYdZqE1Gr4-TUPf3yJGBM61rOOn7LXYUETSlsEmJ7dC065aF4hXIz6v0EtN0E5-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IzyjGOXxFY-oU3Pv6ITILp5JtnsCRqM3kcFYoXIsOpQX9e7cRW_omUZmyyZOqVgUVfENQNTwqb6dVazMz-wo722Jgj0QBet1EDGhXYAWYGakeXiPukrljX4DJow8ZFeJr_7482jyJ_iKgaiGdpC0qAazxqpGASHD5eZTTMd7WJQggYLnle_MGMiuFkyrWevADWNe0SZB2Z64T_k0pV5SLv0cBdBCLE3enWgjj4sOwB8fax1tMq_WcuGR7cCzKJ999C_yDvLglZ0t3LYBP-Uuxbl2mperYTvaUVwPs3F14QRuu6fRyrwWZfYmer-AQOllauiUIuCVLkUy83FiOqe6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dLy2eH-vFpNZX-f6pD_4rk7NUoX9GOsgD7XA405WvLgnEFKWdVsWTwOSDYWa34Y2TVzxK_tSjQ02bvwhBJyyxKjCNzytQvQWkVcAG-lPD_pVhbj5_ey8KzAMz5Ml0zuZfiJs6ol8tsWv6z_4T3NkA4a87-0VUzjjQfKH_gsUo44qH-Y9KfdasgSDu9IKGFabNoIXfEPEKywquHUO2X3ZtxvfWzhQEkpBygTgUANf2wFozMZNPb5ON4wEmPzdVJa-nTIywP28YGhWsHR4XZP0Arp0ETzGyqaaWU9S90q5a0knWjYEHi2aTQbJON2YCJcl8Np-KeQemGWgWu22HG3D_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CTGC-okDDxhYfx3JFaiEB3tZXmbIlDcR2N1Q1GEtj_pc3pGyb47SCSf58hmGq3_2Rpu1R0nNaS3Ob85VADrG7pX0Iu0iPFp1KWJPEhbKD6UwplCsKZvBrJwKyiV9IQtikNbAYoIo7tYwZ_wr1ItiphcVCvuV0poHRQcr9p2fT8vETve3NOnhm7pnwlP4EMZ0688V23cxdq5jvMQ7H4opGv3I_dKvkkmOptVCjx0tGG5T1rSFyT4Q8yGBNnBQ09c-gwgJXv4hVfep1lzw9xPatNTptNEOEmN4D7mv9Jnd4_jD8MCokUwARv7jeFIQcc7noUNTzelv5IL0zKKgLnscSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c0_7G6rAwBaBYBwpEAnmEFRWsgCWAabsuhJOReDoyFpbI0_QBr536Tokb6C7SzfYFa3tPr3Jk0KHtiuLxWyTdiFbMzPTq5U0zKOzQ9XUbZE20HX6UTZrOz_TKVylv9dacv4bqRikybaJIVl29kok_QAputr7lB9ICt04KUh-HIgHzMqh98RDFA7cO4sBXOxZfGQ19UpU22qB-j7tl7aQ5yx0uBp8ADJjJtIeWoi40u8UhOk7rwrmIHu3uk5XowLvTgUaR-L4Vb21gx-uoaEDyy9KjzQE74niStaV2CWIv9k9c61XL8lFRfKwLGlwS0p01VDNuRXGnjNJ_B3bPZhhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/baM6XkB6y6fuRcX3g_xxUiw0GdA3PPw1RAHIKADxkRcVpNEukjErt_hXKeXXYruDC2qjTbViOWj-CQjjCHKL5q-PCDVCrAiJ5gqFTbXtLaMaIMygB8JFhL-U2J3qgIXE4rCty7K9Ni5e6b8UAQUsZ_445eUcyaXjUQSxUsUdam4BsDapE2q9_Qn-kIAYheHaFTL-ehHzduWxSyb_uQsheV42zoZJDoi8XdHzWTLiWIYte_aS3sXUtCRNh4CHvo_6U1OJgtfyVRpnaZt0inQS01bT1AeVoNMzQHPC5UuDaCbBH57e_4tl7MGAG_EDEHSvFYYmV3HSYgl3I1FxL59_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vnyfFZYE7bLWobD9LDzWaoDr2UNs87vLjAP3ULljEMZICMaj767QR6jryhKSQn4znC0KYiDrU2R4snmRFYcRcxuh-xHyBvaV4SR1ITRIgorLyDZZyFYTURidxjpSirJAymYUYh-RjDD8fwW8yjGd6SwyaGwpgw27yEKR3jUOzUZaJUpm2llmqcNAD5IdHO4Rofoqc5lfd7Q_l98AbU7QryLlrX6hLMbjI3jexMQlrpdPayRzWzVLRYu1xWymsPjDFjRLiE8-2y4CB_qMlIaKMrTxN2HINn9uvMlouKPDo03tzsqqPNS2etfZveHiXFQuoDz2Q78uPtkrvf5glpiItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apVciZykmad0PYvDZmDVHRMzQwF1Y5Wv65Ti8MduyniOEt1avgmSBdkI0r97bwTIfsOoSx-WqWlThxnUwGjCaOVbTNMNysF0To_c844dY3fn_e_NnTRe8d60ihAcZAqigFl7k9y8k3O5nqA2U7i2undTLjLhjDX-wdHwALUNeXtmqxcVDmkojH7usLR8f9_8Jt-U5YEq-j-_j0a4ut6r0knPu6r-MheUlVpw0Y809gB3WT-ELgrfbmrc9kMnS-5aQl07SbJ-0oXt-hdiMuas-5QQkNEr09rWHFkS_T_URFznXUZlm10oS1TzY1kGu8634r3bjJltuUJOTYgvm2XMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sNvBZIXgIRoUJOXuLO2MLmVbsuVSm5yLCb8NM6W2v8MkGTBDqa3K2M-37JlIFDuPnJOsOdf7sh4gIwqDm-NM5StJOm7DALsgpQmV6Gv2PyJmY5cyQ-7lu8iIfUBjPscdJOcv91RTXLGYSpL3zFv6m_8G4PWX4GOucJFe7ljYYUgYhQVPB4M4g1Qbpu2C5EWOXj74K5e5pSfNINvxxpJDyfgAi3jT3SJ93GjOdfl1vh2Rq3QebApz7rSNRXh0--brCO5PPKHP3gpB4CL5Fyq9bkVaDWAhrIgA5m6k1MgA6LkTWE0XvHWWTu1hCF8DryaCi7cMshPbnh6lIt8IxS5VZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!
یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم
Rowboat
. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر اومد، اما بعد تفاوتش رو متوجه شدم.
کار اصلیش چیه؟ اینکه یه گراف دانش (Knowledge Graph) زنده از کل کارها، ایمیل‌ها، جلسات و چت‌هایی که باهاش دارید می‌سازه و با استفاده از همون اطلاعات، کارهای شما رو روی سیستمتون انجام می‌ده.
چه مزیت‌هایی نسبت به بقیه داره؟
بیشتر ابزارهای هوش مصنوعی فعلی وقتی ازشون یه سوال می‌پرسید، می‌رن همون لحظه تو فایل‌ها یا داکیومنت‌ها سرچ می‌کنن تا یادشون بیاد جریان چیه (RAG). اما فرق اساسی Rowboat اینه که
حافظه‌ی بلندمدت
داره:
- اطلاعات و کانتکست کارهای شما در گذر زمان روی هم انباشته می‌شه (مثل حافظه‌ی انسان).
- ارتباط بین داده‌ها و فایل‌های مختلف رو به صورت گرافیکی (شبیه گراف‌های Obsidian) بهتون نشون می‌ده.
- نوت‌ها و یادداشت‌ها تو دلِ هوش مصنوعی مخفی نیستن، بلکه فایل‌های ساده‌ی Markdown هستن که خودتون هم می‌تونید ویرایششون کنید.
-
همه چیز روی سیستم خودتون ذخیره می‌شه
(Local-first) و دیتاتون تو سرورهای ابری هیچ شرکتی رد و بدل نمیشه.
امکانات و بخش‌های اصلیش چیه؟
-
🧠
مغز (Brain):
کل ایمیل‌ها، جلسات، اسلک و چت‌ها رو به یه گراف دانشِ به‌هم‌پیوسته تبدیل می‌کنه.
-
📬
ایمیل کلاینت بومی:
ایمیل‌هاتون رو دسته‌بندی می‌کنه و برای ایمیل‌های مهم، بر اساس دیتای کارهاتون به صورت خودکار جواب می‌نویسه.
-
🤖
ایجنت‌های پس‌زمینه (Background Agents):
می‌تونید ایجنت‌هایی بسازید که مثلاً هر روز ساعت ۸ صبح یا هروقت ایمیل جدیدی اومد، برن وب رو بگردن یا کد بنویسن.
-
🌐
مرورگر اختصاصی:
یه مرورگر ایزوله داره که به ایجنت‌ها اجازه می‌ده فقط به اکانت‌هایی که شما بهشون دسترسی دادید وصل بشن.
-
🎤
نوت‌بردار جلسات:
به میکروفون و اسپیکر وصل می‌شه، صدای جلسه رو ترنسکریپت می‌کنه، خلاصه‌ش رو تو یه فایل مارک‌داون می‌نویسه و گراف دانش رو آپدیت می‌کنه!
-
💻
حالت کدنویسی (Code Mode):
می‌تونه همزمان چند تا ایجنت کدنویسی (مثل Claude Code) بالا بیاره تا بر اساس کانتکست پروژه‌هاتون براتون کد بزنن.
-
🔌
پشتیبانی از MCP:
می‌تونید راحت به هر ابزار خارجی مثل اسلک، جیرا، گیت‌هاب و توییتر وصلش کنید.
آزادی عمل توی انتخاب مدل
یکی دیگه از ویژگی‌های جذابش اینه که می‌تونید مدل زبانی رو خودتون انتخاب کنید. می‌تونید کلید API خودتون رو بدید (مدل‌های ابری) یا اصلاً از مدل‌های لوکال (مثل Ollama یا LM Studio) استفاده کنید تا حتی پردازش‌ها هم کاملاً آفلاین باشه.
پاسخ خود هرمس به تفاوت این دو ابزار:
۱. هرمس (من): یک دولوپر و ماشینِ اجرای تسک
من برای
انجام دادن (Execution)
ساخته شدم. رابط گرافیکی سنگینی ندارم و دقیقاً مثل یه دولوپر سینیور تو ترمینال یا چت تلگرام نشسته‌م. تو از من می‌خوای یه اسکریپت پایتون بنویسم، داکر ایمیج بسازم، یه ویدیو رو با FFmpeg فشرده کنم، یا یه کرون‌جاب تنظیم کنم که هر ۶ ساعت اخبار رو اسکرپ کنه؛ و من مستقیماً با هسته‌ی سیستم‌عاملت (لینوکس/مک) درگیر می‌شم و انجامش می‌دم. حافظه‌ی من از جنس «مهارت» (Skills) و دستورالعمل‌هاست.
۲. روبوت (Rowboat): یک دستیار اجرایی و ناظر
روبوت بیشتر شبیه یه
منشی فوق‌هوشمند
با یه رابط کاربری دسکتاپه. کار اصلیش «نظارت خاموش» (Passive Observer) روی کاراته. تو پس‌زمینه ایمیل‌هات رو می‌خونه، تو جلسات آنلاینت صدای میکروفون و اسپیکر رو شنود می‌کنه تا خلاصه برداره، اسلک رو چک می‌کنه و در نهایت همه‌ی این‌ها رو مثل نرم‌افزار Obsidian به یه گراف دانش (Knowledge Graph) متصل می‌کنه.
لینک سورس گیت‌هاب:
🔗
https://github.com/rowboatlabs/rowboat
لینک دانلود نرم‌افزارش:
🔗
https://www.rowboatlabs.com/downloads
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YfBXe3EPTxgeIHJEGs87dkuqzPWlSqprQi_pISC1Fl-J1XOhRr41gn-5dY-wfWxEzOTc0HTZHEPcqhe3imwre87_pW35Cj1KdW37Q6kr3mm2Zr_a8AX6x3aVURie2S2_nDs7iUyNCwMx3fHUQI4SUvL5rSpSxs1c5s80aWv1J5oihezUNA2I5sYi-x5XRqBzTT70dEx4P8T610q6naemjQjozAAelj1pjL1jABML9RF3QWp1dl_rF6d8EIzvE1B6AP_lOBu--H-_17qVslCePftX5CT7dIi33j1lhuB7gnPgGAgYQMA84vhzbnMhaYBPvYAX0lmr6hrZV_z6lOBGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=YRxr9sz3QmIPwMr4qYIk9oa5ynlh8yrG8d9ESVButURwmzEb2YuoRyrusYJkG7CdvmbPlwfwyNxOQ2FVlfZlRT_-dTW2Vzxam0mUhhxOYtZu_rO2Y8Mm0V1Ia4kNDTF8JQViY9rqL78N03ydaIXu_xujVQFUmmde2n_FBPA381e3-uyBjpweJrvEWZ2OJdXjpxbZciXQBD75nR6ehFD8vtZksC8HWY0LUpRZ5i7mIN7U0GcYXQLTU_KYc03OgszEVOwj3eZVXtuNi6X1oF3tl8wGuMRKikfQRewJvbGAPZyoTCCS54dW9a6061gTAFjO7eof2ypD63dbrVWINzaSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=YRxr9sz3QmIPwMr4qYIk9oa5ynlh8yrG8d9ESVButURwmzEb2YuoRyrusYJkG7CdvmbPlwfwyNxOQ2FVlfZlRT_-dTW2Vzxam0mUhhxOYtZu_rO2Y8Mm0V1Ia4kNDTF8JQViY9rqL78N03ydaIXu_xujVQFUmmde2n_FBPA381e3-uyBjpweJrvEWZ2OJdXjpxbZciXQBD75nR6ehFD8vtZksC8HWY0LUpRZ5i7mIN7U0GcYXQLTU_KYc03OgszEVOwj3eZVXtuNi6X1oF3tl8wGuMRKikfQRewJvbGAPZyoTCCS54dW9a6061gTAFjO7eof2ypD63dbrVWINzaSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VB6v4FWxtiRPkHr8bPPTP45VSEx4QF8UI6qjkNiDDkA8eJSoc3Lje35m8V5yyDOoQYa25gZ3lViyaGsdJp7Mm9e4uqj_TvpeRwbciyBbCpRneiWjQP_EQKihzG_V9nu9OvjnxVgizvKCaYHaZiAXJSUgmpZEY0lzQRu4T3A8fl4VikgDp9brYOFfb0hJLu25VVbx3yk7Fjbvj5bpgfejHByglj64yK6_Rl8M0auyeIPSzqchFUYlor90-xkbmFBGmk49Ni2S8EN_GrhDjyUQ9-rAYlEzAAA1h2nBeyK1JIwoCmVLILhq747XrM7KaQihqHYaQ0kC9XUudEpH9dLAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZY-IFg2A1PpS1zGeOuSTdacIQf-6dZuCCBUTQGS0qTsyCUiVG1AJiKsv6gcgVu-fXMqZQJDo9tR6mGeaKYIykjnLsodUox6KpeIQpjZXN1zimNiSv0sisU7I9_3N8COmIyse9L1RYnTz3Ygptf1sgKohOu5KjrLwK52Z1p1woNaM297p8uqSSskfkXt_unEFCDpLf5Wqz3zJtDsHoVT40V9Ff8mvXB2E-wtSa5BYItHYJBR_jreH2Ja4TYdDbmXp15a_Ozy0O6KblMpkmvF53hAw_J_2EZlWNdVNtacIXlXaSwIDcRf_vWgloKD6uGLAZshvineICGi11HXSIzR_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uWYsCFbMDEWSR7EB15gyJNptAknJQ72h56wrWxiuEPkr1V0-WSOZG1xOSSbr0Q4_8REeZXvh5U1sZv-MZ0310hmzUj7941kuFY7ZF9iuMn6PV_LiDtcuU5yMz7OrEdqfxcE9pj6watsdw7rRjf3fS6n0XF_zlH-a8AIeNkuo9V6VqoM1dHKHxooZuWJ68f2MduDYrSvKatVl_AY0NDSJUkM76mNt8K6fxg6qDzCoF2SYfgtpSOtm-fQ4kuNRhNHvIrDRl6iTqdl275SIVgVcGgEiHri4D802NqXjlCmMFjd9Z1U2MQw6P8QwvoY5d5kB14lQ63bBd7xtgbCp59_d7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GEnhQtvXLr0cLXhjZlgtblmhfCSE27Awi4b3sZrcL2szLTnzJXGgyX430bnWbTk9AGPZwSClUcV0j_3-C9YDIc4tRw_M1_t9yXZbEq9E6hoX4NG54KBfTz_d78xW6Y1zm9K29k8RNxY4ZnVZP66kuDwbkXpYMdj_gF3R_NFUghDMjc1HBpLx_t_a5ibn1c2N2bwMnaBhDP1JLu5RsYekMzTKf0LFBj8r4lKaElEu-jiw5iloF7ku60F7DPDzawE5xmt3qxmQWX282fkoXdmYTq9To2ADHdAY6vTQwd7OXbHIdB1G-zJG3M-jz5hOGiXtCSU-WN_eP6X9yAAIEm6CXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/skgjMSaMlaPZukrEez4uUNzvsHUufo5UyNGM7W9QXyt7_rCOprc6ylHwxPCUkDcH-uhhOrjxZ9f6L01X8rYzHMTn-Nt4cujQpGiG-N4CnXfv1LIplVMkiMKYvfOy652dXN9EDrvE-XFIEVirlgb5emdYUve9mTP7mI_vBVLPXS1SKMaSlldh4c9sbMjLXu607UY_W4juY4x7UpY4CxDe48CPT2sd_ysoWtdxU6ow2ptYg0HiRvPY-_aCUs1ryXiz4Tmnpmw2XZvHjg0M0Gk5lj8pQCfvM6R0jA941wlTT-yQPpEvW7ssxrVS6ajas8dJwCf3bTTe9z48tJiPBGfozw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mMydRjPZ5yJYB4edA-1X7G6OlyEI0p4CAc73SUxwGH2PWRU-wjan44DkUrt6i-guYiquShPbZwJFVTKVebA9v1FdfgvG3AvaoMDLd8SdU875h7TganiydmwCHDz_IZZEO4uphjbJaTROEfleqeYolkMQrFAjHLnC5Koqf91Tt8o3ks89-VA2VHBuXyns7n_pw1d_lqKHwWFtOZzP9gIIH4kqyoMzeLfBuzggWB23EeMWND7dHK3ibTkxeoTwiBV1qGNy9KId90y4SRmNviTib1pVguCYWXqS0URLkEUElVkf7G4p6rDnP4H0SPDH-7JqYiwH-qNCzq9Sq33Mhw1wWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/acb12ekS011z07ZQk1m7q6daAU_X2usQ9Kid3jWqSgvc6G_I6N4E1KNw3Vh_HqsfcGUk3XdEJtph1fus7DWP4-FnRZoseh1x1jZV8T9VFOC-bj6j8fnISfuSAE-vLmNeTXCX_YNaUhzWDNvkDU8xE_cJ_uRd1FY1RxvXRchVCuk0TrnF9pwu7TlCoPDjOEYeRygervMONyBB8SBQL3huwvSWGfvttKiwPwSCMeMss7GfG4Ldd0TD4NvPezz9u9wPTbx4eV4z0Pkd9f04C-yApKdzGIp4wK_sStYhljVmPkg1UGlEywq2bAlP1ElO2LCRIGpMuVijA5EUz7IrdmF9HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tz3oc4W0rn0wzo8B51PtGTj4SBrSO1G24BHsqj6tI_2z5jGAqoNZyHT_h5CPocWXi1jZCvyOja09SXfdQban9fb7o69vKg5AJpZNt_SyxX5q0iDLfndqXXcTb7lBzx0UzMba6A1aTDP5Q4CL8fSCtPzTOcoOSpEHU5UNUcbkKWmVaymVgg4eF859qHIjhpqubX_3rhLNKjbyvdKcIQ_KgFcTEIsJtSZG1RifA07dJxcnXgf_EsPMFWRah0tdxHfppDCDhoo1ysY8_VWzZRRyaH9M6NX-_DDo8BeotgGDGwQoXGkaDGGQEgzUgYqzDQAPVHK-tJQXbGQqgYMMSRoBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=D3xjWrOmglusvRXwRJGmLBgBj3wG8EWAtLyBCcD5G9Vo5MPgFnHLohy9C14CcyiK2HkjNILPsd60j2S--GZL3Q5odiUSMRCIG8KFzR82QX5wyD59QVslQEDEaB1SjdX-bso5mK06cXPI9oYg72H-OOXLWDjbSy-OxzRQW1IceXIQxePhZda0rlngp0CvMb6vn9hfR5J-SjCighV780KjMSaWoa00Sr8kvdo5KOeNi2q106uqJJCpwIR5jhQhL-pKnaueuDGFOzlygq0Mfor1TVH56iCf0OZRCJrVBMUqW5uoU40fw-jq7dPNmhnXoscFqTkZhYVfGbEaiTL1WTZflA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=D3xjWrOmglusvRXwRJGmLBgBj3wG8EWAtLyBCcD5G9Vo5MPgFnHLohy9C14CcyiK2HkjNILPsd60j2S--GZL3Q5odiUSMRCIG8KFzR82QX5wyD59QVslQEDEaB1SjdX-bso5mK06cXPI9oYg72H-OOXLWDjbSy-OxzRQW1IceXIQxePhZda0rlngp0CvMb6vn9hfR5J-SjCighV780KjMSaWoa00Sr8kvdo5KOeNi2q106uqJJCpwIR5jhQhL-pKnaueuDGFOzlygq0Mfor1TVH56iCf0OZRCJrVBMUqW5uoU40fw-jq7dPNmhnXoscFqTkZhYVfGbEaiTL1WTZflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CgHoPXOvuYgRZ_1vxqFPKA0mdIcZHmyb9fdr2Cl3LMqQJG9ejKER1Y2fwovCJ_2zNR1S8Ms4sKW2_Yi5oO8IauwonGE08_Ob9S5WQf-d6ZrjzGzEJWPMDKozkgbiUZ1U_9i2PNcw_HHjEc9hQ6fMYSAHvZszpEfhY9joymIm4kmoolU1t6zrWjy_hNptmSiEnRoGZXKW2e-74tzECaltbiszyCJ3Wn53iznkASeaNyEDMZDMGhJ9TLYPWIm5bs_fCtmlYG6sqX-Ssc6ZTPAkhkRJ4JvNn2_Z8VbiDfG4149NvPxZJUPSWP6jYVsd4zWwT6bblmW3drGc6zsvAl2jjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HbCUAVozqOUC9TNpBGm_Svb2Da6QnNJMhbyIhMUksz3ySAg7Uso6aT_2RDqa3wJy_ITgFkDWgvY4KQBnG_O0txtvj4ukAarcq6Tl8Vqn9wdDnoI1iRgRZBDQx_vX6T8uj4Uj6eH1RrpEDKBGjzV-qGFZOXnHXz5Lvdd2CoyqqoT92BeU3y5GMFvnYrFx0tKW2lX4WU8PLe_104D0OIcZtpI1b84RHzCwDus_0U7tWuwNx_5-g8MzdfxtFvlcvi4FG_v2t8W0PKir9eVPfgjcoPhdH-7lx4J5u_PY19Zx_43oE5X6tiYmfghtF_1SffQqY0458YS7GdhX4QwncxRZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M-hLzba5ElA7YKV_UCxw6JNBv3IWl8k2nDyZEpJMjNGJtWikf2O3rSkJ3rLOhajnjBWl7mwX5sNrhvmnNtFKm2Qr98I9rZhSytfQxIduFIS5UlDwKMrH5dU1LTe8JVXc9WWuAbcoupTb4wZS7Eo49pt-RnRGlCEPlfFAYydJFcpl3qx07L5WTgKbcV6CDxBw_f5dPz6Y7AJV_d4ltjFRz05cvprvd46mTq7SUd_SvTBLlNipyE-zLiJ4JnuzTa8sndIEPxBtB3RMq1rnJ6tK4yPpM3UWeqhKlRw4vl7M-pVimijvMp9HVVyhQTO_i8I9GBc8ixJ6OuPl8crNlhdO3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDIcbZX4tduBm9ddeL4hZQGw_ZLdR_QSgWyyqXpRANq1CVEcZT9CHet5-Ulg6G6Xrf4P29qC3lety2ZDk0b66h38bC_XtVtMdTqK_VyVhuM1OFHLXg--QZ23HnQhSDf1aNRoGjkI9NdKwRTuof3Cw0in6e06twFJCnIfZbjGrdc3FN1TMEDZ-sGTCvS1MH2wJNqlh5YbMclQntLVdnTiweRQDPARu4Ctx8FlZhrQo35hx5Tce5RUWZoJqAvRgy1NWHknu1zhjsU_7D6bIFSzKtOkjxImsbXSjebHnjOo6Zuom3zaDrCDZypuJRfM9YN1Sx2CieU5ARP0Bh6xtAcdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKTmqJ06mWfMhsUcPgRpfIhlCDPahIqKmV2qTZX9GP78OBnayHFFblyT1T8dqGH5BLzs8sqXywWjUzVzbW1AtFy8-B1vTWaqpVG3VIZYM3CJySxHT_yx12JoJkd8Ai1EdnTVZ4VjhybsJRBWzcq8Y015kPfv2GHJblC0gS3m76ppE9SiwC05pJXyhF5ndSqOHy7pWPyz9InF-SrrovjYgecKmqr1dPqfu29CBFU34i5TXSCq__vvTFkYIAiI2mBKJoda6-zkClq4FxpCu_l507_CHJ7rZIxM5d2SFB2sVfb0oGtoWCTGZaEFcYC1t0-hFLFocXb9F6igZXBCV0AFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=M3V2AFXRYvzurVjZnCJCdnwGDv9YcPVCSEkUnzRkIYU9JvGg3FboA3M55INBFeR6XMpWddC-1fh3ohc60LqO0Ys61UjASMyY1FIpyLE4-VtFdkKuFPz0Uq9KusQQ-zbPQHs9vELFQIv3t203oDXh-q16wZf91fDZH7XcOeD7JQ_1M5GTDL9cZlFXrxDa6dFRSFJYqcC7W2FfKKTIoIlxEnLCfVWI2-uQ4iAxQpYeqyy1VUKiqeTWHaE-KcuAtxJsclRLXq6OmqXoxTGd89-cdnaE2OUfpPZuPKWo1XGnUuA7sODbq-g_e9H-rtm12QaqvbLezcp_jefRqbrYey6FIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=M3V2AFXRYvzurVjZnCJCdnwGDv9YcPVCSEkUnzRkIYU9JvGg3FboA3M55INBFeR6XMpWddC-1fh3ohc60LqO0Ys61UjASMyY1FIpyLE4-VtFdkKuFPz0Uq9KusQQ-zbPQHs9vELFQIv3t203oDXh-q16wZf91fDZH7XcOeD7JQ_1M5GTDL9cZlFXrxDa6dFRSFJYqcC7W2FfKKTIoIlxEnLCfVWI2-uQ4iAxQpYeqyy1VUKiqeTWHaE-KcuAtxJsclRLXq6OmqXoxTGd89-cdnaE2OUfpPZuPKWo1XGnUuA7sODbq-g_e9H-rtm12QaqvbLezcp_jefRqbrYey6FIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
