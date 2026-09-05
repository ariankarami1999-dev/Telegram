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
<img src="https://cdn1.telesco.pe/file/Ix4OHHSshHtlkUS_UYAGO6Ue6hotTxe52n163ulAUUDqpJ0KNqnBQjlzOM_oF0ddp0pVSNNqvnYOG_MFnJNjcOJC19s53bOg0bHBiVqopyikZom1frYaO9CltdjF6mcPzm2vUpv9lQJ2hhqYN9Dx1ZvLLj4kTXgtXrgEy89Kf3GVV1IeLTS5U7_e53kg54Vz0t_5bAXsA9I698XTqEkD4hGuyw701WLO3lhkCRd6YxYoOrgJerD9TFKFmbvJxIFxLgVbJ_3J_3sGBdqFvd-SCFA2XOubWV8MHoqiVa235ua0bBh1bazsf9FY1oCoL5XJkUhhKQxTe0-gifJ7PVYTyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rnc47cKpVVbFV-E9oEr5_8M2swQQwDJ-qlrgUpXqTCoftwpVOKxae5d2-VCJ50odnn5U23fcBkp8Wpg8ToObDkCXz4dt3dTYGhH7Vz1lJ6LySmvDadRoWmHTqiNQFAXumYcA9axYIykjZNzQCZOOcuPWNLleQ5yyGF_0rtu4mNmAxuBz3TY14iaoLZTQIubNRe4sIeY4DdW4KWQ2HffXWYzhQXVWjTEpu3KesfylzNMJcmC6C_ImAr5vvmWvAQES7N2Y8h3CQllQmVAxMeIUbTG5MoH1vlUmSOgQ378RH_vQkVazHQeKZUgfjhCv1pgR72dTKZLnQdh-3S1dLh8XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RhUvUu4s8WXHuNTD5c5hCDQHzs6LxM9q0vbj00pj55fd1KaSa9IO7E_t13DJ-sphpV-9WKPqzSfTJarpspkdIGk7H1Rt0SvSLdYID0EqFDxYVTs3CltfIWflrqZsNlistCjy82Jac2jsAIqtmrqmBhD8OSJ1nOVcqdFdOnmohR2tAITVIXczriCDVB1hZlkEimGnG91ezOI_NNzcmFgHISvlld2knSX2O3RvgkhjtKQs8FJkBC6N41rrIuXnTvhc_PfXtE-zLkHQx7Rn-GD9lfhmUrVXwQVCjerOc6IjDWmqmRgU27urvoeTuvisEJHrnWGI8mHPYaaGzFmkZxe6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGoAzZlYFoD0a1UBJBd6NrlahPBCGY9QN_50W9StfS3dPdGk9zHyWbRA7hgVI484qVjGt6rdplCtONK_DBD-p9uqJ6IbtSUoMsB6HQwpR8bC4VMTwua0gzegcc1XCl-zonrXKhfUzrQmJwzLn3m-_Otvw0Hxgkld6SV4mm0q5vyDHwlKy_-TkfmxO14d8WUPuJqAnfuQEliIbPUy5SX8URZbCYWIBU3Qwg7LfUviOK2MnS5pvY69U8Fp3TCjMmmXCGQiUelVeqPmaQXhDIKKI2VOrKHh5zxF4DoBfXyvTWmq8H3KOSD7eVdjp1v3Fm_ypjjFYeNsv1ARv0ag4Y8UFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMGL59OqNZURsC9rl4RaaKU7JHd2o9VuM8hPuPWadJfOHk_46rSFmmkt-cVViN6x7KLOlbjdtOEDB1ODEU37vzUw324OxzUJZ_ld3rInbwTuj1UlJa9X1XDPPnU67QY1rXeh5vYxLrZ3ezSuI8sOqNu-5Brh0yOu3eszgkWqeBfza92S3QXNG9X-itGJtQwlUWi_nxeg79GsbhX9sWtvpaOwnfkJcwEwFE4F0giDx7Pr0rHOaPqa8foz3dthq-N9_mpVxbLdInoMbRJKtwnVyWahD3Pt5R1iu4STzZi_6tdyUoIAkCBWQVC2IdBoHgh2X7G7k-C2TyZZG9Gi116zow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sZII-Xszx9gIO2hhpUs8-IJtom4pYK3d3VjQ71dsLRgg3ubZqZdWRoM-xV2wC-I7gddf5-nBQz9V44Sd2eIOYnmAf2TLjgrYYHDBBYEOd1LxbyxrQIPKsrlXnXyTeI5LZ9CWokr9vK_KRslW6BzZZS_M2hQsyW8wpTjf2EJ06k3lQxG0p5N17p-ibN10CxUGPGTM_ZY_VI4wYZP1OoGC_8p62WfbsgXQcm7N9x_e4tfG7PquIBDLaLnjhqWt_EdrSqkbz-Nmt5w5UcPA0wuu-B2iWrUpzAuHhBPgAjbvYTnr3Eb_tTyICbb00RLTGAuqc30XZFcCRdEuTVhKa8x6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/URhFLRuEZTVECSzhpxOtE-fE725Vf6cXDeYiw95xMCm11zRIWSeliDV1uDeDmoTyCce-EVtdpS3RsCbQ3GMuYLHOHuJOwWXfeGlIRSzQlaO6y7zmwUFEP-nCPr-pQpcnp8tLfAB35q1oRvEJsyeYoB5qQ7xljSOFSMYXSMDu6O8vGfyw0yXiHlhNAeTbbz17OmB7G2Bmz9CvxbRg4hUw6CKx9HXq7-0XGQl2b4sP82-dFc3MyEqjmw_HGpBoqzTUYWNagIz9nFduhNz7IzCVQSC-L9YzOMj1PaKxamRrmPLhT0xwmRWjlGGNW21LzJXE4YlrMNyFE4NQfV3m8LxyJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZApblh3gcGwevIjpNq7596wf5wkLyd6dxb68L61-MkDJz8xrVah05BAEBOEChSflr21poPXeklP9jXtN4vOe2Ypk1QX1er3lFZ6X5sqYzpWnA0SOgSxsxwMcEb3cftMRv1kNRsG5F2cTSDMiMRu2ZcrYf2h8FN6Tyx7OVTF1RV2uLRI86hIIFNsjIRApicHlUeq1UQjkgDgjP18onq26JLGxr4IVhjL9fxhHmj9n4eN0hEBwaI8Xa-rJyc4WMvabxrr71UU1WvKKqibc0xP2qsud1P2QKjeCHVYlxtNA23ZCXgTnngtqRX66UPbNjPna0Fw3xoeZEgiIAXDuLYP7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=BnEKwNTt3Z64PrFnMaV4pZYjs_SjZvU_EfdYiJOMC6C9xH_JFCyLJ7lqvGIXeueDu9AdfEhzXKZQGvF3jrPsnLT1o-bSiJNusH9gMFt1-GWNAMP-8mOWp9c0lLkW-t4hy8NVwB_zkx3JegHvIcw6Njkm2GHhKVDjEZ8ztl3Ac_t4EebfPMyUokZvBy-mlQOgNKJpfSpiIUAi7Zi6HN-a5FQ8azUxJsEZGw2Wgexp_K8Z1omCysIHQs9lD3ADVeJOKS8PSW8c5IHGB_byy3pYnmc_haoVYiAA7bRX5-jN0pvUYdLFVVmDAejaxTpkeNNAoKGIQKH3cm6IsShKBs62hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=BnEKwNTt3Z64PrFnMaV4pZYjs_SjZvU_EfdYiJOMC6C9xH_JFCyLJ7lqvGIXeueDu9AdfEhzXKZQGvF3jrPsnLT1o-bSiJNusH9gMFt1-GWNAMP-8mOWp9c0lLkW-t4hy8NVwB_zkx3JegHvIcw6Njkm2GHhKVDjEZ8ztl3Ac_t4EebfPMyUokZvBy-mlQOgNKJpfSpiIUAi7Zi6HN-a5FQ8azUxJsEZGw2Wgexp_K8Z1omCysIHQs9lD3ADVeJOKS8PSW8c5IHGB_byy3pYnmc_haoVYiAA7bRX5-jN0pvUYdLFVVmDAejaxTpkeNNAoKGIQKH3cm6IsShKBs62hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CP852iXAjj2VAwIxPmbCP-A3FL3pHjJ4foORROo4xRR1F3lTBlbAPRxP0QlPww3qD0MOtfYg8ZWQ90R9Gl5qeqP0qgGl_558rYeA5P99cOsXVkuAnVRrWCKivdydqeI50TgOgbKq77Z-vrCbIH8K2oG7Mi8fxGtXCK517ROwnSDJpbvWHMZ8LiyFCV5BZVKkHLQfKu9YM5Y9Pd9lh61ArDvhQFUT_if_bF14FN0ZGby4ujeRQalrMyWZYHyICXc9WdeTM6xbYwYuFHhfezSVpzcU9ZacbxV6l0egkOlRgUbYHhKjQfyTnbbE9KrkG9HGey7tZovAd6WT6z0tPdYkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJViud7nYu_wKFGqYq7CZWOEq_TCB8YDHUQLxKp_JT7vqwah7Vywr1lbqkYoX4rd41NHmewVb4zCjv-H9P1aMz23SXqUFDczqxjMbJTWeVsONerP4L5cK9xZU2UhoRVDk3aMiNcnOd1hIoIS6Q6glUEKN8_ltHkMFLZS6UkcntDpXYg6R_yRdcKm7kC9lDmh7LZ_jPLuM2PWOCEGFRajRwMrWZctk_EIC53UTfj9LfNQMMKk-0aB_gJ6n3V95L3KI7w6bqNT52wPW4i0rTPhK8Idoee6xljzZfdy5A3yli-0f3isfa5ukUlMcEobJAwTFbNPOW_fmOwA8psFuL61ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJCV6-o1d7ETpDunt2HRjjPl9cLU4njcOLXAn8l5S439_3lZSdoe_mx0zHrk1Z524-SH3A7r6fFqF8VvdTAI4L3ZAOONcf9JR47gWp1pecAceuPktNNbo0-QOiF407LSXY74AR4lzUIMzL0UQuZjfe18M4DZysB70DyvH-ED84cRvXLetQKJnzi3HHmE0C3wLptbU3vY2lQPWfAyZipgVIEGv2NcvBqw3BotIw3V6nzcOHItZkqLM0oDMEK9CQWYBAWMcUqBznTeRR91cnQo8rt8d4Jqgwi_sjJ_g7FiRmOWw1faUvkCS8XjuYOf4dZzC-9PTYSec_EDITtG7bvZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXqzZCaS8NOja3CQEiaBVVwllizl7CdJMwdIBcABN1Xgo0Ts10fp5w_owFRd4DcHjAtY3txfMqq-S48E6L7rO1SmiuBtu8j42YuRuBVPRYMhi02sX5m-tQMeEK-UtTsAM4OxNVmF0kM5CzFcvWnqxrA3E2OpPc5B7kSY2qQ9OQaystYoPY92GwBCJuSVTy-PL1zeqBqq3EwH4mV14w6e65VwsCgE154bfqrlrE-zM7RikHRl9kjs0fZsVIhZCvS3PfB2YZbLK3TPbRXTpB4tmZdvvkemVQzv0ufjWaty6f0GQcgs_H46gyb4Q7I-GSS6BCMhxu7QFZDEUFFMxT0FyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPcX4W5983bZduV3ubcDcKgzV-PujdnILqjh0BwS-yvZywFlG0GUhLRT5kjjNru2fj6YI448n6cZW_mwWqGPXi5Ow40jSjQTwcUHSqf93OCnC1isG2KLz3aoP97hXh0OMBo0Hc1Mg9PYR080qsJVeingVpO7AHZfkSI-lKoMdbBryLIbk3KyZ7xu8kUuYJcwEIr59DAz9Ol-oKNLzO51P9vlZLj23MssaaGK6mhFPXMbYrZ0dU1JC-w6KVDmYv7pwsT9SXvI3aGzQO243JBkHgr6S0wAu0zxbOmlDbm5CrltwfXqIXZIkVqhFJLilpzsprdyOhQW3iKTwYnTR9j2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jClAMUkZnOsuhT0l_pwQdXOivlJ0wwGiXo3cHQGwl4HUx-Qy5txzxaKZiydelzuoFSrEmpGa4bkr_GHS7n0VrFBgRxi-qUHVwWCUixcad7jauX8cM8jAP3yIOOp2nFYyPqkPZTXHPUqXR9fnhBTwkH23A54HdAA2Xx6nqryxmxyQvFWxe4E_OHbDsWTbTNSghj-AnjjB-Yrnlp8TnnKkyAx1P_sNp_CLVh6DkhSivwQ1AxGa47GeJ4H_gxi3IAptaphJ17sT0F4jtuw4c6sp8F9UJoVl46OR31uuF98LBm5d5Ke9mdYnxlTs9vvuSTSkQsaN8_EoIBGIMwCKtnNH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDETvYwlpy2NohN0mCkFUt7OvAB-SyQOxc-IvUTb0NYrcVfkgtKQIFfn88z6Ngd1ITfF6pHJbsIZzpOcNJgCpwWKkHE6DCV0wtHEBwhEI6Ri5wr5bwcuaEcgGtt3nmb_wZ_U-J40ohS40G8WNqLvqKddg01Fqcor-bpWbyYJ4ZzBD3bO_MY9rKTQJY48udfeA4-3QwNUzZwKXIpDo6GCnCkwRlpGzlBcYYKh5gR3wAdvFbfTDRak2wG3ZfHK_eUaxHDiiiYxeCB-IQibWs4Sr-rIH_6FCUsfTzdwtp7Uv3r9N4lsVE6hWDucYoezW2iY1BbCOBz9tLA1orbmXSpAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i3jL1afVNq35yHizJZ5fWM40MW5p5SaD8ze1A8R2PEC-sPT-TG9l5sbdj8buXfp3GPYgtfBM0V82-IFPA4P2jiWSVpbbLKXJZdpZDB6TIb7TOh9A94aUUdxYqMQ6PAxlWtfU6W4znb7XLVYEXdOOkZeigiAXQUCX2WnTs0asuA74mzgJbGaZmrcwtyv7WwEgt7b3nprN2xrRbPfklVt1NJesC4bsem0a_zS4NgpKuPtcFpcXUxDL2gMQG4pj55_kMA7e3NGHAnIGcjuzEY5lgDOheGGFQF7YwDLzBzC5zh3c5vcMWM7sIt8gS9jTSu77Ns8GNBljdtpw2Y-Mstz-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gr-GBnRDCXdx5vnixQRBPqDSwyN_PS71L8zvKSWVkePWCz0gfqIlcUcDmKQNvVJjf6ie4KM-aV5Y0YcokVl8EENemSjFa7PTreGcdokw_Tpn7Cz0AcmnRd1MMnRlB5syd87ACaimvIrvT_9hSBZj_53U6VJOCnvR6slGsdHCPt2xamfjztsQQ_TYFdDibrylC32GTTVbhpBhbUwE6QUJGfX3xXToHq4atuKRo_fLWiNzkpJ8F6VYz1Y7Mfr1ARPGwyjyAxZnPZPvW7vlAPVye2zHrci-JnYLddgnhqjZqrRD3mwIM0F3uMu7TlmcmOoptPVc4Dj0dbDvu1CvGALQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QY0M_vaLs7SzkoGNjonGVwqd9r4sxLUSCxmDtbIg71OJ-akJ_lufbDtn5qZ2lpeP2rJ6Po36YtljHW_UJwLV9gRjwS8EQUhE3AW1q_mc-8F9vwHdVfA2A34_xwO-1Umhw28kYJVFtMzQjYgs5ltOKS4silzZyEiHIaVcS3z49uptPQy7mEvMels3qqejWPC5tBc2HbyLO3MTWxr1ShIlBJy5EhgCOfryH2F7OEwMT7R1VXQ_UuXLp3_Btb1c4QIzOqO_PY3FlCfrBqhAIUv6bBOdphII8oaa2MdN-E5wWf4EMqnLWuW5X19n0R9uxicPtoQs0myosuFw5taX0d5FrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fud7cUg7tlm1SS0Bv5kZ8ni4m8VKFM9nBIPL2YqDcV6COZKKs9t6V5LP_KXNVuoKtOOfXIOqaYU2DGGISPm1R7yLPu357T6AX03k09eZIx0wqu8xOsM3qh3Ik6CbF1kGGDvj7pdqwIlQnI250KXpxZ3igyQR4YoLnNCRAHA31z-PWWRfXl5vRa6vQo7TFCynI9L1zrvqBMlRng2JzZfmUe7G0VqypycHooibFPO0IJMr48snNTNwfyfoJ9sFCjBIV07qzp8-u3nEQ__yzT-dyz-30N7d5xWxRhuTwrCXF44quSQioBbUVAtOK_YSM6JQyOoQShJpsWsH1xIOHFgdTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6JvtoOK6RYbi--ibdFOnjFhsNIHDBFbxnYtFZrpepkqfwnbWNEtOom5jxUATiAOQTmOAFojk0Z6Tvs0_aKI1WRFXlRgKZZmGXAXMPHmjh0-VyDBCyjN5w2jCfReJYD9hmoPBSC9tkE7usGzC3AiTEUZiu3fKBLpa1by9klDodAZsF1pXtFj7SHRzVoSSk8GoqJr1Xd_IjHaLe4X36doxsQBE9dleuXqtuktIe9S1jo3ON7lU88baV0ZOQcIkoZPOLN5H6KFzjkjApxeT7acAB1jKZpyco5YF09LYtTVdo2wKxLK3d0_tS2k64WzRlWIC8WHOvnpQMGraDNjHujjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/adeIv7abP6xDFjCwUsf3P-wUqM22hdzkLe6BcoAiQEyQxavwfrO_azOpNdj3BXwosolvYa9Mqs0rr0iXqQFipY5m5rueUuVGmJlJ7S4SrWVP0D_tEYKKyHjJEUMB6XV-pR45dePsHFDt8gdWDdFMrPWMbzY9QZZLd739lKPYeCFNbQiJrshItXKBRPWERxjyd2XASeVkfqvOMO-tHf2avBgW-u2iDTC_fGm2wkO6Zj4s5E_jTLqntPEuhekHHR71sPgwXrxRz87nfk81a-YpPE6hNFGivthqkj81jL8Kym3xreXTlideJkmA7BIdl5PNt6r-K_0UbXQ4Pz5O60HMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dIZ6EJxBrNNXYPix3vLvkSWBbTRZXfBVRDucinYiaPleozZU1I2rHDwW6-bpOCJZCNAxdzJiutvs-l0Cqgh5f57zR6rbnp9mkSHcZwSitQCVL0_5EuacSyDltaYY3SeCA752J2zZduYBMvNZAEsylwlYEkXI4ST8rtl-wdiR-4PNYOBNI-c9oAdF5Lqhf5-Vz8pzN8h4Cf5pOlcvLmxx-rEzuigU_jeGJCx10QkN10qoRcqxYTdq77102OzEjTnQN3lgafr3rIP0ebcGEe5VFRC-VTN8wm39kMASw0Qcoko5npeS7XYSeE0SSJuz59dC5MXaicaAL45H8A46uslhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KZRRKyuI65bGCu1aPVtJtNy0rY0kVJSv1yGH_O5Ay8it0G-2g82ClDUM1cwuCDvrt3HeJwI3qkdAHzBUwMhWXKUq2ZTdte4T-PSaN2OFTUPCkpgTom9tfpC6dAHK1ykKxMc9b3V49eTLu4D0vTUpPM2DE7HQmLEw9cnrjjy6KjBpKJ4jid__SZw17fsvHVDCwQyYaV66GD9AZ3vEw8Ly2_Vas_Jz36ET9d7aM4i-ZT15eXEDTr8T1VSAxnkclErCP3tHM2mzJAxJUTcAl_oEV3BJxlPRUDKZ-PmLn3XhtNBF1xLgRzvzWlM24kUwa195FiaRAL724xpl7XqQubB9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YZg95r-g1OE2NCSA1bHQV1ik7yI5H_9QqG07E7idlaD16s5z1FSKXorL9KcGy3vPun987mArH07PqDDxW5ZvuiMbvSoDXPlOoaw7Pcly0zfapPGP-Ck2h3htI-uVKwU76xXNQy1yxVF3WQ3EhQZIWnYvBDxqjqupE-1sjSnh-98_tK82R1ZWcO5AwwtXmiYosCII2EdCveDLElah4K0VOG09vWZ-f4aOkbEOKZWhDTdwbI9l817Up9_8nOiF--wi6rTjcwv1U70nrKbRxC-rixANyxMhKre_4RVgFgzKDjGpZXidy2xROOPt4RHusOD1AIP2Gik43Fq6Tz2T6Ywd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qXNLAh_HqLFP9dReF8lz5b2qo04oR23OWpji6qEPOSvE5NDYZ6uGiCCOhctZ7n3MXqWYbQ4cjeu0oSU3vRoNaFrkBrvZPRNNcqkFs2C3ST8RpPumCHIgnwENEotLR2FRo6Fku_5-REAdahF2fAPrjmfMYfg5a9GkQKFBfSf3wUkIGyT7GvA6Fig0q5SvGiCAJGAxPSMTD2jsa7gUeMbIKaBSL98NHbNriGvibWtJVW9TgXQISVl79pQJqslMxBXDI5pvKpt6VVaxnv6xRYCgHh2Z_A27ChgdjDvQhBrm4EMT2gUFumyzNPuSlV5mDFWriI_8Ll4cPuci0cQs7WuWJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kfR0yiTx22MHz2MdVoddQVCr5vMTpfzyW-0sXcVCo3BfYsl1n3gh682mU6JvIeDIQTontWrS6AVv29IImEy_wQnh9nyHZoF2azLM_8ey7XGjqqBCA4B6W_vV08OTRswoMFW5xq6Xgo4jVQ7TGAT-RldIMNUGhxYL0k9uGXnh624XN0NHaCzjdr56DrsqpGrsjj__PVaJCLqi4354kaUH4Gk2vsmelBIReZx0tT8GtgdmC24a7jEjd7s_MZTbb_J8FWCZqFCKYBv2mskxabuefVkE4KLDHmE6JAvs1N3UxBuDJOIoAbjJGv07TFDCimAxvkUkKAD0C62rBiiFObvTPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcHFtXz7absOZKg0UgJOqfDtf8UAyNLV4sUM6yH9sCdQsyv3aDThGeUXTAVC_6ActLTNl5JIy_iEA9bgl76cFixxxzBCMbbdF41ch5vM8nOBIJu1_UQl_kqF-iKfhrWswl3jnS3D2k4KNprYRc-RFTKNsIhc_Cpn6w3pbgfdk4AjMxDpIK67xyxsKKb5fVzHPM1DbY7wXaqBgU3aLkDhG9tGhzS8czozPAY1DIpBwsQNmTntp_zl90oRRPDa7mvOiKCmWRnSN8kKEk67-qnXnVNF4zETgJv-5i3-jkIFhYIqYIjATrRc1lvcvFTFG6fXWoAmAosNxkl74ZuGRtBe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rJ4wn3OSj5i8aQL6Dr1OKk4iWbLhI_Bhq0dvDlEO6tmRtVXtDKSPYvUzhZJt74z0XaI8izJbytIPVg1xfAzkJmHpmYwYz6sqwdpJudk2ctWkqpi28lfUiZq2TVpu3m7gBro-XDfgTpbMWNb-PyceZjv1_kX6D8fUjA1j3P8XsQn56pEus7V_6EbXi6X1OGUYd-jicQlKj88XOjCVxY9PrLRP-js77aaMnI0EJVoD4OnvT17ZsjDgIHPhby8Ico5wPw8VMIQzpzS_rGEtnbEtf-4OcdlD77PYFfr5kUS24T0-bjBNLSHerJXg2iDAbcsyHXlB7AIG8y3BBVhPzodh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D1M0wjZezWS_jsSbkIWb-SbxiHWQ4-IFmhX20siv_s2IYUA1ncocZ0LdaeTvaJ05D8Bqc2R972ZdE3X8X3K6bDjCZb3CUsX0ySSfR6N_q5wXdXIMqI1dXIqicIyvJVN_Q_Tr2nbPPneHso1vVFiAwEsFqqliNn6iZO6kbjuwzab7xAo5rR9ppfid6Zz3pYyeyGz9OtjElQa2brTf9FdtG9AUE2Yr8-ueolKzJMT_UExbhCMR9zRELN1tF-bugiftEVYRM4tjM9R6X4SIk2muDy0CSnD35DAZfOKxAfg_IYhKY6DwTPQEwBNmdMtdRd3Z5H-baCaoplIBjYM4UfoMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jckKiF1l_FtCTtVlU5jN3yuzEFb7VdDD2D4UV-kGaRyCCPRr1zMswsl7rWcpFDpxpcw0UKFmP7uORSPr586T1CtRGFtw451V3GGYyHS8nHW-WvySvp9pg_t1onDrP22FFdYcwiU0lyce6yP9IENMUHW38Wva_hxjlZXeIwGMF0HHmbeyy3Qfqmm-i1U6tL8Q9mosE494vLJXTVAzqVRZhfC4-1nQIC_IJdM7mi3MTsTYwRXMAzPLi10b_cIZS8jUnrDF4Lj66nnc1o164ZwUEvT5aLuh1did88gXFVtbmXTwGt8mHCLANdQDRG2uWrAB-7HsTQCfzGtI52xrUuG9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dyE6gZ8WWDrGB9ADSCNnwxt1JfbgXtKByRRGrfe4Cm1HePsra5Kn8yZsHq-qvYVDSd-c_UjfiVasROji0lqaTKR0DUAniSVfzJTwZ6XCfmP7ou3RJmatdkxd4WbO324U498lytptzQcZVOb4ml6GliQXEVy819JTrbyQY_MN5pMIv6IDGnvttRXuUYW9yeCWj6vxq1bmira2YLpCzG2yowf6U8bbXjTJJ4fCUdR_8SO-cKkmWeLbntMEpjmPCnHOdGLJ8jwD8NKTyOPVUovroS4NMaFCMEwZJM8rbYoSZsjE6rsN0AJB27YkcmW_4l8fEQ0v9nZvKX5Rd7mQpIcXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eqbjw9ROmil5h3o-EKgS4lSZc96Taj-DtOd47Peq9YbqWBt7tzKxUrZId6-ZO9vWgnjwtKqfACHWSPwgcVMvtDUn2fkKxZ_FojrN9J7abg8LiFLypzIETf-_9qD3hwm_QHaF3tY__nZG1_XdH4lWG1Ku8Nq3Tszj9BOe9ZoOgN-ZucCRptO6HuFU1stbAX3SmTcIQhb4ilni2V6axwXNkX5EgpxkQFFKhdDWc650FF3MXJW7qt0fKlvBuqgOk0lXMIDLbCTcFNR21D-HM2kLrbY3Vw8v13AgP-M2AtFZyNYe2JpXaEy0iSCwAJeL6O_yAT8BwnbGO8-VR_dck6UE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AviwObs632V08rT95yTwb_tDN0npFpsZmcVadhjLJp6ankiDqbnnKZXimgEgpCLe9kNZSE5QmUuJ0I6cacznXskyphRTe1rnruaW7j3OMkxMEembzqKycpP24TJ-tw-303sWZ_h1WmPTgF9JBLM0bhnfZ4JEfUPJ-7YE1ieF5yEzbTfHDHbu6jvhupIbzqBZA5_IIB6WG-x9MMPVfdx8WUXuYp99j4ukD5ky3yTouesRgP_W13lBF2YHn6iKKhzY1rOVqRZsABB4d4Lbs1gpg-0Ji-stuW0EyUakRWhGxNmWqahvvVdtA84oh7E93hDYSEOBCl_a-jVrI1XWk13arA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aU_4zOqo1-aw6_cal0E3oMcit6pQhyLqIwKSj8ca9HWfr0VlTlSrSKsM91JRcJXoU6d3L27p5xfOxY_zWgCatiIEoAkA6JG5zZhDsDrTHirJW9-5ZghQSC5pbHxf8Jc2GBA-E0Tv6AWObHoEEWSfIamAa-L3S7Kb21nQbJWqmwqL3yX5TqicWcyjoifqSv8pAvWHx0qAsOfWWXqIQ7vOiF93KYsbFPwfJFcuL-jEkyRELe4HN_jz7bBHTjzlkZ399erw4J4J3HZSTUd3Il9mkQRCKf6ZqBJ4oNJ213IfY57etS_HezL4_yJw1nd5ppyhBcploUgd7PkqFcv1cSMRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WVGKeCpqQfA0EYfiFpqRyTCl4QAqZ1f7axvVQ7jbo4Aw7OhCoqqu0DQHbGQrcz1e7Lp8FRxD9uLjF-PKew62TdyWThDUaRPtSVnipyqjv0AeJuQkgD-8mWk6qwnZlQ-nOqjuAjkkFpqr6FsrOgMCg_ngpao37xFKXyfhGG8mI8HuHN7dLVi70NXrCusWEcUFB2XOmAljOI3pZ_lrkR8To8KJ4nTAr23ZiLIYqUBztTRXuvyGOwziqgtA8mUX3-v-_lXWpW5cR3IPsHHXWE2qh2wYIcVuqSJm9odK6ePi9P3cO4nAfillTe9lC-H5FvbPILetPFoKi5jjech78t2Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vn8dzO6uH0svxDOKHSxNI8_SO0TsJruTYge3jfQwCNjOHEmJb_hshAJi_H0qFRM7D4iznZ_Hnappu_aP-VAEPkzF5ltSGpq6UySxAu9Jb9a8RhKZBy7BiMXFBfcbXX2N32UeQv8tDQkE4qFMU5Io2iiXulNoP42y7Z4qw82ttZGos3rmJtBnPAsPQ2fxe6VtZVeZRw4_lboVrm-MkPiropRmKRbs8_afAPMkUe0fTIS7Qle8eF279HHZc2JjG5q3jHIT23vn6VWswnrDPYFrHbZbMCYkgKriySKp-P-J8ydKorQxFajvOUA59rQhvGaE86flQ_Er7L0ejAWf1CQChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/guRnPCceDYq7_v0pGfo3i3YmVWdurEhDtjRxyKxMsjgjTH0OMVgrGz46OesQjPLHCU5Nudn8q4z_Q9FwpKGlRE2LCk8Hxxyc_GAAO9Wj7qVhfcudAQ5Ap55svCL9OSlVIihJw8tsVskP0HZOW3BjJ_6ZDENQgjk0159YEoIkKvnaM7RfTHnQhbmNROp8pt3aO-fxMpr9a7_hMJsNClaxmcY0cgnIMHoeSkQapYSN4ov4Zy_anw2onuwdCQjVMpcWEfVVX3X22WU1MdJ8C-Go-mRwfv2Nuy7IE-DkCy9PxNcYoXSVfkD2n2rBTuLW94b4HgOnFOMCNpgqJIwCnyff9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K--fuqwmUydjaOEL7SsoRs47dKPla48h228GAFkHcIiw8eeN8W7w6xk02x_nv0OakqCbRXLImXy2Vi8_Amuv14icImPQ5DYu5WALrInif1wzTXdQRewDUHQk918OsTISYBY14qzMkKnIIKK0tQSe-SZSSeO4mqps9pPWtmmyXBtW2RaeWWihl2U5MXhWENZZDURlhWNbD3hKofT3Ibl0J4whissU0gCDnzxiIr0f4ljq1VcVnpU0p5WGnAcdfyPlQQw60Lzc4tu0y9VCtKAQSoVQoKJKUyljihgvuSFTpaIykFWLxA6gCI30do9KXuxzZBkJMcQeFpNEGNq1CohnyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kO9fk-ziXiT0a3yPgo5JB_wgVv8tbW7bTR1Re-uLkCoIbKNe7qB6eG0epba8R6OeHmx7mLlb4ls1Gsd8vmz2gbtFhLbx5QMXCloguuNteJPCz8N0xQBVmmLZ8qk02fq9zxt4miikcZtxp19dheTymanwrupMPMRS8N1QtBbU4Ploi63WmHYFfoLXa4o-GSdcDMJW9vijebZ8HPZ6wngMcuCpqDRNTc03y1I5D7-vZ5Hkk_XqizjHWJ1Ptk542U3OONQDKkvZyW7PetH9iqcKW-4dMlC54htjwLC8W5utUVTA4dgEP3V5JM2bmPPz6-WyZ5wF5ESyz2jCw9DT5cTEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIcPJKkxIw3LcTZX5cJ4YJD0hE21A5b8mZzA5q1ACRm138g75t9tbcNrcFNRDl7e-bXN-sSTNVEahKRpUSKQZn77oCMFncD0-8S3lq-m3z5xpbd6imLovQ5HpRFJgAGlNI-v1SRi9-lZfRPndjnVrbRuOAVHck-kxG4cX25zzjQGQbYyJGv1qx62WyewZitIhpRtQiJcJByJFkqXD1u5NlBDM3-tQQi0oxtqE-ame0LU-tsaZnmcyojaJqa3WTSWxoJ1QYiJJ5MMDJVzbpPXXAZ5NSqtsACjlAY47CyrakV8z7lo6kFkj4ZWV2KxJuWrsUE0VqNJTm4JU02J1HyvYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk8jyaJwreIoBsmKyHNrALj2A7lOnoi22P13fpibmNvkEDfdX8_BrzfryUM3OovW1FfvbinTkICQRhXHCSefKtAXNJf7Jp0o1KG1RCHzU2e2B9LcX0peTzQgjFHY5P_Zz0yni-cn2y8Ba8ALxCe4kLyAlzxludf8ohU3QbN3udq293yKamQ2Bd3OYAU4BmJFQvFX8-97cRZqUn1VbTN-Z9EWbzgdNKyKegq3n_JZYHS2gm_YxO7kDai_UnDO8sA87MPoqY5fT3w8rtLZdIjSxWiTwzgL9dkm2ra_qzcM3Cp0StA8KPEbYelmYK80Su-qG1Z948xsZHxLWcIuDHg5JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIEllOlpuBpuiYTHLU54aCG8CiTUv1tG39IlmjQem5XfAYIhOrUxliMEaDyW9mcEFIi2r_YceORB47n-MxHS5zafGEhgQtKAEEjXQf9OK5LSB4mUFKmFXcmFBTasJaWLzpJ4oV3OUn4kVOBiQqK-B1MOE8qBNf6Arq9aTJpW2SDezNTSSvQUDSgIWLyG-vCgEEXXkxzkKjfKoUwuTWH6xO9PUGsrtKKjzpEi9505YTHCsVPoOkmQ9mBakIWRBP0ig0uiBb-Z95RU0aFOAGce74DuRUe9sDdqOLFKQu82rJ442rpWyshB01mqICjAnJRpZb4WjP5a5Uwsp2755XuIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nGPR-x11_lrZFHtvNY4kJJFC1bVMqgqu_wBNaeFgVlIhiOzQrPBymAG5P3-rYy6WbBO-B3AHhZtbnkxkM6RhDSLNcwX7KY2e4nHuniOUvAL7gF6jJ2Ch0LKf0ykbZM5oegMz-oaD7-RGClp_CWPOjx2gbMiu9UXclCjSwpqX9UXLZxkd3SKMCkKuxE44lARH6OrDuvbVv2ra3aD37iQ1sLXi9N7kQkT3QZUHCjH3M2_l6xd-9mL7BGbXn7gnCggrswnypMnwVghvGR-HF6J662AlAtNWn_-zOmjOlAV-nrSYPTjZxCKJpTfX9csBttELnhfYqq6gaC8oeAqGJ6ElHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dRQebFHoKwEbGNLXoGj1dRaYs_fyxoUQlzEo9FL7YEX4Ri6Qn717UGHHjgAGS6VW3qy1hFFxeL-uB5D0p-02xa2zazgYLji98BcCx-iGxFBPmPA6Mi2iQR2rcOt7OX_btrRcm_z33wN1fv-_SJTkIFJ4gdo3IgxWeTQqz18zf_-KozEeM63DO86fQnhIT-5RHyyhVgRGqnAC-HAbnS5RRFWOBnckKceZkkBl5V2B6NtRcq_yEOREmE07KtLU4r_nggjEsKgXZf9qMsNSzmvGkdet7sasb7Q_zWm4iYdUSqc9lqWPkOXKTqh0E3nGshZTLb0j3rz1kYw2vvuDCYjkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B7x3XlsPK9u13Wdc45VBF8IItl56ak5Mu58ERNufE8KHpzgtc69ZdRV6fdZ1R71KWHxIh7_cL9lhHEYxh1YXiZ6w3LblIetBVjYCgspjiPVwhOR2fS4GlDd4fgmBeOgt8yFXnDz7MI8l3nrJNpYABar8k0xsAqAIFlxFEj8Zb7VpSG98sLIHQMKHJhZyUl1qz0UxJw6MBtQoynWv_4nUyW3t2K2NWeATfg5xUgyiBBEXy8kZ5WUkVuVOCszh8X_YyiT8_JxE66wNz6mS1eco7lL28QOkS_EDshKH3FTbN7_0fSnhMVZTZ1nPHfh6IvzGn3ugzCM8VcUnVlnAa3vPyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avLB_hqboVoAHGe8AbLjZop5wJil15kICtBIdBt_VhK0RUI1vnC5r_8gZ5JxjaXHP91n7VLrD47FBH7Uy0yyJxW7sqw21a7_3Z0-weORsbstJxZxP0MW3YCp4PGml4QL9VKvCdQltoiS6mMOPcuGg4q6KU2xyu97tzwSS48DYI4WCE3HZTDfzGC_rtJmP-Y6yyzOvSTOH_AVTrseLlYqPAhbj8-dQTdURbQKKQSuu6ApCWMmU8t3Sg_C0Tr3Y1Oj7kla9JwgFy59XQ4Z0kCXb-fzH3hinDeBLGL-iwyOe87k4_rvVOYFP3MH7NwauK10LdRhDPP4-amAYOKJRCRxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jF6bu6q4_BYkhyDPDMo3mRlNMACoVMKVHKdUYvys1npTp0XRYQ5Ru6q0nF7i929etGpXKEzgc7zjYQRtDVg7G15XBXCxOhEqhPDyQrVjrnWEV33icF6UA6dpEi7dpGR7Vp8sRIelXGxYNZXYdJqhtwspBZfKUbdPcpdQ94NqPrAcg6bWO0ZZNbIhYYhz1VXB2qixAFUhCS0dzLDbon5smezL5Xkq87QFICHPDyadwt9d_8Pn_j0syPWFfb8vLYGz4DCpm6CP5BQJJACN3GmII1Wvndfk-Ojl0uldvC3H9jSFF33j6vsgttGt2SYb6Lho9L2fYMo4ls-kjoqC3qHlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L0a4yq-vBb0Ayri-j3HvRGUQLBu1Q6r7RzMUqQ_jQ8N6dnrfTW5mJExx7_RVjPqdy_wz6CsXbkCcecrI2Gu_cC8b69ksHkP-ExjEgJx8SeNa-Z-dkFBipibuizZtcYMwb-D_XK-4wJaP6qUkAbQF_pZo36iZDeNZ2CEyW1rpW1UOTHCuN1SWb-tg3ScgkmMWhmg-TG53s4r6w4pJPHZU4Wvk1RNumBjERYMUCUHaN4ZdYGibr_xvtaUvWG5W_mVDS0SuSQkR-M1FFFOl4dcBQIsflDalFGkGzCTWMUPBEN4tNmUWtj19nvfCShUT5EMNlw1Ojoo6xWxcJYUCuD1ZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRWi_amVIib-A7HrS1bNDCwSd8mlug3QfCvJJ0dJaTOQYa5A8Egy00_BjtiKPBbcMJK0zw7TQ0vvSc6R8tobpK4w3tyxDxDJd3JUaolP0NGaLdqA-jQkj0oN866a8hFYDsYhieTpva4nSezorc-G_I35SJCLuLPuNO_zRej6NICx4kPAA8aW3xSsRcRqcEyZJWQJQZU4rV9YR3MUkWdzTEJfRgyFZ3SHfwnWVgq5h6LQ_ymLXngulLVtPQRn2xID1RsbJEtTblA5owjv-KFWIFnlTPfZghqWkM7qzjHQUc7pkGSRMM5HV2Jfejzp-NreMJ6lUaUw0M9oWl-XVIYBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCN9VnsWG9zskqih2QoS7xG79ixAp6Fl7Mw9il8CWA7dFXGwyTWwcZrCHdfV4qCwUCKYsoa1Y6Wk4e4YvkqjQOegAD-iGyHbWInic3xEv7pOq6o60j_crufgDXwsmkAvrySbOWtJOezhLSmrclVC6CD5kv8Ypm9lgjaP3ol4Byu0JQTjsDhxA4VL8fMofSqYHQx5WvPP_sFkd3uXrpDa1tP2h7PmiuOQuqm_eNcr2cBIjf8czFa_0W2UR2-LLc8ej1HTjHOPm536B7iIehgfDRobF-U9vfDp5pKePCKqWTa6gop67UoJrWUbL2vWpQEU2ixjaF1cvbAph82Vm9IeVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iue393qd5YgGHKdx-R-n1xeGqJ4quUvlb1MXKIMYzKgt80zyPyPqith3YB3wMrwNkVQIq-Zp_4Szr29doXfIcauKoGG3AXZqzeHZLdeYD4E-UmJQIAa1BnOXGbaZ1mNIE89pToZbuQLSGGkG1cUPmZrVwBeqxS1dMKJK359JHXluTuscGBUg-nXfYru1b3IDgY2jt7XxTE-MKjNNEnFj4OEua-_VOT-uU2oyGwrbjZ7XA8Xog_XJVumHDRvoKAN7HRW9O-PyKXiUCmFrclf0X3tHH9OA6ReIgGyJs3QTv6HcvIGujhnjQUK53X0e503Zs-YW0BIdJ0yQBL3MDN1Tmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Eti5P1uVaW0y_jA1_VwoUr-ivMtL8_JD0gXsqNIGftID7aogDU-LCXynZOpPKTlSGwqSznL8TOb6KpLl5BDqMdkMsx8Ty5q5YB11b9HvVyV59TV2PbUT5hh-8GVVL7Uz6CljlMkDm4fTK4j60tNfSyNTyWwlzXbPUROgasQ0LsahwlvkeG2fPzZwYLPOYeCS4AWBUr5linnLAn3Q-InsO3JGwizyIblglkeXCH4J_vWHNXGLtJuSB2cleS85cqXgDr5nTnnfInv0QAk1_PjyuvLrcyX6WJgPSWamGAGIBoZHZhkY9rRv4_bs2VIP9K1ZfotUgwQX705jcyrfEepHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e7YrKNqk0vsaF4XVMYVpH41CSoe5q8x-2Ys0zdIxeOC1YprCxkF_QelwQMlGIlDRoYQsjWNUi48oaRN2luqGGMtTuB7H8CxpegLkH8PWFEViU6mXp2SRHpYbwDp3EH74U6OBycQ-SrS3_u6SCq9dq9bi_c0lRfSFmKYfj_ax8w8WAOkw_QVV4pK-0KWvmC6MejyXc8evMppNHlv1ST0at9euPwOOWF6U7JNTst-QaohrD7JkQfbtbQ3-HEOjmNd-roXZl-sVWFJUlXYwQiU3frlRIXf_rmqW5fvkU9hRBzv1vwEBu8rYwYNXUoa-Vtp-XnPgYVwuqUeLcBG4Pds2Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nFZjEc-tL1r8HE3TWev_H1gngwnvBjefKH5iLaqtGWm8UWluLJjBtvHQfFAPdSVJPlOG88BVvzrZVHuVkmR1ynqwCUfRBFT3n0MQ9Zmj1GM6hDmshG_PXteme6vve2zJdCrD9KnKP33oWYaumnfI4Fzi2PI1eHDcPUTgCgbYdhGzafe0oItjuEFntDEf5ulc-Mzr-GxAV68tGqpXwBWlGS52DnnSZaak6uTbVJHS228VNMOEV1FDtoG7U9aT9PIGxod6XDb-vCr0CyaHUUtJ-YeQYba4rn3S7pqHcKS_TmRskLWoLG-1_oGjdnZCDXdOBrPe5Wc4t0bppkUZsZ9BYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/al3DTCNEv_Qcbxc15nzXfBj9vxtjug2UwAqrYdzvsID_2uf8-_mPXIqqujTb0Q50NIe0SWo9ownFx39aJ3daHr2RB-suvaBxJIkB9hHFXOkCL9z86YkYnQh7BSaxU5-T-lZPOKSO5ab775BQ8pPSyd3FkY4esQK531fqP_8gPnwfY6-NhUi_bMZi37aqKbb9d6FKGv3H7rHWHvM-o_w665lU-3o097kycVc5DQgofoPTOAdhedIPnYXwDPXsguveRr8DyMH6jXVrbI0HiUsRQTPOTFyF4FoxzzS1pwMi_oId3jUu4QJ8GgEsFjYENnLWQz6i-ExC5zIcYjvZ0E0Lzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sen1HdKgd_7YAitlm3qCVWFtrr2I0EUbI7fbNZiMa3oCzBtDIW_CT8VM-LwB7DIbLsBs9BefwqXND6wNLk8ZAWUYB5wzez4tMOn2RoxhVojdtV-ae1UR8ZCJN27iB3GmyyjjU6vMzTFpJIvLtWTAfMmojn3djCTp10a77W5HUPggkNEjAkweXenfG0zw7cOxYzpA5tJV2Dk0SPgKdhmroH7wa_zHridFYI6_R1AI_dgcmwligioXatzu154Abhh9XotLrOHdbslX-IjATyDui7rZqZJpdhaUDeFI4H6SokehNdnhXSvJbZOvd4extQ5-qElKS4hWqNiTcCRZsiDCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cR4fiz8NB_JvIcqlP1-zuU8HRGaD3j1W5zSlR18KnpsJSMVBbFMzs_ahdAaeRCnf0LgeBWlLqoIvzCt65H1s3JwqfMwh6FC8hauEu_5G9q0PRPTWq2TyOcekzeMYGy0GVJE12CHbke4ZbBTKYcs6GaRzeY0T8yW9InQU4n3lv1GffYtyXtaK6lS-wyDm3q9lFuph6Trp5gDHHUpItx2pUyBzrcXnjG1_08BCeMdB6_NILbFiJTKfUjq3MnXy_liyoOsVLDv898UCSmM6FB1ab2nj5A_6NV4VhfxQYuQJyvOjmrcFr2oMVsYjLsw-8aaycSvARzxP0e3FqeWDrGMhxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B-M4ZO21OI0VaEE9e19K6qT3eN-KlYMIGo6sNNNHucPJmmjvJEiWMwDHqYleo7ypfawkmvaa92UrwlR8-u3RQIw6mYOZjJ8tFeHsQ5tRH4uAJVTPKntolnYzBw2_KF_iYel7m4biV-Q-AUQglGt-ZbDDurAdGxkmjTkjj2Ng_rW7X_tjAzc_t7m14sPpQrCg_jB8dphnnQnmvIRVKDmTpB5FLqpbJUUpNcGhacWDOFA4BLd-J4Td3So9KBbbHW7lgRi4ltGBHjFD-avojWJMSanBJMpTtIM9kG2SxLs7anRffoVCNJw61mGHxQNoLuyO-GgX7cwQJaJmlAlCtyi0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=mknJP45Rgq99fDckxD6VuVssjjfXv8iaqJ2iz_Hji_2QBtGz3A_3kgWNYwoIq6rQvHi2YJSNjzDEWvQJvS219lgT30rYWxUiJKr64LGAmqyZuuc9sPznebwaaA5hCYcKSodeTwhQ1BMGHC6F-3sqhcwLSfNnCC5Ssx75hO-RZL6YyfVSMbARmAfrmLKETAa4F4DE_j3DocLBqKMaEyBzzHHP6RI-A3-LB0Ch7FGzWwIiOEVnMSBCM0O3xsYOs4syBuRSkCPZEr1SWWvISN9AyNSgUQxqQYt82LgjZrndILveho5uXoW3DiQmg1dKUn2xjsYLtSbzVAKh7QlbTE2tIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=mknJP45Rgq99fDckxD6VuVssjjfXv8iaqJ2iz_Hji_2QBtGz3A_3kgWNYwoIq6rQvHi2YJSNjzDEWvQJvS219lgT30rYWxUiJKr64LGAmqyZuuc9sPznebwaaA5hCYcKSodeTwhQ1BMGHC6F-3sqhcwLSfNnCC5Ssx75hO-RZL6YyfVSMbARmAfrmLKETAa4F4DE_j3DocLBqKMaEyBzzHHP6RI-A3-LB0Ch7FGzWwIiOEVnMSBCM0O3xsYOs4syBuRSkCPZEr1SWWvISN9AyNSgUQxqQYt82LgjZrndILveho5uXoW3DiQmg1dKUn2xjsYLtSbzVAKh7QlbTE2tIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/pCcA382FgTZj8qUvO1d_lN1EdGIaBumd143SXLNNml8z4VmIiP0s9JUIOAdrqFFz_cMxOT0jzqRuVYkjJyWS3502NYT5757po5T6I92yedTcXSpP5dYQwdJwP8LBR4nGIdLS1GRhEBRyBU94R_AdCfdHxz66tcarT57AWEat44ZxHKIb92HbFCCQSLma0Lo2wOzUU6fmSymmQx93dYTb8hIMhk1IlEh3vPZV5puYUGP_f30LfelR3ntQ5b0x3Hauo9OdvYYmUqGiS8B9wHeO1EKZh_cRp8dJ6UqzuZm672tJeLqEd1FoeAAYwzbNxgOqe-C_bmYZVqHx84T4IM1Nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/X8NxKzfP3Dhs1S2dSIU4bm3aLvv54XjYlC9-q_2WUh8Qu6hp-gIkCpsO3_TMqBklRSzcbcBAcwGaOiqcA04VEWKIaDn9tFxgk4IHGALvO0rxrnEiS59t8ykD2VqZPQhwh7ZTppvkUVD8kBsKKF1Wpi156Z3Ar1h3QcaBBpZyqegc0FuDiMBnLf2mJCVzr_Ocshar3SIIRdZH5Q-hr5MT4HrT9X05flGpz7pJkHgDK9vFrKgUZoGzGLd6hBk5WzB7GksC5NLVAhmtIgGg4ytDHfUxprDDAvTnyiAQaMIXhWgrUJ_C6iIf5Vd99IVaSZqZdxAwBaq4jyO3GJkw3jiftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/tVnxa12Z8yHkYMbamhiT-mOOgx0zAsYa_dyjQOx1j0LiCLOi7vax4ooQzH3T0ciRlP9rSjoAW6D13402SN6qUZLs_3R6s5To3wy-oKLBOMMofbcyZHUkltaUSJR7JFElBFgcE3LqtzcMmOu8wEhiB-Mv6DKlXv8QHJuPsjq3BF3rtycAWl8-uC_LLlv6IlSHg-Qd8OSo5AuvqPO6z1uQWiLEMfCecgydEafgdWd37A8n9TzZ6k1RyCRoMN1_O8jljT73I_LisUti2p6f5X3KXfPkyYMFMj5H5E3Ao0nQI5fJf005XPpPoLqx_NkU4wH8MuE9DqtCvnPqu-sT1QzEqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3ioeJU5Im_5C4uRNNIuwzdS3giKbFGly_6F74GspUsuPGMLXZst7NG4yofxw5pfZjfBv8c2MHIrKAbYrS1wqOTnPWs93dzGVqeCKU0icmOILdRjuCibeskrExzpdrRWoGjRLdfrhq747WI7DefSeCKoNA7W3xdQmKVMX9shRWR_dZgfi3fEVSOl0Plaz5tjBlxBnE1A-eqkrAv8Y8ivP-eROQj1oN3tH0clZmoP_quwYdZRxSo_SGf9PcJ2W-9EtU2SfA81A3PQ7QRdPIkLqE8ysfofT9ld0i1qvvpLoqFKdcSgUd3lVNOoMd8jEtjCCCqWXvWTjfrx2KIrsRhCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sAxK_JyyNojQChRJ8xF4faSSJ5ptCGwmJqXgiAinKihSYrgEq_QFigPYfR3jweNOZDbgciFRPfTR8AT_q-RJre77EvehQmZw3hNtguSaa_TDQMJBmN6AIeEZ1DwyU9ud_wUSjX0AehX1n_G5qMZ1rnK_RTPZnh7dQOcLH0L_oUqCtzyaua_7ISrndQQ8E2_Akjizm__f5i5oFEs95Yg9HNUSb0-uBwjYjIbeMLty3mm-qU3jsAjOVgDDlHwWn6i7EhjBK8xHbxUmaey1-h2Bf3n5ig02ztXs_46xYn-U3S66g4llBaw8kL3FoGIJIzvKyJQN1jcPQodmtJgaRBa8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrT85bXzRfp_PRtrRkbq-WN604oFmsV4B2XLw5TTKS-XIX9SuMl50nyACbKWqA_nw05Q0GEX5Mam9H8N5qkPCwdAnb81TuFs0uaNrBOvMYDb7e29szwUJuP2Y0aO5TRCRjqwFiqPU7LOi8p3MtrCQ82U7M_8BZ9MYgDivIJw729Yib01rV9xvNDq3GWpo9aaI41LOoZCPNrrFDnv4t5L-PdPsuwbWIWcNPV-Ey9j6iURhcmJ38M9tLnTU3xxLwWq_oPsy_7F95P3F_ZCIT_j4L57fy9FcAvZg3sfxm2_eBrWgKGcdr9QKSNvsmTNEcA14AGUDIHmP-VJma3clfhChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JtfTEpAjjyikREVFlW-3NEu-OMUtkJmLHF_8unGFUwHz15meRpfHtwhd0YWUXFDplEsbzaD7ytuzCm-597x7t_vr_qlhkxvOTmH6YCdaREY4dIGL1q7Or5r83D2uQ04HXEnxAAVTHAShdrmlK95le0tOaVEWTsY9v702KWHuXJvaxmiyAcenKl7C241GxsngOSfM5FDEDElm-jxFXFDbBfmUhhuPRdsGkH8A3T3uzrBFmCn6m7T9yFhzPIJC8GwCVFKajoE0NNUqZCWhg7cAdxiGdvZ2ElPSLmbbAnwkvAU0vkx9nhC0K9BKXPMF6VLOk-32HpCtKpqubTHzgfteNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpIg7EeqRU-nh9QraQniuSV4L0xknLv61j7ZTGLXd2OUfqCw-zq87flNGI9oF-48vgwVs4UnqiDLfu4V50h4M1kqNHJTrL3k_9ZdvrJSYdfTyllRKrhBVP_iaet4kKpuzHvCmVaom_LCWzFM_bYzI4thNTrVxtqCFlcnevkHrBwp4OhVMTWWTwR6yeaCNHaJomXxB8yiYjy9mFij3kYPEnJeSaesw4YSlintfSIa43TA7hE4cuxJxKp6eOLhQkOvIctoIRzbyDPVOfDA3T24T5Tq-8prXnLAAr-nkgCSQoBOQJ6DybtkLcqnks2iiVypstmuS2rmPYntpAC00N0Ofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
