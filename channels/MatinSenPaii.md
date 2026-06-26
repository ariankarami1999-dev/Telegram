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
<img src="https://cdn1.telesco.pe/file/c2hmYqtXQVfoAMMYEmpB5KeAwxLF-Bb2B14MTX4DZdJDIscPf9KIJHt2dhnrRMlPAxpt4v78sXC0MUJTeTX06hxnmhwaWF_LUut6OzFVg2qHT0H2v470SRWHRqWxxeh9s78vJI8KQ8kLgWozNnIuH8_Hfg5qa4ZL8VQM0kdNoOVO26cA3larJsEJvFmhmwCELibMGvVBz-Xa0Pb4XdQdWxLRJn0RA09L10g86AppqZ6r9pSqi7zCX-S3v7Y92fA_lVvedXuhANsxVdi2dXz8IzyJM5CWRdoPnVZ0ExRXZIZSZdzd-mQK1RF9hxeeilKjqiXRxj5DkBLbRkzkfv507g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 06:03:55</div>
<hr>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R4B76WvTVzd9NPKAbbU_oyhmyeeQJebQiX_YvngmD3oySlo990SHrXY60EsJF6Mzp2cVVZP591yO794j3eq6X0JOhBIkWyp-vcesDSsLvuo66-oTILh55dYPBTGhWw2bYidxjPIjcrFrqz6-g1I6wdiBtvorij8lAL8ZIzAxUySl85cRyX6tUyKUkOJui3DevyacAfF0ha3_KEoEz4NR0SUq4NB3XF0AuuT47rLg6rmMIgGvBU3zCFArF8etjEAMqZ7hpxbltOw7X49Cy6Qw0Pq_A1Dus-mxdpT6dhZRLI_XD5x7UXS3kSUUYTmQ34egURwfM-oFL3XZxf8liy3G9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4037">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKXxvX6JD4vQ0f7l0vTJjtCy1pmxmWME62PkhJ1Na0alg6Tiq79NCGqQDWnA2yadDpBTwzopboNcOPX5NNeA1vE8NElGs7cvMw1KN3Ee_faHNLnUx4m55VrjseVsQXeTFHUrROL6eKjtDROmPOQvVjopNP7_94koHo5s30PkJJsEvpPaDypKC46tWIbzIEQoarbRSqTTo3kFrfywWSUBzqBnUthm5wrG8sAlDIITIMpuj1CsLtYmuVg6HmVbREkEA3AmreVPfL5S9F-qVVb9I7j7w8GmQds4Ireh1p0S-0pxXcBp5-QGikxKPoGHTN-L8k7_pSGAdN85OjPDxA_O0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.
عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:
https://t.me/MatinSenPaii/4023
)
این ربات تلگرامی که One Shot کرد، کلی چیز داشت که اصلا من بهش نگفته بودم اما چون صرفا فکر کرده بود که "منطقا" باید وجود داشته باشن، خودش نوشت. که خب هم خوبه هم بد.
و واقعا نتیجه 20 برابر خفن‌تر از باتی بود که با MiMo(که خب بنده خدا مدل رایگان بود) نوشتم توی ویدئو:
1- بعد از اینکه ویدئو رو میفرسته، خودش پاک می‌کنه( از روی دیسک )
2- به لیمیت Bot-API تلگرام اهمیت داد و محدودیت حجم 50 مگابایتی دیفالت(قابل تغییر در صورت ساخت local-tg-api شخصی) گذاشت.
3- کدها به شدت تمیز و مرتب و با structure درست نوشته شدن
4- خودش چندین بار همه‌ی فابلیت‌ها رو تست کرد و تا مطمئن نشد که هیچ مشکلی وجود نداره، تسک رو تموم نکرد.
5- بزرگترین تفاوتش با MiMo این بود که میمو صرفا تف کاری کرد که یه چیزی باشه که جواب بده. یعنی اصلا فکر نکرده بود که این قراره یوزر بیاد روش، روی سرور ران بشه، قابلیت سرچ کاربرا باید چطوری باشه، لیمیت داشته باشه حجم، و... . اما GLM کاملا فکر اینجاها رو کرده بود بدون اینکه بپرسه حتی
6- مهمتر از همه، یک بار فقط بهش گفتم و همه رو نوشت. نه گیر کرد، نه اشتباهی کرده بود.
حدودا 5 دلار مصرف کرد و حدود 140 کا توکن، که به نظرم ضریب دار حساب کرده خود AgentRouter برای GLM چون اونقدرا زیاد نبود کار، نهایتا 1 دلار باید مصرف میکرد برای همچین تسکی.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/MatinSenPaii/4037" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4036">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">می‌خوام همین رباتی که توی ویدئو نوشتم رو، با GLM-5.2 و همین api رایگان agentrouter که گرفتم بنویسم ببینم چند دلار مصرف می‌کنه. با همون پرامپت و با Cline اکستنشن VsCode</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4036" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/4034" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4033">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4033" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4030">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A74BqHTvrOZqv9-FnqwS6AuweM_YumRh_oCxaK69BFSDeVUlAAVs0XrHwwRUAVjErYTD6QtunVCplOqnofdpU6sIo_ZuzPY4WQ5T6R1G_XjJuQ6AmcerLsG0-WzKUQdybLEnFl_HKF3dOTtMU-gOeWl9yY-amHLPZyP_P1ApM7kFb7uA5xNzT_nxqP9WrMs0MNhtUKDB7Rwir7UHjFPgUjJkznpAQ5D0JNcIbjg35VYzrO0D8riImczz0g1-_hs1jeDUJTzj9Ax2GMn98ZD9cc3h7vTTDL8vdbxHe8MwkgE6vqz-HJTd4OmnYeMgoKVcMwQKMb2XOIBHP-AHnqt2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر براتون سؤاله که چرا OpenCode انقدر شبیه به MiMo هست، باید بگم که میمو خودش Fork اوپن کد هست و بر اساس اون ساخته شده
🧮</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4030" target="_blank">📅 23:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4029">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واقعا یه سری آیپی‌های تمیز کلودفلر، سرعت آپلودشون خیلی خیلی بیشتره. الان که ویدئو رو آپلود کردم متوجه شدم قشنگ.
خوشحالم از پیشنهاد دوستان که تست سرعت آپلود به اسکنر اضافه شد توی ورژن آخر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4029" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4028">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شدیدا حس میکنم یه چیزی اشکال داره راجبش ولی نمیتونم ثابت کنم
😂
۱۵۰ دلار آخه؟</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4028" target="_blank">📅 22:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v4PDek1YDkzv9DFvhaFug97taHy5BBStLNEHfoKCCjjj5UhUj_8_cU14wnRv3Q4rl-WLIf_oWrRyxaJFLiKfYG_Z-PfXeJ0iugV0uF12aj5cG-sZXfDM8d0sKndnMXewLd2jtMVavkPGKI2uYPX9c6BnUrikmiEjn63HVomzs888ZxU0zKht8UKpGhipjwPEWWrszLfAvNo89RjbngvadIv70m8qF59GPDYdUpilOAPeSZKmfHmLu1yXxeozuceUUY0Fm8Yzt5rEYhNKfwlwZtvE0-yKXWZdej0Jbr8TMhmXMYqvnVKz0RJggH1iyHI29433CZvv3sJAttV0MKv7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IMVpPsHMGwF4J1Uh5Dv-jR6CEmyf5sg0J01rqNiOv_CKDETiT54hi3EAYnydgf7BBMqsNCo6oZCgMArNLN-SiG02Xyn8pd-kIavdEhkW5pfBV3JzkIfDwuxr0lF6DUkP-FCK7sX9MU84GhlI6I1JBe32w46N6fTEjV3hzQWshibdy55WHOVkPyX1s5yO4iGcuqiVjJRgnahuGaaADHE9qTQtMKANiCO7uD59VVYk3Mojfd4-qTnJeiiM6eVQfIdxvSIRKRj13GeyhsocvmX3tkaYwbh3bfdkq8MlOl1M8wmOpXvEy4Jr6eTZGW7CbqXlIZtebKbYW2YfZeMgjrsIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BGJCTUcAZ4z1d_c9hnHdnsQKnNNpALhMNTcI9GgSy1uMjy5i-fbUnIxj4aNi-gzwd3HwE-AWkfR91Nihe7XBirmmbUkK-UgA5qUskqSEVIulEEJmIL0brDuEZjYmDpKPNVZrPeRwhqzZg6gyBQY_amhH0OqjJNulE0yhjt2oyNJ1xHAAZjGZEkYWPNoP7FGTlBgXhy4v5Y2UxPvuFK7oFlhBOIYw_qLObJvzSyDWU8i6u0PDa1e78TBmDLItP8EQnO1-33nu7cqGX1XRdlSgSqdTX7xzbenaD1bBhGrTjbip0sLOY8dWjpvCiwYIF_OJs4cihv9drCL_I1c8QHxM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jSszhSJp_DSTVmL3EKsRNpXhWtmpUGGTE-3joDlZN9Gxv3kgP5MkTrOHSTx-5d2p0TLP9h3vn0jLHvzjvdzybFc0a5YIQvNcAVAh6TGZgPYlVgKHfGHJ9SEAHggWWclSIDqlJFV_KvJ7-5v8FOev5R_ZvNUT75aoGcKLiD7fNJdXQc0w9hi-TbvMKr8cRQpgrgmUaa6FF4eEQ_qMje_35hEaZi_Ma__VIz1L-fIfi_VXUNyaeBjvZHGRrNkALBpxMfxGImwW9FQwejhu6BuaQ98F0M4SEHrityJRo-qJFSyteQVFcfW0YfSn5G_dKAGWyKLOzlLW_CAjzCdTWY9RFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YwBX2ey2sEnMmgLc6tld6vsPF-coOOZ5JaTjnQ_5EW94GlGTGxvDJ6n4lLVk1YuctqtcJUx2rtR1WGDpvB4KFkIMdeDy9ekiA69N6lmFs1kvd1CmTrt6SulK4-9x4VtnwwC0N-60WkN7S6HMAxhWlWQdS7cwMB4WSbc8qBKJPoJCH0T7wX3r8XGx9rt-tinrxc5_uZWf1yexDALWfaxb58afkOPOOjXvpQDx_1k8bc-k1Hu-bg_MPh9xrqYFo9OzuyjClUFh30MeU1Wj8QUFeSfqxfNQOAn2BHWmtBDDJAFIOzyYdjqiXY-Ptb3nBmBEZN9tHoNYQMlV4LUBATHgHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این وبسایت، می‌تونید 150 دلار کردیت api برای مدل‌های
Claude Opus 4.8
Gpt 5.5
و غول چینی GLM 2.5
رو میده.
منم الان 150 دلار رو گرفتم. با گیتهاب ثبت نام کردم ثبت نام عادی disable شده بود توسط ادمین.
برای موجودی بخش wallet رو چک نکنید. از منوی همبرگری سمت چپ، account settings رو بزنید، درست میشه طبق تصویر.
با تشکر از
شهریار
عزیز
فردا استفاده می‌کنم ببینم چطوره:) ایشالا که نبنده اکانت رو
من خودم با لینک رفرال ثبت نام کردم، فکر کنم ۱۰۰ دلار بیشتر بهتون میده(به جای ۵۰ دلار، ۱۵۰؟)؟ نمیدونم. این لینک رفرال منه اگه خواستید بزنید:
https://agentrouter.org/register?aff=PvaZ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4023" target="_blank">📅 22:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پارت 2:
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
پارت 1:
https://t.me/MatinSenPaii/4021
#MiMo</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4022" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPTzXkDhsL1w3qyTYuThwjp4E3vBLgue91SX7O5uFAf7LQxNlUqOM99B6_VPlFHQmg23viofizj2Pkmy7Sd0g0BvaXziICgLkFN-gdBdIXegIBzzvV_X5FxUway5Eo1_sVm_CpINjHwpIZH7E_gfLuD-f3Y-Z_ZaZZAdEDjUteMGNrWOEL04cMFIAfTWwXTOscrffUx3GF72b1l740IZmFXUB5ocfxbpa3v_m7smPufyCEyevuKakNqFkxpcrDaFBQWOzc41JU2jFOnH68q4H_h0GijuE61VKpRkzV-nw6XWUMtX4Ua3e1ounkdWoVNzhMyEjrg1NEDVRCbsrR4DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:
1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید:
https://grok.com
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای مختلف رو نصب کنیم روی سیستم عاملمون
2- ابزار MiMo Code رو نصب می‌کنیم
3- کار باهاش رو یاد میگیریم و مود‌های مختلفش رو بررسی می‌کنیم
4- یه ربات تلگرام تیک‌تاک دانلودر وایب کد(5 دقیقه) و وایب دی‌باگ(50 دقیقه
😂
) می‌کنیم
🤎
اسپانسر ویدئو:
شمع‌های دست‌ساز لیرا:
https://t.me/liracandles
❤️
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
✉️
پارت 2(بخش پروژه‌ای که می‌سازیم):
https://t.me/MatinSenPaii/4022
💰
دونیت</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4021" target="_blank">📅 21:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">توی ویدئو از عمد وایب کد کردم صفر تا صد. و قشنگ می‌بینید که Vibe Debugging ده برابر Vibe Coding زمان می‌بره
😂
😂</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4020" target="_blank">📅 20:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ویدئوی امروز راجب Mimo code شیائومیه. و با پلن رایگانش یه بات تیک‌تاک دانلودر تلگرامی می‌نویسیم با یه پنل مدیریت کوچولو، که خب چون یوتوب به شدت حساسه روی ربات‌های دانلودر، مجبورم اون بخشش که ربات رو می‌نویسم و باهاش از تیک‌تاک دانلود می‌کنم رو اینجا جداگونه آپلود کنم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4019" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4018" target="_blank">📅 16:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEQILmy1UpVocldfM7JUcfIxN1nsLu6U6pHk73jdWPwe957zH9iyP8CS4ck2K8MkoumTHM-O7so3TFvBIF7fyY2WoGyu5pgnzpXiF4irpJ4Ud4v3qQuBc9d15HZmS1tTuybg6MYA0gcDucxJ_0TxFUChXuaXx3-3Gl_rCHqy9kMSkjQe7t8dcHd49Wu4bp-lM5XQgh-bM_YWTraexd5zI6aTqSGaW4L4KchyXU3qBZ2lCwMj2uc9JczjMY4b7FVAYtXYZFpPhbGyk1vOeEXKtsPj4ZxOxpWQrMkW7Jxz8_g1ecAF1fxSV5aBUKZqY9doG2iv103EKIl7Dj2yWM80Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تازه فهمیدم میشه با توییتر پریمیوم از grok پریمیوم استفاده کرد. بازم دست اون عزیزی که به من پریمیوم هدیه داد درد نکنه
گروک بیلد رو دیدم، جالب بود
خوبیش اینه که وقتی رقابت زیاد میشه، 1- یا قیمت اشتراکا میاد پایینتر یا 2- کیفیت بهتر میشه و میره به سمت تسک‌های ایجنتیک سنگین رو خوب(و بهتر از رقبا) انجام دادن. تا اینجا Mimo و GLM و مدل‌های چینی، واقعا توی هزینه و... همه رو میزنن</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4017" target="_blank">📅 16:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ik2-si0XFuqOhb8XDa9rK-a2wgO2Lnf2ykk4748C9aqc75-CmShD1qlr4uBJ-O7gjD2dpmyLvhizvf_hdJPmSfKJdpj2bsHYcCSs2zJgcyg9qyvpFCKk8GjxChiDtYpLG-NMuWCqh4xKiU3RJhHuq3HcVYTxaufvq55zhnLOaX_Aj5RJ0e_R46n6GILmhWUHGloX5vAoiMAxsE9vhB5SLv4g6rs5Kj6EF3_hv4dZcX6ORR-6qjzOB-SA_E_dlKGtKXDheQ4C20XQ-nuXn_4X-QPATBf8L7LphgUmjgTWpy766BsVxWeH6P7fwIj5U4DFgqJNHtdqs-ys_qZB-MlYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه بیش از ۱۸۰ هزار star گیت‌هاب گرفت — یعنی سریع‌ترین رشد یه پروژه متن‌باز ایجنتی توی ۲۰۲۶. مجوزش هم MIT و کاملاً رایگانه.
تفاوتش با بقیه ایجنت‌ها اینه که نه صرفا یه دستیار کدنویسی تنهاست، نه یه wrapper ساده دور یه API. هرمس روی سرور/کامپیوتر تو زندگی می‌کنه، از هر تجربه‌ای یاد می‌گیره و هر روز کاربلدتر می‌شه.
مثلا دیشب که من بهش گفتم جدیدترین اخبار فیلم و سریال رو برام پیدا کن.
رفت که توی گوگل سرچ کنه، اما گوگل بلاکش کرد و نتونست.
به جاش از یه راه جایگزین استفاده کرد.
دفعه‌ی بعد، که اینجا پستش رو گذاشتم:
https://t.me/MatinSenPaii/4014
بهش گفتم که خب جدیدترین اخبار ai رو بیار
دیگه نرفت سراغ گوگل. چون یاد گرفته بود که گوگل روی آیپی من بلاک می‌کنه، برای همین مستقیم از ابزار جایگزینش استفاده کرد. که ما رو میرسونه به اولین و بهترین ویژگیش:
🤔
حلقه یادگیری بسته — قابلیت اصلی
این مهم‌ترین ویژگی هرمسه. بعد از هر اجرای task، هرمس یه لایه ارزیابی اضافه می‌کنه — نتیجه رو بررسی می‌کنه، الگوهای قابل استفاده رو استخراج می‌کنه و به صورت فایل‌های Skill ذخیره می‌کنه. دفعه بعد که مشکل مشابهی داشته باشی، به جای اینکه از صفر استدلال کنه، مستقیم از Skill آماده استفاده می‌کنه.
ادعای عملکردی‌شون هم اینه که ایجنت‌هایی با ۲۰+ Skill خودساخته، task‌های مشابه رو ۴۰٪ سریع‌تر (از نظر مصرف token و زمان) انجام می‌دن — که توسط TokenMix هم تایید شده.
📚
همه جا هست، با یه حافظه مشترک
تلگرام، دیسکورد، اسلک، واتساپ، سیگنال، ایمیل، CLI — یه ایجنت، یه حافظه، همه‌ی پلتفرم‌ها. به علاوه دو ماه پیش هم پشتیبانی از iMessage، WeChat و اندروید (از طریق Termux) اضافه شد.
💪
ابزارهای قدرتمند built-in
جستجوی وب، اتوماسیون مرورگر، vision، تولید تصویر، text-to-speech و استدلال چندمدله — همه از طریق یه اشتراک Nous Portal یا api ای که شما می‌دید بهش(اگر این قابلیبت‌ها رو داشته باشه مثلا جمنای) قابل دسترسه.
همینطور با Nous Portal، OpenRouter (بیش از ۲۰۰ مدل)، NovitaAI، NVIDIA NIM، Xiaomi MiMo، xAI/GLM، Kimi، OpenAI، Hugging Face یا endpoint شخصی خودت کار می‌کنه. با دستور hermes model بین مدل‌ها سوئیچ می‌کنی — بدون تغییر کد، بدون lock-in.
:
📆
زمان‌بندی طبیعی
زمان‌بندی با زبان طبیعی برای گزارش‌ها، بک‌آپ‌ها و briefingها — بدون نظارت، از طریق gateway اجرا می‌شه. یعنی می‌تونی بگی «هر صبح ساعت ۸ یه خلاصه از جدیدترین اخبار ai بفرست پیوی تلگرامم» و کار تمومه. مثل n8 n سر آدم کچل نمیشه.
🏆
اپ دسکتاپ (تازه اومده)
بیست روز پیش، Hermes Desktop به صورت public preview با نصب‌کننده‌ی native برای ویندوز، مک و لینوکس منتشر شد. اپ دسکتاپ از همون core مشترکه — config، API key، session، Skill و حافظه رو با CLI و gateway به اشتراک می‌ذاره. یه fork جدید نیست، فقط یه رابط گرافیکی روی همون ایجنته.
😎
حریم خصوصی و امنیت
تمام داده‌ها روی ماشین خودت می‌مونن. هیچ telemetry و trackingی نیست. از آپریل ۲۰۲۶ تا الان هیچ CVE عمومی‌ای برای هرمس گزارش نشده، و به صورت پیش‌فرض اسکن prompt injection و فیلتر credential هم داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4016" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خب خب، دیروز فرصت نشد؛
امروز Hermes رو یه معرفی کامل می‌کنم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4015" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3-2MwY-c-kjGgTIgunQLBksbIxCSZV5g5_syeKTKIaYxB8pVIY_cDb_XRe0XBAGuMCijl0YXzqePMiBOLUk-zfDYBcsGPeOksW7DAclSvKLfg-fQjM1LVeIit5ccWDVG4L4RPJ44-0f64O3i5vwz4cHMFhlSOltXJc6mYj4Fpt2290sAq9TCM2MK-lMy4JdO9-qlGqa2mA7W0hvPv4f3BLxTfGIlqIwqfciuDO_fi2n60yOWcjtnMD1Pw6bfe7XqMnErSiEOVS8VEC-VAeZRVEexcKqiperQ97QHB4zeCu_fViPpDB4Qq5ZVUMjFSJqo8ni82ZSB-Ti4iSJcetZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UTIcbUCDsC90URzGkI5OjqJiWC-m97bT2S1uXInL9bOUqwOa6z--NKiry--xG_0gzh0bdbcaim25oeYQRITWif6pYQScUtiCGeT3MVHhpbeMz-BveYRsBpoZ_wNLjKfW7gcF0HIdDHiN6JVByzpl3jOUXcyxBmmy-egL3EX2r510Zvs3c1B70u6EfhwnnlVOkezrKR72ki36T62Jv9CiSijOkcQQvQEKYeEMmb6tx-pO8r-gNi5Tgk92emcMmWv7UzhKIoBE8a54sUwpTqYFL5ug579Nv973xI60S4d0GHzQNlEHaCX7Le7L8LYHh8eRNNuKaOcTCtjY1ibagES6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U9jQ8IpBsbbVG7-Wpx8ois38faTCMsjyFfHexIiUTK9LliJ79ULwu1d6L7Gnx_-4d_DlXHkXh9D8e5VENc1sBQyz5ABsAnpEYsUW-WHGa_JWQaGhEQse1IGhDeF2q0t-pYQ8Olth9UAu2biMLNWlPm4Hb9Ds0Y_y7XFKmKfYgz07aXmwAREVqgdufIek31_A7lXgy0YZDioCN9m3mMmIUeQlgVHMtdqWv-Mv827Q2-E9eEHVDBazHy4MWJCBM77YhoKSNkVTKy4EXelCLxKgVASZVIli_uBUYtIN4rmG5uJmrmQ-ADUqKyK0ArcWkQpvC4l5i8Y3IqBmA6oyJFxGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/no-AYvNqvR4HBTgM9VVe5PGDpluA4QkLZ1KZGjNaBW5Gzs7ALbLzIsioQpvWm3R_y70SijZwWORu6E5r0LvqGdUGB-VHA3RhdruO_IL02i-E_UH8tBlM6FY4KulWNKPKV2beZD4fpHTDc3WW1UNfWjEDPgUxYU7R48USRyGo2ztaaA_qS6RiZARRCoZoSUDK2zDJm4CG60_4PYMqvpJPL2yHComQINBXN9Z2Ohyzuqeb8LgTsmyzQQd7FM_dENEuujFsJ7mDAnuObmnuQcMQIgzLfhSCKJeMYs1Ia-yo5JjiGNKn1VNGOXrO6xNv-cA-Pwp-MKwY8V-QbWoZtvtUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4_Fxm3hl7cWNB0tIwt-KMZigLEXjdb4eXL1WUy80dgxRDuekrlMNOJSCU4HIoCm9z0eD0ugFS77vjCIWOKorOUUzPW-KXE2CS7v_KIAvEsiJQOsgsdl7IyrfQyMn8_yYEjw3nY9zBS2VLVegAjChDc9wyocs15lfAJxbTJLaZWLL6iPTo4Qbo-Qx0IvsKOdi_k4tf7v6KfOq6SFWr6L37GoCcvFo5IjeiffhgbLsmWC4pqV1NGg7aa8kFDsyieBs9_V8FyK_MTNi7Io7WKiXetSiX_twcZTSn1kFPT4ki4tfurjbeeePw35SHXejmVt8ilsyaLoOBkJtlH39RNOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V4st45i7Wugb94fHlYGXtJ5bRoqBLykyt-LAu7vvd1ywgtw2ix2O-ac1FZ9pjBdr4dUVBLQp-z5ge8jN6aGA4tWqgqZ_KbwwZ5zMESZd9OR_6Sm7IlTtrkEzTQhpRHK77pgNUsm37lYJoUoX5h_pyCh9qSBOTy22xk5pCxz-Yi2BFB0ESp-UWDSy1EdljlZ_IweBNYi533NGOry8DpK_C7WbxXnQ4Fs5PSsnrCXb866Qj_6K9iMBSRFunbSgD7Y3xgOI0rlOcA6q-8OJDpyvzOKLeftnEhKVObyiweN58ZiX4xidypv86t2qHfKRjkIuEx4gJDJ2r4P9iKkW3jW5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از اینجا مستقیم میتونید برید سراغ آفر دیپ‌سیک رایگان اگه گیج شدید:
https://www.openmodel.ai/event</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/3992" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/3991" target="_blank">📅 15:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n6fL_xgNTTJsdITamplHS_g5PRnX5przBvfOZDEu0FvgK0aDythoXTf30iRWjzxMC1jR24GNog0c6eRXkZg8bujsSZOiNb9E21sz9mj_qqBXYnaUEErOUg8lLg9bzF5TjYcZpdZ93cvFDFef6RzflOMG0BInPd6XCEb0vVqVcsHWhDbknsJMx4q0pdF_jDMyegieusRiwEWD78lL72uT_DSKjogQ_YXX5LLFSPUueeprVpP_QPoKqtLmgkk-JFB-lZq8ejx9LwD4mDjOlxt6duO1UGWRKMVS8T2rGDKnZuv0g2Xkpoplr-cZcNy5VMfhG6L_YEYA2EeL9h6sCVT05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده
https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3990" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Itj8ogGDYEE_OqWDYKU9_e_opWlJ6b4wiiejwEBmnEMdFKK2fuKzThMfySnroaJPe1WA1xh2R4XY7CdTtfNo_ZlwNMsTybYuER8DOgCkEFjm3u-2trIPL--j1x6xizGB7SN8RBievpCD817kzJvpVMwYmzFxTOyvIPryxVAX17OdOuwBDc_Oe_8SoFMiO5-KpY6I52ch4XSLllDTPdgAdl9Vl80bp2tDRchYc6nDRtfy0-AUQeErhFmDCWO2or76aNFdGwWgumQizNHVESdozkRn7388Kpy3qoUNMFEt9-6F6eAc4C8tQCewGbAtDTKw501kJnQ2WGmDwpJfxSibaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..    Site 1: retrogames.onl‎ Site 2: retrogames.cc   @Linuxor ~ fireabusefyan</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3989" target="_blank">📅 14:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3988">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx2QHcPWx-E_yrRj2EWA9fDcWjDn8OhlSEjt554M6xcfcfb1HnFFArA_Op9DX8nYXGeJE2QoVA59qstu_khtOlvjYPXNXvynXHoWBZ2bsZO8WDeqGCOumEDf7Lxpos-y07yjUu4PXcSozCjYpOm2W-KdxJz97ij25p1SWiNgVN7tLCNcIR4GlaHRk5vVrJEOIIFZSCjOAEa2N5wWBOPZVE8gDSapJy4B2p7oopFirLf0H0o4wR23feyD5Vlq8tjXPziiZvh9QBpn5AW2R2Qaku7YiL6cHai91i2NVzgIsP_-gaPydQodAVVd9IRVtPC6D5NNd5i7_CjCwtXNBDRC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..
Site 1:
retrogames.onl
‎
Site 2:
retrogames.cc
@Linuxor
~ fireabusefyan</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3988" target="_blank">📅 14:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3987">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده
اول باید چک کنی آب وصله بعد کارتو بکنی وگرنه ممکنه گیر کنی
✍️
ادوارد وانیلی</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3987" target="_blank">📅 13:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3986">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkpCFBNl_6XqbLaAV-bamWltELYbnecUOSFn2GDyjS84RYGOa7rQ263Hjf2_ahuz4Hao3KROeJW8FO8T_UqKFbnk2CYKYETWhB-j0EizVq1W3aUhIwyW8aepMLBNlLtFXkIpa7wgnIjrhixqnzJPbjmyOxdze7Mvy0ueIsBzMd04Mi0_Uk3Cv9_nGwYKtLteqk79yAuBKOIkmjzz4pvscmOHy-MvjN_WzeUWwNe5799LWhfGHJcvO5Pyu983rwwrpYcXrl_jKURD7QSBCtZatpRbLk9h4hk9sODSVvilyvaw-yJrxH9JM6jGmoJdvx_Lb2ek0xAQ9nEsqIyR308CzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید که توی توییتر یا جای دیگه، ننویسه عکستون توسط هوش مصنوعی ساخته شده(نمیدونم چرا برای خودم رو مخه) می‌تونید یک بار اون عکس رو توی save message تلگرامتون بفرستید، سیوش کنید مجددا که متادیتا پاک بشه و اونوقت اگه پستش کنید اینو نمی‌نویسه</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3986" target="_blank">📅 11:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRxbGeP_mhDoNMRJ4zC5bD0GQN47qBf3v8J7kUQkP8CuAhTXwYfKRuxVgwni4Sli6URG6VSB9PuiPfd310J_511cnyXX01IbMDIL5ZoOj97bqv2YdvWPLsfJIrAAS0wGQ81Gr7OzBxMaBrNMmuAtFXnQPugC4kbqXPBi0YZStTtELYiSpC8PrLUQJOgaFW0wjyn1jiZ_mI_VNixcVwbL-aIEKgL4nNAEL6iGDh5ZqRKLFx9xeuYgO55VSOaW7TdWoFm9F5hmA5bYtPAfIugRBZeTZ9fthpchbeZutRdD5JSViVfapMz40SZA11nMRKduQiS5KzvlVR2odgaxE6ZSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIwana?</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Iwana Proxy_1.0.apk</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔰
Iwana Proxy v1.0.0
با این اپلیکیشن میتونید به سریعترین پروکسی مناسب اینترنتتون متصل بشید
✅
آدرس گیت هاب پروژه↓ (اگر استارز بزنید و بازخورد بدین اونجا ممنون میشم :))
https://github.com/Iwanian/Iwana-Proxy
مثل همهٔ اپ ها نصب میشه، ولی خب
آموزش نصب ایوانا پروکسی
@I_w_a_n_a</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3981" target="_blank">📅 15:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">با تشکر همه‌ی بچه‌هایی که PR زدن و مشارکت کردن توی پروژه تا به الآن</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3977" target="_blank">📅 15:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KtQXRHDVEdiYcjD584D0j1DBCn3wxlhT4BLTIShtxduHvK_Z5yJtfNjhYdJ81ln6_Y5GvVmVUbC7knIxOqdVVAaiNNRdUdsuMh3EAUleEdCAR4maNMZW2JlrNRNw8FYoO7eKlhsbW2l_jnoMK3lNpuhrSZWzFRGPHz5_55hpgpAZ3EHMpqEiXCQ8MQhEU_8FGqDvJQJ9Odr3zQ17WHMr13YKtjZJw2I7-_l4RhpTgIP-u8flgsJ7HsOCALFbBGZAnB7bSmHjflmL52yccPGEU4qn2knat2qGFsWWfvuGtRu8oIRFuXteIu4v_2ZJsOm1tZboVBIAHdyMoTELQF-MDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/thdlKPzkQ_fdgXjVPmh3A30H3YX6QCRlVsKT7FSCdKoGasb6WP3Er3P4LQyjHWZoB3hpB5L3FfJZElhDYQ15AvWa1b3-XIDPFxrWJvafuzLzcbvIrr2eh-PXlhPr9aCONjcTdc_1vxZKDR11qgIcB8PvsdVDYjdMEjhsN9A7lPkRVIlYTUsQdp7WRJnmPkqPq2KHClvnpj-hZcbgevBl5JAUo2mnObzPtHBD153fm7NuEdLO09dGD-fPn5yRj8TPS0eAMhXWxD2OlPc2F7_gC-KNrNZFb7f6gCAE6HGlVeXhbFO1u_-rePn_9wKpOmL1BlRmt_hPQ9-EH4RnZ4OTzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متوجه شدم که SenPaiScanner تا الان بیش از 60 هزار بار دانلود شده
سایتش رو هم
Samim
معرفی کرد. می‌تونید آمار هر پروژه‌ای که خواستید رو چک کنید:
https://github-release-stats.ghostbyte.dev/</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3975" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3974" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بانک‌های ملت و کشاورزی هم Came to the party</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3973" target="_blank">📅 13:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3972" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3970">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sOmQhqqkFhxbx4IB-IBQpmoCZQfVId6aZlJ7IlqTqzfr830TrCoTfvu7HnPCAWk667TrFin7NT90HdInuOY97FsLZksDlL9Jm3tpJPkUE_VSvc8GhXdBZ73dF5alPye_6TC3eKfzrywm_idvUEOAC0ENyWLbVjMOxpCubLKwykkfTL_TmJRYAtanVlN1Ry6krZDT7C2GlyyZwTOyGkK6D1jC90G_h5kltqaaZmGcvLJPSBi3s-qzzQANq8OuKZ8b-nNodpVHm1S0SBGiUDPfQGg_tsElODN_Rag5zFH8y0aDsBIbkxU2KgnrJje5d3Pogk8j0ZyasTQkjY8FZSquJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U4MxHWzhYws8wf2eWX5hpwOfhuRhMWwRUTPofDBivzVffrtx2GDmCpbhUEUrweQWMuottuMsuL9MaVa1_GycDbOxvjtiE3QYa4ZZz2rh5y4E5Z85GuvZ7qjHjOYGnJ3i6LcnYHxBaxE9uuVTBWcfoDLuoSqfsuGGqCdDVhl6K66E-5kri-9-acGhNd0dk4ukT8IM6eqwqmdMnjWJm9LNBpREuw5cV5hTSyaOgXl1SVtpcQFdAUKojf58WkkOWth54q-mAfIh7DKSkwg8OgyUQtYKmcQpWIz938y0J6TnZyk7ffvfy7E2tvaVZrcUOwOIgFfrtSTEG8FrcIk7Q4BO5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول: یه سیستم که تقریبا همه‌ی گیم‌های پی سی رو بالا میاره با بهترین کیفیت(عکس از
glock saint
)
عکس دوم: لپ تاپ tuf a16 ایسوس که اون هم خیلی از گیم‌ها رو بالا میاره به راحتی.
و طبیعتا با لپ تاپ شما هزارتا کار دیگه می‌تونی بکنی که با Steam OS نمی‌تونی</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3970" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3968">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CR1WebJJnHHQSUEFhBkjJFaKHSrv7dSQrWFTDB0SieYfazSxUO-V48EUOGD2pv-qJnO_tjCtCKzxpMSE_wUTKECBfrK3vhif_1bv3ybCJFRUaVETYxYZbr3lFzUJAve-mLOKNoL0iwngfVaEzOwsYI9iIjBVr4TiZnLeJw3zekWH6fieYdbuLRoLgtRw896HvubMjZgjyR4WhXzK_PmDhk27yOzf7jiqdlkReRuRyXDoClp7F-bsHL1PO9VogtAWVL6T8VTCbLRrBMnjO_pr74qBhyskYJ83ncHfaVMtGqlBT-C9IU-FGI22BLjEm_p-YsVgSf3fsakF1hI5wd-iFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TawfEfFh8okoBVEPYAcIpydyYeF0kZdb19JB7lBH13l2jHGHUqUukdYph3gcp7u_IlIRSMCAOatpVdLNCnh3lFvjPn9IF-xiEYCWgns2rUy6WZcc7LYdyeOltETosYl9oO9ZY6rVHicpV6_VDvCTIO3FNdtI0v-fNeKW9h1BdXVU84tqLATE6xHCyTK5UYJEyi2yXZWxWng32hAed_EIm8aYj2Cn0_v6qnx-vyeRIyJHhd6sMMDfQDpkJZpzIsSDnvj9PYkwvcWseK5yMTmIv_Ae0oU0h7fNxzg-CgWqWs916i2bkQz11t_BLl5B7w69Y8t6qvazvbZ-WIgx2Fl61Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنسول استیم ماشین معرفی شد، با قیمت پایه ۱۰۰۰ دلار!! تازه دسته هم نداره باید جداگونه حدود ۱۰۰ دلار واسش پول بدین
🤣
تازه پلی‌استیشن ۵ پرو با اون همه دبدبه و کبکبه قیمتش ۹۰۰ دلاره
نسخه معمولی ۵۰۰-۶۰۰ دلار
خب خارجیا می‌تونن با هزار دلار سیستم اولترا خفن ببندن؛ حتی می‌تونن یه لپ تاپ tuf a16 ایسوس بخرن.
چیزی که دیدم، کاربرا هم توی ردیت به شدت ناراضی بودن و انتظار قیمت زیر ۷۰۰(با دسته) داشتن.
میگن که به خاطر قیمت رم و... هست که انقدر گرون عرضه کردن، اما هنوز هم در عجبم از قیمتش</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3968" target="_blank">📅 21:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=CWFz3hG8F8hBQcytE67qQg__dtTlI2_LBKj_mMNp1OLte7ihGMJijwQ1xElw45JUJhU2ytkhJFlukLAKenoR5jd8-NWLtVGDXkfgrfDADKOSEQyDLfg4-ZfZReXp_tw2kUqyoLvi5ZKKUE_GMCsaCD92h2dj5789BE44F7CF5juPPd4ox7GAeXE3hHZoAoxsF1mwP08v__ytZfQQRW3yJuCZ-otnewVi8WECw8oN13fZ91AMoD5EaxeoUGsVc5pvIWgHpivpJAx5ibQhxdaUJvNUQueyi5zz83J30yYZErF3vk-4299J2zFMDijxRwbUtcwQRxezXpzR5eLU-GWYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=CWFz3hG8F8hBQcytE67qQg__dtTlI2_LBKj_mMNp1OLte7ihGMJijwQ1xElw45JUJhU2ytkhJFlukLAKenoR5jd8-NWLtVGDXkfgrfDADKOSEQyDLfg4-ZfZReXp_tw2kUqyoLvi5ZKKUE_GMCsaCD92h2dj5789BE44F7CF5juPPd4ox7GAeXE3hHZoAoxsF1mwP08v__ytZfQQRW3yJuCZ-otnewVi8WECw8oN13fZ91AMoD5EaxeoUGsVc5pvIWgHpivpJAx5ibQhxdaUJvNUQueyi5zz83J30yYZErF3vk-4299J2zFMDijxRwbUtcwQRxezXpzR5eLU-GWYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pq0G6AmpsVUUTj0Z0B3p-s4fiV_xEkAjVaARL5tRK7K2zUKnx9HC1dNiLYTlKJto8Dio3ZRInO6e5QmBFqRJ3xSngjYEAm7LIQDpoVhqP5oRtJGUz0uD0mConXupUWi7jG0eqw-u6ML8Hj5xcSmPAWTjAWLssQ-9Z_mG9B1MfYJVGi_DC69R3dWqJl9gZL8xbd0G4mBta4iHF0cnjRq0yTMORhNa-gVoS3NiKlkBh5IPoWsNbZUAxpBuPeU1gZDunZSjj6sVkWqrtgDxpKBzoHV-pdJNGC0y1rrTxibpvCvszrUS3qQGU2vzHQg2THxdUtoJvnjwdSuMc85QRsPk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rp-82dwr1qGB0CoHodyZ-PMJEJ8GtUQ2W9-EHciVT2r7U_LQvaHScdZCPzU8Uoy-1FkMlCSPiqCpJm4WTcrRflFG-8ROL_onCzv_zzIz4VbyNfSDBwcvm-wuCVsFzEXnPwYp4qTAHe1C9hqxrTXViKPOsl8zYE7sGuumg3z-8SligXSElzaeZmmVcpVGnbOXD7vHfqBfLo5GupYAqIPbWJrhPv-Mvs5HpL7U4p3BSmTnNybYOC1Lv51R5zenZaPDXu2ivKJAR3p5j9HNiLQpzGmfsii-MiovHN5NhmRkQKdjI3rN6KScvHTR9ogFRqPTEJWHPe60H3cbDGX-8qo_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMgwGcBbyiz8vFVgr-4tg4Ch-ZU-2285LIojQbZBz9ZJyvhoR8qvcR_xg4yQID__J1Drmw2Uix8nvdmAHNKMR7I9KZDBAWSpjSZh_UiNYChRHR7nelEoENq_9u4MGAGeQsNJgH8Ky5-T7i6iA9rA3SrEAyAJNgF-t7GllKvWdAsk_96y_k-kVVZnb5h3BkJpAtoNiCytvtyXmyjDjVWufr6bV7O1Q9o3LamM1WBmwDgRWbyeWrc8Qqa2YE_AeXxgaG9xtn9GARevNRjSvk2M2W9SyGfG55QjD1GedVCbamRzB5W8SssOTvG8lfF86_gB_uAuecKqEsE31Nd9VBdxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRz99DcLqweJ5lHVYQLIlrNs3sn1SPULHLOXUNM6ALOAMQ_TkOdfiu_7EX1wonw9G9ZSaEotbZf84CGYjjSkJoI-3KKYkI5eAvjzhEDp5QgFp-XkznHUMQX9idIfQiYOFeghRo9OBW4PbQ-5TcWBcRuqvKsyNanRnut54lEy0mpggu3wU8eP-vBwaEJ7NUkdRtIY6V3hcnEp7s_yVAGWgmPObHun5nB-hX2_vwcPPekglogiV5uxbwQ2HLc0FAUFT1dKPTB2V4e90HlnHVSWrG_0VkDLMbQn9t_WbatXXvGgxcVvVGCZEKyE4BR3SLGNPzgzUTUvbWNuGMCW_nZk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jaix_UiJlnSB2qhW7w17QnvPJyac8D9CsZu_194_wb7dkLDc8K2ZDep2epBwGv6I3sEGTeG1VeoiHag-hLtWYhHK5hxNI-qd-7I6sYRa7qaGS1V0Vy8NwV2ER4nBnL-7mm8qFiFr2wZEzNTPeUx9Sw-hzuXqHZiVXqWict-OFFnjoW2wFJPtXbWKhitaKXVaPQ_7jYaZhvOOwO6PAtC0PcWuCTHc0bL73AXhIpj7nPGcCjkaAoVo5-WIIVL3oct5KoeoRStYcMr7w7WEHV-hAYtuOi6-qCWCFNTRNFTo_8pPhfERr34pSYIkS1jaHRf3NVzRXEC9D7D6p9Vfu6dS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jo4upA4MtFiKFqxGBYaZRQKVyg2MBp9ZmWnGkf6o3y8u79u5GR39E5OS3kzzO0h_rBbrJxn7JEFEjfNjVDg9NetEIlbl06uVrvmgatu0ZnBqvR0X3hMhnl0PtQpLrnD5_SAwsmwNl6cASHLn9xxzXcACC90RI5ROBF7_zETacolknj38FWKSzQMG4X4tqcPH04JU9gWQb7wl5o9lsDXS6gTueN-8bz2HoW-Bg6GJ9iRPnJYkj6bi7NZMREkYYLeofOQ3qQgw0-rpHrYL9GCpWPyjf4KMqsKCfZgNpwmsIfJcH3dWLzOxC2fjwPZEamXLmhQY9fK69gltz3-KXIYI0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2aoy0K7Abk6wJipxpb3c1WM9YI8Nox-tLrSAb-HN0TWUa_BH2I-eygpnKipDJREoUMWUIDXV0qVTDYwNFnwnYNsw5mQxzx8CBQhRFMnYl-kXwiS8Zhwf6UKhqQFX8P7ghdMiZEFSyxTIVHSB36AxMz8WAPIhEKwC-r11Q75c9Fk0_ug4vpGwnBq9TiKXhUkG-B0Sis9ihHsExdrXJINQr6pnT5gDkceuOOOtXxipKFpRZByrE5ZT0DDMz9QJlaLlyBaCbjmyqJgKR0-6JACx1FoL-bVNDrLUkJ0FwZbwuifCqPetqu4xEIwrIGcrEDfvOBDudGVdCC2OgP1rnejhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BukYldlLG92Y15tzdBT1Oohy3w-p8OXr0vbrWRYP59UyDVpi7sEBZouSIK3jG0gH2Xzlkxa76nBucy75hig7hE-BmBhcLdC4WOGgT57oBOKWiz7bOG1MipexG8vRX_WPOT2pExmpxpE211GN6ZaIx2-q5MD0DHTOOr_FxzigoquU2c3iJX7-3VhTQurW0oX4VcMh4nuKySXKG3qRlvtLSWth4YJLYIA0azzSSxUgV9letFEqEHZbdLFDgLQDknLHFMmz5xyjOU2lunJKomAQSjvrYUBZS0u5jjqv_mcU3TgIGDKsw0IvE61CzTxeb8wPYEBbmP4GgKkS8mO1uYE1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISVwfDznzFgdHqCa_OS6avgBbKxTmvYWZmbCGK3giMGSRaC9EZ-Uu3f2B9MbSocrb2yi6XmjPwAwT6fboOmEYTmn9kxYiamC8PHl75ZOIb0TjyZXHtWnkAC4ELZXixVRHsk-NUZuTD3zUMXurXiQRRo4-t8SUl-2HrnFyGheCaitRBh9XG3-fUkr6cYvTY3EzGessxLWboZVh0RMhkNVckThoJ41HgQiZny87_Emw3mYK6HDdgxekZr-QHs7Jt66Se9tXAaH2SEGqTAX9F9oSHmVwDBeu484iNuTitfnGlimOcuC3I7b52Sn0e3PyUF-AGMX5vTkxrgpTMITLla7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eh6eejWl9QWg0sxHDkjC2BjTCfLzcFpWXxuOUqyGOCxaW7h2RKKDQfZ_c3D778OtpwK3FvpXZ-OA53r5dwKPm7bUuf13pMBzusKunNxe-dBDn8uCsnncSfyWgGTODTxMGzO9g0jrXUn71JVzlk0wLub33jG3cp_TExl5oAiFXbMPeafCQsEEc0WEJbeknH5bCQ-9gIgQySXcDVA5NopvsD2Eiskuj2NsG7-mkimIAhT7SXL1DlnltQmbUFMejXQjLAtsBwViUdcmvBB7h9XnvGUihNIOSnc333NC7dSRdDTwk_y8hXk8Hcd_WnSOXEElx3ewOGPM3J1-Mz0ZywT5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YwtVZwQbQjQsRn51FDwpyr4rG90Frcj3V_b1cVDXjJ6dLCbrrbEnw-5_3m1Q-WQDcicqvd4yRY_F2Z-t2HFRwjZl5p5ljT30EdjxkHz-xsGttEbzEdY93Mdbq74nJqZkluK1TG0Fb_exdZxzEPz4x2F5EjyIhX9xBO078VN32ixbs9QR1hIitfgec5Re979nLy1DuEfKDh0FhvWbT2slaUXdFP-tywEjZCo9K-NxOd9Kpv3d6AbxSId1fjGM-cmqGOGAmNt97zyCSS3FfDacpfLUF9sXwDFtY5vgRGHwZUsdu6fRg-32hFYe5_DIGFOXMePcjV9Y2nwtNCpWjear2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o3u2CQz-Zc-vUf3oLBIXA0_SE0ke9Q97SgdR4ZyXIoaSUDU1nBYP3ob4wopp7TcytUUpT3SWlAG-ArzSA1uaXBi1Cxqg_3lGS8EgrrCJrqPp5fJyBTStynZf1TavzDsqIWhApoNPuwuCcFkZdRJxHhaCt5mMVOgScQNnBn7jcdZIhT92kL28TT5am-gKrKyrFsfltAwrHp7EH0fp41krVs7-U2WTVvcuwleHKat6y1zkeq3d8uyPB7X0O0vh3_JrIXBZbQ_rWaRKsR5ub_d8I-ljxU_28fyb2gk66d2rOQkCrWXj2S53OeGXqbEekz-V_fBnUMqie8XanF25c0daGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W4-snyPfLdXq6YvNsL4YPxJ7U6MRDJdTaQHWh31hExkcUdvmiqMz8ISVOtf-dm9ldMElY8cjuGADBujlpMMhvNM0UUu7QLxVnv2VFnbfldguuTLqJovOpmhIlG0ksUPs0pSGnlcVEDL3sQnhM2dDMKWToc7lBJXY1uqhuRVc5ksT2eHr2MOhiP0D2i0TFsckOaZur-yZdDSO1g0StGpX1pQWZMIFD8Kz0YoKq0v3LvY0CYc3wF5sQyaQJ6rlgDzWqTtQFeVDt3o1p_OZdXS8gkjSa5TXCjyaYo1v1vKlElaica6Vy_e9IRmoGalxNbJcm3rsDdqYnF-cEboXdnsdRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BCy1sbmCVAYODJ5kTJcj5ygK5pSc881o7IdF7TukOE1Ejr2HYEtHjeRfs7dyEUxke2bjoqp_-x9Q01yvL0y2r4DsG4Rxm7SfomuyVu9Xk9R5nNCi4uqpUXApyDyHRqVl0b3pDDlJI3xQK4HSwBMGd0iOAvY2ck97Ppn0MnwtCqAl8bONGTfeOmnGgwUmmka7pYYV3bUJ6s9bqfQ47FEd-8C7Pf75lhJTV42Qw8TlJ13vywq5jaU0OpNkwDCEU7XpCtEBcbTjeqPTOe6swZfBiSOXSrL3OQ4uP2AbTge_VmDslRZcXFHgrSDUtcClD3sP-SQG6qbjQSBIiiO5_QgAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/envDk5lxBPdR7E5KA6aQ-j6vctYghRaOAu-FqZoNWugDYAC6oGCcAVSknfwt2Ba_W0QXW4UgivRXakItfSOO6sEsVR3P7IguzZp-5Jxz9NMcitDiMbEH4UT7ltBGSNYNYzdfRf4Wa09tHx1Uhe-iXy6BMobgG9f-TaGO1hqL_moCtMljG10NpRkvmC0kd1wLzeBn2ov55CLRKKUvDZp2dtO0rIJ2UZ_7PUa3ksIHZaNGejeGVpvWrcjoCMPmmT2Iz9cET4Xukh1-Lwh7mzoWPtZHspBpcABoTn9bSJpO2niUMjrfTrtVbX9HsNYEYcL1_ULjQwZqtzMtm1ksxSkUQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bq0ZN7Nog2Rky7ucAGANM6-Adc0G46VB_O3NwxRqy_NUND7BGr47HsHpo7KcY0zZPeIjzDT5WgKzSKNTylPTZzqoQPAgxD77600wgbA5GT8DXu5npfLws-xYCJfiRChHgaIjOyHl8mSbrLSWEmLptI5gz5M4QlniphrNqQJW-3YaYQXBoDOGOcDPzjiJlGYc7V5HB2HfCi-yxlYq2pxbIoNIsxMJyD2MfzcFEXIZO_YLpmSCouvmnOg9eu1cbBdxt88P3BMb3dmg3BXOxnMD-crXwJkCKg61X6lH9nEfgcf5r-JPsq4p-viu0YywOc_Bgg-62_8BT9bW45TOaJTGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fBC8wv_ibhazoUbum-UPFPYr3VuVmXmC_CnCftVqeaxgxXVhRtNoBlAtbcJWSGbw_fqX5Ll9dHU2S0zBIquYDdd3_seKUMn6k_trqbkGyBpwYUAp-HCwx_WiT9t8JL-EiRJKWG3oLFDaymRpnMUFAU0N55Os0w21t5CG64QGyszeaPS5CSJjcShDKosztF87ePdJTHXUG70gyxo5WcNuM0yP2ntKu_R_aCpgDhbvIrP46VHWqUlB6gPTyxKOrMtmlQei03byFpClHlwyPPYylgl8C6GxzpK6_FnklfMuX5kQJGKAf7RZZPlW9ZqgWyurv8qNVMW3IJ8U1cLqa0CdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UT7UxjN6t0GQlmqPbHJFM0Gf-ldbdW_Rxpez1o4hEgCu7ETYNayfUyu2FBFzpkIPef-R-t8z9zAFXlCYPsG9cq5zfoF0ix2h09L1a_V7AqjGLgEpqFeNedd5o2_wa8i7xSrFA0pC0Z2hKhS71uScQ3MzxvYR6yRUhjZfnZJvNcykqKbpZpIZFKHYf0nWwaZ-ze9gBbOyZ6Vtjb1bJypJJBhhlrvWhk7PhDB1NVlz5VipkH1iHcc9UF1hqQroYmdtKkmDAeyMv9bAQG40bR1iBywXr7wmVmhiHXieJAnUgJoZLsvhxcrS8VspZwA_pTZhvd0yex4mHmW-vV11EodmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MxqecL0u4U1yu-x0OmateGKTmNfAt5i5kNInv17lg9962TLH63F8Nsu5fimZrDAajnImGymPgVGSclc4eyKHF8FMe_AxHR0iEM3p6rSyaaiZ_y0arDEz4sydCACR170BGCx3KeOqXYRjMEKm5CxH7LTK95KerqYnjCQmIoypBJxGWFOEmqNfpL3Ca-4tR5YJ1wibY-IM-KGMSg5YAuBeM1ggnE87nj8WOh542ykAjVN4vKqb8X5O_rodcjNSdQwDeJeu3DXZOfqJ7bACNIo5OiLZ0lI7TltqNXia0V9ulFadPZemF3kx4jcNiqGX-Tp53Rn-t0iHSp3elLLk_OxWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
