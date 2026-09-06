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
<img src="https://cdn1.telesco.pe/file/Y9vZ1uRvNDiTIo_a3_SROBlDZAYJeKyKOXrHWp1C0hLwMJeJ8PBSv_7AhwVWy74Bg2rQDdxUNPYep2qyXaNvDTVRR8IL8_eBhsHNwZ15j5EkmZiWwX2uVtifBp0eTVHkzaewY1RxUIB-t5Y2HIDHu4QP4RyXpUhMBtMdxH2hCMAlHI-nvKMtap8PQYnHRjizSywkNOPMVLmFEWo-wbdLuR-E0zxoyQ9pXoHYaKILIBf8TCQucOjb3BwZ4JvpOVu_8uMbvFHQFMZycsRyYlh-bukDInNTpLYyddZQMFEf0SJDR93818pyMZDWwcj0dqRWiB0YzzJgHnN7sQ--1Gq2Jw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ex3PUSBhPyQz0T_8MQwvH9smV8SXfS7TyHyua7Jj8EfYggD-b2nu2CiX-5-UnfPPUnBrMZY8UCkD-JbxOT63InMar2B0A7WgDKTXxikVoCW0Xvanrxu7TnnCJYAP2jUHmcR1IwF8a96LVICj3fpOR7y0M29jx5XMuqcQGtGf1bScDGcGRSCH-k-VF34rAVNfJ1pLNh52jdeTTpE8npPDtFlJs4C5SAS_X8F-9s_evgbAbyuxehI_J2FoW2Ug7aEip0B-27nhKaUgLaSGZIq7IsI1jZZ2eOL48e3wgbw-L0snmk0jbsxCoW3OIEZZR9RewJ2Bed_L11kpC2JdrNAyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=suHWMiChv6RU672u8ZsWPYgUXhuYgaT08HVXx7-luBXuq66IyWMy_bglF4Pqu4-ich5We9h_Eoa3lij4ed9eP32IKs4qFi8r1QEahzSGAbvkDHtyikrdBUP6mQPNWAGzikjuWN6x9eqq9P2XMB-ioDfl9M1u6KgezycaxzYrlkIjK60n9mFJvD4DzFBJN7rAnphjhkwcHWGCfD3dZaZ6WHD8tZs1nZwuh86nV1zMA25mPFh26cc2IVIuYs5iW2o-bQkObBxSpJyWifXrW34RjT1bHdA4huVKeIoAgR-PQGpQNhnkfrIB9lj4U-uaEvtuPfY2w_cO1Gp4ykcU4E7N9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=suHWMiChv6RU672u8ZsWPYgUXhuYgaT08HVXx7-luBXuq66IyWMy_bglF4Pqu4-ich5We9h_Eoa3lij4ed9eP32IKs4qFi8r1QEahzSGAbvkDHtyikrdBUP6mQPNWAGzikjuWN6x9eqq9P2XMB-ioDfl9M1u6KgezycaxzYrlkIjK60n9mFJvD4DzFBJN7rAnphjhkwcHWGCfD3dZaZ6WHD8tZs1nZwuh86nV1zMA25mPFh26cc2IVIuYs5iW2o-bQkObBxSpJyWifXrW34RjT1bHdA4huVKeIoAgR-PQGpQNhnkfrIB9lj4U-uaEvtuPfY2w_cO1Gp4ykcU4E7N9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7TDTVgvVrBhpBxRA8YFbuODOrDNjCEU4KB-VUMw-_UVyGHOWohkqu4cYK0io1eQe1E1gub8GGrBZv1z-1UpVGWL57Te6TxxsqbSGIptlsEXj6GrjW2X9rjBLoy6kIfI4GPdONko2YHy3JwH4dVOetQ5ifEKLMggquyEPTUnm69SD4lL4pcoM73VeAg5rL0h0kGLV1qs6PuiYqlc-9Xv2nPeQC6Maj3NgB73vfeJHpF68y__7gM0SH1W4NyrDpgzQCsxC2a62gDh4NsY2hzpxKDAdKoeCO7Ro4qfKicE8HTVx2mtw3NJdAnQCwooFF708Rq3ghWfBp3v4NvcrEFe7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1lwUauonw5fvSrRF0uBN00dVNkWDwjD-o0QQva4NkYwKNcwZd0V92YBp3hKIabE6z0OMs4lwdLH6prACoTYN8heTzOfhHRWpIclzFEKdnie449XrxZ7KsMxnTlbrd9m8JUP2BD04uPakShq8GoKh3niI1vaiStPU3bRuAeNJ9lGNUrnTP3bRit_HkcJMTxk6HH9-2TU6aWAWC8ht5uZ067_a2SmLl0ogHDPMh6ap-_213-Yhmk09byY7LdillS_SZB707Jobo--g8T7mDGnTxMsK1l_RLveQR048vL1ieN-J4Qv3ewj19YlSH3C9XAihICdPqNiLaOotRvtEX3wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncdqz64P6O7ZHjIlfGh8FmtJCnwGtiYx8UdXofQlnSG6INCr8yP3Y4jSudzWk3uzJf8D-bzmBcbU4JFdE1jIh3lFTU4FVZNlQ_BfeTKQaFygNjNJVDAdV1FWt1pxlpeIwAH7LR7gOfYp8-RDuRO3GZy15YR_P4kUxqeGr9u0AY_vRDBLWPTu6yI7o8KEvLNkcbPTw8NKshH8s1V4fPUHJmp-gDOu72KH1bGQVuYJ5AOJO0YnXD8JKRTW11P_ePFU55beBkFYmaR1P-9Eoj9WBBoE--YWGyqklnabe5cDTzz8hIOrggcWuDUfaUoMgyaou2qCQOdfyVpXUOsp5LSmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4p4yQtad1WlAEPwWLEouGUDeAZ2gTbOJxqV7amUOWYqfrMv96StA9O-7nPJXv8YHJRQaIHfxXzN4eBH8TNefM4dFWan0yW5vmeoGRrqSYecTeaeLDaJXPLjRO9Th6LhQ3oRotuo6Pv2uZV731VUcU5DCP420-zJDqFuNSg7pBbRwKdE29PrBV-AO1G-YXV21GWr0ZaayOVo7T6bBzYSK9fTmFgLj0DHMVikaQH3AD8GBCJUx_IH0vAnRQyNezOU2QOGk4B3KjVO3ThFdub5VK0Xs746KHCAbxKx5LCvldlKvjJ0fJUnWAK8uvycDbo90jGcqNbq6HWDPZz4BzOp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDv2oIkn4B-nGKAx8yaMC-MTVIJIL1TM_-DPeUWH7M2oiDW_EVyEA_2B9TuYwwYdd-EUM9ncHr_8GH6DYiUshpxyQ1Kz1_8YKEzhM_qKwihgp7j7d3mKdy54Asqf7j0WyE9J0ygMtJ3dyVhLfDUXz0cidaRvqEQb3sCuSVSmFroia39AtAlKEyWvryu0POaYlysp0CVy0jg6RvZVMPQXaDCcm1_UpKuHzuOzlfJnOW3fCiLJdFGNR-r1j69AOgPOo7PeYmSVfKPQIUnwymq338ZZNauKiYfQEyXNG9U2DI5Ewd9Dmm0ctCm5ZRBcF5pQtnNDT9NKyZ9xys-DiymdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vT1317pXxIX_nXsjrF2JkEq7KK6wMJ5-1XP--b_IcFE8-Vthw17Ev0HoOycQGTRfMHiyOfV9H7AguNZ4Ygnhg2sk9i0uIDicSxinFcb5m9D7IcOAmIqefVk9f_QAOs2jOWWojud21wZekg9GH1clUFRBzuvIvXb9LW-WiuCagO9q0Fz2eY9SsK4i4w3r1A_C1cakNjsuayf272KHpbD90mfaZxXnvqWDE6_rSBvR-hsiYhfbeY7HJRsZYIk9rH-Yex5hBSR70OTgVCqfE1r3p078WPomOoez3IL-BthQXBHCzOgo4IvUIwvINEgD5Suz13lOLiGaU63FFlkEfiBFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rO6n-EZbz9PeDT9APMy_B5UEbU8jw1t1JC1sgTWIQ5lyk5REtxPAdZs4jICBdnYa1ztx-17rzlW5OJuvViQrAUFE7cTpVv0le7CtuNqPElKdKib7JnQIAmxi7cZX_-88I-u1pZkEKXvf-_yQCvFbHZwhqMwS8iSqYfAeNbMX4S3Y02_WrogEHlFZybY_M3XKbdEDF6113VrqMC-idnCzF8Csrd6AdZ7TumuQQ47thogeU7zTJN8JDeruYU70_JV3SwCVR4bzRT2bfb9F0dpqUzn6qYAwnKQA8tnbn1CImm_XDvumuZz3tGN3_eTWZYo91s5JdOhgF0nsQideoqEGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kez3rCbfhjLpSPvxg44c8gc1vqhbnTNu1uJ9yYmFT1-KdnmV4RjlZ5G9oRqe_qiUEt-k9IjkOrVL02sqHzWVw-YenUzKea5l6PoeMlpLdNEsEmTw_6FBzsWU5W0vA-6OXtNT8GIEk_pdFi5eA3RWxzF2CT8hXwS5RWc-4gz2heyb7E3e894WRpUltruL34L21L4fSw5jAKHUOiVb8k_Hq05NPDZbrqe1R2VsqMcW5vuf6xAHvODqUNGRdTXLltbBrBOLU2AYMCvg8_aoZN3XnXbaqJxoak_JHwFvWWO2Ok8t3QPN5EZIxuFcf8PTGofrks02ytqeMdIPQJ2COwnteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZFXPkqpfKIxnSBy013fybGmNIhKS18cnWrJcDlUTVQJBEXP5RjabgmmXDSec4Bt3HgAl3TpCwh-azUU2VWK8esLGuINg-XytWpuMx8kJpKMhmc4z045VWOOopRhBSpgjtCV6hLcTdDp1SKJVZvv3SCkhNC4PBb8Xa9LeD7kaBv879JiWz1tgOIJ6ndURduik6Z-iwRuf9aJKIughlnUwajAAHJ2VEEjuybTVKhoT4sy4HbfPw3nl1UstVunXM_KN7nkBldlzgfLXK5dJXxy3PiznwIe8-5ZRFBs6mktp2EfYQPHakWNnLVmvy0N7VXSbfO1lhbQTwnmG6hyw1jngag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HSwvko2dPolM6MSPRzQhM-jEsR8XC_s0gc__GZkKKwb9GI2VWV9LC1RWsEH_ORd5fjvFo5h7rHZ8FFvO-DEFwzQqdWV8--VpwND0HuVgVZGECl-kC0AAPFmMr-KcTYNb9M03qi9D7nERY1XvV4izWJobmU4ND5o-EKRjRdWq2aSPfGQFxje-M2ORco5jrYZnfwQ2xgfdQTTXGJrjftd6NsIGyzEBgKtsyLgX2kF9wczNUpI1-NlggsfVwmt2QkQIJRwDRn3mg77q-l8eE3NpwrxXvkIn2G2i0YYw1Phyvcx-ZqQms8LI5aMIyrRqeyMcZaLikAfkTHivBCXN5Ow5jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTx_6zTnp0jChojLXX1vgliBKl09R2nbyB0ocQtiCEiBZHs6nHlfcsfd45tAJdNZZQXdEC4mMyVBP_s3tckyXagZBX3wGtHPtDE_2uwhaQmNocnkAcXAck1HIztVzPNQkTitQ0wy5noWZFQjaPCknbDBRZTePsax8GEHzA1CuQTqtyQs0M6bTjwQ8_yB8U5sU1NjDcoY4NgmCcQJVEhps7bMS4JuRnbm_lktucKeUmWYL39xTDRfxqaZzzrlyTMhnkv6lFFr0jxDDVmsA5EYOG3YKcel7roW91MEOf_NdcRFmh_uGN0tK3R2EJ_in0vkWo1yA_xUBzuzYOZ0zAAPaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=ABIU-s-n_stjnPZ51FnN1ieyBDgLK6xWNhRjyOT8CdtLWss9iTdu-0knLBc2oWD8r8-yz9vwCgfUYBKfaZw8DbDTFir0xBUYOgN8WRChz8ODfx3J6hOpq1IC092d4plgVh3EOgqQFT5HgoL7TVeb4vXri6EgMXnWiNF236ISxojVSncjZS-ZzakZaY7Z0oBkLNpqPwnM7z_X7rJQ3gi_WVnt9ABaQOU9f20B-b9FCpU_zLMgl3wxHdW8XJSJkIOk5oYuJdKKWtHU9B5VgddOBjF9gxEFKgeLuwLD6Ox8eqzzx6RdSEiS4d-yC4R5yhLXI6WSS8knob25RjIUTtVddw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=ABIU-s-n_stjnPZ51FnN1ieyBDgLK6xWNhRjyOT8CdtLWss9iTdu-0knLBc2oWD8r8-yz9vwCgfUYBKfaZw8DbDTFir0xBUYOgN8WRChz8ODfx3J6hOpq1IC092d4plgVh3EOgqQFT5HgoL7TVeb4vXri6EgMXnWiNF236ISxojVSncjZS-ZzakZaY7Z0oBkLNpqPwnM7z_X7rJQ3gi_WVnt9ABaQOU9f20B-b9FCpU_zLMgl3wxHdW8XJSJkIOk5oYuJdKKWtHU9B5VgddOBjF9gxEFKgeLuwLD6Ox8eqzzx6RdSEiS4d-yC4R5yhLXI6WSS8knob25RjIUTtVddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5tP1RvO2jHaMyBixap2oVTcXbt-_HYtsAxtDG0Yy5i_Xt2UJGB810hdV7xwCzfktcfHw1fil0yToHu3lUvTqCk36c3ed_iwP2Yvm5b87zmsL19Oo4fROwLh0ixEIia7Tn2l7EWBUledOEw2VVnjx9fuIi6vHev1KDOa8MHQZI4OACav7pSpGzoziJB9Ob_URHPWRBu1z5q2JG6Y8dkmjb9HqkACEoiX0n5IFYBnNdHrorpw40VfKtY2YcIfrIFDBHHeRRf1LwUclFilGSvZ21xgglMkh1y5QjdTZ3DQsnp3b8stG2L-eUGo2BDFO8Q7Ogf20xwfekZ0pqLyTp-lUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UL8J35JLWV6b14840lHD3KVK_Y2ekyL5N1PH59HIbO_FosYKe1F-XIDjBuN7tYjepqNvU6xszCGve4olNo7_iw46p65pFeSPlrMELnw_DTDcx0e8cFMJ8l9na2QeuFW306j3zNIUrxGvsMWygJPjY9IF1cV3LZZRZ_Ph4zzGfxovQ9t3LxaF0_vU8UqP3Oid8FIsw6BzsdZ-F765YShZMs6B5CaaX3N_GfUhXqX8LRCSJ996LgqpIrFvvm7JPPKA6WCWKudK2JmGEF8QlV33TkfM3FZJnQsalkgWc8H4XuPqFI_snT1pn8J88LVMljYVfuh5kAVwK9bpjvTaRuId9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-YjFbc2jBCn5qULr6Ok-dV9-LeYs_3WY5iT835KsbdPjf9WCPEbNy1voukkShsCxiUEHLFdeUIl02CbgD7dXdrJdwuaFomhrGkKKpxqKIEjfwXau5ed11DdIUkYN3cSx_UpGtIRaxOxL2PoEN_RauhOqsudw0vo0Saf96PpAV8_apa_Hj1dZJyFeb38K7ilh8szT6AvX7yV4t5L0QgQat2jZlBRjkwhk_spQe5o7iAZFZlfYW1XPMFmSrlqx1aQGL2s8DSFb1a1MfOm1m5mdTEHvn--6L2K8mESQGNaCBUn4-E7RTi2N_QNcvaMusKkc8DfEd5W9t4N3X1OebruLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fywrhl0AxHspsuDN-cshdZV_Px0DFwna_NDbbjSaBoQG3rxVb7Ek8QmwzM7S_eUW0zDfieVGPzVpQfnL32XC8kbxMmOEnGwRc8_y55VGkjc2QnYR_0iHwZePLrhRv7Pn4MlZjnlmsvCkruvBvK9UNyC5eSgxObUoGCGTXcK30eWdKXZiwtUSOrJfQd1wxlKfR50QdZzkHinJvtmqnuMeKnyZGlDDtxv72Y_xS6BbDBqUtWEz5hdWxPVPOihnIBJiLrftoXH23ydGzSrER6a3XxaNy4cb5r6l7htvTTa_AC0c6q2eBAQmQAD4c_64tZ3asF320o4FZUwEwDKs0rNbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6TX_rEqrpjjEIo903D7AvaeHDTB1J6cTx77e0XjzQUeW5pzp4sbw-7A7dQDQhR2tt2HfrnWWZV9IzpYZinGLNviZtLgJ7UEmzRewZ1SHiAwuIZX5B-TQxG9r8x1XxZ2VqKn7VhGX2WtFeRY3Yf23xroYqCnL_4G5bs846I8iHeXVv1x_N_bXUg8CaQJQOXYYcif5knEnMkjtqfk-dZg0cjLN4ZMFiCtpzoKq7qH9TI12L5f3tD7HGgc4tz0XFOPO3xFDGZ4v82mFEjQofYl0_aqfKYOJ9zUv9KXunfmCHv_3oQD6Qj85SmH5rX5wEMgW2ze-83j5avag4EYG_ntnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1IPoi_7kLY2OnHIwTpVmJaPet8c_v4vzNdPrdgNmsCBfWch_Z2A8YC4i_dmpOe8CvFyHp8W-UHoXIn4bd9Wgl9e1rx2YYGqqp-X2_IHjoT6UFp0oANCjEerddHF8kTt3pT9LmGGjSy8YIr5FGFXDYRpl_6ZUei1uH_8RJrPNbo-2WDmKas6jPcJkA28yLZ53cWbHeka0L-LfaY4NZaJl4_6DFcsg0aHaXtArOyVAIr2sSH2evcwaQmlJeP12j4YUCkgBOKWdFjS1-12Iu5Ozq_4njay37jSIiROAT51DZY3r--cpSdkn-yypIzVNvGEah3kTDOht4TzvXsI2Ugn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vbc_OZjc3tJi2Wy1xecEQikdwb7inttGyZZ8opzNmrlDttR8TLapf1txoFhKLkppgz0NvBPhvRC_U1qxC_ceugnQN7KU55SOr0WJDgdDGSHkwXWIVoUcsyGjwYrEainxfD30VROMKnXS8CyMONmdY4-MR1cHTNhgRUPo5HGOW9tslZVcg-G25ik3mIThPLhybTRjulOAThnwKUuWfRcbX3XF0qKvPhUL-4VPI-7lZH8kATcRXxqGQ99nCURbxQQ0b0rQUXDMAJTeN_GryaCGVVSTnDgKthJLY9FKcUxTFbu8QkD3hUPUBU_bp5z1GZeyilxZvvfS6GwRS-x3Dq0SQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P2gDvgPJ-7bCME0dXejjougeweobfWyh_TCLkhgOYj0DD1zG8abBLEN4yVzsY8fcmjV46euBKe4AtJU_8bFV7tT9zVYe-roF93urSrw0wS5J2FSvU92uZZuHt3InfMauOnLDkgdDY03zKEKJJg0_1ItA0XoXmmJf-uiwBhxihimnPb7ZQzKP2mZSL9Ttcdi11y612JBVd81PaNeZ04zD8D3riYRz2kSa4V3_-e1Q1onx-a93GLfIEUIMD3flXJZmmkprpZhKFZaYXE1gcEGrGrrtAJM47SeZdLiz2G2dqWaMmjhBWBdKh4zPZwxnFjHcieElpecNjtdVSvalMU3BNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fyLNgLjQJREh9gr1xUtPS3H2tKFc7jQjjLppcP3f7O-jUa_pPOUY71vflRQZF3WnQSsmM5kLWV6IvLkJZOa2v-9JF855UZY5amxpDvlZ5mW-T80l6px9NdJVczJSWLHkEm5NRXEsbyBRBSZ2Q_uKSVeqkc7070TER6nCgiOnGh8bxWzkKsp1WgtCupe-L6D0yurlzoAMGPbDjFkLVBj7p-lEejQNb2fuO8Hq1Cdginfx7_CGGaPRV03yq_jtlHv0w3nm41GZ7X9ZOx70P59WlbeqM-koJVe5p6ZMqtZfYgSWdg48WWdkCThNAVwPWaEkBKtcRd8CDvL_LX_lAUDhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TtA8Md8UZXb7Jbe2wsdfd6uaehsEjGjes4WdhI_gsLDmltd7CYsT2-SVNSXEotqsULf2W5NRZtFRooWidPfPkcrk9f1wjq8j_B3jnx_3-6o6s_e98QxIu2i7H0f8f4STzQJBU2FxjoTY3HRnoVO0AxSdlhvWOQabjKGOmJ-6jLpjKOy9auiws-8_v_1l8IICpKDnz9uEH_M7bICAjpVYTEKiZyzJozx18SQjPZydhTM1NXEtSJCzlyQ7BLstosjWug2niZnGuJ_OaY7bw_xhbO0IgSi7gIejYz8C9nkSmfT82ZB8xp7WadAGhL0GmZwCcwekv0j2UxQ61k7iQ-t-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VqPMip2lUp9gdaHSUSWVagS7VFCnTylOvublvtFPKwMLJuSKK2ocYJkx8kw6_x_4HbTfA0_Kumkg0aikdNXeeh37d2llfoGOO1JgCa-XvfKDfRmgZdk5k5cqMbVOn3t86V14H5CQtiQ4WAHj9tc5VsoqXzD38NsollyjwVGNlJfvBtHIGeOoHzEdKcUGbLjClm0qxEacRK7HPEvvlN3_RehYRayG7xHkQjYBECtkuN5Xofi5SAUr2p6otZZ8hFt35DQ2nHRDKHnYybXtIbMtrXomNhDe9UawGT0X3T51Yn1tQBAQhrgJEmfFVsBdQ4KPTfeIDbNaVylkIqxXmkvgSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4TIYYeXeQzerCs48sfYfxdbio80j_zweRU1j3zM0H4pHFYSOdrtRWqxpWm61J6UXE70oIShyu_mVzxGK_uunBIIwiaR7q_mIw42NAY9kb-tcUD72u4NpeFt_mSSNFW-WAUJUwX10f9M4hBe-Jf_4PiRr5KHxRF1CuHBc_1qHgll56o3nE6-jRBryucH2AjF9H61PSjKeaKbUnSwF5u1JN7T2fU539S7Wp8Y6fgh8TJNhh4gm9rxqYsIJ9f2yib2vrChUXV2VOffvkPjiSKUBxg32Ss4AwtRq82-yxHTn0tDHSRelV-tienvt4Vty833Dmn9_yFWXPkuFlfgulyNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vHmf4udMKCpge0SGnVUXJJcxCtjZOS5o9IGqyfOb24VEIhENg07DsW1_8TzXOKLOJH77rbRhX33Prm-LLG8r1_-g6pRcza2kx6R_qQqfeflfJN-7Hf4b4ZnH_RjcdGNW6WNiChSY75P9xrxpkjc3caUEqu1KK63GfWiIDHaVEs891QyZMwJYrImMyTTAESy1h6H7wKsU8XBk3bKUl3oBEPoPvo9IaPKvV7DvJtazO9qIrM8A1zCsUgUXNx684j4oIAWswNuGlp39rqJvxGYkEppXcblV4gapDSLZZsXvSgtAgQvz8BbJSupI9PBjQo5H0tBEl4Qldetkk4BCo7gaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KvC5VJqnvatEsFH9gYjFTNsVaNZQ3sMup81k70fX_WK2xmBAlNH8qo0hNTx2TrMVencxk03HSdVCSyy_4yQP1x5MA6RC9lHPkkZgSwzZsUMGyhqjm9KZg1rYIncW6Lqm_twgtj3yeAkxVNrVPE3CzpQtwT54DnizzhxrYi8It1PyxKn5PRs4_0hWF3CK45vVkfCkbAiHPcZkmnJpHkSgfqy31lfx1rnj3ui7pNJcHNrE1FleQ4STEI6ts_B7-W7n3Nr_5kTMov_9uZz3QW5heAj5irvTH834l1FqSZ7d42qDP80BbasVUE6y46exiBUx6hfmqX5bGzakiC9M3HUVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BBTQaW7mn899bwtye7_0-1d23V2D8gyJMq6FhT96ywtmnMonkWMzTuOndP1SURrW5077qgE_2YHZnA7-BHfaBru0R_8J5Aye_ulrAAuZHLH-3vBNgCUQUBRDcnScAW3rNQUodnq3BrwzhgqGPy2nneEfM8gXFN1Yr75FtY72lHDQpv2UeYxIxxdVo4EWGxH3GoZIyC_XHQCuB3wdQgmDx0rIN4EHhqxahsIMmgpsVW01TWbL4fXTDPxz8C0bz6f680jp9u4rlv8bsMfeOKLolVE-Ymb7gjj83j4K8AfOE8K9kYe6jFaWxIIcjEKF7CYEZ6wWNB1EF-2cMNctamqFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GcFkpPfZG_eUqtzNPMvn0TcubuCDSsVt9VGNzghXVijt_4bXgQSqbDgWGxzaWZt13vyJ5JWxAgje-5uye_zDCD2YxoyJofUUNn_qNeH1sPsVzXuFXFeTIU829Irtqd01T-RLPb-C5Ya0S24zsn37J8tAkjL30OxuxLqcplyH4OhbYM8_wkS-yurNe6rQ7ytLXIF8Pe9_1lIPAuvxueV4B2wKkFO9qTgpaHRkV3QwbVlRVlLCNHuQaX-suSc1o8M1LM9_USDv5fPEO4ZTjnOzK7jAzw31tXGvzJ1tOMLcjSRwx7FnKaQZcuFLTsdlWc6239pkFc6tpnJN8o7AnbBjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4o6VrK16Fbkftebfmbz0Xg8BOYqdIJxcOyRVx8QBHSuz5cH3rxYEuEaONSe0g__-kd3Dl6HnYKIheRzb_EhIFIXxvAjCrICf0TL_FQIHNf8SIgIq4-iN_h5HhSiO_HaC_dk8ho3W2YQuXJePKw_2A6IbWvCKuHKkd_1U5OeA-lGrFr9mfscEEqzT_hPCyYewlAsnGnCb98A8R14kBDgM__uFj_kWP_kV0NBTnBIxTB7NYKcCyqf7Qz0VjEBpgUJYf9a3XS5rs9_zjFholztEtoeYNSjoyDARdz_aPlJJYn4Cmo_8nJl2992IT4yJiGeOGTGXBSDDiHBxYZyz8yP8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dYNMGmvU8TWSlY2UURQITJKoWo7cIHsSjMQLpiBu6kWmqrA-0C5uCeSrjVa8AC8LPyr5zxF1eAhgNmD2LMzLAt3VHXwS2kfcbHXw_jhr4eoWcCbP5GhKdTjdN-DHIzXk8IxSj6HQ7-3Gjgqcn9JJktVS5lmxCy3W8cXKCeMdXvvFQ-peWufsZGqTSeQ6WEqZqxhqMU02aP6jPDjoeLw6oc0N5MUL008SKMZh6mxP4MNNUYY_7rwrhyxNmwToYayGR4plM7pJ0-9NRPXX0-dc32wKZIRMdufkllXvv-zzKIp9Am0M1X7rT4v0ZTwGh13HxJl_Uy10UAG5HSSBSH2Ciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9G8W9ve_rqqO6yX_PdJd51RdgIQ8YP8UxOFPTKkJbXgqf5N--0qofBOjy6hpKqHUvksq8MiNKrAb6A0rYgNLQ4MuNC4PS0yC81r2e7U9EOZPNaxeqt65oeBGaHSpC8BhiWcGlAfloFql2FSRtpS_CD-AjQzL7lfEcUL4urrlc3Poe8XvcqMIfpJ9BLyTMbh22zvFjXY3YUDeZRtSmdzy5m544WR4YcHjrgA3lqj1OEZQ5G5UULrHdNjhpYzTp2FOUqPuKwnypDRohbP8CgLUWsx0-SSbfMH0Y7vfR0SRbrleDu5WinwdRHPHRaD3oATi6PjSLVBYfQWeZ1Mk3HGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oNdtKDD9hPdjoKCSQkq6JGIMPcav6kvnoqY-Nza1XrxWg4vcCcuYMr75ADtqEHfoeK4Qa7F4bgOhT_XpB3g1RMg8G3XpGanJtjslb-dLHdu_tLkzqYnoPPeq7s961sCi4qlwnuD_SkeGJGOEhgkxqdcI1AyG6G-Hc8u_nlyWYdPoImTeJZb1WTDXjmc793kM8p8yQ1UhpLoH6mIbzVZPk_jdWkBfSwK690hZy77dR9Xh8WC5kca8_wDSDDjPXWOqX1p9osFdlbgw49xhtDKsSO0ZH7-4joJZ_s05ddj83wJp_X_vi7l1JbS4ZoPlQC5jRSdOScwLCOxj4rVIwkDAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qnp2Xs6xwxoARjeiGylFaYRQSrYwV1v-WMT67DVWySM93hHPWuNDNjVrzUjb5Hr7TKgW1XY5CQXmXA27OBQoGimnOIbbaYHJka13wHk6tWKsYUEL-TcuSEEFwx7NbUcgJKER1BjVoHh1tOo0dIPgz8TjBO020eo1typgITKeC4Z4JeJToWKew40AzWdGzOOLVNwz1qWRghURwybH10dAyzN6EVHaJw4B_sx3nJMwqcXi8lFaiewRWR6SNtdDPJppvSCfGbwm5whgCKYd0634WU3RmPDnfWp3l1yV5tU5hL1ZNlUNWxPqhd8KS26PSFSE5ilHI58_k93GtPXc2aCi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/isK8BcLBnuFRFm4EoxVgBjNP8SWmmddCA9UFO2Ywt-qZeqZtrADgzK0QB-3WlaTeb1-EHFZ9bHonYBMy1CuMfnn7C8Cn2F39YAuY4RX5LQ3f75-B-mj_QdQft30HCtVnLoQIoOcbBAxi8uVFNHecSFRMMd1PAmEDMm3R3GqVVZeyOG7GMef8KXczVysQMBhkC2kfciree7vVJZljjGvb23VfkBhQ7nm4i2_dDfm7eG6UZHUHI7XvyJnFTp9LmJpvwAuTBx5ISx4XrvatRvdM_NvZZkTmknY-hJx40Z1YILd1saZuPUPNN_LLZ523bfVtC6_Po3tZbc-AS9H8Cdz_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7FuUEZn51E4YDu7V41fPKiOLgrQVbhnE0j5XwBhgtWlOB0pGaUPIGEgUVOlqnlxmpe-ex3h0E-Sm264TLsn4HKnLHfoWMaEdJBin11t3WZ_DgNxMzJP5zZ7PSBG8BgU100xp-oF5V8_4ZYspeDWSt2CuG8Bwp-Nk_VXTvmm_7BgyCRh9znSI6Ws4w4POvutcp25eX4_svZqkZRWDTIIQ7qNNvxIAFNLAtjGbi8t--Kf9RisT4AcscOaeq31wLQYrHrgc2pP79T7yPl4tTCAIjIK9tRri8zhFvnGKaUXD0eXjr4YRDtXd-lBH--6X3GF25dUgKTln6EKfGh7Jjc3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sd8-YryiaKW2631mSbAtr2HtCz9x8ePllQH9UAEFQk9CXPHR4psPZNfhHzpBXMBcj7mazU6sryJQ_mrsWKSNJb_OumHh2z7QENksPVJELdmgN5sE4b7R1pPfXCYVgETXUTFHd_EBXcgBMSZEaa-840zmRgPwCElc5977JpGEZ791BjBXbUD1Rb6hwoAHj-zQJ2DgNC33n6ylS8rNTMwVZP5USIEm3kFy08dZp7KObG30t6ZyNKGYEt985kSBMK2c_k3uhrwi__M2vQ4FI7yZxvl1dvbwph3f8SLs4GDLAf3yEe8Gw4oJmkTjIFAaopNWvZQ6gRCcoBgPIG9fuZehOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJ-cq0fveWsU94nxNV3T5sF7kpSwU1vHRlGbYQE0HmSnW1xjAK3TbzMLy4fQSQRfq2yRetYRXLF3o_oh3KQuwqYHLQM0-tallDLSo_XauKMX-4Zf8Tl1bcof3Jm1Qb-dnYtHoPrksheYpgnyabweFVGlAN-M0So27hz_A-0yCqh-biWKO6ae3oMZBT8NNAfYDHuAI-5IulqzFGHI7iZios3bmsUN3rPwkNw_v2JCIwkemiTwi4MqEf5yqrTtMYhPj_rlHnznu_QUScaFAt5m3oVav2o4QgYByOV6BPTg3EgI2DGsL6LBT0SqYxBlk0wrrTPw59Z9Ev66hMHwEIM3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxzzyRpp14MrLOlteihf2Paqsp6w4zstl3jouYfqRqWNG__yqN0PxTtOZB3WbpFuwJSW_OxZWQBvmGlY3118AN1_DMRgccdjQg6c_SvRy2jcTUdQ6GgF6C5Esy-HttKEASfYzTBzh-vtqKg658wgtQ0clp9qPuHCAH2QTRPyYU2Hp3STaZAslnO3wk6H7gjAn0qFbR0WfKGlegGhpMV4gLLdCcdVPbz1nB2giXFz8hzXe95FzQDHB6r_hzl-fDTCXwSgCx-upFDSJs8HNLlAPHpz7YOCYvZYN7GUb2B3iVrc9xvN81cAl8LsYlPqMcfaCltdD29haUzMOj9RDnUTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kQTofGygm310ELsS4UbyNzuRhFelYGEIDH6QYPZY3Xet_DZYxZ6jbaPuzMwncman-nxhrFC4xOH4ff658R28jlo3c5ZPcV2uq6SVLL07O7Pp6-q6ghqzpGFElMc4MOnIE7lcyWrnqvIKUoxxj0I1J1yGgMGg6fR8xueGinW6Gu_qF6mJXsK4zmKUuqzA9ztDL8PsLGy1Xwwt3GLmvwZE3jZrMONXvSYPGtZP6AXB-6GLQx_0u7v6U66wHl0wb25J-7eBUF7jCboVwAVP4PLqfMb35fJ-Cy4EYe0XwqMhMyzpA4y-RAsujk9Ofz8kAD4eLh0gXMsayyK24kudSbnXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tM9461nMXRAgYX9MdivPOhIbVPNT7OJDyDj-ozbUfrlAqVX3v_8rVw_DqDEtYjNfjQqkDqjo20vQ2lU4GB3fBa89UKiC9eN0dRvPY00Jpw8I2YybGSeVz4GSsr0hxELI3FPJwCryxWoJFevyXYFXKtSHXjhlGD_gChyOourleMqNNSZKSjRlwrXrYXG_qLPvNPvQp_5QoN6-sN7cDjbPwevDQLncJyMzXiurezD4u80ed2c8bwH_X-z-bcg33y64iGL2fsqt3OEmwGZ-vsA4eZDWjOQBM5uCeb4WmFx0okBqq1ukZ-yHmX8Y54GVZhYgTh8MVN8HaxPwFT3ReXuXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eLK3CWNj4lkxYj-UhMhi26OVxwNkL4R3PvU6MvKvbpyt1-d7Ca_j1z9_sL7EePaO2a8hwaqtouaNQVbfOAseTCZQ8iRl00sii--3FKcgqVu2zrrP6wI41fGk6XEVK44kDBDKCJmazsWf_vE39re92A5ocfI-lHX_lM-Lealr-s6eZ7vXiViuQ-W7bXEd2QxGyYNA6x6464l-fjr8CFvXJ5PtYDiPqfgPtfxZsQocpmsHT0AJMR28b4tnnIByGUS7CVtbwp-29BTiar_vtDBNfhn74Bw47NJxY7GzyrhjkiJWPMaY0s7KlM7VUcB-5bIzsZ48QAdRILRh8M8HjfZqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NFnCyaTdNhMDfkNGd6a19Um9CdyTnLRrVk0RxSU3zff25DbeItkZdmT3VJAbAiNTOFsyjcyiQAXtlFERFFFCe7EIl-SHGLOA8DiBvJpkEZrg3C8AVgokNFNbqBS-jB3xyy55s-DTbcOT70h2OdyG2l7M2z_D0JAn0gB2mAIxiF9SqmvnZ25gtUf0afsyY2DMg40f-8Es_wNfhdEYfn8x30eJ9Dpzi5RYmboBC7qNjJ7Aujv727vdvxeJfdTTD_Hg6Ixk7xm-dO-beBLc7K_yH_SALhMrwNAUWEseozFT3jPIc4kgXtmDCxw6bVgf-KBFlfJbLoJrUTX3tniLd40skA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mx4xLZDWRE46gJtlQbZYCS2H_dvKWB0AAAw1DkHTS4lpBuBLuxLaXU6E5Ur96sorZPd0Zx5kjucpbBDdSuRa_nicST7lehMpJ8oohw51qgjMlMq4zc1jBrKk3D_36zPTiRJo7Y86H7Y6X6UTHVhbwtSpizjluno4LHwog5YdDk3H0Iaf2YKTs2Ln87F0lmOBDSp4nmleNOu06UDDquSETKkaP4Xvoh9dkZjX78mS3H9n6XqU77BEoXdSmAd-ldPQ7Njy1Dn53b5iKA03Cgoa5nHsx5nE8V8w6MHNQ7e2YNYtqQdESbI-nrJ_1jeUYTobz2079EKIXuYpos3Lwga_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_5GB0tROL7DEsoZdrQQvH7YVG41kQgxXDG6ocJe54JYlT7apnnjOtibpRfPsoiQdJXbXJDmE5aBj2_OJZNbY550wlA1ALOoJabwk309dshNLe7YZVEYI_lcYazVspjV4bAZvism-9VXD3vMQTVRD-JHjycTEBNY3asC-orLobS3d6ajECKv8CZJOU1XqLVASW59YigJ62t8PkxVGy0q6cpSUj_1J1NCiGjppnluZrl3Q2-IVSBV1W8oU0SegZYkqNCcbZ1WqRaBKgKi1devQxAiz9sCeITyAYOODVsNCBQd5YyhjVrklPzi4joqmaGPgdC3_BXzvl68QMZMKk6mHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxtn_rEm6GrBIGlKOWZLQnebo4lEDWluB9OyofWNXMN4JzMSJVswgXaQGJNYj-WbNJh0i0ZnhlmHgcaOdgJBNXlaggX8LG0riqVi_u32MHfRsXHfQ4bzW8gJfMKQsP3v41FFiKP2APEhRiIKpvgEEgXB77DJQBdSSJxK_FL12i2_IsTjY-1mUxbChDDlx8iEpA9gRv446FhWal_Y3Ibo045-SJHhYof1s52CleRVRHBk42lsfPikfRdaVz-AljrDH_IYlBa4iGpGGfIDQeWGqepqFQ27_UWBEUF6ahOCH9L0vkP_rgLjA-iBpNDCkj0eoTDTUQCwyc-Tz6Ctnm5eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uchQoQ2m5l3Jc5Uc1fwQOy_ZYSBkn4LHTRUBrVCEVgqOunGWyc35bv-BL4eWL2FiWG95Efa59gFZHAcNLX4Ql62ea09lj3MBc7xxZ9FVAg9qczFhV-1x2I6prwW0UUul4IQD7Ak5DioZUOmPU1PTNOib58jLPCwtnPu-BkHGmUyggczcKLe0yrC55l3Sen9hZHm2pJcgVLr40TZon3iLR15oYie6pMj3KXUsfsS5M5sZ5Wv_plLRNcr2GSP4nWcp7SDCNaj8YqhaS_-Ew7nOwy6VADU0xz00AQLAX_uTA-DJTZ1fXhSQbL_P1Vn22vOuypz4qshCbkS3boCzH4zsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KzfiveFfmSkHbXPF_e4dLKPfyogq42BwW0p1u7MjzNVajVawBwbeDhKeuBh3Lh1vrPj1iI3GiCG4Shkn_F2i3Rm9n-5t1IZamap287s-xgDPu7QftOxU8EsyJ-5JzRYNqcMN3oBjf4kSBHOYp3N4W9Yf8kWMLy5oQ2lG7cS2iidLRGQ4kNZkIir4ZD9SCIryeAhPyTj2mW5zPabQmpC0eq3ppEPWZNJW1jMNApxgvNMSHppoVxtMJYEwy0t5jI0PqXt_4SZrbMBKZMUtnAomV1XU306W6irluzt2CZDW9zaYrMWWtRGxYAjqEGVAJwHlp7eekdA5tz4IlGA5ErWWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nm_Mrnb2tjDYyiRjjVIWd5kDyFTppFBTOfZrUNE0Fkrf5VTZ75-PXoxjWC9Oz6F4guuNLqnI5HQ-1qbAHwYBeoWpMlHQ8WEfEVxEHoAQ1I3ULUCZK9hJVucF40Pc1LWfddpu3u2V58TryGdPNCzvmk-MnWeu2qrJNg3LnnkJxnBgHzz0gb3LMisLhpN8dLFgaU6BA12m1PytnCVJYYZSiVCSU3Q4Tzah0dTed4vTdYc-aishsL5dkJSNeX9nmbdmTMePv9JxNRA2AzhNSwDtpCKlNpgEPzENvo3uwaEr7juHxeFTlKFW_MMVa7RhQ8b30F0D6-4gKGzyxE5m54zpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nYdTmQtEzM6tPt6OgcyfVfJInSl7P1o0oOtaxg0YEST28KMvQM2v5EI7NoV9BZhRu6DQLgkRwJhFjIt_UXUfmgrCP5X__FzqezVhN7vV4J3VJ8o2RB_04gnWMzwAGiSI5ZcyHA0MEUlpxg7QNmdUjlcJe9Dyh4N3Xrw2P2Dj5ri01Q1cTvcyqNMM6snlFPml0IVpW2qZx-65M7hmGJMHNcZGjI3Bbz-8FSwvhat9yrJAc9c64q5IU2ywpjNglJK84gTPCUPKtLEAPxlmhjfgOA8NNKpQmA-CrvpsUKpZ0nJ2Ihnq4JgFhdct29nTAy_cAIHFKXG0COK0JfIgaoBFTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/atlyIT8qdKB3QnTUAlNeQNpIMFioZW-_gud6oS2JafzFtEJXHykeCNcGH3E2_sYyYrDCJ0F0_0abS94j5ogl_1c6Md3000O-xSCbtSD75nmVQFukhjAJjvz2F83sY9q84j67-w_2Rwho1ZI5N2EjTf424tZTQXKBEu29lxpCNR3vONkoH8yYmekGkQRdT3AzsmPvPiDna_qBPvxoW3fXeBkHcJGwd239edq-UounIfQ4OSElhv5DPfmDWcNb5QzeOp0_SuEMjOhDFa58tRC13DzxA0ivl8aspWSrZDhmGktwApd-DDetSoSCos52yuQl18LyenH6f6nh9kjnLC9a1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMj8tjIxZ9E8SV_S0Vku-i3ZvPEuoIABlWV10bhvHXd9KTIm0REqmZxkClks3N19STKn-SwC8yC3z9uCg1BzA9PzDJ-eAHYGf5Vq7mtdGzbB1E9V0SJuwi7ZL_AgyK9mIZAyAGrvMF1_sXKOVUflQgLwPn3PdmR5zlWuuyfUU1mjcM3f76sOJt_BUn0-b_0fUqyJfK1BbSOdmWgToTU8GP42ffQdfidEKZS7TaMhO893o1Cewbb_C1T7SlksiQPOYVuTXxXXVLLe7CGxKIATammUcmBKN4UlA-IpWZ-a-1Te1mfmFy6NnERYz7KuKlDEa9NTflxeq9weP8jprGvU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEFZUNvnYedZUhKAm0BZXionQJG06oQOBN9g4sZf6LGnBR1JDHwV9TBi49t_TbpxxW-WZzbDakm2xdiPf-bE8xqiwh08ubBqSyxtsMGQjeVJuxyAhqPQ42R9j-9kWoirySq3Tjpv-hjqiA8hVqRCHY-4bnCPDrvjDPJQODPPABwxiAa5bIjNBCCN42Uq4dP_iCfphg-1kgN_oSJjP-vzS4Rz1JZpzbu-OYZVEqqQIs7ZRvLFD5p21XcrGFvcGiVp_I9QJIvrLDXoh6hmQMzQZh9s5qgfvP7CmpdvezFtGGfkTXpmTZCfZ_Y7AkQBgwtuhrb5sm_UnvNMm4AjuCKKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4MS-ZWbW5fxom18Mcq4MFgdLdRDRLx_tJq18GtU8yMgoNON3YhGyjSG1x5ilKiaz9aeHMrmSGPsZ5jQOzashsD1VxsgUxHUfv0s0EJUmuAFTYeZOiP9E8ZkN90XZ6L2_XB9Y8FoedNnJsk_sB9gvuEtOMchUNo_detSRGtYOY-mILwkSGqW3YTe-CeBhJx-XubMvvGirmxlP7R-kI4BQ1Od11Z2PMH8xi8R7GCpgl1wCqx2AWTUZn8yEyBPJodLhpl_uW7pnmsKZx61mi3pWraVCmOvoTS_MLsDYl3ePT6hPE7xOcfAYhhgqcAzVIEmgJo_UsFexGRGhFLU0I2d0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SIw7KUrKfQqbPxathoBKinllZ82OZTiaUrLDcQX6DH6ggkn3L4bLgpxCRZwMogEZB0b60nqzUrUGNamkmQNas6JDWhyAn6x4aHkjFUjHBc7khC47u9wtnrHS6bPS-XFiFWJZlJlBqD9DQY6CHDL5TjiS-YHRH1wlDSGe6ahRp7xNpUvQXbaKNM9fdZk-yz7NwqhNGb_kpvQwih6nhQk7WIQ_bE3vFA7kWMJru9i3kMVv0kai7tm2rB5N-5VU9_QjNOoIaaIHD_3zlZlWEve5IJzdlXa7Ml7LnM2vYVf90rlPawaH9eG6WT_51snBMxikYU52RS5imvMCgYLHJmtyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OruHG6N9ytRs5ivlWVY58xHUv3MLalETyhoW2s5SOMP2MpfJG0-BoId0XFTCdmPeedkPbAkx1DQb4LevKv87r4ou9EY0A5zOSjvtkkguE3SXs3eV1UbPGRD6KMJMOglW2uFX6S5iqANFJD0pSLFfcT5e52nSVDQbEioSiDyizsD0fOzmmqxL3hI0P_5hfF9Zr6vJbQuvYkB-O7khvkxD79U7chWwiZIB_E8-ZjhkYjJfeNgQFClNXCRfu-vUirzlmEIgkQDfNxFMRsLIIADjKE9ILsD6Z-K9vg4A-C53sbHRAS_WyNlgZ34HE1VzxiuDPceOrQ-NBSvdplZdR9E99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pw1d1Oq9L0RtgQtF3t9xPgWWzjQRBVKOfkz4r4uotEG1TPP1CNC52eT-EiLmFz1QTAaFlHG45fJQSvqqlxnu0r5RNbBe3quv1PYKIpq5uZkf8Lii-wwHKkKVGu1t-CwRviWALE9KdtySRDiSk_ljme6a-lVykMA2JoaCxIbiiavObcpacht1FYSjIJm89xFNXehDq6sx9XrwHDiQURIlSf9-gK_cIoPLnSsaLM4SEdwqrvc1oajmQwcih9JYmVJcl0asndyTq8STdBZd9xdPJOQfpEh8L7vOxsbAoOC3SVNDG2cAdr_KaH-7LWiDB27BRTi1vuOBryHNW3IrU2pt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C-mD89yFmyofVZADfG0rTaupzOwKFFnTT7Koa0izJzSgEokOXN0HmqzjZlhpm8JeQbm19CJlx0oPyFQipyV08dIdRFdq5q9Z1Bq-jd-5vQYh3kdCnLXTCATK9FbiuYYE8U-tYdXDNVpexpVZX5TZcims0A7SiTk65a2a6TbQzXoFGCvx8CbXVzLENB75HcZ6qbTt0s7F1zP1iuAIB8C-nXAZ8TXaatuBs1b46Fp5S8vyuf4-D2XYmiDEkHRhvNIekym8b4g86YLHbFy3ArSh-7zyq3zM_tLmJ5WzVRybFIrG2D-GnAmb9rvHIcVRyFyYIjL7OCbOLOgnI11vAG4Mgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cIG9xe_JqwZY4CaHiYS6gz3yAh1GTz7-3_yoZbmMSvEBIs0_FA2ZKnYb5Go5pHNnUUX24HHo7d70P53BkjI56GttorAOgQqcWYtz9mXtgM3IQb6ijJiP2uLoETehPfM8-scQ_lOBez_V-2n7XaFtFwKRYDyfNIwvzCymJzvLzZx6g9d3pl9GUlXQcEDMOBCHnKrT0q_B6zhKmTYGAONM7eqrrFfbfpmSMeGhUWCQv1V19QSDvzt3dKFZs3w4ZfkVgv8tMKHPuDmtk6tUpOnz45IeT28GK0Qlsq9g_obQqnGb8_iyGrq29bGPMoH60j4-UHFjHcdIL1WDw480A3_lsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rj2jnHAw4gxKO74Re6Wie6uojLIAx0e3BIjNNPqfaXDJQR3OEcOa_POxZQjhK0N0Sex3ytbLqNhxg2s7rmQcDuE6k9ZBfTPvLB0wU6_VR6TFUCuaXtlt6QNd0wbTgSZRLYDDr8gkKxVln1Yq8_ITb7OXiFX0Z46U0mspNIbLiZXXbBEt1gTw5H70LKoNQyHqUsQF5ilMDLWSOaUAu8Fhjz9tk7ZaiWJ_opOZA4sitiPdb70KBt65aIpcwg1o3W4feMydkad_PQO26MWW4lulvRK3mCFkY-Gul6y9e1HuxI9BgcLMw0QA0M-fBbGZrzjUclHFhAVu4O_tFS2CEFmsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npSDZlL_Sz-BFQFTnXY9QXIc5cRVX9tg_dWb1NdNngJe_fZQxJyeyKkgjTa4YvtGlHn71HePqtemlcKg8NVBWHDezgP7X4Ajx0o1-YANnUIpjrepZ8w9_QOxVPkoWHwGjzXLFi3wJraaDxKekm_LOgKiYfipC9qqLjUxpjPhe9SdGq6eokp_hqWlx_7RDmmDDLPzh8iuc-dyI-MP6V2lbBwQZpgLQf8WbBT6-oRcd0BSV4AvQ4tOT8-dUZxPVURTP8DIc0DKKJz7TyH-ZzxHir3M_eTIuN234X6xflNEiWFIwDpeAAjuMFQkFSnqgEeziaC-efXNLO-mdDFhSGP7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/miHBhV2CmsjfGX32-A044jEHkEMDV7HWU1ZVnc27SQ6RkIEz1CGlVuDohbGKPXitqB-EaMIi_HB7FytQ-nxxx-1LATC_diqddNpGHiNtaISx9cvg0_gFQ3igXJEoSh4wOVJ3Pu0ae7UrtEBZQ_6bkrf0cIfpjt18G3weX-e49BuBPX3yWqGleF6qSRgW6OuBfRKqcuTCy0SswmaGRowmOCeykCOBKgfSvoAJdMf_29iQt64l2rgqYgQ5325i196631fE2fSgn5GUrOaQMl81ObANXvp9h246vzeXskJc3WKQwmACwFrT0g4UIyCVam-GSfjkB19kfzkAD6iZVGhMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwSHAPBoxTv3I6xWpI5wjxazB1dsv-ncH68oHGq7HoT6vIQzqNimumRJx17OJMB2jxShtLx3XkBWpP9Urhysgp2h2yYE7T71XoodOywD9X7e7xr4PYRNEAzSwIPVxssAimgIePkDFuQwCfstxqeIQCKfqGtEuiSx4DChwMOeeM0OjAzpPWgWQr-4dCqdsafj2JnoTEPgb-i-_fxKR3A5PBRKvJUYUq-PKaZa2KMcfP4d7bXcKZOCJnoJvyVQFPvIhPqsGYs4e9XYm3qxuK0M4ywSfgpaFVljjLI15-eTRQ9BojfbHXzI2ZYNM5IxrG0Sm13DW0u0sXbOu-WJF88Bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
