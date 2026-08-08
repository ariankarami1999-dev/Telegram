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
<img src="https://cdn4.telesco.pe/file/ICYkaumb8w3_U9X_1qVn2OL3pTmz1zkZx3yjQpajsGh2V2MwqnDbwr1eOvGQw3b-uEGXmtFekQCnfLIBfG48f0T1LVpI8Iz4PhUDDuQCKQlzUqiv33JODV_T4-Ur9TWhv_o4hm-jymhdUgKc1qcqrqUZYR4XsMLolhWrU-9PeB9ChQE6CIQ6ix1yHD0sl-Bllq1wNn2xP5jWQBduQyf0JyZD1jr255aqS9XVbxy4EkGAchxICSaigUM7CneSObeYoaqByeQvZ5DvN438nH3Q-bTKySqCA_pMa-hOohjINJjokuzEO2WCaeQwcWMp3FsadFhcinR4UhhmMGour3QZ4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 14:27:45</div>
<hr>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…  https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u  بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/20676" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آغاز ساخت پناهگاه در پایتخت
معاون شهردار تهران:چندین مرکز را در سطح شهر تهران برای ساخت پناهگاه پیش برده‌ایم و کار اجرایی آنها آغاز شده است.امیدواریم در نیمه دوم امسال بتوانیم چند پناهگاه را به بهره‌برداری برسانیم.اقدامات احداث «پناهگاه و پارکینگ ـ پناهگاه» به تصویب رسیده و اقدامات اجرایی آن آغاز شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/20675" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری آمریکا شد
سنای آمریکا پس از چهار ماه و چهار روز از برکناری وزیر دادگستری، با ۵۰ رأی موافق و ۴۹ رأی مخالف تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تأیید کرد.
بلانش پیش‌تر وکیل ترامپ و از اعضای تیم حقوقی او در پرونده پرداخت حق‌السکوت به «استورمی دنیلز» بود.
@WarRoom</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/20674" target="_blank">📅 13:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پزشکیان برای وادار کردن خامنه‌ای به ملاقات فوری با او تهدید به استعفا کرد.
"وضعیت اقتصادی ایران غیرقابل تحمل است"
پزشکیان می‌خواهد برای خامنه‌ای روشن کند که پریشانی اقتصادی کشور به نقطه بحرانی رسیده است، تا جایی که دستیابی به یک توافق سیاسی و رفع فشار اقتصادی به یک نیاز فوری تبدیل شده است که نمی‌توان آن را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/20673" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ_qLo1Fmkpj7btG6ziY70fGpKHWSP8JRhE71_IvvOhGEPitEh4Yd_ZFDAFpQQmruMpTVd0gXY_6B4XOtbz14wLYCW9JDth-kQR-TTJy9_4upp6A5eNwCPlmYls41_QtPD5EtJIPS9irhR46m2I5rx0RI1CqCUNmzSCWGfF5eyUxATRcAbz3KgMzmKOkLcWt_pf_eAER2AO-4ycC6VikJjRvHm2hZYCXsCZ1VaUXayIvYYYE40HHI7XkENoLv7jcJG1eUvEvEuRR61Fn2qm-ZXN3pIE1hN3U0mOBCt5pa_wdTR1shzvYeR3EsDHLvs290QvobkNZ5t2HTX6WXySxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن.
علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده.
دقایقی پیش خبرگزاری‌های‌رژیم خبر کشته شدن این فرد رو تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/20672" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20671" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=PjLoN-xbc5OWNG3UEaQccs5LQ2PMkKMpKPXME66zWuSDjrhHJ5--m2oi_oepFeSZAH46bt5AwggxkAO2uW2JTTq4CAZirQ7i2OUIju4ACAGO9VCA852UZxghg0ZZcKgK_9MTSMQQ5XFppT0YDE7cgfWElDNpE0fhXSxQpk3ytOO0Nwv4InaPQ0dTnlLycOrmPEXAQdPL8-t8o543YVyR_KLmSLI96jtvdme2xiGPtBhEPP8l0JEb9TSOQZL_OTikQyk-bY4OAay5fJ_rNBg5cZFWhqF5xlhGBDbIUWQf4s2ddv93XUrIuIVG7mzkbfgZ3vf1XtYpYBMtbxyxhgYmwii-1Da7ABHVhRT8WxJ5_L-iiugJ50p87B7dj_g9dvTFzQ8KCVIx8aKyfk5vq6ZSJVMecbjHypAAIls73TH1M0OUOw-4bIkohl1InqiRyAAuqnE3wbgfrjRwtpZf9zMMV3m9Z2Rszms1tD5Um35AWHksnWXyrfOFUhU3lxMG1FTK8JfEGlqwoaVQ1y8r-9YGhUn0x4k-81NEwpeb13cpHP58NZcoKHNvfzEe7EaTMpPC6_4Zga9J4vLHhjTOA2uJPgGvwb3RLfYh7ZSD8iLc4va2zDt3So7cU_D2hOGyH6AdCSmLwUnZWSV4wo2HROvVUW9Ffn0ZpyvopHOXfz4QzwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=PjLoN-xbc5OWNG3UEaQccs5LQ2PMkKMpKPXME66zWuSDjrhHJ5--m2oi_oepFeSZAH46bt5AwggxkAO2uW2JTTq4CAZirQ7i2OUIju4ACAGO9VCA852UZxghg0ZZcKgK_9MTSMQQ5XFppT0YDE7cgfWElDNpE0fhXSxQpk3ytOO0Nwv4InaPQ0dTnlLycOrmPEXAQdPL8-t8o543YVyR_KLmSLI96jtvdme2xiGPtBhEPP8l0JEb9TSOQZL_OTikQyk-bY4OAay5fJ_rNBg5cZFWhqF5xlhGBDbIUWQf4s2ddv93XUrIuIVG7mzkbfgZ3vf1XtYpYBMtbxyxhgYmwii-1Da7ABHVhRT8WxJ5_L-iiugJ50p87B7dj_g9dvTFzQ8KCVIx8aKyfk5vq6ZSJVMecbjHypAAIls73TH1M0OUOw-4bIkohl1InqiRyAAuqnE3wbgfrjRwtpZf9zMMV3m9Z2Rszms1tD5Um35AWHksnWXyrfOFUhU3lxMG1FTK8JfEGlqwoaVQ1y8r-9YGhUn0x4k-81NEwpeb13cpHP58NZcoKHNvfzEe7EaTMpPC6_4Zga9J4vLHhjTOA2uJPgGvwb3RLfYh7ZSD8iLc4va2zDt3So7cU_D2hOGyH6AdCSmLwUnZWSV4wo2HROvVUW9Ffn0ZpyvopHOXfz4QzwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ویژه آژیر خطر از فاکس نیوز: سربازان آمریکایی در جنگلهای بنگلادش تمرین آمادگی می کنند, حکومت ایران یا توافق را میپذیرد یا بمباران میشود. آیت الله گی قدرت پدرش را ندارد و اختلافات بالا گرفته… و عناوین دیگر که در این ویدیو خواهید دید
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20670" target="_blank">📅 10:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_lMa26bD4T0Xi2Rg8O3F9Ms71f5GPjM0MOT9ws_NvnviqpgwFkd0yaE367rXC_IOvaPEl4rfJTpOfgFWywI3RN2utTX4oyRpgyhGRUMG49mIKooRKAS6Nv11x7TV7MliLf3XwZv5fziVmByHWngF9BtZC0n1fPH6FuToxUA1W2bc8cWj7-gZOmVi1q0tuvdw9XXe0jtSL7yN8cSvErCwnmCowojvP4mgekT2xsKmQ_6X19RHr7vez3DOIN4-Ir0DUQcv5X28JTwgfM_ygaY9cZILjhIU88VGoj_nMrymOHS1jJkwPJKz_52ie8OpZ41e_1dQHjDlhAy2v0hNZQ3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن روحانی توی خونه خودش یک هیئت دولت خونگی ساخته با هم جلسه تشکیل میدن و خاله بازی میکنند!
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20669" target="_blank">📅 09:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20668">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سفر مکه
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20668" target="_blank">📅 02:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_NwC_fpokjrb0mAPF0VevU0jQLK5bQLqQPXlLU7OwMP3-a9fT9JnfC8dZLTKg52H2iPN41o_KEov4boAbDiHGuKt7ggkzGhG7s09Bgq8mBL4RgKKcrnA82p97VYqDFK6z3ci_QJtc149NBCGb2jpnegvtsDWpMBH7A6UDFahdcByWc3bQezecjbuFUbfZWhnhQWqoWTyPSv3CL9sGCOYZyFe-s2BAFS_zwFhC_Wwvr6OCLUfJY3whY4YHMt0uqU4HCfourMsz5Q-AQ11EkArGVmALxCoZ1r-2CAkha1m2nEzmO7zJkntgV-_hVijXuD4KiELn9-yeMEiOctwMjHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین به ترامپ : کلکشون رو بکن
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20667" target="_blank">📅 01:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20666" target="_blank">📅 00:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی خیلی آدم حسابی هستی عمرت طولانی تنت سالم بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20665" target="_blank">📅 00:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی
خیلی آدم حسابی هستی
عمرت طولانی
تنت سالم
بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20664" target="_blank">📅 00:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d253696.mp4?token=kjwYTJ4pZeMblEV-AiIA1rNk57Kj7M_74mP-SJgUZjmMT4LM5WMKyayIs0KVV-OqUNMhnzLEntDCOIhGlUHyYjhxd74THmziMlsOzMfmkSj8CC7MZ6sABoJpnY_06X7S9gTYBCnSuTuk6QwTsHXg6M15BHZ2fheuEC0PjQfBr58j9G5u38v_rbkLhQ5V_vQZ1MbkvZWah3QjEjCBj2GlHz44ODu9jGPlUoC8Mpq171zxoboJTgPtLMV6lJJeFSE6w2oYju7E37kWfpjSrk3SL1YnN9OdXs-NdwzKY1lHPSNB6GNuyxwmQ-mI_HKpXItB2dVHWbtOV74MeyH1cKNAAaRZqFRlGjVgOFWpgU3rH5Gpbe0sRONm2srWX9CJhw-jIWzjYWIvqPU0av_o6O9jyikpdP5VMf8HWCfceb6rqEjucN_AkYRarsjHIy4hPNjciGArbouWm4AlY4gyCttMIoWcJnWv64pki9T_9kFBcTDDSbOkonmT8ass_uiH0wonVEwmWTZcnyRkOAHfAa0QKX-5eXd8AleQRSSUEJ-8NWJwmyq0fd_B2hRu7riX6tFwr7T-hT5dbk67MkSDIHB0AkUpYpt7SIO3IKjNdB5kolPHSq7Qjce9if0g_cSSq7C3LlDew9OteJkW9ujwsAn8Rxj4z6_Ub1UqWsWe2GdvviE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d253696.mp4?token=kjwYTJ4pZeMblEV-AiIA1rNk57Kj7M_74mP-SJgUZjmMT4LM5WMKyayIs0KVV-OqUNMhnzLEntDCOIhGlUHyYjhxd74THmziMlsOzMfmkSj8CC7MZ6sABoJpnY_06X7S9gTYBCnSuTuk6QwTsHXg6M15BHZ2fheuEC0PjQfBr58j9G5u38v_rbkLhQ5V_vQZ1MbkvZWah3QjEjCBj2GlHz44ODu9jGPlUoC8Mpq171zxoboJTgPtLMV6lJJeFSE6w2oYju7E37kWfpjSrk3SL1YnN9OdXs-NdwzKY1lHPSNB6GNuyxwmQ-mI_HKpXItB2dVHWbtOV74MeyH1cKNAAaRZqFRlGjVgOFWpgU3rH5Gpbe0sRONm2srWX9CJhw-jIWzjYWIvqPU0av_o6O9jyikpdP5VMf8HWCfceb6rqEjucN_AkYRarsjHIy4hPNjciGArbouWm4AlY4gyCttMIoWcJnWv64pki9T_9kFBcTDDSbOkonmT8ass_uiH0wonVEwmWTZcnyRkOAHfAa0QKX-5eXd8AleQRSSUEJ-8NWJwmyq0fd_B2hRu7riX6tFwr7T-hT5dbk67MkSDIHB0AkUpYpt7SIO3IKjNdB5kolPHSq7Qjce9if0g_cSSq7C3LlDew9OteJkW9ujwsAn8Rxj4z6_Ub1UqWsWe2GdvviE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت قرمز ۱۱ سوخترسان و ۱ آواکس در منطقه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20663" target="_blank">📅 00:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaD2nWJrulayaM38krW5X-OI37FGTCgzgjRlsT7wrAxBu1dIZPKm73Ou-OTppjPfkD89oeI5ocyB8L5-e61HAL5s9LsjSX_PYzl5dd5OJ1MkwrofTP1pCTDQ-Czx3Vz98rBT8x2PdYcCYraq-579OulqAbuTIH62bLqrXxNo1h5y329znTbgz0qouEOhaKwf0Ysbt-sHfZbrc62VjXKQTc6f3X41MUE7fOCxGvf-4vnKsCg1QGYx7KWZRlk1K6HfhJxSXtZC3S2CK9jst1lj8c_VcAiUGXSdP0-wDB0JH9t0KJCNdS8uNI6_kYYrbDk6zS5CD5WDpp5Jsk5Vn5qydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…
https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u
بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20662" target="_blank">📅 00:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:پیروز جنگ غنائم میبره، منم غنائم  ایران عزیزو میبرم
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20661" target="_blank">📅 23:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=hGbZ5D2NQ4G4OYMGMh525o5LAPmhgVSO2u1ZnsSbnrQwLasXpRmLOFntumO2WnNVQzXndUii1_6wxm5iD4iKY1L2QrvbKoXByjRnFYvvsX_qmSTDUUkeVP4Zq8Ol2IB5T32F3_Xr5tG47bJz7DL_1a10MWbU04eab1DQStUcMOjqgu7AisOHjE1tDOKi3PgepMzCmXhnmQm9EHPOyr7QpjUw4YyfA4ct1YwLdNpLH9XBeVOaAbyy_mP3fvRxJCk5xmMhoEPyFw2RGZSXrfCCNAKNwsqm7aULMem1B4k_6rlnVc2ZJDq5c9SSSdYWRXq0FtG07W0mp-GCG2TZvaYVew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=hGbZ5D2NQ4G4OYMGMh525o5LAPmhgVSO2u1ZnsSbnrQwLasXpRmLOFntumO2WnNVQzXndUii1_6wxm5iD4iKY1L2QrvbKoXByjRnFYvvsX_qmSTDUUkeVP4Zq8Ol2IB5T32F3_Xr5tG47bJz7DL_1a10MWbU04eab1DQStUcMOjqgu7AisOHjE1tDOKi3PgepMzCmXhnmQm9EHPOyr7QpjUw4YyfA4ct1YwLdNpLH9XBeVOaAbyy_mP3fvRxJCk5xmMhoEPyFw2RGZSXrfCCNAKNwsqm7aULMem1B4k_6rlnVc2ZJDq5c9SSSdYWRXq0FtG07W0mp-GCG2TZvaYVew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به خبرنگاران و حاضران : اگر امکان داشته باشد، اگر بتوانید به سرعت از اینجا خارج شوید، من سپاسگزار خواهم بود، زیرا ما یک جنگ داریم که باید آن را به پایان برسانیم. این دلیل من برای خروج کمی زودتر است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20660" target="_blank">📅 22:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓮𝓡𝓦𝓲𝓷🦅</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaeEhMo2nFHkzZ7HuVa0uShQT1KXZqDawQhP1kGAh9Ph69fdb-nJI5L5aq_neR_SBK6uWt8iAygf1NSTWO6wcbJwCUoyRv1QIqo-uxf20fh_o3FPAu2-Ns0_aG_7m6PKdTmOTefwxbDO7C_F52s97FQ8DjY3vuJuFem08g5isNKNvsVnQ7tb-1SRDCVm5AZ7eh3Kd8OGmape7wWVvzDBAPqT8DB700QF3tjvE-e67R6My43djZin1-Mb1qPTcnKWpE3W55MAxmVLb9wVUimLQE-PXdcem9euCDkS_oJqBioMRAgn_X9pR3Rp4CeFW9ybezKm-eo0LaSZG_et7_D5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20659" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq57LsozvNL-RlHI__-KX76fFapqE65OSYZnxXiJqvg5Tt_mDaH9ruAjkmnoNEMIYwUtRdp12rfXyASPvNCmMQ5gxD59ic5kzQdRUUfqQR0GA4DI-bX4Qqg2bwT9x1TX8NPLR2UbRY5zm1pdpdI2HKTwHIx27cjnhQLrSmcZaSYdQxAeiBS3xAJi1eRu2a3i5BMQzwE3x77LebhkqVFomoGh5KSILDYNMsBcglRuOUmpNT_yg6P2up-njdU0cBiGPZHK8i-DC9h1o2_L4gkt1jShN9fWWHG9JJ9AsvjiLXvY11NbN04lI8U-eFEzggnrlHhpPg2coHN1837hEpkiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20658" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه آمریکایی WIRED گزارش داده است که پنتاگون در آستانه امضای قراردادی چندصد میلیون‌دلاری با شرکت AeroVironment برای خرید حداکثر ۲۰ سامانه لیزری ضدپهپاد قرار دارد؛ رقم حدود ۴۰۰ میلیون دلار ولی هنوز رسماً تأیید نشده است. سلاح اصلی این برنامه E‑HEL(لیزر پرانرژی پایدار؛ سامانه‌ای برای سوزاندن و ازکارانداختن پهپادها با پرتو لیزر) است که برای انهدام پهپادهای کوچک، پهپادهای انتحاری و اهداف پرنده گروه‌های ۱ تا ۳ (رده‌بندی ارتش آمریکا بر اساس اندازه، وزن و برد پهپادها) طراحی شده است. نسخه پیشنهادی آن بر پایه سامانه LOCUST(سلاح لیزری متحرک برای مقابله با پهپادها) توسعه می‌یابد و روی خودروهای ISV(خودروی سبک تاکتیکی برای جابه‌جایی نیروهای پیاده) و JLTV (خودروی زرهی سبک چندمنظوره برای عملیات نظامی) نصب خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20657" target="_blank">📅 22:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز: ایالات متحده به فروش ۵۲۵۰ موشک دفاعی به بحرین، کویت، قطر و امارات متحده عربی موافقت داد.
این اقدام با هدف جبران کاهش ذخایر موشکی سیستم پاتریوت این کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20656" target="_blank">📅 21:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20655" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اتاق جنگ با یاشار : صدای گشت زنی جنگنده های جمهوری اسلامی در آسمان بندرعباس هم زمان با افزایش حضور سوخترسان ها و متقابلأ جنگنده های رادارگریز آمریکایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20654" target="_blank">📅 21:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شبکه CBS :  مجلس سنای آمریکا به طرح قانونی درباره تحریم‌های روسیه و ایران رای مثبت داد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20653" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20652" target="_blank">📅 21:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20651" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">امشب بیدار بمون</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20650" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">داداش دعا نویسم گفت امشب جنگ خواهد شد</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20649" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbY0ECV0-PuvXFsfKxwe6VbYntU78-rrUlm9IY04XeSi0M8IePLjVdwH3KetXbSoRM5JWu4dcW6Gg87BP8HYFSXDHbfyMsRgTtQaShPpmIrFbFbKVcee_bAhibYMMa6La5N0sw7b-AAOj0VJ4pfambIsuPSHDOtEZp84dIeF1zRutsSOpwB4dO_VwljdXBx01xA6NVxYUGu22vvNW7bMMi73WcnqDhBkhubS73Dzf-8GpqXuavavHezClMdzSVZIjPELcava0YA6PDqCbTBX5bWnJvfrHa850-uFbqM2zO-uNh_-FnPtPWmK65mR3PHoDDbkjTJF7PKg0J8EavNJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20648" target="_blank">📅 20:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C93oQX6ZpW9Kt7XqQGTsUNGJ6yVQIdHcR6NgddLM0t9IojY5yfKEobTIAPS7ft7LdGJS7UO7q_dQHOtxbA2GkxHOlzJoHAGElKDgT4AkLiFT14OIZx7T3d1MAOChiMaSC29jQaSMN7SBshd4CMLoYHTx4WqU5E9TawEnfGikCsn1cc9nuC2kLi26iOLyWJRqJ0uDZpidoy5IqyO0LJ4mxbruwDea-DVh4XtIhL4tGuOYUB5rW0QnlyxGrQ1Tj9rsH94wCiNP8h2Z1LfLKlT0Nfb6f1navS-VuZeziH3SO82bdfigcQ7WqBx0FEmvG5pWZ7AEdbay8Y4KKOrXvDQ9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : خدمه پروازی یک فروند هواپیمای سوخت‌رسان KC-135 نیروی هوایی ایالات متحده، در حال سوخت‌گیری یک فروند جنگنده رادارگریز F-35A در آسمان خاورمیانه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20647" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20646" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارت دفاع آمریکا پنجمین مجموعه از پرونده‌های مربوط به پدیده‌های ناشناس هوایی و بشقاب پرنده ها رو منتشر کرد در همین راستا شبکه خبری CBS دقایقی‌پیش مصاحبه انجام داده با «آوی لوئب» که ترامپ او را مأمور و نماینده تحقیق بر روی این پروژه کرده، از دست ندید.با زیرنویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20645" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سناتور جمهوری‌خواه تد کروز، درباره جمهوری اسلامی : اگر شما یک اسلام‌گرا هستید که از آمریکا متنفر است و سعی دارد ما را بکشد، من از اینکه شما یک کشور یا ملت را رهبری کنید و منابع لازم برای کشتن آمریکایی‌ها را داشته باشید حمایت نمی‌کنم؛ این جایی است که ما باید بر آن تمرکز کنیم؛ حال، چگونه فروپاشی حکومت را رقم بزنیم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20644" target="_blank">📅 18:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=uz1gRiTWTe8W49p2V9Pop51y4zMJLwXIgQ2_227ckRyoq-Mgme2Ru0XPS7kPpRnkfFF7_vie6D2KxQyzYlI21V3DM2JTNMGmkvevAFXYePYd7jtoePFbwkB_7y_s9K86GXaVm6Mr_kB8WZBQ--__H2Xv3dFzdff1hYvZwXSLSu45sC5xN1MHFpTLpEczF-oSpijnvPbSjHLfIk8K7S9oMMwpSAixkFPMlTj9e0QzMJyQzZoL7fYqeStOinTW7DXQ3wiSd0jFQ4HLILjZfLybgBXu2AtCa7hO6vYap3zEOkgZDxJ0j58bgIS0XyvUj8WCx9tTl3CvQYY4Kz8hhr4MUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=uz1gRiTWTe8W49p2V9Pop51y4zMJLwXIgQ2_227ckRyoq-Mgme2Ru0XPS7kPpRnkfFF7_vie6D2KxQyzYlI21V3DM2JTNMGmkvevAFXYePYd7jtoePFbwkB_7y_s9K86GXaVm6Mr_kB8WZBQ--__H2Xv3dFzdff1hYvZwXSLSu45sC5xN1MHFpTLpEczF-oSpijnvPbSjHLfIk8K7S9oMMwpSAixkFPMlTj9e0QzMJyQzZoL7fYqeStOinTW7DXQ3wiSd0jFQ4HLILjZfLybgBXu2AtCa7hO6vYap3zEOkgZDxJ0j58bgIS0XyvUj8WCx9tTl3CvQYY4Kz8hhr4MUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شهباز شریف، نخست وزیر، محمد بن سلمان بن عبدالعزیز آل سعود، ولیعهد و نخست وزیر عربستان سعودی و رجب طیب اردوغان، رئیس جمهور ترکیه نماز جمعه را در قصر الصفا اقامه کردند. در این مراسم، محمد اسحاق دار، معاون نخست وزیر و وزیر امور خارجه، سناتور محمد اسحاق دار، فرمانده ارتش و رئیس نیروهای دفاعی، سپهبد سید عاصم منیر، و مقامات ارشد سعودی و ترکیه نیز حضور داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20643" target="_blank">📅 18:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp1K2WJaJc2K6QhSbrNNL6gNLmn9mJM0-AODeIciwjQxsjawfQqooRBoLR3j2Kc0QIb_JVyX8mpBa6Okb5jd3urfT_sUlKxmmwQi6rAP_XzsjU5xl507TrGdw68F1UidRpSMg4X01iM7W1Po7ER26UlqUMsHoJoQO017eFYbmxOGOTZV2BlrovslMAldimKcHIm-6oMR4I70yHU2puSV16HJBUrSge98aJT3jBan8RVn6kXRLS6wGuzXiTK2s50vi8jhOJxt84VAoh3UGqBisGgisIV_lp1oQ_rB3vJTL-ZKutgIcEljL8XCvee-TayfuV6zZToeGrkONpQ995znoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20642" target="_blank">📅 18:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شبکه کان اسرائیل: ایران صدها موشک پدافندی دوش‌پرتاب از روسیه و چین دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20641" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20640" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20639">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRVFLQt_CfoOizKhzyx9128GLUV0NWnodM_xYdFL0KRVtmJfHsVs9hJDZbgV21kcuQYFz2E5F0Glh4l50TVDge_sE2-369P7blQwLa0ZV2XrrmaON1WCXMe0gbI2Pk78c7DHbgIc4uIbRbveLzBnogJ-sPFAXbViQwooEtuI5aeVlABBM4zLdc0E_CAzOZU81bOa9hWDcN_YA5icjh9X6wNTMVxfMJ-8tmH8pXVvEgBzIeUW-ygQjgtYoA0iMPod-otS6VN3ta5veZkkH_R8HAJRfP1PSocv-wRd4va8onCjCRY6Spp4SvXfT3fqIij7lsKUbQVKBY859WrYwXrDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.  متن عکس : ترامپ در جنگ ایران پیروز شد پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش…</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20639" target="_blank">📅 17:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏نیویورک تایمز: برنامه هسته‌ای رژیم کند شده اما متوقف نشده است
‏ بازرسان سازمان ملل برآورد می‌کنند رژیم همچنان ذخیره‌ای از اورانیوم نزدیک به درجه تسلیحاتی در اختیار دارد که برای ساخت سریع ۹ تا ۱۰ بمب هسته‌ای کافی است. داریل کیمبال، مدیر انجمن کنترل تسلیحات، گفت سیاست فشار حداکثری و اقدامات نظامی دولت پرزیدنت ترامپ نتوانسته توانمندی هسته‌ای رژیم را از میان ببرد. الی گرانمایه نیز هشدار داد در نبود نظارت بین‌المللی، رژیم می‌تواند ذخایر فعلی اورانیوم خود را به سرعت تا سطح مورد نیاز برای ساخت سلاح هسته‌ای غنی‌سازی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20638" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینستاگرام رو  هر روز میززند و باز‌میکنم دیگه اعلام نمیکنم حتی ! الان برگشته
🤣
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20637" target="_blank">📅 17:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqOimgFFW4nMz8tJbDOn_fqrX4n6vaUcKs9RPSbfdsPM5PIa7hLMiY-aZ06TKfgs6xmDojXrHTz8hsC9FgORfK9sv2w4EOM67vGhswgWwTppFum6YqanhEvzpVXn7JTaIS-hhH1Hkg3Nepsz1ehsxhbaMM-ubvv-xQtE8U39_arOT7_fhuTxOEcGmRIoA-Q4DkC6rRfhTv3qxKzh9McZDYurCSYJgI5rNVQ0peges2g5Vj8nCqRTGDSMeMywWd6DFhwB-u7-RcKMpw8rPaAk_zrArNjIvlszF7rtYoZ6SgMVsw6SUvnnhBvLDOGeQkIxh0l4Cb9VJOkpLeo_R1dCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.
متن عکس : ترامپ در جنگ ایران پیروز شد
پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش صحبت کنند.اگر ترامپ در این جنگ در حال شکست بود، هیچ‌یک از این ابتکارها و تحولات در حال وقوع نبود. آنچه امروز شاهدش هستیم، افزایش نفوذ آمریکا، گسترش مشارکت‌های منطقه‌ای و شتاب گرفتن روندی است که ترامپ برای برقراری صلح و ثبات بلندمدت در خاورمیانه در نظر دارد. این‌ها نشانه‌های شکست نیست، بلکه نشانه‌های دگرگونی منطقه در مقیاسی بی‌سابقه هستند.
رسانه‌ها و تحلیلگران می‌توانند هر روایتی که می‌خواهند ارائه دهند، اما تاریخ‌نگاران خواهند نوشت که ترامپ تأثیرگذارترین عامل در بازآرایی خاورمیانه در دوران معاصر بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20636" target="_blank">📅 17:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به گزارش فایننشال تایمز، به دلیل محاصره دریایی آمریکا، حداقل یک هفته است که هیچ نفتکشی در جزیره خارک، پایانه اصلی صادرات نفت ایران، بارگیری نکرده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20635" target="_blank">📅 16:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شبکه الجزیره گزارش داد نشست لبنان و اسرائیل با میانجی‌گری آمریکا در رم بدون هیچ پیشرفت ملموسی پایان یافت. اسرائیل با پیشنهاد عقب‌نشینی مرحله‌ای از جنوب لبنان مخالفت کرد و تأکید کرد تا زمانی که سازوکار قابل‌اعتمادی برای خلع سلاح و راستی‌آزمایی حزب‌الله ایجاد نشود، با خروج بیشتر نیروهایش موافقت نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20634" target="_blank">📅 14:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">«توافقنامه دفاعی مکه» رسما امضا شد : هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام تجاوزکارانه است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20633" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=LsJH-2aPiUe6ZtnplAShIhCtT8FH3HG8AMZrVgy2uNvQE7JFECDrebbR1_erDlrZLi0e5tl1Ka5FX_LaqE4U49rJdwmUdBOgRsOh1RMUTobxqfWlXgJYh6I1MVxMqvBzm4fHcO-NEZmovn3nQiWY-I8_F25dvfTYJJ4s-yFt1neB8Tv4-dDRm2Z0UyGK-WgCiG71gssZmc1bA_towGPXi1xnq3Mukm-_hd4YNifdIFvg3Hz0IQOmIL7-HGn2tsN6_YvFpshce_zxnA-B_IJhAjcT0zrWvOH5q-NW5q7aCHJWLeh0WFo1gk1wnKSGFk9x9iAZ3Y0S9QjD1sqPSgv1pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=LsJH-2aPiUe6ZtnplAShIhCtT8FH3HG8AMZrVgy2uNvQE7JFECDrebbR1_erDlrZLi0e5tl1Ka5FX_LaqE4U49rJdwmUdBOgRsOh1RMUTobxqfWlXgJYh6I1MVxMqvBzm4fHcO-NEZmovn3nQiWY-I8_F25dvfTYJJ4s-yFt1neB8Tv4-dDRm2Z0UyGK-WgCiG71gssZmc1bA_towGPXi1xnq3Mukm-_hd4YNifdIFvg3Hz0IQOmIL7-HGn2tsN6_YvFpshce_zxnA-B_IJhAjcT0zrWvOH5q-NW5q7aCHJWLeh0WFo1gk1wnKSGFk9x9iAZ3Y0S9QjD1sqPSgv1pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
: فقط همین را می‌گویم؛ اگر اوضاع به همان سمت برود، آن‌ها این کشور را نابود خواهند کرد.
مجری
:شما دیروز، وقتی درباره نوادا صحبت می‌کردید، گفتید اگر اشتباه نکنم، ممکن است قیمت بنزین دوباره کمی بالا برود، و بعد گفتی…
ترامپ:
نه، نه. این فقط در صورتی است که مجبور شوم یک حمله دیگر انجام بدهم.
مجری:
یعنی…
ترامپ:
قیمت‌ها فقط در صورتی پایین می‌آید که به توافق برسیم. آن‌ها می‌خواهند توافق کنند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20632" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20631" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرات ریخت ؟
😈
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20630" target="_blank">📅 12:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20629" target="_blank">📅 12:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟  نوستراداموس هم نتونست بگه! مانوک : انقلاب تقویم نداره … I LOVE YOU @WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20628" target="_blank">📅 12:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز: نگرانی درباره تنگه هرمز قیمت نفت را افزایش داد
قیمت نفت امروز در پی افزایش نگرانی‌ها درباره شرایط بازگشایی تنگه هرمز بالا رفت؛ زیرا ایران با همکاری عمان پیشنهادهایی برای محدود کردن عبور برخی کشتی‌ها و جریمه ناقضان قوانین مطرح کرده است.
قیمت
نفت برنت
با افزایش
۸۵ سنت (۱.۰۳ درصد)
به
۸۳.۳۴ دلار در هر بشکه
رسید
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20627" target="_blank">📅 11:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=C9QsRd0A__V8Ve4LgPt_rS0jGbaI0TIJhaMMjYueloNkU-KvFonK6ngsjiax0mCl6X8stQ8R9hA-EaAUj2j89Dim_x8p4g6a6Z-X1RR3ln-dT346sQUENiByXiJgIo2bxez-5uzKZDAkKDtEkVrGqClGtN36RNTQuozKJoVEn3F04rP1NS3XkPCZwF5zhNLiRjBIAoK6Kb-_VH3gddxZcRPN5L_rja_Lkn_8N73P4y3TrP-CGFUYoiay2aTprsHO8Mrt0Rp6IKYZ1VH6GEubogPGZFyPfAUHNha1_SS8chjqSIlKe49sbjgU955resZUGs12JRwx74arLja--EgSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=C9QsRd0A__V8Ve4LgPt_rS0jGbaI0TIJhaMMjYueloNkU-KvFonK6ngsjiax0mCl6X8stQ8R9hA-EaAUj2j89Dim_x8p4g6a6Z-X1RR3ln-dT346sQUENiByXiJgIo2bxez-5uzKZDAkKDtEkVrGqClGtN36RNTQuozKJoVEn3F04rP1NS3XkPCZwF5zhNLiRjBIAoK6Kb-_VH3gddxZcRPN5L_rja_Lkn_8N73P4y3TrP-CGFUYoiay2aTprsHO8Mrt0Rp6IKYZ1VH6GEubogPGZFyPfAUHNha1_SS8chjqSIlKe49sbjgU955resZUGs12JRwx74arLja--EgSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟
نوستراداموس هم نتونست بگه!
مانوک : انقلاب تقویم نداره … I LOVE YOU
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20626" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سی‌ان‌بی‌سی : به نظر می‌رسد توافق ترامپ در وضعیت وخیمی قرار دارد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20625" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏خبرگزاری آناتولی به نقل از منابع امنیتی گزارش داد رجب طیب اردوغان، رییس‌جمهوری ترکیه، برای سفری یک‌روزه راهی عربستان سعودی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20624" target="_blank">📅 10:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbYISUOz2X0Gm6E0MbNhusEb0YWnNFf3s1fJubyy9UNwRCWvKpai9aDPfunVWzG9ArzpYh6EpMNHxtoadZFY_J7piHah_qUopuDmrNwOj5l1zNvSW9IOhK5qB1ElkvHretechyXetQHKuW5hyqK-16PKmmn1dI8-eBp8co2Vfcfky6GhUS8R5h611vqAhqGBSCEgZkio0rJcbg8f7y8-HD08MLSmWvYHzDrfJ_s7iXrPD0af2ufrQOiGv9UE4fcVM0uFjOl7HSH3LZZxJ09UMi-ZaoYi995rd0sHG7evZWmifD5na0J07reqoX_lj95b5BcVlZueGWqz349qoFw0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏لکه های در تصویر منابع نفت و گاز در دریای کاسپین , طبق تقسیم‌بندی جدید بیشتر این منابع به کشورهای دیگه واگذار میشه
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20623" target="_blank">📅 10:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پس از آنکه وزارت حمل‌ونقل اسرائیل پارک کردن تعداد بیشتری از هواپیماهای سوخت‌رسان آمریکا در فرودگاه بن‌گوریون را ممنوع کرد، به آمریکا اعلام شد که هواپیماها باید در پایگاه‌های نظامی نیروی هوایی اسرائیل مستقر شوند، نه در فرودگاه غیرنظامی بن‌گوریون.شبکه i24News…</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20622" target="_blank">📅 09:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">instagram.com/Yashar – Ruhollah zam and Msoud Molavi @WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20621" target="_blank">📅 09:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=IHAWUtQrlgvOsDkM3dF3Zjz46VamPQOqLMOCeSGLRsoXakZ3PAP3Rs0xGsD7s9uqKT2h6bi1r42a8IpzGuNl6I_9U5ECYN1RrULs7jOhr-I53ZPabYcw_85prSv7t3Zrer1klvd4D6w2M7p-g4qABEWF89NyiRjTcl2fCkirvmDSY5Y4fbrfT59ay8XjLm2ZKsJIhaqWalBeRVOcUSC16nDaQsWAtgOBxn0z3pmkMMpq5WXRSm7KCufM9OHjrrEaUOoz2a2NB4MPgnqItKapayK6D364YLV_hc8S_PLZb0vLPQdh5JPJA9972FXgemYam25xaKGjkHi9hPMnhi9YiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=IHAWUtQrlgvOsDkM3dF3Zjz46VamPQOqLMOCeSGLRsoXakZ3PAP3Rs0xGsD7s9uqKT2h6bi1r42a8IpzGuNl6I_9U5ECYN1RrULs7jOhr-I53ZPabYcw_85prSv7t3Zrer1klvd4D6w2M7p-g4qABEWF89NyiRjTcl2fCkirvmDSY5Y4fbrfT59ay8XjLm2ZKsJIhaqWalBeRVOcUSC16nDaQsWAtgOBxn0z3pmkMMpq5WXRSm7KCufM9OHjrrEaUOoz2a2NB4MPgnqItKapayK6D364YLV_hc8S_PLZb0vLPQdh5JPJA9972FXgemYam25xaKGjkHi9hPMnhi9YiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز سی‌وچهارمین سالگرد درگذشت دکتر فریدون فرخزاد
۱۵ مهر ۱۳۱۵ متولد شد و در ۱۶ مرداد ۱۳۷۱ آسمانی…
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20620" target="_blank">📅 09:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مارک لوین : رژیم ایران باید نابود شود وگرنه این [وضعیت] هرگز متوقف نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20619" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">العربیه : یک مقام ارشد سعودی می‌گوید چندین گزارش اطلاعاتی معتبر نشان می‌دهد که میان حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران (IRGC) برای آماده‌سازی حملاتی علیه عربستان سعودی ائتلاف هماهنگ وجود دارد.
این مقام این گزارش‌ها را «تکان‌دهنده» توصیف کرد، زیرا در حالی منتشر شده‌اند که ریاض در تلاش برای کاهش تنش‌ها است و اعلام کرده بود مذاکرات به‌صورت مثبت در حال پیشرفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20618" target="_blank">📅 00:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=IcRGRaDveWxBor_I_cL_mqqygGL3K9RyzHLNFltki5iSgabPjTY0RHSH6jjnBrGQ9phEYAskgrB_sO6Yy_E3q8to3urxab9mXgDG1eNaR5qkj90-TsbmS7BeysSEPAIpkEwuucu8TvLjuZLxwcdQ5jzmkT7sq6TDhfVPCz3_ki8HTY2CzkVNmDuUXgP2VfVqk6824Ov3QSuFNNVA5dUlT_dFZupbjIr5BBAOPanpZlp-coM_PyYRpfPqbefKYWqieHZzEacdlVpbd2qiVicZ6680NYAW10JyBadOHxTZb0J9Y9jY2OH1HJVPSYtwZj6b3WNie_Gui01Xu9DqtotdRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=IcRGRaDveWxBor_I_cL_mqqygGL3K9RyzHLNFltki5iSgabPjTY0RHSH6jjnBrGQ9phEYAskgrB_sO6Yy_E3q8to3urxab9mXgDG1eNaR5qkj90-TsbmS7BeysSEPAIpkEwuucu8TvLjuZLxwcdQ5jzmkT7sq6TDhfVPCz3_ki8HTY2CzkVNmDuUXgP2VfVqk6824Ov3QSuFNNVA5dUlT_dFZupbjIr5BBAOPanpZlp-coM_PyYRpfPqbefKYWqieHZzEacdlVpbd2qiVicZ6680NYAW10JyBadOHxTZb0J9Y9jY2OH1HJVPSYtwZj6b3WNie_Gui01Xu9DqtotdRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در سراسر جهان مهمات داریم.
اگر زمانی به آنها نیاز پیدا کنیم، آنها را خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20617" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=rBrNxo5gQnRF539yjbRKGnWMMIlXCcjms0wV_q_ByBpgquVKx6cjhsNhABBzCD482YjB0HP_FTv5Iq1zCyXA2jcX4IcK4AZgpNmmiajGIaH8FvgoRiryEiNJCZrnq_TuT3cxCNt1pyMrCnlmcbd9ESV_7eHcoCV251E7mMfCOKeDODQ6Mm1pukums53taNYFh4XoJvTWdzZw9EudbrABR23TC-YigjhcrAu_n-u3KF_xSNDv6VbBsMcGb9_pQ26RPL8p7y7zQdy0HFSIx8UdrMGb3gz_TvsuL-XyredR5BSTaxJSyXBHj0IGEBq50gb7p0grQRl4_BAFZ-MF1Xt_LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=rBrNxo5gQnRF539yjbRKGnWMMIlXCcjms0wV_q_ByBpgquVKx6cjhsNhABBzCD482YjB0HP_FTv5Iq1zCyXA2jcX4IcK4AZgpNmmiajGIaH8FvgoRiryEiNJCZrnq_TuT3cxCNt1pyMrCnlmcbd9ESV_7eHcoCV251E7mMfCOKeDODQ6Mm1pukums53taNYFh4XoJvTWdzZw9EudbrABR23TC-YigjhcrAu_n-u3KF_xSNDv6VbBsMcGb9_pQ26RPL8p7y7zQdy0HFSIx8UdrMGb3gz_TvsuL-XyredR5BSTaxJSyXBHj0IGEBq50gb7p0grQRl4_BAFZ-MF1Xt_LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که می‌گوید شما به اهداکنندگان گفته‌اید که باید کاری کنند جی‌دی ونس انتخاب شود. آیا این حمایت رسمی شماست؟
ترامپ: نه. من فکر می‌کنم او عالی است، اما خیلی زود است.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20616" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=IzuikDf0NJ2RBQvqpUVzSBoGsFJFpEnzT0-xAHbXv7hFFQg8D-qWoq4HqiGCibJvbKZoYFonCAelc4CaG8od53PVrUPm9mc7MT2ZcxwI_R2TgLewuxNcCfWr0CDHXM_9uj3em0t0KqgcTp6-69M8ekP95WDRvKaz-40dlsVAZFyPXFkDbx-Ro_W7Ru1QBoobQ_jOu0Q1_xcNvke-qDkwsEDc1cMl31sWd-sODHGqzK6P1VvtniPkbCkjLhhMvc-ltoadrbqMuJd8LnSZr7XJu0m53VKIAvAdvUFesTw-OtmYz4hKGQHWJ_lTUOseyVyZzN-y7Us65DnyZcVHKMzBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=IzuikDf0NJ2RBQvqpUVzSBoGsFJFpEnzT0-xAHbXv7hFFQg8D-qWoq4HqiGCibJvbKZoYFonCAelc4CaG8od53PVrUPm9mc7MT2ZcxwI_R2TgLewuxNcCfWr0CDHXM_9uj3em0t0KqgcTp6-69M8ekP95WDRvKaz-40dlsVAZFyPXFkDbx-Ro_W7Ru1QBoobQ_jOu0Q1_xcNvke-qDkwsEDc1cMl31sWd-sODHGqzK6P1VvtniPkbCkjLhhMvc-ltoadrbqMuJd8LnSZr7XJu0m53VKIAvAdvUFesTw-OtmYz4hKGQHWJ_lTUOseyVyZzN-y7Us65DnyZcVHKMzBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: فکر می‌کنم این جنگ خیلی زود به پایان خواهد رسید. به نظرم آنها دیگر نمی‌توانند مدت زیادی به این وضعیت ادامه دهند.
خبرنگار: آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
ترامپ: نمی‌خواهم بگویم که توافق انجام شده، اما در حال حاضر تا حدی باز است. ما کنترل تنگه را در اختیار داریم.
من در مذاکرات با ایران دخیل هستم. اوضاع به‌خوبی پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20615" target="_blank">📅 00:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20614" target="_blank">📅 23:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20613" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آمریکا : اگر
هیچ‌یک از والدین شهروند یا گرین‌کارت‌دار نباشند
، دولت قصد دارد در برخی موارد دیگر به کودک متولدشده در آمریکا تابعیت خودکار ندهد. این سیاست به‌ویژه افرادی را هدف قرار می‌دهد که برای
«گردشگری زایمان» (Birth Tourism)
یا با اقامت موقت وارد آمریکا می‌شوند تا فرزندشان پاسپورت آمریکایی بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20612" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20611" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSM_hc2VFSlgKNwVHJi6EW5LWn2g2EbhCdeXI3d-67gw1P-etQJMm-RgCgXuLuM0qY-Yap2aPbJSsJA8jEtFXCFCkBuOC0JcXYZeGpSzaujD3FNkhU4-gbopIcBr3eyZN3digvEiijXeJcs-GnMbOBGxcYpmyYhxHjE60KJTTR6LNW4qFmUaiUtA0l0iIt_aicMWH6jwm6NEv7DuuLss-wNjqjXKERlNv317v7L5koZcZgeLogx49kjZBPNhsTU97PKlfKx3ZWf35C2mPlCPeyxh6xhGyh5oJ3pyOGubLOr2pHGpKUW0othnuQGKwiFTOLE-21E6QVYSQV_dk7xLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم اکنون در آسمان انجام مأموریت میکند. دوستان بسیاری اسکرین‌شات گرفته بودند که این هواپیما رفته، لازم به ذکر است چندین نسخه از این هواپیما در پایگاههای آمریکا در منطقه حضور دارند. ولی این هواپیمای به خصوص همچنان به مأموریت خود ادامه میدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20610" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20609">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏افشای تکان‌دهنده ژنرال جک کین :
‏"پاکستان و قطر بر سر منافع مشترکشان با جمهوری اسلامی، دولت ترامپ را درباره اهداف واقعی تهران فریب داده اند"
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20609" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایالات متحده، اقدام حوثی‌ها را که آن را "حمله ترسوانه" به نیروهای وفادار به عربستان سعودی توصیف کرده است، محکوم کرد و به خانواده‌های قربانیان تسلیت گفت. @WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20608" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCVv3JeSxQ3as4qNmluLdrvhbF9qNguDyEg_aUzlV0CU2dB7Ir8R0F4dGQaNWAYFmewE09Slv9wdX0dUwnVVdVRJyMv_uacARrNRlrtffLB_XtiWUC1qyvTKZnYdW8bKFpYMreSiaH33EO3xtwkpuCzM8S0W7gMng2Wyz_3LnfKmtqUxdIRLwGR-XqJ7t6hZK0A4YrlH3eBWMomihBBansWYLFC3BLVmWlT-NC-sjuKvEf0RP_DjSCEyqwtF1jjBW955lIK-eyLTbScxDtwPcq3JPb52QVl6HEPqDM-CT-2e7yKVSTe1vT-NaEo0IESTVEVdmyqbs2zTv16dwsgM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20607" target="_blank">📅 23:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iev2o0wMjZQ-V4M0kyQ7J2N8029y8jvUD_kywhyxwDYZWMORgut0qYy8m5TTRgccxz-2WTAKDDZ2A5kHfFnCmIMPMLYrUgEVD0WG8u7RW1WEwnC_zJPFXssGuwXdNN1qaUVPTtvsJJvtsXNrXoQTbgiW8AcDKvNLFLKG2WZHFLUnmnxH8sncgoNHeQB5D8i_mIkPWHuUGq9-g9isxksxfJx6Jpo75uTgTyJ2mlW6ayEGU__HsfCKjs39l4oJwxp5d0Ay7RgR39hV8xOiRmAgRxdPvz4vxsfXBb793JHXD5tw8N1qKoq384I14eeZ9eBmTWZ_X4xc1Ga29m95JQejQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در لحظه گزارش شلیک موشک، حداقل دو نفتکش در حال عبور از تنگه هرمز از طریق کریدور تحت حمایت ایالات متحده بودند.
NISSOS KEA و NISSOS KEROS، هر دو قبل از نزدیک شدن به تنگه، سیستم شناسایی خودکار خود را خاموش کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20606" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تسنیم
: منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20605" target="_blank">📅 23:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تایید نشده انگار از ارومیه موشک پرتاب شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20604" target="_blank">📅 22:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جنگ میشه ؟!</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20603" target="_blank">📅 22:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzRhzwsPvbHVwtdk9GD7XXdo8doiMurplnv5TUp6h7Nifo3i7CRPrDjM1hI111iueI3W8h8IBJqiYgESPRlBXPRwe0BxVpOdVJWl6hZ-ZoNgxDJHa_k1abDocMl_J7j-uddzPePSwgpaDg0QHCfFI_1YnLf7JKsMjXJ1O2Ugv75exUW0GmhK-mV2wKJiLkTl0wIXbEn0HZ4H3ZU6nEe8xO8_h8jhIbb70LQCmElQOQS8WrKVmS9gAyB8VoSruAoPFf_I9kVxDGi2X9j974sCt6y6rtXNFt4Eee2gMUSAEK6CbdIstsApw2WoNlmlLyMSAybKIcAVw1Yi6OsIsgtNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دود از پایگاه موشکی پارچین ، بی بی داره خنثی میکنه شاید براشون
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20602" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20601" target="_blank">📅 22:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز: طرح ایران برای تنگه هرمز نشدنی است، آمریکا اجازه نمی‌دهد!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20600" target="_blank">📅 22:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اکسیوس : به گفته یک منبع آگاه آمریکایی، چند ساعت پیش ترامپ و محمد بن سلمان تلفنی با هم حرف زدند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20599" target="_blank">📅 22:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر انرژی اسرائیل (از مردان نیک روزگار): حتی اگر آمریکا و ایران به توافق برسند، اگر ایران برای احیای برنامه هسته‌ای یا توسعه برنامه موشکی خود اقدام کند، ما پاسخ خواهیم داد.
ما به هیچ توافقی که امنیت اسرائیل را کاملاً تضمین نکند، متعهد نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20598" target="_blank">📅 22:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش پرتاب چندین موشک/پهپاد از سیرجان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20597" target="_blank">📅 22:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش های مردمی با سانسور : تنگه مال اقوام درجه اولشون نیست که شب خنثی سازی کنند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20596" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قالیباف با صحبتهایی مانند آخرای شمخانی گفت:
حمله بزرگی در راه است... صبر کنید، نه، آن‌ها می‌خواهند مذاکره کنند. این دیپلماسی نمایشی است که بارها تکرار شده است.
استفاده از زور و تهدید، همراه با وعده‌های دروغین و اخبار جعلی، یک استراتژی شکست‌خورده است.
حقایق را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20595" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش مردمی : اطراف یا خود اسکله بهمن قشم رو ۲ بار زدن ۴ بار هم دروغه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20594" target="_blank">📅 22:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بخشی از رسانه های رژیم : موشکی هشدار آمیز توسط نیروی دریایی سپاه پاسداران به سمت یک شناور متخلف در تنگه هرمز شلیک شد.
@WarRoom
بخشی دیگری از رسانه های رژیم: صداهای انفجار جزیره قشم مربوط به مهمات عمل نکرده زمان جنگه</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20593" target="_blank">📅 22:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یک صدای انفجار جدبد از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20592" target="_blank">📅 21:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20591" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش صدای ۲ انفجار‌ در قشم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20587" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ruhollah zam and Msoud Molavi @WarRoom</div>
  <div class="tg-doc-extra">instagram.com/Yashar</div>
</div>
<a href="https://t.me/withyashar/20586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">صحبتهای افشا شده از مسعود مولوی با روح‌الله زم در مورد اسرار سیاست و پیشبینی جنگ ایران و آمریکا.
‏این صحبتها اولین بار چند روز پس از ترور مسعود مولوی در ۲۳ آبان ۱۳۹۸ پخش شد. همچنین روح‌الله زم در مهر ۱۳۹۸ توسط جمهوری اسلامی ربوده و یک سال بعد حکمش اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20586" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش حمله سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20585" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی تو شرایط ضعف و بحران مشروعیت، قصد اجرای کنوانسیون آکتائو (رژیم حقوقی دریای کاسپین) رو داره. این کار بدون اراده ملت و تضمین کامل حقوق تاریخی ایران، تهدیدی جدی علیه منافع ملیه. معاهدات 1921 و 1940 و اعلامیه آلماتی، حقوق مشترک و نیاز به توافق همه کشورهای ساحلی را تأکید کردن. اما کنوانسیون آکتائو با اجازه توافق‌های دوجانبه و چندجانبه، اصل اجماع رو دور می‌زنه و جایگاه ایران روتضعیف می‌کنه.
این اقدام از موضع ضعف و مغایر منافع ملی است. حقوق ایران تو دریای کاسپین قابل معامله نیست و هر تصمیمی بدون رضایت ملت، نامشروع و قابل بازخواست خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20584" target="_blank">📅 21:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۲: رئیس سازمان موساد دو رئیس بخش را به دلیل شکست در تلاش برای تغییر رژیم در ایران، برکنار کرد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20583" target="_blank">📅 21:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2eQ5NqUVnemCZtOX9DamBmG-K2NI-xd4uiV_U2PF0r-h7xJuAGJ73xqvgUO9k-j7W_lMPxUCUbkn5QUIiNCrqeL11HHYkMQBF0VB0jWQk1aAbQkE5u5dJCqtpw5Wtkl31T42PIa3gvFKoohB164Nok4BZFsiNtEJwXaoR7YMzZvZ45ViQqvSSbFNuQ8aoQn-fvrTMH4fU0t9PEs4iExCbR-ByP7PL7otKDY6GuSwb2K0oMFPl90WQPrK8XDc71o6tBsdcN3JZkK2bMl8wwVgn_v2dK-gLEhJUCgsdJT5g8sQ5wIkcaFf3FsvkRCc46Co_SEOGTTf1ijL3otYWRHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جعلی، مثل همیشه، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس هستند. من از عملکرد پیت هگست کاملاً راضی و خوشحال هستم. همه چیز فوق‌العاده بوده است، از جمله حمله ما به ونزوئلا که در کمتر از یک روز به نتیجه رسید و به ما امکان داد یکی از خطرناک‌ترین جنایتکاران جهان، نیکلاس مادورو، را به دست عدالت بسپاریم. همچنین در مورد ایران نیز همه چیز به‌خوبی پیش می‌رود؛ کشوری که برای این هدف که هرگز به سلاح هسته‌ای دست پیدا نکند، به‌شدت تضعیف شده است. پیت در میان نیروهای نظامی احترام بسیار زیادی دارد و اصلاحات بزرگی انجام داده است؛ از جمله حذف برنامه‌های DEI (تنوع، برابری و شمول) و افزایش جذب نیرو به بالاترین سطح تاریخی. این شایعه را روزنامه واشنگتن کام‌پست، که یکی از بدترین رسانه‌های این حوزه است، منتشر کرده؛ آن هم با وجود اینکه ما به آنها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این نوع «خبررسانی» جعلی، مصداق خیانت است!
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20582" target="_blank">📅 20:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توپ در زمین آمریکا است,ترامپ باید تصمیم بگیرد
الجزیره : در خصوص مذاکرات باید گفت که به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است. اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20581" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9djB6wgXxdBUllWBeFO5aPIpxjAa5_mHsBTlVnXAJYqf3VpTAjtRQ4KD0Oa9_6K7F51nqc1ZmkDJ-OfvR3JqaLy0Uqb0s1vZ1ko7S9Fp4oZH1NHiiiccVMv71oaMgimw_MCFg9m6yEMCTLhPo8iXIG4xIoExuqikCIi7aqXiGOxrrlHRdOf-aFGsADz0z7q9juGeNqNM2afEjnzC_UPSpgQce1cvqLs48PPTBRSbnVv6W7jFKNVTZX_rnlv5vq_f9K5EXIX6Uod-2HhTlRbSP8Z8ZK-X8tE0o_T8atZSoDvHo2nz0JXcHyAJhWxmXRQWAJ6b-9cEyzvio7XEaFt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب‌افکن مخوف B-1b از فیرفورد بلند
شد تمرین کرد و با توجه به الگو احتمالأ سوختگیری هوایی هم امتحانی انجام داد ،  حسابی خودشو گرم کرد و آماده شد و دوباره به مبدأ برگشت
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20580" target="_blank">📅 19:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20579" target="_blank">📅 19:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه های رژیم : طبق چارچوب مذاکرات میان ایران و عمان که نهایی نشده است ، در مرحله نخست کشتی‌های ورودی از کریدور شمالی تنگه هرمز در نزدیکی ساحل ایران و کشتی‌های خروجی از کریدور جنوبی نزدیک ساحل عمان عبور خواهند کرد. پس از پایان این دوره، تردد از هر دو کریدور متوقف شده و همه کشتی‌ها از کریدور میانی عبور می‌کنند؛ به‌گونه‌ای که ورود کشتی‌ها تحت مدیریت ایران و خروج آنها با مدیریت مشترک ایران و عمان انجام خواهد شد. همچنین هزینه عبور به‌صورت بهای خدماتی مانند سوخت‌گیری، بیمه، خدمات محیط‌زیستی و سایر خدمات تعیین می‌شود و ادعای دریافت تعرفه ثابت ۳ یا ۷ درصد از ارزش محموله‌ها تکذیب شده است. بر اساس این گزارش، عبور کشتی‌های آمریکایی و اسرائیلی از تنگه هرمز نیز ممنوع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20578" target="_blank">📅 19:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20577" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuTnL0xrexuZWzUX8NkqQK0JWNujEgdtTZlQHNrGEU2IrNV41HVJzkhxCAg790lB7hbH2tZef82wAWo9s704F3KLfJZqV81ESQkQz7RtsFztZM3NbAmY1BVa3sS56q0SFjy6AdrLmL8sawoiIRK-7u9U6tJz-QVXXFpNBdxxfYy3qAcQiOOohOGQQCsn83J_Ved2FEbUswv2kcAk90-0jiLhrcIrORzNZcAO2auUKXLWZhN1Af5SmT7faGztCdzeX87kraHRwfD6Gjei4SxgNKdp6lbH6J9sIxySBP4PQ2V4MdEh1OrmRe0rr5z5QGyqOf3Wieq2gJTeEZXZfkzcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20576" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تعدادی از نیروهای عربستان سعودی کشته و زخمی شدند، پس از آنکه یک موشک شلیک شده از یمن مستقیماً به پایگاه‌های نیروهای تیپ واکنش سریع اصابت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20575" target="_blank">📅 18:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20574">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ان‌بی‌سی نیوز: پنتاگون جلسه اضطراری برای تأمین تسلیحات برگزار می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20574" target="_blank">📅 17:32 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
