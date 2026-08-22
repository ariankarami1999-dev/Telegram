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
<img src="https://cdn1.telesco.pe/file/V3r2xDD1u_J1LOKPy2aAFAQc4SNErf68v06mv5rjqrEzcjGgv4dAhNbS87qz_x47GcpWO1Dvj1Oa2o8ytL2W1GH6oy7ezxqkiuInoPmLSmpe_wuzctAbFk2AClD_qPCRNF2gCJoakr-9JJPBa5pkdEkGlNpUiVPrLl1LiMpIj6T6p1iINCHKIq5xgDOK0JjOE627_UKISyH54WcYvfIPuivWUVZ4tSyBXVH3gOUzPBckZPDA9hBfoArKMX55hSURu_-oaSDPtZfTYskk-NMucPvCmSXdGV2-FKZKvlHNEqPTxcgAHI9666GsAI81W1eP7pdsIP5GoG-qkhWoaW0-IQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 21:12:51</div>
<hr>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Drpj5AaUPxBuOKfqgZkrZHd0pP3-Inw-A-C8jqWGVqmRUWt19J7JoMPW4z5hiXOjMFhch9ffcNIbAYOXInlAKubC6oRGGNmjOntNAsqRjOo5K3cULqHO77Eiejf1-W9eJ_WyaqiyADsoztNGloStJZBY8eJQrjBoXHswrw26MuCMzRil78vnwYz7x-AepHjI2NoOv1IJxsiklm2ZOzWM6fOHLXvEgOeduXqg6WSDJOJrnFhhaflvz4_CfoQAjarPP3RQKcDbErLJS5ebUYTAeuzZdXGQxUJ4o9v6EJho0YsuKdT6-_M50BVUIeA2R3vLh_ZZyxlpGsrv24xiuJNUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWcrcXmQjTWLyJ8Kc9n9ahsk--MIOezaGVGpuviW3pgHJIoSFZPoolRTC1iLW88hfGxCO-xBLAvKGi2uYlq8OWPhCrZwcXSpD4sjJ9uh6XEaysvHR_o-wA1NSGHVzRk9iWakt8DFMqbTyKO0WJHm5vL_X54OqUhOhq6zE7IWWeCwCGdd3h9GbwYVxIRLL1wHJVm5QeX5PqiqNHAR6ZwK-pKaKz9Ae7HRA42ACsO3DfDVbD2IclhCuOpVsTfEWb5pXcJ8QUgLXDSAVP-39YX9dLBc4P0L_dwiW1lfoAZflIGE7Jc2_yaV2XZHqIjJ01-meQPblTSFcea62xOueWAXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tF5uTid-Fy8wduwgszhrBZsKhoqizEH2OkJPRWiMl35KE_eiJ4tGmHR3dGDWYqLHcdEAw1LRHO7591n74G4YVpb2AgmDZv4KCQXCUkyeXjXxJT6Gtnr5OjQbeeEIVrPCtQlbRFOpUhEDpbnmnkCWYAAvLSmN-4AVXHa7IkSn4IkH2L7frSrvjeWuR2usvr53Nib_jI2jAW8dreS6ymTzu_kkgfinQu4arfegh8TncdL_YaZ1X5Z7I89NNGa2Nvhylv9XgYnGLmr6li2zLfEAVMI4bPSGAh8XOIof8cLVfUxNVXt1p0-MZtfy8ID-6x5MW0xu_JmeaE1GC4ChfTqM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Y-aCy6pc01nqcK38iiNkNMYkTcW5LUUmeABpzM39-NmUPq7161c1v9Kw99K7aIHpU4oxg12HA74BZ9NhTIuVq_UisOiV6sbN8sNPiMgoPVi20FofeRKyyyyWbhhO7uu958MGYFiJwpVHAiYMqPiE9m9eQRpybnl2trABjrnacveKqIXREdNd5pMVLwC2LtDmJq_M07-W9UyJZxWfLVl8UmB6zB5CoQbm1OpI-GV_A679LFpbcAVYCEx9XwjMQHLnb_FTV-g6AJLex1QSAliJsbdKxIfDnLGMTjheHaGQ721av_S1KL0FDCIyUigXrdpSQ-MwaMB_uD6LAKl2dA2Lrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Y-aCy6pc01nqcK38iiNkNMYkTcW5LUUmeABpzM39-NmUPq7161c1v9Kw99K7aIHpU4oxg12HA74BZ9NhTIuVq_UisOiV6sbN8sNPiMgoPVi20FofeRKyyyyWbhhO7uu958MGYFiJwpVHAiYMqPiE9m9eQRpybnl2trABjrnacveKqIXREdNd5pMVLwC2LtDmJq_M07-W9UyJZxWfLVl8UmB6zB5CoQbm1OpI-GV_A679LFpbcAVYCEx9XwjMQHLnb_FTV-g6AJLex1QSAliJsbdKxIfDnLGMTjheHaGQ721av_S1KL0FDCIyUigXrdpSQ-MwaMB_uD6LAKl2dA2Lrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7ZalExVoR7cgTPo1ZbnRoer6l1ohPFezKWjEiwKkY-Du52Dy9Dhs40AZaNaZv5nFGjXwO7I_oPtlYl_Kl3N6WwtWB9QcwIRHkhmilCdQNcgky6taWCXDF_n04iHkW0pDyEcRSTgM5oxEsItchg5uLh4Bu0vVlLx2n4VcCwYwhGEs-z5jBUg3-G3XHbAxnR9E9vuAqHaTMdoB1ePy8uWbI18tmGkh4loGY1ilyoZZHaP0R91BpCt-2WYue1LIAcDYlOG8kvsmUpW_Chfw9dqulfATLTgxuSuHfayWdINOsyIGoDI-DOElwlHjWBrUgsdP-CigoaaW_bbaih8jXoewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cz6pcFwcKxxUt2S1OBNUxy5nORCl2TnxqcpRz5le1673htYXOjogk4qgO9LKFBvxAfzZSUQCDnQR0noSBSnRBdvhq7scmyv3ZFZPy8j24VZCSfH_fqZgxwL1e8X2jF7dRGezUiM0X9wzgoRD5raK0W33Qdb4jKWBzEz1AWVlwx1kDs5hdwTd_u3MVuSWnxD21KKboW2Zza3KhKOGAD3uFvLKwKzCIoRkuznnVuL6segdW879hnucoWgha__oZ6g2dbOLR6hBvsq2_Ko6Y1g_weEJLU4vsZ3ghVMBWl9wNdd7gggS0eblogot4qGA88jmk7aeBlmP-BJKA_fpoOBmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SMlk0phKSQyqZM5XTl0KxAJvmuEQvY6sN-Rzt2kZCCX6wPF_MRN-SR1PvEC9y9rcazZkdinkhNwrHxUAuit3Srn2YsWsfRJOrKx3TYMDZju3UpUcLsogHpppuum3ZpV3dmwzw6WIKc1EN_XgvT8S86YW7-9IgEO-UriXW2qqfTRnUaSksyjNHYtdGT009l-dqrkhasbJpIlICY5HMXjxGy33tqH1VzfekHTuvj0oBRkJcnyWXicvelpCd8BOhpA4BfV_JwVNnn6cDhQfaAcDu3AT3Ncdtr5u-LuP00wNwtwuUbv79gEUDnhJHX11vwphYNyyTLMgNG4tYqzhHJ25aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i9rSZi7bpVKu3_2Vxbo1C2_y_nbEDNO0VessI_KvSilLj2Ts3y47atLZnx3C3kxJto6JnAb655JaBTLSQdz8yzrXsG4QlmgVJ7zv4jEbXsAQjOl1v3OEu4C6lyQXjzAI9yf0_rNx7l9GVaAvmuwqmApNOPTce-jm4VJu0KzthOlvaUBKdYUGeAhh12Tu122Dx_Fu7vbyIylydKcHUQzQqefNIUU1ywpeNZLexFTI52YeMIlBVEHJOy6a3WmIkeKap4mK54Gi7xCf7UJPAes20gALVpmRedgSN_GByWhH5twA_P8fNWtSVc4NOMpJ-AealzcoNqy4RYC8ShxkH29RGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l6T8AkPBvOCn-LAt4ZWpSCN5L1jW8FGFSa9mlwlPkgpWv1pNh-p_9E3fidqyTomsxy1029ZvB4wQe2HwaGhbfvyxiHe1AENAw_dq4UTj7QhFgySq4Wn2dK1xIuKDmBsb7V-tNyHG-zBvKLVWW1HsG1SdUoFS1985bbrQ5P6UVKYpfsevZqpNf7N3VtXvyQTO7PhfeODK03uIBEeuqGqJ3Lmw2ABj_yFm7QgWNK4pKZjhyL29QqVUwi__nt-Kf_IqLHpQuA28PgYiASOhff6MrN3AB43bB2SsAfGzS7Iqz5f7u25NRUiN3KyDcLIP0ywTbTJiuB_sSLoXLUOVCrFTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJk0NFR1CacW7k41b7y4aBxBnKUW6RkSek5mKAnbukiC6jH-KLCHJ4U67lgoU6rb9U6n_JSRgIlgYS1UHTsHPZv0V0GWyK5ZUI39zNFsz1pTcSeT6HFDZdkXgv6xMkOKK76nCx9cbsSQ-5_zzvFu9kPYuPbZwZKr8nGkHBJFjfZVE7Nfjx73h7Qy2Qk5TtNzFyhaCGdu2-rU-f9UT_QxwBTQLO8JfNeg9_er06eyICHlvg-BMhs--sPmoWthtdiCw7Kr68qLF_PRGyQ0pgkwbd4ZdpRPoQC3tH57GPNADs7RtEZLI3FBSxcT2dsdX_zvQt13OHN-zt051DtHLhzURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p3DCgY8yijSEJ3FszVF3EQvKh2KtjEAQs2y2SQI0qeR1Fqk59VVtuevJyy8Q4_vI8yj3raXNjsKoG8vm1yiBPmh11PZaiGHYsn5Np8LkqsyF0OI5fDFivbFHnjP7UHJ7bcqcWKSciXGyDDlou8xVda_YGrRpmHECGSYLrI0KAfbp6IFsWeSjfflt8vy2p5yqvDgJrHGXROJ0IZt2Z9aoIoEW7Q3yVgHPTeTrbIS4c4CoOh7wl64Jlcb51tWt53PKE8H4L1uz4xAtaor-AAzPFQ42OHPF5YpZydrWZDGnblUB6CogJ83flwwqxPSZ-pLhBAQ4rii9X-0JkcPgae6mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lT4ZMDLWGPsm8yH-e0DBWW8vB0mFxltoJj6EPF165JISanVjLDLpJEayhgJTcVHwjdydwX8ZpBSL96XGcTCv1Tdyqo490dpp34v-ymSLwqY5BsWOEK-YMrbx7ahoIfE2EiVWop55-ZB5dvedLzwAUOmlFq2uL_bFLtPhmC3vsqQ_5ey7LyPN75JFNx7glQ7s61YHFiFV-9VXhweSIzno2Znrg0304gMpuh24IXU8za0QvhAyjVfwJuJqi9wVliMASld3mcwOLuZqwtmkQ2WFVJSOTboOdTu37ygf2_EDb-dMua9HDujECkVAVbgiGGinymFtb07mCHazJ9ydFMAD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xe4xsyIBfxHGGl46cTYpduOWlq0DMKzJuMnPCnSElaHMPXnhWII_TFjRfeMEpUsUiFWv8AslaBPerjh_TjcIohnk1mKDP9aTAEH5hQL8vsMqMFPApYOUAt_L-dRsC4UZBtse05mVXQJnL6Cy0tpcKuzR7yuNKOx6-cCo2tnInPH_XmJYV2U4ir4LXZ-JOU-baKfzr_gi4WdN-PtK8MWUPRrTgEYLkmzE0CtL7csQMutaNQE7rwB8JS84Hsp72zOWlykCz1cwDwisOMxStRgjhPozq_J_a6zXAJS6LBgMORXt6O28pzywlZ6kwcquvNooZvkWH-6yr_MZcWnFKJ3Vjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AM09p2nx92O9b5MWqerLMNMSTnQCT9PTySjg8ZjR4QgnVVfmju6ZaBytXzc9bAfp7W0JV5N_lxeNEWi-KkiiKkOhR6PIwu5x3qPPxw1vT3uwrk5Fk6_VRgTG5cSN9CxjSFYg1NLOFThda7Vaw4t72OWcXWKvMQ-hy866NmN5AkCx7xnkyvk6XPaAg2FmUIkXtjYbqgh7HQX0uM_bV6nXNrGa5Y_4zdy8M7EXVXfoLXkWKTHWQhkIL5oJDkX2MJKacO56VajczQhIAOBQgs7W1YxswZTFtdMnA2kh1Z_kCBEuXiSzL3KMm2JwX6lkLUvutrGs-uTvD-drI-P6ogGfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6ndFoTGiNjW5eKfT7Vazjhc3ZvA_xNaEJW7c7B-v9W6BkkNG25UZst0o0H6oEx8IroxXQ6RPGICDdohCZ4ua4PdLzIHrQvjgC6DgbdMQCTieVMiBYZ-WnuWtkV8o31RN1kz2ilyMe_lceeYUPJPCgXYGFGXtcXzmQI-Nwi76JlwBaC_O9iKpyNZBdhEcAN8v-5t9KNlyv-668-ghDm2FUKtv_E4N4AayZFgBsG4AUpz2_dEEs42Q4rWDbYcKRoSqeueHCTyHD3i18RRCMhtBa-d1-Z7pKiedfJg87dq3i_ZuuOPKOAInBWGdkG-HNR3ht9wAYYwbMg4V4fHNfHebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T337RqC7QJdVjXl42I1-kb7pZA7iUOiJHjGoCiNugKkCqa8ZfC1cm2fW0Ln8VlmiHy9yz7heycoCjtxkVODip816Ec3Z0xRkL6tp-5-YUI3UaiSSKBWBum89uCuGHMBuTQAZVBZQ_Brr_NGFF5X5EiXvRw_5MIGpeGss83xB3qj50R5HfJS7o3gdhwBYlmJ6th2QLfaKG9FoaJAmAQdqwEiZWGcwIk2J-7Izx7UK4AgwVnpZvuqPoslbrxoIB0IdgoP9IR8sGKP3d1YI1RlcwECW5b5N5gCccNn4Cfldizpacu2U45mknC_PqpnAIQJGZ59pJV5Laj4jx3mmscNmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tFt700NAHxzdOrulOh-HnLFJJsQTAYcrs1iXW1r_xykORpyOqBxKW-yUxo1slSHcx3Rah0nolIq-OEmLTMznxuZZB3c-UPCnl3HRLnzgFhW-qg89ltd17Y-BnaUIpxI56dlZTo5B7_xSnVEOVWPLiYfTMT9g46qTvBauV8Yhf7o02Wx0fRFtj_TksHAfqKskdA_gGt4ie5Uzr9rBTrZ5SzIx-prNXvIpKAjNrF2dpo9dY3cl9rYVZKkmZTAz-sy_pGGlnwRttc69XiJqMmDr25N57oiiasHb2yB0raJa9Zov8sXQmYQGCtQj7phB2XBkLSK1qCEPdaUC3lJ8z8FyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KpVEOl2_5gAyDxHmE99z_F3o7-6Qmsdz-fEOoRV9wO7oTxLVC8IyDq4ECRtNjpMYyYphY6TCGuNMtZu3r2ZolT2XjBDfuie_3mxwiivP-x8n6LxPQuLGpx5Gh_7YeIofHX-VRtPdbKk7Sy97q--YLMp6nvzQtfAjzgQ2ajb8yDWrIsXzNv1pnf7PonNnDWTbtGT1Aq-RgxMZb1n99WllyrnKxEdiWyBhkEdcS0o2AUlwXmClpH-_Sf_0ACvik70AiirqA5yXe-odXYgrYeZnj_yDKFvnRSrld2sA8y4ioAaVNwTCg_lkN4jUZ3BYomWRj4FhPYISqaTwgOQRcCpYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZVQRw8gRJ0kUeRfvSpC1ZXQA-75y4d3j2VvHEMg9YEImDkHiH4EWLJbGOKOPRrmjtu4g-WN694icfyhbxXVVMZ0WJGsdab1auCF-mo0KmMB_8brme45nkYpdb_tYn5Cmy0zw7eVlgD-EyucfvfG6Ulgdx7Q8vYlrd698YfEHkxYormeBN4nkfYZdjF-GJE3mlyWGn1m9qMQPB0CGJEqtyByzS-loE7FlMm1AyRrwwnYvmxgVx2Nz0sM2PgZPmGQOc7_qQSorKLq_JNN7NGPo_FCf35IAawpeAhi1cvwYluNb5pbWMtDnofebCGrSERUwRgGcoajs93VLwtzNfFldyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHadAF_LNVKj16yXLwgypUuv7kObS8nlY2PSRL7hGhpV1Jm8d8Uw0B_74D9z_5VWUrPtp4IJ3IAYKOmkHS7y_0zb4idgC5u96swisBcyj5SUQXwCAu0Hb04s6EqHla5rN18Yqj91cFMBcXj8qgrnN9p6PLsY7Az60Bmd1AqEaNgwVD-REbQT_rZqHnFOkJ6sbYeYKkKGeLpcM9Ha7KSly-n894dCLZV9c-yG2laeBwKAq2PJlEQ_aLv7s58xZEzmRYzySJQ8ou1CKCEIToDPReuxm0qn5HE97I9pl0wO0vetY9yaoEF6mPCpQH4CuIIRk_rXPhulgT4cL-nKTxtmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DgVggCKbCrzs_nwS-2turhW9Rrkw1S2ogIADS7CxV_OKtaoKNDuOzuS9eumMsKuQHDBbWy4QpR491XNsfS0o3CeenjhujNXa6zgutfdUiFU_b6WRJrr3Snql_DWVm_pQNgCyl2aOXILvmWPrkfd9VGZYpfENbQKgApx2_tZ1nAIWgFXdLLtvmemfi3CZI-oCuLCHwnfAam75DmFIbQpC9hEn_2Cw6zrhxIgwAAElAe6TWfNckWttfLeO1e-Ow6bhVLgom_1Mztll_yt47LkqWpetFB75ipeL4AsrcDGp7ruXEmFw77WpaSaroeixKJo5o5gbPSID5pPLqyPbgf1vIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIJn6aG1ESaWsr-m0MK9VBvQ6AhW0oRnakaLNooCwDTNtLLZZdVHfZEMQ5aWRRDeGIThK55FohlCZVvX-pIMNibthd8tKMcDxddG7E9jj5K8FdZInc2q6Db2VTmpV81MiclyqalL48gaxqwN_WwcqCD4pwuDXToWWmZ4rvgY8qq7OfTzcYHSrk8Hh4M4SJrQh8wMyVvFOuAZTlDfzarSxSGSznzpUkRVFWkkKhy9mCF3iS0r_lByQT68VUueaQkRvXRHhMixoznqcoHOkW-sJDdnAl837MHmg_chfEXHhU3NJZSCd9nycdvPaabRtCUTofGgbdorYYVqUHiyQt-BbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAH7ipyZfTwNfNKKV_Src4cBAydnBW8xp9L6rd4zBe3vUb4zyxE_lUZGyZX9UmVSwImjnQ7zn0yQi7YL_AbEuwy7qOnkESkW6umlJ2UVY1xhF0o0qLp80CqF9BkSy0b4rHDlTbd7bk8u0NFWhsa-2Cv7r1sggnti_GvTppKnWUohNN4nGs4pZTh3hZvFLCwHSGPtpP74pVDLEJNU0cZe1tu0srSqLFwNftr1oUou1RJVk4bGBgnc6oyIpPxeK-oGxSpqFL5_34ef1-ZcKy29vKzcSa-1oQ75uwyX8_AE9KwEH7jTOt0MkMepycn3Mv0d8q24aMuhlc9HbxjACHI9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVN_pvzpNhA6RWjTjWY7QlMLCDtaY0Nm9AfrXlAUKaJMJnMWk9qEStQ3F9XCF4MPeLEbbXJFXwLfDma72vo7tkVtp6NKCEftKOFletRsij5qAcGckybwwwhKHjpGztFb8IZJa4rsVjir1R_uq-E0-6BmGkj0_w26cOrVqWPhPPw-jt21NiQafwromACaM0pTyECVIpFGZZpZrg3QY6ELsRafOE8cmhNAUOkcGRN0HP3zb7KHnPrr9ZgB-gBaLgVl2Q7vBt31Nv3-offbiu6vER3K_Wevp7AHTmKOPEUOMCD-dmlRSPiMR-tASLDRKuRo_R2CNYhZk0xyfRaxzA13Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PYE1WZF36DrN-uZcpeEDI4Qe77wkmY6Bzh3Dd0CyqegrNMXAjRkUZI66Y2MjZowaIfiAnDf39ABH6HT7ruYEcXfPbBc1JDG6r7S81XSTge4puWRwI3mdfSBCLdF7ryNw3q1zZPqO2y_PbDSRXoYQ0RZP5r6PERfMgmNce-biAUtlPirOlPyojKhFRfSOJ7IRKXscjZKYa6ELF3FhKx-8-ja6wg15_5ECVUD3UmqhiKM8s_VIM4Gs0v9E57hvyrJvaz-VSenUKuPot1A-oBuVHdmjG6IFzh62YSTPXM5N-Ys7LSa-ttQrLqBvcoglpwy53ChXc-FxuyftzsyCiabnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oPoAdoYI1bqaOzsYHctYOFffRPRrqJRQxH6KMklbCVYG65li9pXaYSf4zIumqPyqhaVf_8BG6mxbZi3SMjnxVxsFpzWmQJQsBeLUkjiDj6uIojBO5AF8eFyKK-BrVks0FawnLkWgoT1E37xEhsO3rUzfIrquWOEV49adSvzs5_LnIQvrQ5IrglZSrWi9633ArTJ5G7Tz5LOdTOms5GHTzN2ZnddBEAal-tYGW_KXVSlz3l8-dG-MQmcdZxdBq7mYsLH1ixH1po6wg46s4rgAz9ahN1bdHGCcPuwFah54H7ENOHfSMzYDaUWpyJCTzqjL3xJ5u0dP_lmY4ByemOaPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTmzBz_h-mlKwOSmBiw5Pp-Y_wS9d1r6WkiPfdHAgdcBBkYiv1zjFphRphqdYZL78SzRf5CDGybxmDHVeWw8tpvmWr5olCxPoeLl8YpzxWLl_ni_IxFb_9yT0KSAf_iqIp6UBpdTcPz6S6k_q4U3LOrrPQ-x-zyQIAhDRB3uITKfysRRuxRfqE4yD11EAmz5YLKMLGmL42VJFeX5VvCot6HxS3vUjDkF69PJfNkn9x8exFdqwbuKjLFG653c-jHJ7dU6EskuqOGaEtE98gElWy5Z1a69CosfOmiKp-5PHbcxRhcG3wi48_ahP_I1whLywMP1bMc3ENm1W31BfNM5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dphLxyoFZvF_fpTMR1iwwcsECur-QTLnupsva5L_rY3-qN922_J9rIqgSzRFi2rHeFxyTBYh0oNyfv4u7hC91y0Q4iaysvPTQfjcKXhz-2w5aG8nFfw3HtH6i_v2zz_s4SMDZ2nEC12nTaceAET-_KEFnf79HsXgNkEptCVFZ8fyLYjjoBipZybgDpTfZNdmCo0S4scwwHj7hKNOhH8ZX9huVBlm-Ur6BVR9d6feKD_OW9Q9lUCFPwgs_uS9xXGs2EovG4VXRp_niQZV0O6xBXvgSZvVpdPoy7BHf1aHyrxoZ-ClkGaJkOIFPWZUWW3mGGuvaGEE3pWCuO-3XaeRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6P2CIL6An9ONVCnD_g-h7bBv7tk9GIlca16NxoHHN6Zri3vmu5jWlKRrvkjFLA92-vTBhDPIy9aLw5kR7I5Omi_EjRO77QocngRefJUU4QMemSBNJ3-W4kV0X1tRrtSsGWgZw87qxySxyjNGvBWS0QM13UhPpqLAgQvrYfi--pyDTasEuS_b0Lz-RGhjJq7cDOmigD2zOCw98ECMKG65BREqLX4KDCs4bQ8N1BtZfVakWrYw2c74wTke_krdcMHbLkiEw0fZW89kc1OPLTkRaZuPg2VuZoTVDEQE_Eqk5EaEQ6C8OMt5wMzbx77K6YcOQdkz-bIfT_GUoUcXCs3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RCAJIj24Hx-tu0ZCsA4sibVlBhE5fIxPh_FqJ3q_9AnyhoYYVlSeezKibWpXC6ykgUtkF3V6yRH7qJKagPvY6UBuAjRRh7YZObLZ0_SW45m-JbfMWVTg3N_3BzB0IFxnXb7ohHiiqQNm2udu99jTTQf3dTWeq8MxyfTU68zupq5DZoKkmSq_VOcbdCKsuYYRDpm7Y5uWlc5UWIXbXW5y_Y7YeX1i5_31HyHfgRjs1VQ4LOOAIQ_9VzzXMm_ELxoAKHH9kJrV5RFF7P009YHBYnmf3Hvl-qUDGzSS-hjsmnHgB72RD_TdXgAGH2T4SJ2d99SoIKeBzUcGlniYICnWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8TC0x4x8kj0tMSgYBTBsOx0MuRFQMQY-dE7PiuIxhzGgCWR0OiXSvp-Nh_Ihjkk2LkGjgnLQO2hmo0HEsuKaCLCvBhz_3pxzqkvR_UQHN8KYpv2je_5WBSbqfoUmtAYGSrO425mzslO_poDm1GzCMYo-8NyvbX8MRdG2x7qbozOrgPRC6DNmIXRAN5riE6LfVCARUUKfFOrOf0XO0S1wNwMfHuZ0Hbfhokz4mtMV60w_R1FpIKrl1mYnZRODBZ5mXAGsYOwW13W2dDur6jM1awHhtww8CzP-ylxahlfs8QjBqxfdGu3yxcdhs93SbYq5ZcvjMRYv7qT9QE-tkzA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7Kd4FW80tkUvfHeffLNlx8YR8EYOI2P9jp5oqztxDsnOBZzX56tTvBTx6zlMClI9rkG5R-N6o-t9IB_a88e0jRgSXHFYmCP_7m3Q1G3ZXY1JUQ0k2qGBqCKMps2USO0gza3MVd7KcFp7KrF8L9aRcdDMd3LlNSmOHBG6LIG7rfV4G3Ha_LoAZJQxeYHCW3PD2fb4Clz9wV-nC07tbHQvldFJ4Ao4RbtQkXlJfGC6OVd6T1q40vPAiRu_cljdRAwqSX0pbv1cipQnaSzev4M85B6KCCzgrhNVaTd_o7g8jtZjWYi33WW6F7PQzTbkjmB9SEBUmL_ndDSfeI4xo_xkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJFA0Bwdaz4Q1vvctZnmB8ThSg65g8OYr5GSQec_E6EMkIhXd8ajB2G5VjJkVOBqWeVg8WcPCkTocSx3-JIpUgiAI63LeD3H87YmcjUsOKQYK4C-xyUHyyYyJ2YBFadjmdEOcaM9RfZ79uHRkvCaQqrIzQTa2DH_kqrFdwEHDcPAxvjGcP18c8ph4fmUDQLzmbOU9BoT1aj5iswlAvx1Vv-KckCcZVkdahozQ7-cVJPu3iNdL1r5sngyaHlbej91Qd2CjnwmOcihEILcBKF6Ktx4wYCQUYxl67DPr1H_IFv1XpCPOvqKNBrgI2fKgh3RKGIBCnjwT1cXT7x0dsF4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujOZQHWYGilTKZeik-CNzkIw2RF05KjNjovG4N7g0WERAMn1hMiCbOUZkZ8g5MtVjWVYRzmqVEiLYkdJkncNPNEkLV4AQLebuFYP4KA-efnZykTCqPJAv-HZ1xMsm8TEt-xIy-GllNO2XSIT6VvaeXpZBtrWs1M09fAshCozqfNBEZd8TsQbIP03nRnFbMG07qYqfW-Oo3TQYzT-BRKX4JolCO3YxcCrRAcw4JR4Y1FGo35Y-h04cLYk3yAo6oywsdjBUKl2nhFrMw5nIEmi0KcCj8YTLlR41rl88SrcTQvwXQpO_48dv9CmUJ0hwNlcPRAKYMSgW72K6Iw75p9FpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mR7LqEyafQF0VGPN9hnGqhK5qQjZbZvK_zvFgsjziko_cErhAfP-KAfpcWyusk9mIE1biug8br9flYACKIePmZ3_ZV9hXqRaSFhhvS2x8Wq3gWfeUQTj064PP7c2YPl2Vnrgbg-nWnmIX4ULIDEMurmzwItD9twpcyj7YnoZuP-PT55-z2Uj4vvVPa8jheU-hbfX3HH0DL0h-DA27XPOM0p3_gNoqWksHPL6ZnxkDI0tpzNK0vMO9_43EEI3hYKp1DDgIhXuj8Ajc1u1SyYEf97cllFub169oLtTz0oTHfhyIw9nmvAQmohu-rbpL4BlBkxD_ZDM4HhMLQRTQ6Cddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0lAaTsCqA52aJJqfJPc9rhs6WOBfe917kj9Q9RY7_jxfOefntxpyxfu69O4j7Ybzi5eJGkoUPvh6ZU-gjCzRlHnNuVkZ6bqzg1C_7biGsE8q3z_2_rG0BYetiC9BX-C6diiZdaflBzLoQSwhVk0ZDQR8246YFnZpeT68H1OCpp1ek0lpBrcdnTzvQdylJgFZO6YxNXvt1h9cSSTDpE-9vZRF5QQnUs88kPtmQItoxE-Xro0yfTuObzQsrn7rfvVlQse0cXZ-0-rhisp9E2b-nltC-rmcOawII_amT8wBEtR4N6dpzY76jn6RfYxwuhS8JAPElBh933HKBOda7_Ndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kINTg8UbOyeZQajpYaEJIVbe0GpDs6z_WR1Hw1XQR45UoekkuMnPQZjRfMlC0O6l0LlOeHqPqYuVVvG8TpaIR2vYYKQfbrilj4pqYQOH8SlexduuWavxNFzscPP9TKpwX6Vn71n6Ji6Yz6mwOWAc6VHlhDHUATDOAY2qWuXOMxa_agdZttORpmzWwpnePryE0xjjZP_0-GiV6Sc8_QNz78_dJJziOfPs-9wofAuHFAEGndW-rjKWsSmc1eZiWS0-vcK0Xscax9s77mvc8Br4EXkZeolDpQI73KNE2KB1mzxjFtVVgMQ2x9wtvIm91rq-0Lf7iKdCWCUeXOnsUonynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKinPGcd535EiUfShnvkyfoCHBJjRTDok1LmazcctAbo32lIyudVpmZrdHaa2Ce7qev9v2F_W4AZkoN2gJoDJy6kYqr-p2KF7u4KSwSjlW-tI4EXxcLISfQTB8MgQQ9vygb_qCI1Z9hjVmJT07fiFVMlOffPJTaihoTGK6jB-BEbwf_klx6csdu1xjInHTDi2Nrv1oflEhXT8Byo6oABHesoO-HnPGS9dkMY_E0hYDXNaBAIoB_MWAhrSqhQBoL7RGvIQ4WIdkHk5SGqV8-4hcGfRIBgjcZxWx_5oUX459CMf4DEQLHTBkv0DpCo-qF_iuTo2Eput1vOZBJXs5WNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgjSaiUAkldYsAdMpN-K7NPgo7Yf6xjdt4vw9R1JRhPCERoBMyT2BGThRLhAZ0njhkMtR_MC6rkL3XJKHU5wZzlrUM_MXByEvgJUduxDKd0S9kPF-wZZ9wRHC95LBQfX1OdTkIu82qbGTQ8Ob1vU1qEhXdWyALvTB3c1jBW4JRkmojqGM-YgYGsq7HGbGkdc8W99ZUXv7vQZga6uAmy9EjgK65e71jASUjNK-Zq5NE6oC5Xx8dr4I9S7pru7U9jevZg0D-NNq5Uo09d9bbQqm6HR6iqamjiHJ-2UzAbAAw4ANA25z5HVLky1QlI1vWrEdycn7spXuqOMgtGcSHz6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/elHfB_4gkXndJTWls5N4Ld5xXzQqZrLnie6f9z7Qn1SwX9b7pR5Q7bnL6uJ7WSfi1hXK2P6QUwP3qmqLiGNlrMMNNT6NXCcgfO33de3q_g9Ic3nuZoQHl4uzGCLEBGnoR8qf1-QtKyiMK7_qZvhcGYmI9__ch3omk5wcmSMdL-m_HiQPtqVtw0VYka1bzrD-bezee0CoodR6YMtJtSPbFmqfyAoc_p9HHwmwRhSk1RytMSQqrlaNW0dts1xuedNR6ImdExBT-4Gz0tydksih2aLJAD7Jhg_67NVns8PmXDh6h8YKD_48Y1_YoGrsWEQNccROuMm2APFA60nSXddu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmefI4as8B62irlUB-tqz766RpLxgvo1834gcU_we8kO46UOGZjPkxkPdmXk7B2CJnL0CqeE_TMQ_mV1H2bX1qqcmRQByheJ4jGOCz7DrkPECGgK2I6M-bemaBj1-ZBFn4mt0ZdWUJR8NtedpE4Q5bNU1EiEnq4hCFR6L_cCdKgIzXSOnNyHgdAfRrxm6944KYPJSFgEPRrGFJdfm2oF2uU_QkqzpiS14psKN02LUnB1O8XyW2yoKR1WbFpkp_9eTGVTcMYEmW2MFBUjIE3PajeeXmmXzK34Vv3AcjOUxdP65h-ovMWwNrLPkY5oMBpoSOqORi7TQI6HFaHIxyQ_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7BG4cjSivRRVZauHsOb5GpnWC-acP0Sns4cMygYiv-UdJC4-9x3janK7bYu_-IWBFiKZsygbCJgoSnaYWzJjEJGwti23enE-sqpp5zDjZI89r6eHtp2wdnYYXilIgvZtjzmW_d39Yb13kQ2KX8iI7TmM_XNUKLgJfc8QUkEBnJ9oQIPe-KhdaAfv3zm-zNKFqkuUYUAYv9sEjiUeKmndDtw6C4ftRizLr_7rcvq-471DBcB4NC2zqicvfvjeAAA6uzaOTwz74Mvy2GEbbRdO17gRa0_ldefEuRHpUEBpFXGJE4IButS3ENXb7SUC3iBQFSSxqZjOO4ci4V9G9yrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcZITK8aLa1FxwJLHRJumqpQwySEP56HkNBokYtappceOVP1WBxaR11_r4F7WtTetw6qM-wB1524AwCx8Gbvv6oc0n9j0YEL1UjsYvPDmbfVTBjT0osN0Z6qNlwhFBY0TNkrivNjFtk3TW1ZCKzvLR7oJS6IkyFPqLRzQB0_iKtaGz3S6xo6NGBdTOmFVSBf1otDcDNRen1cRsUiwkCmnPy4gQuj2W4ZebL--jdu5aBxj1IGk95s-mTuLENj_G7gSWVvagIcK8JR-2_kjks43c3LzYPEd59PEykqDZAg1DK3T0TC4Cz38pwhZXfYcTJGsyxu_dmcgtvTqb9uodHntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T8AwjQqkgLmxjyA0IIN32yrP2MhEsG2kZsYpeMPeM6z8kgim-NV1uCM8e0Zae9uo7vxaDllD2B7K7DhGowmVZDazWZR46pELgTwXUEuZgWMCvY2PKeT5Z02nCFnQKuSrQFJfDo2eYOiypogAhpqcSBRixzboVuC9eJevW0dj-LCRLZKLVKoxLc8Z7DzXhtSeoBR6HpGc2XL_8-92djpL38qAWLGNhnGix6HtpTeNv_xe_H7eQVBTY1n_Qu7YBbDuIxOMaONf8eFrDb7HPBu5nLYjz4lfkV_oUHKLU-O24DmqUkhmaSE4N1W8zgLhV5tSKBxVacogm4FXxSS6zE3Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JMOIhby5bNhuYIcV-fkAW8BR21uxG5M9mcRf4M0OcVEv9ieB0reFgBmR264Qbs0QrFgZR_cDrYJ-khtMZOrxiQg6SLLRT1e5ESYWnaHTAK0pHI-s-G4FIE3y5954etHY7jcq0xbMHos568jxOkjOznRKkDE53KL7mecZAOA9QDLiF7G7X7xcPmZHCQdRyHCS2J1-c_IDgdX0jfRsCw9CRkRwLLSwddbccfNkbIeg-OrZ36fBd-X1NfFB6g5xkCnYwFeMeBf_MFB9mBWmWuv4sr7eg0zwHZQEh_Tk7vHQWZFooRGAZuZvyexok8FmNnADavVbf4lNWXFWMJX22EQfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SY9pZeA3rAekNUIDJt5uvM-07Rv0bEpo4ZxDrOyEogYcoM_iu3Kb2q-v4iaZk2cXnJglEMLMKY05syY1Voduc1DWh0kdolYeYpz7mPJOJ7lKAneiqZ1XDebIbT6qupMllRjIC_fhXFsxJ_lVWlBiwcQsv00HICMKSWKFowEFYv4HlWh5BcUc6pwGIU7hLo4NK73QecgbmXg1E0KJ5neWqh7dSLbzi_GWAvseBEkybtNgPsEZyubjZ2wAJ_r-LowZE3Vt4qEuvGZbW-KC5iQCDkLjO3GZkjv0DTY0ig0ovA0oSHmFv_XzvJyeFTgcNeUAKWxbMYZ4hGT52C5bMu3BRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUI5O_Ts2tKaHFj3XEIQ0zj_9ay4kVryw0aLeUtCXvbMGFsVJbMy2tuZYT6iic8sEPAV-IyvNX_NJ8k_AJG7xtVQCiRJTW1eOn9hlzXx1H8YwbjUzk5ecnUovghHq9-nnsW0b_Xt4IWtrYL6g_UcBBypDM_bIwr0Kvlu_tmqbAKq0umk4iFKOOcfHeXY4VgSnN3CadUpOp__n4WB5ygnYvN4jKE0V6UmfJYj29Dnb4rCdgFX6y9nfYDFbkOvCU7IZFuiZ14huwkAMJYbp4TLIFymDIQht-7MOy3pPQ2U97IFni-3NNmi5lZ8Axbk4vbJioxpT8NOrUsVl_mBDmGtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJ-ChuIaLkEIoHgkCJJBnTeoYmh-kXW3JZ-9GNXVLYllfphIIWXI0M1UG-27hyTe5c0RzLr0ztk-Vdjv6WS-fyNbgbQVUG9E0U92NqDnaOqUESYCNtQEefTfTl7nAihr83nqYpQleLRPUV7XqCsdT2ztNiGgcj3b-VuZkau6PblugjUda9NMiIhei2ZxiyiONMrQA5WRIr17RKt-i9dbAoGCyv6f4v4obTQ_Tr5uYja6MFIyfiZyRpCUyB9Xf2GEcxtvWGvGtQzMn9-5oo0MNTIvyc1zXk2mv-ji6pfYJeTxVP1tKP5M2zVZSc3J3UsbUYpxiRW6vRoj0VPj3mJLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgo2pxtlotirmWwsW3fv0Kuxh-sio2Evv4ek4ALvkAocrihXRTCkqNnyyHNXzL9O9a_l1dF6s7N9wAKjEaOz9KKRq-57e8uuxm2gJ-aA-fWr_9zWdW1sFVlNxy0Rfy3KEFr4UADkzBFIhdQLWUpLbGJZrqafPHOEPOROwmeV_o_EdhohaVnTGDtsUFQ-wEC2I8n6OPub6hjppZFdCUJ7B4PmzoZhIAMEyJrk4ZUm5IUJpKzCrjERqpSv3d4hrAt5OyTFeNdcn4Z-2RsNRA7vdlqkEcfnAdbNnggtn5Fo2qMRG-ZLjeselQA9Vo3ThSnseV83ZAAz3V-Zs1iuF_ZZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DqQxTCdzVlSmfBAXP3afXjMvNlgl4hPJ7L9yIyxZ5L2Kk1z6Xv_lnsnxOhdge9ORkZto5-0bt10jmqfu6xrgUsxuWnMGzmVCj4zjgYxTd3FnxgcdPLNIUUDNfE2y7IsacSpQPcXEd5_G5I9IYcxo_bIC5P5PFeRS8uMzNrZGEdirCGO1Xa5qXjaDYgnkN_I3IXoW2MF0lqfNDMGWGG-Qt5acDeFGYQiS1TNro2GQTFzyKEJ6CKwdbYeHBkukIzxLyN0slFCQ2HwsXjR21xOZGirvbX1hI3BcOTSvg3V7mpzF8bZRgMFSOfZURxpB1QIv23Ys6FDWuuUvlEVBlY9xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWKiH5BJY88z-S98DhqyjuRAZLU0OEK3Z53icwGGYUqBzPX5RUwUIq-K7k-7VtFhxxZ71FnISXrs8rOZpM0qQXveV_QvUfMB8m5dKbkND9d1okWVwMcesMKJyH2mJss1s-Hdjgylq8IL-oN6FTmHqdXpi8Dr0VGJWOmBh84q8crPx4_ud7BUcYWznEL_iJ_kYbnUzjqkMDCoh1wPYPobyCjmqFu1A3cBzuSQ5HjZzI_HsPAsUWgdXXP4ChAGkhhsm0jI_ideV5Akr4lHoQmrYdpftiYOxjRi7AqK2nnf7q38gsXWXQnDWxTqjYhsWxvb70gcizgm2VKoVop1YYd4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpvgPfPq_VdlEUG0g69Bl5JW9Lkmqb0aVpECq3HcchskAf7hCAeqEN2MzDd4BptL2MmIrXhbtMLT1gzDP31iu5f-RssogcaHkrvLZu3v7mPe7KnYI3gyeDca3kNeoRNIPz9lV-PVuPCvCFeGkkH9N7Uhs0x89Ht-ETcq1iGD6buDeOgzVwJyyhorNkm3ahTY8NAkb9Qo5dpWoqBiggwRDJhHdYexe5xcmJrtKnewusAK2hpwhysGvTgqTA7ULaYngb1XQbIlKvyvDrLV9c1FkHyuo5qHZAAJuvJ9QuWaGIPnQEO7FuP9u0OS92YZsXzztAlOqeYIb5GxSTQHa-Vm2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/epg_mo2zc90p9-4y7WtyeC2I1QQX76QNiw7N41KA6A9bqjI4o8R0jbXCh917bvrOTyNhiZ4_Bj8WUWXRYahOkDpUwG3dICz-p17hZLaFZbSONLvja9VRGK4_qhg0CPt-GkNCi1Oh-6LmY4WrYjkeHMp4UWzncOdLIHwmSmINUEhsJBhjcGR1AQ5Xww2ML6DKQUlFkgwkVnBZUzNAIXp9oKUH7ZX8Lw1yFZwLGb4suqfSjUiTVb08jroaqWu5gg25ct8o3ScRysvtV-U7WgHMRuHNCkhxa0IldrkMijsEnNOQqjen8BJSrl63E9tkXQr7-j5wEFZpSeblVYt9Fz1Qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KB4-4DBJjT49nrtHE4DLgLPIbqoU26lNJMNKDonTW3pv8ZgLS-akIuFIchcFQLZnGq7hKJEOdMtM9aC0d-I-l2Zbp9CfiYdb2gKiOp4hK9Y3Wr6FG-uSKcuX_bplBzOlRuBwQg7j8LVwPVTP7gY8_ZXJjIuFxXLNNKGuF3zpjT090t5mtsps7JFO3Elwu0xgA1cEi0gjbeAqTes9oOtPNmJHeHzSNmz2M0Bep_gAgNJHZnUBcKIhPbcjGB4a7YL94cMV9WtQzlTUXDFqeQVnf_ScdAGybP1xWpeasoDkw_nxJMWUL6aBnrRlx0O2BAMFx7TCfjieTEsRcvWEc8CPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/APJ7gWQikGJsgOIBrI_8v48rv1aO9mYcPX7jpxo_XjHC-TFnmoALpzkgPS8jrqBwXIL-SFb1XES1OI_WHAdXmZE9J-Tu4CSGpRHcrOT8KPCCUpQthIQBaiHfe1evy2kgxQOtNQbVvrUvM-UU48Bapfsr32Xs_WVwZIv_P9oB1yfO_FfQxAfRMzLuhyeW6VXgCEawd5DwRt0cOVWoaI1yi7i0Bf_LnpK5rmmlRj0BRd7oGVYmKS24gAZwOXWSYAxl7SJ2JD48n8pVAP6en-_z-92MMt_Np-x73tTt2B93yO8cTqghOtJjTsiRlpfholfemGL3k9wAr26Ow7-JxMDErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dKGg3rSNjSohdW90cEespIzj86rIxREjQNvfTuoNY52SBtBQVf2nm1aJCnW9PFeQKGdiJGjVCh3ZF4MW-MaGwn07BPMzWuXH9y-1nSBgz9yk9MSwVVLu6r3lgJAvh2jQ-2wPSxhpyALJM50HyYNcBoxrkxOQ_BplkijDShLrzpbGF2SeLB1gEVLmTjD-yBdS42HOTcIfm2qq8biLle0bUGKH4gWW-M8vAgO1AfyHb0icdOwCgp_U5RDchAqFKxMPKHROoVyVjqFu6N2eGd6ziMky7CHCaxA4ZHzOdqUah-VJvzYgdrFe-leCAlnG0q_o11CFRgZtNkie_ZSbMXKm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XHmTzmWkIeh9ILX4KJK31ytTjKagedfg37KA2nHVIizXKKoHs5TMoAf5468DhbAGfoN9tTJ3az8XAJZ8soN4LtqlwOlp_D3YTkAUOrCld4Cn7WcyRZnjz9zPS6IBfCPffIZgFoAGowz4HLt0RVFuBUo63K5JEUsKOFa_KnDo2vi7uztvCwJPt3Wy-83x9Xgg3NhHgwS7Q4IUD27go3mCObIPxcvSKCSewdI7onqKoiZgXH7PnC8IaEuw8tXFKmbv8OZ8bZzxla777oAzRkxduMqoYZSzk5pakYNgD1241s8Zt9F7HnQMx6mJ-g5pSi-AKDSLs2Z30-hz1xNa1XJl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYPKw4FuAsZCUlzKFu498OLNcOOJZ8ocv2VyQRD8f7GBy_xrQ0jULp5_CfWJK7X00ri-kowvPCVFrv2I-JT5qUv1tsr3Ca3KEoM8hggp8VKqBO4mi_z42dAJwwco1tj-Oz3rI3CKVrWgAGc2yZalxzHVAybciffuMwsEcBtiTx7W6KBM_om8nDcgCU72jT_abUNmocwwKhYKVMeC8MdiFgw5L4UpPQMDDqNVK3H0n_yAWt7lhPSh2vgwG10wl4AZBq474giEogPwhPxHteZtVbYnJfBoSqXUf-ekDM2FPTwNIltYTrHCneTOtsCivxgsbZhT98x6O_XfvCq0G2HphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdbqHMb4ICxq7RNk2etKDoueHCUx3Lz4GLwFP7ZcR0i7PyNRxWey7WlbKwqpDxNNGo15BVpYuBmf2ueHnFampnx41BzA1Qn2b10NTWvlA6H7bgXkZJJ0AYQJ2viwmm1q7YiE6N_H6OyXwT6Z4mVGsSFBBY__DfWHDtn3gD60y28RdhZUTTy6gKMK_lp7XNOePt33zzqycvc_znPWFr1hIYk6tEmuimm-8dYzP6Ho7jMinr_ZNEbT3W6Q2q7ECu9DT0XqsedexchBU33VqU3Q4a2TkSASjB3T2YKKWHT9AC0a_n8nzN14TU7hBaPwpFgLOFXlqJ80FQBXPZJ4lBWQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BM6MLp2mRH_iykORlz_zZ66kBIQ4Oi-wGSQNtYphiv3ymwS4BlNVx22Idj5bvAkSPyrnSL24yFSnBJkKj22ANt01ShF2eq9335bxnXqXT5Qf4nn9wBUOCcv7y4uvpH3G-wm5rNTG0Gh2IywvXCheqUC-0mqma80mf3hMxG1ioehUczDEDYtUrjj-nMNKpt3s4L7_DDqR3PF6Y7sfHTXhkLgT6fitlckjBipy_gD80Lxd1y8TnO8ysSfpSS28BOimsLK0NIK30oawGH8KMFV0mnGFku26wzhLRSJVVhKBMLTH024xY2Nhsh3FCPn6idi5d-wzXmxfN7wcGdeD1s7OkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovXHz1-onBAjx3m9KTWaeonja-3bV7M8BfxPlk_rwsfSwf7jm0BM9kxuDH4_CdPDateszx_oUje4wJgEStCkNwud6bwYI_P_eUmURJv_wrtBfdVfygItOy1l4-2ExWfRmJHDfAgBoK6lLail5k4qpoNKcS2tb49LDDYUCSe3DSkXmxnRaTZS9Bx7wwy5btu6WM1jaoV51z4WdauoNQw54YgYRQAGjRlB8u4PcLxoWV7bBS0gewcqlQvIA_-PPkB4dhOATuh9WI7g6aXLUgwnqJLmHZD5MR-bUP4zNzQhz0-sOl4XpbyWamLUYggZ5-Vuw9bSYVNMmyM30y6ZeydIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFFbycJXPUD3rogsDQJqdt9bUG51Vkh-dY500XeLfIbaqTFFIBjbhapCPj_QfYCgnVgDOv-yZ7ACNqLj0SePusWfAx8OejLOyj2hVl1L7Huvpxzjzlt0wFr15cadetvvV-_ehK9vgO96c3xwjNa9EfGnTWOsVeJ314ePOoyvfSVXGsaMEpCaoYM9YD07YkDzuB-9z1vIEYakqjiak_peDojTQJ9tV6aXVML5NBcKgWxcSsaBvOVeE3TtHTAn81d4SMzPsfD9Y1JEicfaDmSZ1KRtjs_zHaLXySIr5wnhVEIKfvgdunhLT7RRg4Nbt_S8SGhirdr5hNLaEpRZUoj-PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_oTjEkdojIBXlrTZvb-NCiOd3AnBFJcPIY17Yf-pK889J3Z1fysaqAzUb1Z5UqJMBpNc6GIt9UV2WcK0770uD1nI1SmPkHtffG4j71rXkfzyZ_q1LWe4TYw24zrK0o-D1M4n5LApPd2LNDnJq1WX9qpHwI0XyyyTC7rr2EIPqVYwGmo6EQ0siOYUcSg4M87zwIbvHSiERp7LFEVC0EwLa4viM-1gwBTh_iuymm_KK8TLeFON8sxCVMuEzSS2H_1Mxi7j-8JIih9n8grXMKXoHJYF1qH6GhICqlgN0jtZIvZ-Gw5ZAzH4EUBsEK7jP45GyLco-QgtZIs0VhdU9dc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rUu2eFDET9T743NAQEaM1lb58MzVo9cy7ZYJcb1KFYlluog7BzMTQmAyYRQXnA3fZocgDp0agIx9-R7avjC3bh9_z7xH2jyGv9Drsw-11gSrzYoig9B562_V9qngnJY4NyFR2QNhJ92q9jNjoM4qx53hmk8Y3gt_9reUWwd85InP2P6-sLQ6OU6yHM4lswVJExZxqyluZx3q098viO2akbqyUMndGkbG3BBFb-zeoxAV_h1AEg_yckRdo4vLQu3F9ZIWWADH-5snGeZYka1eaFnTdzjfA24q-s2I2p08TM_YN_Zkna2GbR3xGbgHBkMlYlP7BSR-SMXQ7LAn-oHUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d8q5gJHLWV4i8qyVlOB9Nmg9S9qr-OrzxntDkI7lLDwvpl0j_v_Okld3_OAJs4zVpdkf4-P-kgdNOMvfdszXewU0ohze_G5zDFkewLd67ccBNg8OsIccBOZJSRji_8-vPpCyYF5MUHYNnDS_Q_hkzm8B2aAmd-24B2Z_KraLkFmurb7c1R0XpUh_9S49f3bZL0XSujxrWDrwlsN_Oh9OZZFkkok-C36vqhuyXI8uumLMq-Rs9etsNug5E0U-STPPY-eI0ZiaKG0H3UwzSB5kcGwhKkssBMJJ2d0mCcv1-EZyfwT8NtIR1CF12mJcOuzfaS2EJq4IxBGP-gUptbvWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unveTQwKIzjA72pVIvBFH0s9jH4NlrTHRA_2OIKPDbszFAm6bVc6OExRYsfLSxbhqjUI0ug6tEHwdRO_UnOl0yhXxFzRENYTwJITh55UUAox0t-Zw7GWVkiLFDDOiu1O3Qhl3vWxz5Z4xRam6HBZ_zP5r-tUalXv-epssyYcQairV9abBYzHz_2fn3S8GzJJI5zI1HEh9_QFF5HP50i0z9qbVCLbnDxYEnCEXyLaXcoUcqdvQPdbXLjcZiTMzLHp7txBtWbboSj5a8OXe64wCIOHvGqGJZNQu9PwSB7oEURU5A90W-6t5rey2p6-lhCZp9DJ1Hpc05RdplI5D-tFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SB1a_6euYpHbGAN7hJg8MXozSLYPutnsMtRVZnjbYqAoRnb5ALDtnOvGi77RsPYcEobE9kWhVEMapS5ex5xlzvgkk-kZh_t1ay_iEYSfc0GGug4BPmMFOL2zlw1nJ1KfP8v8M5nWaLVqJC_FBxdZmOYnpmIaTnZSfT0gyvLrv2XQLWH_sCgaW5HwjlBvElj2phn-q3XkVZ0NK4TxjVGMINARBVMrT3OMYpegLg5E5qH22itw7iCJCZNMVIg0XkAWWXtwZuyrsvTFGLy2bivWn_uqhsZH_V7szs0oCBKttokyVxKk1y3njKgO7eaOxozIR8kvZn3qwOQop3AR0eUbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r7amDtZ4i-SBEaMOqdFAXBNpoX66eUiiyn6rNKAt0uX7gbicz0JoJU99Zlx8jBo29On1LXRt-anYxJsg48LfrovfaccfO_TUn-XiIb7IY5nd-4bus-LxQRszLQ8wsv_qiwn2jc8ucwBjMD9xVpbZeCtuMJrnsWmmYZ1DZNZQvgyvi1t2h4lOyY7YHYajoTAlK-dCraryv9XC8n_MYTtrE0Yy-XjN-tHwcNqTY3MONWQZ9u4-v0nWvAVLeS5k-2FNQ0IF_5NOM8pUwrF6YyNb3B7apFxv96RT26t-30UGizsXSJ2xsB1psQ8-oVsSkqsE2zQaPSj_6gB6ej8UUKVlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PQd5sFCEEHj6Opl9mdgRA9pPZrrQyFGec0EAMFYBsXOj5zrxFWnhwT229zBrJgLu-DPKi9zzk4NLHZ4iWp0UOrbnCoLW2Z8hD9evtQHqVi4KHCs-ExF78Ok5n48nC5dvw2EnSGGLaThgC2dPUmMOrSbNQ0nU7EE4JdLoywhLyS-wIWeSUQ7zTa_xzY5XUfNELTPIT6-Q__JFTySdZvEDcFuuCLYOZh5_I5tupBwoe2EYfe7xgpK4NezZTVYXjLZXXCkuCLXbDqWAv6Zm2-kWQowNTpFpdcwwuYj9JP58orQ9wOhVDaesQkVqyIxUvLJGS7nSc3gbcVDWCvULi0T3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
