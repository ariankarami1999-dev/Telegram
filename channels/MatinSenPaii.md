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
<img src="https://cdn1.telesco.pe/file/GO8WjJHq7LpEr8u4VJ0AY6JljI9yWwgKHKW_6D8tvMeTaWPqp_vpqRf0zcc0vh3cy8oXoilwL7X0J9mM7EjVbGp_VeesUK4quJFQrYfqcU7x6Vf7WeP-uxAdlO_93hyuVKpMGQtIhWry93Q8Fe_u7MR5MjJjun_9MW-5tWCQeixd3lRPOAG_thiv5fJe6mi7dYGUGbqjYnq2hsVOst1q2-VeqMUDz_6hgx0z54CEyTZImGeW2ArRZkmdJ5VcIOSZDMGD-zG-Attor2KoHXKbaqDMlMXsyEPqTGEgBltKJ574LA8C42PWiMm4BcmmleDaZPeuDVlJ3lycXwPmI4suhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6FDI2hhDKXSDKBQTMM2l9VsgHv__LvrVsRaljtoATuuKCX23VqWk2smNEI5uaxrmH6eSK0fvqbV-e4xpC_AA8EULgocCTu-Np8Ph5B6mJplllPfBxVaENL83QoZLQUCJbr4m1KzOqJqNbBPvZ9vE2qYwvk8uCV2n_wYSDBptupCzBWSW9AKPRQa3mkI12GgRxnhWmBU9MVc2mr0LYOwf4IUTEH6zLT0zL1usF-xa63YNyMuP8jLhNh82ZYnhXTEJhRthDeA_0F835wjdXzp7E6G5uSGSABHErB08NafFVY9k7bPMmNwJIDhSkgB5PITDXtMpxTjXrO8oZCBAYXT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nY_xx_uE4WT5RllBFAlYZkUOZZgK1V-hhN779zdbk0hVotk7olqWA60L7gsw6ZkxwkHq4zT7mNVFQWhh5-bSyh166f5sL40eGzmTJxGall4JPEqAuAZP0BPGj9e8o-RUuyJnn02G_EttAnhbfaSog36ZSpLC-JvWbZxRBiC89EvCdjK8aLP0lTzg9jSM1iTSVlR0Jw3YYQzSfFmfnE2M_x3zY7lftpuZ9jjvYw4efYSVSu91_DCvC_AYQLDxoYg4y90vnKNNO88gSaexI7lwL-aXIhNyGoHpdFMV0XTMSrUzCyvF-WqSB_8WB8_vYqg0VKAe_J72av12z5rvPKeJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FI4uaqRqTMVsiyl_UXVdiPvZj4wATXa4XXF3H1mALElz3ZKWwDwmZH6LLfoQWMxlgvcieRasssm0m_Clu3JCeWX-GDCxi9ItwtcTwszAlDEPz87KiOlrsri_MzEgJHI17OGb-WQt2n0r-Ln6JNL05VLuga2ZKo3PiKIuoL5Bp5oP6NecG4xLev3vZNiJWuacMPPg0M4E6rRVffUfwOvo1rz2Zb_i0WvVvjLpz1zmI_aU6psT7Dezt4HlRR1VpwijxYIghXSUyzB_ntlWM3UDj3W7yunxWIWyStTmGNNpWE4jOLo0XbU3eFF0xW_DgTEVn9ECE0b28O5tzU-emxG9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=dLnAGxxoNeW_JZDyo1vxZLfQYXTMqv5p4-KC0bgmnS4xah5juKCbrTOOrlLHGQgUl7o0-ctF9wFZNuoxTsudwzZU9oFwm5lx8DdwF876nHS4LvhVdN1ZGISqvbkMYWnyluakt9UijxPNAWPcymoyDjVnfWt6MNdVWxGBR0OdJ2x_tvIxtWRKNnEMdO_ZMXP8auWW0c42PYKFKZWI6y1kRQncuN7STuXvU-H9dAsJadFk5wOJUnPY4PhCbqIUk-4BorjdZQbiMWJN2sj5_n0t2KAabepf2r5_GgG6kKjDCEUy-PCCrM2qcjCiN2dP8hLE5gClPIcPFubsstCaoTIOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=dLnAGxxoNeW_JZDyo1vxZLfQYXTMqv5p4-KC0bgmnS4xah5juKCbrTOOrlLHGQgUl7o0-ctF9wFZNuoxTsudwzZU9oFwm5lx8DdwF876nHS4LvhVdN1ZGISqvbkMYWnyluakt9UijxPNAWPcymoyDjVnfWt6MNdVWxGBR0OdJ2x_tvIxtWRKNnEMdO_ZMXP8auWW0c42PYKFKZWI6y1kRQncuN7STuXvU-H9dAsJadFk5wOJUnPY4PhCbqIUk-4BorjdZQbiMWJN2sj5_n0t2KAabepf2r5_GgG6kKjDCEUy-PCCrM2qcjCiN2dP8hLE5gClPIcPFubsstCaoTIOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMhuAPcvFTxbK-hBBzIVuTc1SL82pa-hkd7HT5eZWOXmQqSa0e2W4WpNShWTV31R-h4x5FFKjwNG36cdcv-GPdbPl_S5eLmpxPsL7BqK_9cs3OsNxKKDHebXphMAiCVuxpkuLBZCaJEpIts3CxV996L_GkKQL8rWS_vTPwt8_ODgDKjU94SajlAsMoQjhwZPbJEjHdZNiGoRi4_iV-eO8E4wUHWi3N6Q0mcLiI4tb5-ttyGUtS0_VrE1uTDCZ8vJZ3v-e9_-3UnnGeT3lHSyAcu6RFAhEV-RdqZ46LqtYVXKNWuPT2NP1x4zwG04ZvK_IBrKcapTfXyW8oVq0RdoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geWkfgZ412ycg93H8xz12G2maPtXZU2JN10XVMD7xVKFj9VcVIfnQeHxKHO5a7gXs8tMi4Zg-vFbmqts2iWMd_tMwXh8KClgr7uyr9dY5iSk4c0-L5r0V96QWb4JCZBZryjtT5k5Aou-AwsCKTybHSHQgTWeB7U6OJasto21aiiXAbvUs8cm95JRTO5XJ1Vawzx1v8zcgsSImQBH0y6aj-B8sRys2zN9G3caj4gAi1OfGBgVLgomXXqwQPwK0flS7yDbAxLaJGcl-ABPCZWuLq5gQJ_ug-oA3gQ1F8VYHArzbu663zYipin4vgaIoi5YtyFKBP1ayc6dNvfr1RHgZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKlwVxN3cpkqXZifisaASBPB-huI_QR1cOaf8YVa9oAop8rDeEbQmQtGRZ7-YGxmlDsFJtfUhAQTdeL2MVMRpxIgDSJ3ttlGDNG_DbeuzvqfhfCwbvIC4B21uhH8v-W1rCm7P99CCb-F7C9LF5O_gVmM3hgTIgPGiIgrYAcosHt9ycMxL-bHYLUrhBiG7yXMjIfL1ev0XasV3gENfREKo_4mIG-SDOw5ubgueQTcSHU5I1FYjl-nTUp-GxINVN3jlukq31-4SLAt9Ud4EzRNR54RE_pgruEWmgVKQPjxoFDdxHWUF9YDNtsVRlR2_x4Fac-LGIC05pHlWIrpw5uTOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvzf0Nv6V_wI1pRIEiQGC8O6yBz6up8LN2NUqCm6jvmDN59pChQlXpOnCwrsRj3p-ZD2ashZP1wiomC0070MbUmv0iQYreK3ykfHIR9NFA_vM1la8s6q-xYjgw9bk0bSek9LTwdj13OgnSW-Q3alFMqvpLbxPBYSZ9oD6222hIR2Wtg8r-zCK2Cu5S19mojXnbOYEl5HRagqkUGrnF2_0eU_0wBqWIryL4xibXf4wBeGXSwkm2F5x6WgB3Zb3blg3UEnjpUgPl3Ba3z6CBVJLhX2ry0UU5QI4iEauoSpJ1YjHfXNAf3z1NS_j0UY8JPh_tQy5PLPrei4w2TOza5seQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YBeHgh79pAZGcQo90kObk3K-LjTrbtWRs4Bvj1I43SZusGk7WBp0ksEi_Fvhj3q3TiZnHmA31VRi2KDgIvssHQH15VDB2MbLQPrhM-FaX013xnw9ikCf8yJE6nHtSYzeMwt-cHsFTaYFWPUv53D86AuMf09X9nCGEqgDEOD1X_xInRWFM7AOmVIEg9Q8CQPil2nZylvMMtVPprV6pjoAMtOpdJTn-knD8Us-uaLrzfxbbkBv9aTJs9EUYYvSkjQUkyKOQpirASZqWuJZKmJiLtDQfHTzkIgecdJCHpE-4bYAWrKdbXZKKW5eSBz3QjodXTp_16G6XIPMtOvTt27weA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gwEpHsyXQ4wU1N-GPf1nVr9iJmKJqkHBauGoMJiqs-F6Z60YAdeDSEsIC_22yO6eKmbbPv_2Ow2JQL_QS0uAPmV3UPJXJ1VcsVvEb2aJFEhUh3hIg6HhWFxrAs_7-eb-Yn0n8W4uPW0T7LkDuVDRbH1V05g4TLXyyD1wn0sBd9tVXqQS6u7ND_CnmAhnbD2qbPujEjBep6MTvDwRRuRaze431Bs-ONXfODtJymdJvNHGRWpbAh36zU-THofN0psuHr2VhMjut3My8ZFL55Mr9mTq8z5XO8bXgI7kghJyKMFiKOH_uQELj2oD8y5jjTawH3npQAlsot40N4o1jThcpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IHZbEAnB7-S538d0H3iBzvQlRa9ZhZhxW-WWwO1_sNfL-twTzNSVDLB-PbAM-DsnmqRx4e2t5LKTCwNIQBThuQYo76fmj1qnVnzEtknx88zcSoYBqPMmA7J2Tz6j7dWEOxtlMdPh57wV-zr60g8iPnAdZz_1DQpJVMfZuuup3Bg463rivY_G4x8J3DuKKsn2kVubkq5IOwPhbuH0qbb6prQyyrOCygH4IvZy2IZeyPjepHIGc-uG7pVNhQ_KmdT7eJo_J020h6SO85tmghkzc2A7K9YNSjMIqgZJ1X18PeO4jlVgwqlLKRV8qFBaTakselJ9Zxx588RQx9AizwToFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z5LjBXR4AxrscYa1EsSs8Iof7i_kshICrpyT3wJlInJRF1NHft14hUCWk-dULK97961rY6Qs_txnEzl6mOQP02Yx0ptF7V3wDEYPkzSbdeqlaqQgDqZh2ggQ0tekxv1P9MOV7vMMk_i4Qn3_buu_OKjzObfHDnLBxq-RRADtwz8ywriw0XSrgMnG-I0Zvn1qScr1Vrg3CoLJTmb7z8heIl3wDNFgQI-Cl03hJWSU7P1QBAVnYG6R8PrqkaJZn_ddCvDJLmWusi6_E2Lh8XdMCr7XG4ldyKnwDfyOu2FgJmWwyWzCjRgGgj1VGO-IXBi2th8rSUS_4mXdlL-hsHofqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cYjxSr9OcFzolBvROjAye78bgFoJ3SbkxbmFhK7WqNTCDhp_hOsiojsOObYOq4L_sNq2wUhLOL6-9ibl54bsDB-AnJjUKTqBAmrd524I8UjIRltW1NZsq-8CWp0RQaWLtFOXEsy8CPGAltt3bUmH-kq71ElNd56Keh2jBVR_RCpRqD8NRgv0p_zBbl_RZyPbxlwLq_KkWIhiDDDgAF3WkYfF3IMxe8FXiY8Z7ghLPLf-zbokDRr-0Asm9DEucmAheqOmgRzTIXStYWNXhZr9GHDeRuI9U9hVkWUEifrlbetUVnCWJn8HzfUBUsY15L2M7rMp0mdkZdPNhks9y8j-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r0iNzrcj6vRnPFB4-sfa3maWR61jr6pyJd-f41-XOWz0YngtzSBshU29MsT7AQxCjVvEtSK7ZHpBUpSMhQbG8IlzBlYOXkZmyT-kPvmV9UyCX7r3wkwgRBmJpHQ3Jk6a1Pkeq5_AKKcLOLbkYZPjG16avTRilDjHlLla5EBNxenqKA4bgSxH3TySRmfBslWSYdJwjQrUEOge-6ewCR7qubbi0sl-WasSiX1FjyWtABrq3thaPcZC28xVrTMr8R3tp6KlE_ETuBMiA6xmvFG4DraskzHOoQ1g-b3SDZgJWOqApWjqGwt2K5Wrmcur_YGxZ0FqYA-ligX96Fkn6P8KIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l7Pc7lCU9MFTemhAV9e-oqcHVta4jBLfndkQ9UufjG5ZMt3bNrfsp_Ozr9Xa9hqRS4pJ30fxoar-QBf6U67aCVAJMsTziiQU8gCNzfqR98FVnHR347dpDxf1Ms5_fgCf_SYt3tAd-EhzqaF-aL5_-tgqOTKgsqLOGoUylhSfHGWmMf-jQ_g6BiQnEVw5zNR5lu6mt-xq5cOYDUaj1QGfhmcSzbCYfwomd74_CFosCiAKSploYmxc4n56VcxPJs7tzywHET0x0vKlxiMlPNAoSa7Kn1YcGx9Ky3qOudZBKsxUAObbDkiSl7hi7OpzB_ykhNSDG6rUKYsQKVan8KIClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=rr2srYJ6xYoGsoxrAU2-fiCRJmHhHxsB4mReHVZYsZIlnKlhf74ABDHkifgMP-c9LBURZXUS4GnPD19XVhxN3pEffkmzTuxqWgt2quCR7CDgRppVpvr-KN36mCMHE3ygUFowl-uJbG8mvWCmqK7sH6CGbGTB_ju4mmePm0GM6dm85-o_3rdi8y01HgDDflKWeZZLA6ON5y2_Kp2AOsagqQMWV0THdSGNMtI-mpod58GH0WNbQTTnSla5RUt0gm0gqn5hsN38jFQN_hTZTLomkFv7WQD1KVqkYJyGQ_5pyxbaIXSnj_Ou2Y8mbz_UXd4ylz6axv89GAiNLIFn_pUKHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=rr2srYJ6xYoGsoxrAU2-fiCRJmHhHxsB4mReHVZYsZIlnKlhf74ABDHkifgMP-c9LBURZXUS4GnPD19XVhxN3pEffkmzTuxqWgt2quCR7CDgRppVpvr-KN36mCMHE3ygUFowl-uJbG8mvWCmqK7sH6CGbGTB_ju4mmePm0GM6dm85-o_3rdi8y01HgDDflKWeZZLA6ON5y2_Kp2AOsagqQMWV0THdSGNMtI-mpod58GH0WNbQTTnSla5RUt0gm0gqn5hsN38jFQN_hTZTLomkFv7WQD1KVqkYJyGQ_5pyxbaIXSnj_Ou2Y8mbz_UXd4ylz6axv89GAiNLIFn_pUKHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/InXsTh03HO27S0ErJRmnyEQ8W0ZtTkKugJk3-q9BMhK8Hdm5rvNa_fyYr1KXWFrxCjr3jhh4Ww1hrYTqRw6VgIDp_fRMfOh-m0d4b6ekv8KwqswmDAedy-OyRd8gxWoFUSHI6JUrlXa7GM9gPlg-lkoltCL931uPTC69lznRpx05-vqXFvQqM_TbSLEw2lEFnfXqkB7auf0VAbxE8KePy7enUYZT_GA_8WDeSIX0PtVL-1DxjIOgtEBC6ZbigIJEqqeH2822FSHN2FsKRMk078j0T8P87oFOhyW1sjkeuK-hl7QZiKolySFjJkrpROGvuaKR7LnFrgvHOR9nJkEaRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiYXvotghXFdO4KH8LH6yFHuqLlf6S94-YRD2HyBAb0h-YA08-OMgT3ZoeiEj37SCSzGqSl96KE6bk5mYSrwJ6lL3GuORpNIHQ84nW-y5A9eAtYEy9vmnVuJC2MS1d-SZdFv_NcXMnXHNSulxBwaWWCTe5LknNJsBmqtVvPgZUda86zJkvK-_GhDkKnpQ2FRuLMSWIgDjLtAk6_F11bPCECpF4E3dkGVLCGsHuPyUfztS_oLpN4fZOFVIDVW0xLuO4yHdeqn83yNAjemazXoivZo8V0faPFBszhgvA_BkIlDQilvqxo2pD255jgQ219Rb2I2n1-cS07IHOPqDRx5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A-yG6sShVk5P2lOBsF9tZm-U7mfFN7CU0hDqvnFBN3hhSdzRHI6rr7Gp_q6F2lKM45LMKlzoREOk50JK2QtNbgTjG1vvHih-6T0-zxXG1sbMIucvJI24oTinDYb5hbrFTLPbhPRbcv6YPYCpidKP1pJHCM5rDn_Pz6pccHMqi1ekjvOVxQvKRmkUIw0YkYMwObA1VwZ3guzkCTFJCJVEW5uk82tPGBADGR6sAKmMdtte5TxLQcLwEfepBYvzunWZ4ni6YmUxu_pkhzrwhRqsoWNQUJuv4sgxYhUmJ8fyOKaJrnrjwCTD15aNyB-Z0ppgn8P4qe6GPM3nzvT3SiB9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rtIWdEk6j6t_Q7PDmYQH0fn3ep-CXAc3sIRGh8qC0jJakcG1ASpQoISJ0ySpe6CbSajGK0lHbC1IQ3-p2BiXJ74CmNfVqQK_OGd9REOHPHNQR-eUuOvl0qCQzMumGLYEVOr3dv0mVMDtN2bHzJZ456LGNbG-dmx4wR_zeUjRKp9PmWOS4v0-awkeaf2yXETEl62H6vdWD6ZiuGWwJppqVc8Frf6ciYFttV_73ah-M3dPxuxAXBMbE3B9J9i-NtKfRQe5EcT67CXOu2lzdVr6FY-yvhpAtzWhF_nFbXgGkV8FLUn3T7T3_lHCgos7egRDEggBsPman1jj720zhV0icg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfOOT3ZzeJfgG8WBIZssXBeLh30pMpagTT6MSbHYAW-7FWgMr_ZkYDGPJYGNKA_QOKUBh4CH61PuxL8GAI0fNu80r88QOHUTuiDgjP3_iuCRy9wVmXwdjYawD3ODLa5FtVZ5Ntg0SUHevdCiSKCYPHzOXjDyoWkDZNCoOevJEV09WtljP5aaqMo2L8SrNDdKOY1_rnsKheplcTSBy22z-0YDpTZ_R1iFO0jDE7YById7q3IKesRyPW5jhJOmjyn2uM6ElWJyfnWHX_cZMh2wcQdL_GdKkBIjJ9CWq5pjGfQJ3Kv70xgMUtN3FJvE_izEEewB5vUr6yloWo6fktKvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lc9Ggn_XmZ8CPsnSDcECb_XeQgZ1ptF1LATbZBZJbZN5PhjE98uPbsz_EpiYb1d0j0yDPyWtfk-ydunhDKgdxBY7XH2JMlX4FDfbNTReYWNiOqniGFND7fQpVezPJIf2gZiHK0WNZtxF46ZirfYJRk5HQmHSJM7yi1vB73OKtD0ai-tj6AltvyFfpA0DtH6yBNoUF3o-Kj2rybd__4g25_9sBtGGHs8LHtiCirqm79X_oEcVhn7-t-qjp-rArCIIqfzbGawn_jUQTRsBGiWvpWtyICL1uhNwRGhBhk4wvVwGn6u6ZRzwG2oUcBXZwZvoQiZ2NEaMIz6XjYsSIpUGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2pHlUr08-XC6-qgZgSNH0cGCj8F9EV592yyQvbSbC28EFnxzo1Z9xgVgcRpJXAj3SRYkMuN6j025pCqzVI1oyDpCYlPp2alrdyVg_GYlfroF5KYzxx_dC42OCPiVJV9RMZAvwwgIYyqoiaTX5MW3op955Nii92CPoSo20BiZJ40v1heHDy6NaiNhd8xiCQom2eNTZXZrOlwgOKB0yZf7BlS-2ZUo1OAftUymgagAtE6NpunYjv_ztRQOwmfE1zNPns1DvlCzJh2hEcyz-bq1EjaDxSeH0pW4sAnysi2vdNeoiMfts2VE9gRHirfsSh-dCG9TqVbnf8KB98FkzPcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YJnoRUsNKThvu__sQYTBZNsGxmMxzLUePQM2QxKBJLdYbhCKkbZ3zW9cSAFDNE9hQ16hVkPeddOBvE82Jep_O3_OUQ2BrAkWWDhSo04a9wSy-egACme3JI55axRpVmjk6KYx7v6WGbhq8uQa8SqRQf28esHIEzf9YJq2ZeMzakzlc0ZIFlvE__mNQ1bj2YiU1uxr46nTZY9JAO_jb4eTFCoBs8g__RmeR_Ahhv6TPCVB_sN5hwCXrbJlmVbw7cX9F1I0SOTLNCqSgxBpLwFme-PhGJhfj_B6Ro6R2HXninjWvGKP6waan3xXIAhoiBsYUg2qQNg2iiRbJdTmPmImfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kGMA1x6jDV-uQFa_jDsd4uY0d7HfMIe4HcR56AzkBNoXmREphcRDrQi9IMg50kiazIeivcU1qZDEzwbLaKN5K--SuCmgJWCsqVVIXgpB2auwnw2GDa7W-w9Z-PYVNxl7dfW9vTOPDnrCY6WAk_aqOJwsIxqHqo9QwwYiwhCmjo5H5swky6rr7tK9cuutzxj_3TNQUnTHzz9WZQy6Pl2JgmLtXbdUR-aTEB9ds8Zt1mxjvq9DNKgfY_LZF-hZ4NwLxi6PaUYZjC_WCGIH4Sjg3XklQdRd12S3yXDK37kxmr5FT0H9jTzgiZIKn3SjjCLKtTAO5sSZmaal1hQKcsdlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cMChDb9bi-FWl1aJILSmlaonc7NvLP_8eUE23DL3-BRDmLVS-3SheVtYgLMNj_ILWCIJAq3cjFRivCcv1-RFRlyoKcoWYiq02x0D_Zyu2KSFFMS-Wkt0F3k3fDGkzr7nZ-OA24l2VxDRF3TZ0Gd1EIDIVijv3PkDU9arYeZszMm2fDRCZDisSF6tYIHaWzzZ3HgaxHsM_cqL1Sh8D6oN_jbG56Vbx-fLLf3YIP0X0AT1FC51VmkJDtjyZ317UnTEQkjaSHFLFG5AEXwuvZAG8Yp5pgZVFQV85cz_7iUIt-_KGoZSL19OjbLWPqR9FBBGxGxI1ytR_aTlSxwLA1W7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pCCMqbK8NapIXxCIOR5dXHo3WuCD-XzEBIuKtHW4I3CodHBR8oVQhoFJd_31iccyVfSQW9Mmh9-M7mdMmUSg5hAOTUWVHjqPsEZY86mAl59k3DtSGOlDmRbJz1zQ66dESH_tJKrAd1w1XVMgfXKPhSVLtfXJwd7RdMvIlh6k6BXxwTKPY1giHFbTfwe1gZyaVd18GMxBnPfYBul4XyLEM_eGgCgZ8Rtwy0pamm0V2767Uqk-jqm1UU8gmlkUDie2oJJGol-JlNQ_1tgJYbRJjn-OaiwcmpVLpwCC_396hhHvmLeYqAiWN9mrgLQNNvIZ58rrtrJclHLxT7k2LS1mZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uAiKFOq-pH9XldcqqSotzwoNHgCw4sOc_Oqw3lxiWPjGHH4wL7u_zYPT4xhDA1v8izNN4pn1q9luJBJmLh19rgYbxdXmO5cUPvdg0pyNhZdulYVwIouDgb_-IfwPZ5r8f8aU6hKqoTNV2M8cgbiib5vOBxEnnRRTTrdtom6HMxTb2_uFrLrb1MqKYIZVNwTYk-ApOJnBigX7qDtV6L3qvnTMMMUX8s_FXbIu4WjkJFHbOSLLrNDrDBhYwcKgBBSJFqBxgSUlr28gPio4I8UclE_5-FmHIGoHWyKlAPNa5LjUwnGOBrkvIr1QM4fWsZy9EzG2qvi6h8Exy-QrTwT5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mq0EpbbszBVfOMH2mLWKdF45N2MG1DFBKa_sEvu2b9eiXGoO6wnM0Oohy7c-PDCROsTxyHgOpQOMeLnf0Xbs2eHa_dEcBQwhWEnQfKPSpm9OmKQh36h-NpJ3Fm6w0e7VbyumjoA0_5MgLYVZ3EBjSCz8RQLueg0mD2LKV9njfXlD4XjvOxBiKmJSd-SmD4l9eiXeRe3rxZci7o9a9HWaTSZFy7nGoZPlEtK0qA-6uwlhWlbD7R4t5UbGz3MCWvICPQVIt9qB4Y1qh58mhnZ9SMNZTyMGxas0iBIvmMATRHAr3sYiI53d7GlPCe3o26lbYBNUbOu2qNHl-G9hBVJwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/daOBpkvkWkkI-4EblFWFssfod0BSHBrehsiTLDYCVn9qXWLiLE8vQYu9xFn7jIBd3EvLMP6oZFa2N-98Qs__ErxZ4BDAYG5mpmszNF0GTp2edZLs3tNypuNRsyvfu6Sdj7KCBD4eyqAerXfmOO9y_BURWkGaoSZVQNK6FrAtr-k-0VMhubWr9rRrke-EV8Pjzpc3_eju-zStRGVKmKIWMnDzcHpd5NPwQJqsnRAqzJ8PH_t-pZmk-tJeywmHRftHmNSX6XSYEQIQyh6aTexdRyPJ2M6enmJAI25owUwPpL__HJ-NWpPFjtcI_hVcvaIHDd20BAbEuIuHsSsVlhYYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YjPbLPATV4ChM0Gr-vj_ZLpApdCiXx7q6cBSItJU8x1cxiSJzG3jmimtE_EW2hxXEsYH8KCV0LJYqtGNjkAIVpCd1F0BLzfpLrGDYJb9vcjZXG7kzPoq99kMa5GHUbe0n9yDOXW5NmBGFzrcfVB5QaM9QD1BOyQ90AZteW6LolHOZtJgh1xYAQTgE43IKtz2x6LbZWgjX6ymzqxqHPT1lKqwbotEQ0sS8gdR-8bw9ZZ_LRrSKbAlDRV1l6Ug-iWl8l0BkwOrEiXV71OYp1SyMBt98Q4G3vvSgMF07RrL7bVLQWAxIpcQGIUb4r1G_ohoTA1XSr6lgSXhsSp105fhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QeFKF7huYXmkR3rJCOMmKCuznum--1-r7wPWwAVYm6deH9syN8M7BAdq1K3SEe_ptGN9VkJm7FBy-ZwxFH-79kLP3rvJ_dLhlYMa77TnRGzQLIdYqtaa4eTlUfw_Gk_0-ZcJRWlfLs2JolWF0f2ZLm0b-SWlYx_Uicyqt8f6NwS0GWraZcRqIlnRmTjFECZc3Q-F0PXrelgiMdQo1E6bsxCXkHtabb69g1s0Bq8QH0RpuwP-Vhk1VH3XFfc2CfAoP2RZ1YUlCDOTmhGuJK2UiIV5XLiY_Qj_Yv-imSrF8Km-EsLYFgKHeGRHTld9IV8ewHxXNQqwTNyuSkBTLJ5iPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eFry4pyb7bY-HNVBkGiHYl7wXTTNVJ0SUT9SZwKjS9LTE17bY_XTExw6gDKoRuVlsFrxPhi1SkBqThA2U2XdM7vdM5dUcwvLLqv1b4CjQd5QGNBPsBc1w1K3bfUBwgVebdq5O2hkgwEkjBYu06cNOt8XkbTZe9lgNNsQLbND-SeggtuMdlzG3AxnTl3fJy-4BHPcDSOHobDUeGpOrfTM9Iz0M6WRsCq-xW8XLQSUFj-aw55jReyUFjegOmU9mzjfxJpMAO6WXg5CiEU7kBQNrU1xV6LJXPGMVtZZk-hsPx2-NuELnj2ogRtPvR59PVBedwsRcZk7ii3Z1HVmWJyZtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oKPq0fzXftLW4-oJs3EsrkbmMSRogV9ynlNf9KvxpuS7MdodFkiSKUQjXFbwvGSiAVz7kZntbL5bxOHCuQxiSTQi3y8FWRXMJvAx1posaT812qnrQAcRMvlnViJqob1-4-TVswfIVv7bwpbQGV-PrA9kh8lITNBIsJLzhT4cR2MGtQuBnGUDWQ3kD_b72xhLwjs2uROgQMaaWwOCkyD0W47qE8FWWUXwLfaq29kIPjkQRGvnfW5zC-_2MxmRKNxyJW-QLdk8Bir_ZILhM5bWbwMpE1KsKwZgq8wIyfpKmhVsiv0CXtXi-IId7eOynXhc4M1k7HKgFh0U5yPFLRR86w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_bptS7My8FQbzNjIcJH1tSND0ko9ZplRFHXPTxCLI9V0DnI9gHIsVmqagokYKJlN4MKL0CIYwn1iTFA1w-HuhMdQpjhGEO8PeePc3YXW64ro9b4CqWqgYWc1XGsybC1yw7brNxVak3cd2CTGW63tylQs8GsIrrMJOSgIUAoIzqAde5ctnzHastYQm-EXtIcuNMBKAdrlFdxadrbz_AP_rvKReSK5RohSju5EHLE4Tz1D6DamSaGSi67eKm8anUrL3pg4J1s7yRuNQtespRRZV9EX4A9DqmtTGExkor0dXKt3-lp3RjZbPQr1-fcANSnEZVqngPjNF2UNWnvXQJqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D3Ip1eA4oGa5jWHmDKvuBYgMT8rIF_US_JaIDgqG_z0HnlPyG6pWcQI5TFONsLuJUnQQh76ArCQm1XHOnVN4aXg5H4M5ku9LljFWQ6xlqRF0bRmlrZqLsPACMy6OLSPDQgd_L2Aj5M4lif7e1pMzNi9HYELnS4saAE_yDnM-5CE5okARUjZU2HjUuyAwnrJxfUgO3X2FdBdoKkoE4uK6H5YkEI7xaeTyXV-hbisFp_m6DqeaMxtKW0SJSuPy0fuEBisJ1WJaUbf89CwMiIvwjNXlcmu7rLtUYf6jiZ1o1whg_s26xeCd9q1qa3QiffpWx-c6w_77QvlmgOHg5qrf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JBKo494hh-UGIaEYNTEm4bgHaoMmnwTLG1U15q3cwhBjbef026Pt9MkvPBl3pNqSlEqM6uzg0hK7K7RyUwAYsyGuX4Zeh_jKTxi8AD_04yfGsdw7bQWok8CcvRnLYCY7wI7tyxxDVx5iKweyHTACZ9_0QeL7OuTyY6QDfuX12q-8m9vqv3yIlM3TzTmHgMYE_KO7GthzuCAilCSkQiYTQNYtcV-GhqvSUW4WdFSm9VdUg14wkZStjvUlUX0mldfhmd-Wd4t7If2u0ltFcOVpN-d1d0AD2QfV9neyP1SNZoX4bHIePsUJBr8AXg1TLNtbta8HUxabpIMLgYaa8T6Y7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AEEpHZjvB2fB0_RUyQf-X8vTCz5l-7LvZ8MnpP7il1IJF7nbt1ZTmAWWshX83Vh0XjEsV7MCiS8IE9-sjrhjN3b0fch9E3r98MOLrTRBOGdaT00Sh69JQWFdJXTDWzY8fuhqlZ4xdHtGgU9bx1h8P5bOljz40JTX5W3roWdtbQUMCNACvyuiF_RphmakXUJk7luyMaFPejyGYx38vAvFBTQ-djJ9vdCQMYvODl7Ro2wK804QFuxQV0iQFvdg1XD7pxgKPqDtpHvzl9JF2K3kkeSLIBAYFM2B4r4xxP_IJ-_xqzFSbmvKLwze0sDyFp1a0jwN8d9bVxZiaiHiD_qGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HT8gCvRi7FiLBhy_ekwhSLxq9I7dDF5E0LmLeUUABcANYF4jD3x9Dun51zOaHR5wC498RfulSz7nqCnt7JK_6FSvWfVOPZlzV_-6QLN8QVjUVX2Jje3wdDUsEAgtwdjvjDjoYu84U5hcjoH_j2P1bas6wpLHJO1TeL7HnB76tO53Jz8SZRBZYenAlInDt_VGq4pT7DSqz-QR1mrzLRwWAIaFaY1xqoy_sfLaOR0ihCzsdL8T48SyIt0-Cv3cl9jLn27A2GMQCBURLp0xPL4kuhZQhdygFTMhpBWclMWAqs8s_xL1IUiy6fvOtT1BfVUtK9hJkxufYAszPBTVAJBkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GAWLZEDvRkmVjL7ONOeqtGlhwgglfFr3WKp6FleO7_PaTDw9sEhk6p2_dXgu62DF3rC78B91YL7DpdtUzSj3n5PXc87LI2TBtZN6cu6kCK5z6_Y2ecf0gIeY70luknK8xwIrrd1RcASKD1lEh88_ndhUkk0EcOQYZpM6vVUGBbXlyigmMER565JlXCrzGS7r_Tl7J5GzwveWybyerUNnrrRwjPUJWOG4G4yEgcFEbPhXxi-rUjjUAVjWh6G6eKlA6dkrXh7Q46o8vByCbQ5NXlpEQtB-CXZs4GFMzxeyOVk2ygHWG8FrrMm4XPn8FkKNWNoYa_zFc9houzPnq2r1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q0iVaIJaf9P1tJit1D6qIemUS_0GQwO89iZ7Z-1FRYISDvvqNGUnjBaqwp-mdwqFOZZB9tSe_bogBT-twuP22EakwBzNSy8KrMa8f5eRgiDYuQk1gJTE4qScK32Ub1rRc1cUjqa0BvhoPTxhNk5DruiPhdBeTCUzegEePRChEIKUr_vxRTuMLgVT4JmFzJeDM3hDBAurAtJvkNVIqe2nysUTgOPxlnpLEAWZstX4nhLzW7XfDNGb3sNhSyXO1fDhdOhVz-eQgJSobCL5qiEg9yjpInkCNQWkFH_zt03vyzE6WFsxr-VCY3qU53FukL5zaGG21heKSwLsfjd-RJLlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OuwWOKe0g1sUnaMg-dxKs8mZQUiZCfePKEXY_GNWtO8rvprqXbFTG0IK4XXZ2ndjvHMtLFRq6ufwyV0SUuki-LZujW-lnzth0ptwRez2Lq9_KgBrX6fPHvNnoVeMwF2JfBWfMxRhO0oYsyNuzjNCb-N5iZxbztHqK-M85Jj7X61dXvPQaFAMUlN7LiNgyY3bicm2xair_aQLawP0nqG00CLmFN3KZTRFmW6zxacf_unwHM03SM3XQfPs1ks6m2IN5nDEHUUf9Exgn3QPw9qzHLIp0GiP-BWIKLYDcUfvAeYv6ckpoD6bEEDQyqc_9FT_y3xOLvD9xx9pGUl1JG7LlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z11bKYu4EczxKvTs9oRYIsOpuADVo8CATPGsFauRtVtpdKPDJsU7wos7fTrTwuDAXMBHYGh0OqQ34CiWrUV4T_NSaekiS6-evlBlS68kzPaYgs1mDQ0GOmfKtCqg8ZGrzF2uEnylhKW8DfDG5UAm3OZKSbU9rmMeU4W6GsU74LwxZSSpsV-HPY5KyAePbzl48Ak5UU448KJHPgmdpCci-i9xkk3HCOOMcbSxyaw9pCdayMVZUgb-tn-ua9Ag-in3SdOatZ6We55be9-Aa4cfjgJMDc9UQkPiWLM15EUJRx_e5I4zvqFO_XzQIZ5VFe2Yr90rP6_CY7Or7bnIlx5s_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fde87h3iUn7msN2X_e-xW1IHMVzGH_fUAMR3seztfqMIMgu3Yr-kNi3-U8Rc-fNa1UQEt8fKnxlHWfQ_y0ac22Q1SEtO-41CirjeoILbZefy0mVRfyUyazESid-sfLV_h9pDchJqGNAWxDtRkIUb7r-mkDtVUQ7Ujne_tsHhaF4OubdTDMZc1Al9_CUHl7lYdKzmwTj-9gnuDGOmcf7Xh1H_n9uD-qR4yph4BAThizlDZBAqx-pf2yboVqm_klqn18zcHAtLUMiOnjbxZ57G9ihiMLB60RxnYnCbo5ZZurDy-TPMwi7GmD04I2MiNO_iaiRz1rnHH9KMtMUi9sQkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QNb_u21E8Hf3OwmpKX03IZvKjK_IeVoEoeFSEbdUccV78nmOei0aAa5aQhMEZlMWkHwmr5gFUg68xdH1fZxFgSaAoCAH-MTpxThcrcQnC6cCNGs-mt2LPrAh5wYBjJ5ZPlJhd8HoGbOTE0a_SQEGOS8CewDm9fBxqVojnJc1SNVD4sv0awYTCAFTMlw1Z2daYAYSU4p0XoyQuxCiYDV_8k71A-ZypJQ8ss28uNYXwdHa29dgwl-Peu72UrIFME-fbdhvtJfYFU5FhQbbncG0duda2xLbvWfgHo9xzj9U0WI7xt71KEkN9YF4aI1NDa-8jNd6nMSEon5WiZBv5iMMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lVSfVvTlqxGCmyE6Q-uXN99uTze3S8kxI7_JpzOra3Ru-bxTQaAQqLiaxawLi1EPZYLECevPy8Ho1eQxpsKmsO9GmgJLws6tm6FsrfdBp49Ty7LeQ6--ObyM9esYhzQkqcYo1g2A6mYWBY1A5bf3wmMlB6MEhGl_ys6AWYyD3ahJkgXOOqPfsHbmv16WpkYIH5Zo7_KbEmvMpJQNfzj77i_gYM8lc3XdiR5g1dkywSWmDpBBsf5V2bkehGedPqv-5WbsQfKpcKrnv9qoDSRx18OxD7kEYH0OEK9Gt1dXMtqhAuyvvgnIzv0KYED7VaRrCrw06ZCWbRdJTrQ2IrOT4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKhjD-BDVO9Q0ZnvtSOU_8eydJwtJfXuYTBkK6faogvI7tmsplPgU61phfCftfeu57-ls9UGl_veKpvfeussXks17lyAfqrVKifBIxfJyrfie6p1h6axlB3_8uWV5n0hMM5t7v3yPhsZdpejGjC6vnYYYOGGJVcK7glMRzf7yieqkSlVHbZd70oDoV8sQ7f6EHoUqK-k4UocXPvnFbYAdXRuRGTOYqNu4tOJKGF1EG86S-4WtQG_IuGQA47xv8YQYpuj37a6MG7C1YHiWdhKEicHmBmDe8Wbc0EckBSkUBzJB3l_02Aoxzv3NPGiaRdlTyybLLcwkBnmGc1AX2Daww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1nikP49lmgTvpaG5X49Lj_PRShR283ls4dw1_w_AZkmR9ti-hVupH4L8XCdrKKtCWHQWusbl_5-xGb8rt4usMvEhyIMW-_jJubh7rnkVfDSDnrO80AD07BkGLVmu3xLTWZKX9qtBLfBvkApyRax2et9SIS2Hu2P2FcUxaMCrdMP4Ua1YypQaXF2Gz0IJ5ySPR9JvUSWZIHr9n7k5Tkb3qEIov-SWOHupFvamclc5bBWObOvYQC9DzwaoEZrIAC43hnuLlOMwmNmAj39QgyK_MpLMB0cJyt1PVX6VEAE04DD-F_H7cN2dA0nmluClQmjLl8T9XwqvJCahxVTUtEssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5KSIHIg2m8HuyGm0HHss2-HJBDIHAUreb5vw1ogigLVy9V3BuXtFXkCQrpFBtW5OREvJVay7s3DVtlZ3qJ47VWD_YZpDcwwreCshjU91TPZOF_wDuQSmUFQpYJzI9IdH1d7Jpmd7hWKkzx31cbNrxelashmS0gVPhZwbVYXTvFSP0bkUIIZpK8OueDVvo4-vAU3R5dQG1QL6rCVXpqihN17sUY7BloShU-G3yVRai9yBuCct2Jtv3FooVlQTzMZyuj2C4yqvpij1tnCfnsnfUJ3l1vgPsk3q3zB7i7ELpBJge2wScrO8rONyjcKUAzPKfw03kaZulW0ahNhoWIvNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGbBp_JJ16D8oVSaMNhfQt92TygiPUgYHrKaAmSUyap4KQ5brQpP4COeIX4dAxmdBdeagJ8KSlsdbY1Q-06JBI-7FdMWIAMw86hPz7tp55YD_evZ4IX0JOmmri7l7Kw7S8abrTHjGYHaFcv6jJe76c2SRlcIzOZsiX6j_z63XR26tDjFsR81FROPvjlQsiKWJOjdmkwUaM9GVRg1VSUI7RhPuPysQODtYjJJsDcxbfV-zeUMalhVZvJPdPL4lO9hDaL0kD7ze5QLzD1WQ3FKIRdJNdi2nLguI8wGeHqEzqYjSo77wZMAO7A0ljU5jftscMdjL0kgNW9RQEc_0J0U7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KOlWZqBlI2SDZCdJF_IPukU7CtzIGaK1xZ-Vyb6v1dn4hXN7wv_KOVlUuGxpwasmoRaGkbKF_hAWauuCLO0ODl-4Gmdf1pEAla-PnocFaAuwe274kJd-TFZELeb5pBaxqUgmUaWJbzh5WJe2TFNBPyNbZ5yvz43zdnTrAnukChEXPFU7j0Qmt6ds8q5b2dgpmVSdzt_Y11OpPhniOu7HuM7LRhOmbKTnyVb2zGOFtWufskiG2CrIi5Y01jhVUWwgLtqYCPqTkx6xGWdAc3NHxRPLNoX1E9zXPSGBcjAA3jhytY1dxtBKupvdktn9f06nUHbxa5aSthkrDYtENZztkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BAAwDllhcUjP0Reefmv-avk3m1dvBkBjurRc2J6pY-ZRZw32OmsozCkg-31SCnXis12foFkk00i_vZrxV7WOX5Xdv4JSFGQYjkMdP2WyEhiLCOmmHz1SdOmCFsBiWYyBEzd2WCYFYpjFfpFiUZcBqfmLAwl3pXmVPnz7w0PmewanSTRvOQT49KFA8NVrIdfJhXlwe8W2mt4BbxEiNhYZ9ZXwBL9AjUhxJbH23xtx1Cm2cYiQKzXKyodJVfnH6Foag6szLOyJPN0Bjrd7s9kcJNdxTfLKkozX6aO4H_NCrjPLtAUZARL44qIpkB_8t4nMub4X-x6qiFa-ab9hlxUeiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a2hOm_fAVflPmbXxouOXfooWDcH26GIKafCPZJO0TKH0w_mqoZ9hCGLZZV1PD452Qrg80w06uhzmE5zQ3UdfymPIiWGyxyaGRWT1Lafq_VCUrSlhZ4wdqsxkSSyHuFFfeCX5eUmHGG_hp239QDmrtMzOTYco6M2_qjPbAr-rTZmokhGEEe1wWHBF5d9EIJHMIRugNszSyJ9rTbannhajlu7U9gl_dhs8uYNiaL4ufO6P7oWy5lruqp7lR2VWVdTBy1erFmIqdAVVIdtyrfJuf1smWwW5HDR1r83MImufE0DQITD5BBfe-FflVyCCfJ2bOgleNSU241HPoA2Gz0PfTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GfmXrUtAbm_0sIjogqZPbOtaWmkVHQGidkTGG6kwZFt8bxsrD0MkDabZGMmUvVCYEC3D0CNcsUph078TObm393cTG334jUa_JtdU2W1XYVYmCjOC43rj3rtVvQFCZCOsMOWdnzNzPNEtz2UH9nvr2m52hS7A9_FUY8o1U0AGnwkfjztBuOmfNW_ar-Zr5CiB-6xNQdv-AS2FbqvRfC4XFkoUVnVI2wgemxCilyk4-ujnvr5A-oUMyhZPhpXRj-nScnwd3cCUoQScdjbSoBvPuCX3sgYb4mR-25skj7f6bXGeYJfjW-Pwij1-R2WLoLQkAv8eSI22q1IzC9SxX5bxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dECq6FYD4g4mautWOPw55ZOYsHQ294_FQaEMGZ9bOE0FFz5qfRVampeTlxFvFSYOA4nCf5mhMqlwYJMjgTzSp7MbZPcM_Le78NcE3WphzqMtxJ7vXyzY_O8orIJCJvYOLt7yciklb6jehb8OAc_wYH7M6gZyYQWEtbbYvasGa5TATQkBKY5c-SGp62-6rpAFSkEmy9os83JhxIqeiHhJrj-6Xg5TAV9-2YTHQmYXc7gX_XUkcE1v_ZOhYcaeIwAkqK6yrZOxd8l9yraWoqJO7aAIPr9PWsXnaJoo1xqSNxn7nmgg-0O4ddONnD5zHWXWHQlwxA2yF2R01GDftzHYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QW0oEkZZ0ujgPYtqoZm16PZjdXBhdv18jBXSZSrSedRcatwVtplcOpLHUMutsyFYOK2jau7cMlRKPfCQRm09iGsCcy32HutFC_QlKX_6i-xesHmu50RSM6vAR2ooedyX0l5uMRHcf87cKTaJtT5gYSe63poMJ6tpl5g0p93zQmDTffuZBABZuRxbBoni_Ocv4BYf68Dn_Uy7ncFMMqt9_2U7pyO8yN8g_4kkxMPdKzol17Z3PCxt6sqp7UBfrlXGOohL9BgSnBeunTPn0CrN3Jb12qwHwDI0WEnrEgYj8wh7-K4RSuvG0hwDvHRDXARWXc7Okua5LUuf62-edT--5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YwwidApJhXUdUcVfAIsdSLCUxHBPwY6oX5K4xEF9nlGH6zaaDwKLTQ6O8ac1As_xh_x9N-Qhz_nd6qvVi-L_C8igl1EMIfKdD9JAG70wTHym_yqFA01ByiZkz3aTRWRY_VF1AMLyQjs9HGnCeG4brc6MkCNkcwjp437QNJuNcn8WALjEVdOEE0pBiJX0SMK026EwB4TfdhpA-eR8_c-Xkov9fBAgIk1wg815BI12YpoY3gETv8mLVNuu8CCqMRwYiw_wlovKQGXluG1zdwMDec56OdV4ZKjWArjO64OJ6jwHeWCKJqL1WFJBk4-mSbjjn0lcX8UXx2C6HUe-pJGa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXSteKzgXWUWC0GCjyqJsgQYiX_gw5cFum9sD0Ow_UAeP1tshshDi7LDtEco-zyACds3TQY2jSV1bY6vqGaWIuuHjRCxAQqV3w0B3gRZgQ9lfaXO1xBLw-MP7CqB3FJY8LNxX5WcgSyIUheeVOnbhuw1iuZg439YJm1O2JTcax4dE5pe0QFDSZFn7JsTnou6KM_bpulho9w148vZvvKIiJ4SCF4S_4tUApHD332lpasM8nlEumRMC_jnhqSm-9ezJ-YcOAQrTMzSxHcVNHfI-zAHtsIH0C-qVE3uO2yRbUTkX8OuY1_JCUDHnCCZBGeaqp3FWkvinYM0rCnVbWd1Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/opCOV5Q0A7oN6fS5F611YOXFbeUVDUkjsj0LcrIxsi_YOmvxL8FDDWb43P44lqSSNd1v1dTXsHnfHwgXApK1flvfbQDsnA1Q4OORF0jx-_8crueQUJ_SyYqlWU8X24jHxjybXpwtacLHhv9XQ1onaTGrN34g-aEggvmna13AVfSIR1JzXIzj4Czgk7z59J_u34QWKWYP0x31YVue6oY-XbRE6lER1Wtr-MPXxYkeeko4PjYFhywe2Fe_bR2xDdVFnVJTU4HNjocSxnkvoNTzcaRPSh93-Nz0Y0C3W_mUvXWmjg5HeIhPp460BJZ03OjFFd3iNP8SVN77n1Nxuxn9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XJeFAQQ6DXqSPI4hqIFjL6z3uk8hi2ul79fal1-_pAbmlDcZUDBnw18sC-W3i4XnATyLDxoSEGPabTKPQCqiLEKyezcv0zU2gCNp4R_W6vklsM8r5dTVqA_0z0lyoKSyjI1Q0-yCF635TIYs89Z55cgM2lFgnLs10m_MqaVxgJwU3wYFoj-UMN9Ymzekscg2itNDd9NXvhLyq7GqotNPVV1XAk-50aHhn6eKRUDfDkj4-madpLOanp_Zo7yGVPFBi4cT0jUu-VA6xc44SJhwlnQYgr5n80jKChAM9r1zvzFjPOUCS3vYxt3_U7EEtdoHxYb-GNf9WVhQu127-l_N4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VO_5mdFV8xoYt6C8lJlTyR0giHuny_wYbC4gBtsXi1CKWT92XQ1tChQlW0-YuUh84SSaD5-lZG0O5M4LES8A_VYBPa41iycAWvo6uYb9DXD-wkQTxZIS89p47YNej_hQsk5BE8Vc45VaPs8118ydLwNgWzNyFN-7EoFIbruNvCF8RqjqVTlPRSE2zaCaINrLeJ5SarnpbI27AhXYbEN7g6PStxG23774MHuCc8D5_TmIvvpgelU4YYQZZJmbB6EX9-ZkTIi7AGtQBrIaZfSxuNB4FvjnCW90zTe31seJDmWvP-pyPc3f5LeZhyarRN-cyyXOMDFQcGVzyb-RfWuELQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LIOteldsFg3rk6yW3xWpO7e6LXlaG0nrGz3HKVlxBQEv1PzmVEfnn-X7o0j7FidLyuuPVoxkh5P60FH3t8OKMS-sPhC4HAGY7Gnq1NHFeZwz1eDcyWuJYAgF_Esp6f8Hkyn7XpTNCUaCK2seAlKL9HeXB-klIZdEOS4Kr_on7SNPIdfD1GWRXT8MOrsNLvB0ihcM65C0kSQyl6stsbAKwQxiw90GCV4auGIyTU1R-acbtHtPEBMKgjenGWKyFipEJ6n5H4mcyzGrSWBNCec62zbe65kLJPqWKNv8o5X9g7iskbwD2SV-Jlz7pZez-UHn7leIGSIgBryI2h5Xety9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fqOQ2tdOHCCEqn6DRcrjqNhDroDSeJY_zR6M6Au7fryWDMauVjAC6JUyjlva0xOdOK6A6A6QKhcmBp9nF-tW7w4rywpvNVcVjmHYjws2ez9a7Yr6VKavk9trr4FsuSoUsZl6JdqJ8uTg6IYR_lW5lZr2x4-sELax5lkL2gEVhiEe-qoSd6iZjA0GpZdYHbQ7vf5yc7iQQSVPnuWT1MDkd9aL4reSJP6H7Pi-iE7Z9ZE3S1_jiLs19mUQ7BuMpKw2PSqdQ5iCH0o58RMcorN3qJv9NT6E6D_8MUHA1ANk0M91wJqsUK0N5TETXwY2H8YU2bsIzUH7zNuHVkOadqby-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onM2cFMBOGN7X4EpIIygZWvujjA-LTB-xiiAXDmjy7dEY_Zk7Wrq-UpwHW-mZumK2S5335vTEPCJqLWf2d4li-c1p9XaB9F33LxjaUPiI_vAwoVWAN1kNIzh9D-bnJbHZEi4CI6eF-jm9EgzCdscdgUSFQMQwd7GXgJPRC3XXTUotPSGdMnB_tH8_RZO5flPHxhObHEifE3J4iak7oE7WF9T02PsS5jbi6XAJSJnmV6dCpkCihbMsbRluO47uHuUnz3UFKIoJJ0D6gV8LfoiI1-JgUhruVIJt3bL0p25KHyBYyPbmXoGlbae4iP6cyDhLeziFHvqcFBQbEFeMtCWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
