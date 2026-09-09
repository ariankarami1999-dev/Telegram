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
<img src="https://cdn1.telesco.pe/file/FSujOieSMhRjMJZS2RCZ-CRNlCLup0zzbCFvm9tU16T94gge8bKhuzH_61BXXhFNOMv82XEebzeTP_e4GrjnbxHDrUjJdcOBtZ1sZE3d0o8xR1A2ZNvryQIAXJnEKde_We6_hpry_uzb49_5p3F3oioMuWF2uVXjlVbNRZ0dkbOFgHxa1DTJRWQpzLEFSHjiEwOev7SNvwHzsHozQ2QDloqbFLzIy3cEiDs9NR34wIVa1qVv8fh_PhrjjQL-tmSxTrsI4AFM7KtUNXMOxA3Usz7N_9LgAgzTz5afNtabdvQEQ7hoRJ9kHpAbjBEpM1KbwkCboFLFcqpGPU1PiB7mCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEpljqU20_xf7Hph9RtgB0kGSCqQnJmKv1g7CIukNCaAcMXw59H9cb82qy9pWM8XDEnNo-B8LEOnqwvcOwZKx1Cr5RPy8iKpKkHK91XnUYRdBqVc34cZPO-o573zSVVBlBBxNM2wAsSY-n_zQ8ul0yTooZSEQHg2OZO9ZmnnH2CTZYiXBcVsmsobMLPQvdv64e4xjYZFS-euJ0G4DL6uMd5BBWXqN63LZST3qCRJya3FszNkkQFFBcJ8X_KTEjSXxXN6YOSeRByzjsuMKW7zCC3wsZ8_JlZZTLJWGQmi7kcl2OialvMPhUZ6BFPmP545qWr06uDTtK2IAdjtGAQBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=XM-sygrDS03vfixPKght-aghptPLliFWPODoykHY89-e33_mDyaEgbiYZl6kuL61us6AmN8qByTRnPw3gqIh_1yD6yzRSyNXjX8YIEOi-5pf1SmGR-dWuans3EVEG2W3ZO2DndoHCyepi88aFvnSXdmQB88gBZljSCWPK61OJFfTE6j3bS1SiF3pPd9dY-1TXnYg5knHtk5N2IxMqBYMVQyEoXTMrs62N1kgULs1HIS2gL0kLpWya06evZS0Dn_mkE___DUs6hqbRIqY9UvbNeHr0JXnllQxJpcfrFOGcSJq5Pghj2fQkCMC7zn3KSkZ_8BYkzMdv44jXEWI-uwqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=XM-sygrDS03vfixPKght-aghptPLliFWPODoykHY89-e33_mDyaEgbiYZl6kuL61us6AmN8qByTRnPw3gqIh_1yD6yzRSyNXjX8YIEOi-5pf1SmGR-dWuans3EVEG2W3ZO2DndoHCyepi88aFvnSXdmQB88gBZljSCWPK61OJFfTE6j3bS1SiF3pPd9dY-1TXnYg5knHtk5N2IxMqBYMVQyEoXTMrs62N1kgULs1HIS2gL0kLpWya06evZS0Dn_mkE___DUs6hqbRIqY9UvbNeHr0JXnllQxJpcfrFOGcSJq5Pghj2fQkCMC7zn3KSkZ_8BYkzMdv44jXEWI-uwqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N89n8Lxa0DR0LTV_0JKaUQEIOSvUO7SO_bDsYGiqoslMZoeDy_01U2YSCk6Jz4qkzzSvwg-0jdi4uFNjCy74097pCIIA3HXUu8fnTAWWkc6S047CaF0TZ7lfqxOUD5NuuPk8t8qYdPb2YbY4FfyBzoQ3UORzucd38urWS39c5DQ6UeW8fukmHVIhhb1GvVoCEG6XHpHUyK9u7VeVSxaslumlrWvC3ZXUX9Y_Ahmai8Ui9taEg4HnkgGydqPTJYQMa75a0jdPNYUhvOpztrU_cs_B6BPpenlPYVtjWVfILrsoRdoA0AD9VcY221Z-ptfoKOVrNY4aNEqqE4upVsC7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=r0cRG5FmoYo1iugOirQ3uhS8j5J_NjaKaHXV3BvH118Yu4y8CgSMVqMxRJGx-MkIqGOF1sPtJ5rTIU7-7B2xHOf2NNQ3Xks0RPRoQLLVLPx4yd3deoRXKJRVAkIUfZO09SzeZsNzeRrqXxcvlYrn2H4dU5p8kBMKxelwrWfwQohuE7kScQ5UTZvofP4QXEt1zOAnh17hUfkZ9xkrqaV6tsMVbl-M9h2N2QhwrYaZKUBXjJLtpITLpP_1QpBphmyqdqPC4r5a80CiKqP5xpk8tckzV2tixxxsLqmzaazcDMhB5Qa4LpvoIX4euRHPqafzLW1uUzjLF0YomAeLuxNM8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=r0cRG5FmoYo1iugOirQ3uhS8j5J_NjaKaHXV3BvH118Yu4y8CgSMVqMxRJGx-MkIqGOF1sPtJ5rTIU7-7B2xHOf2NNQ3Xks0RPRoQLLVLPx4yd3deoRXKJRVAkIUfZO09SzeZsNzeRrqXxcvlYrn2H4dU5p8kBMKxelwrWfwQohuE7kScQ5UTZvofP4QXEt1zOAnh17hUfkZ9xkrqaV6tsMVbl-M9h2N2QhwrYaZKUBXjJLtpITLpP_1QpBphmyqdqPC4r5a80CiKqP5xpk8tckzV2tixxxsLqmzaazcDMhB5Qa4LpvoIX4euRHPqafzLW1uUzjLF0YomAeLuxNM8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=e8FN3lSl6IXe5uZ90lgBXyRsXdIosYoRUyA53D1Da0An5RrUlPxLWrEPbMGbW0L8AisDeBsJlkFAjL0a74JMPTyH_LLdY2E7pP8scQkIAeAJOpOx5hMG3jfz38DOnZOFH2uj5GjqAaGiXO29Sy1HrJUdUostGVOGKsIx-7iTzl6LYFz7oxaq_DM5qcIw_84oE9uA7uOju2p_GH-cHFckp7RCeDmvnDzsWZVRYnDKVbGxWLqJcQ5TtCm01v06it2RDsu40gKpOPjddKkOHW7CZ064Aa3mZk-YkQIthzhOW7ECElGTkL6_4_V9AtxyNms666_zWLF5gQn0AYnhQZsdTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=e8FN3lSl6IXe5uZ90lgBXyRsXdIosYoRUyA53D1Da0An5RrUlPxLWrEPbMGbW0L8AisDeBsJlkFAjL0a74JMPTyH_LLdY2E7pP8scQkIAeAJOpOx5hMG3jfz38DOnZOFH2uj5GjqAaGiXO29Sy1HrJUdUostGVOGKsIx-7iTzl6LYFz7oxaq_DM5qcIw_84oE9uA7uOju2p_GH-cHFckp7RCeDmvnDzsWZVRYnDKVbGxWLqJcQ5TtCm01v06it2RDsu40gKpOPjddKkOHW7CZ064Aa3mZk-YkQIthzhOW7ECElGTkL6_4_V9AtxyNms666_zWLF5gQn0AYnhQZsdTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=A41KVJeYIl7IKa473pP1JbqRb4oqhgbBzcAcxeVwmNmiT0XSsnqlHpnuB6Fte5zQZ1zidruOFBxeb8kC7Mh5kV5CMgI3zdEdf7PKNijJWLe_AVabqRGi4hF6cM_jC0M8mX5s_DDk50CCdF6m4gd_gwqzvBR1Lh-awayGehkdGSlfBO7RGhIH_yOT7pNXc9x7e5LLjgQleAukrrLXjCnvItML-WY5rcd9rQaZhwLmJuXGTKhmLvmHTsNSz5axJiwsNZJVmLs-R2ibmYtrMu74X5pN5xR_Ar6qPEMh7ZgObbO15Mnb12JYtN1kj1D0ydLN-a0IpUXGjNac18YaaMrcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=A41KVJeYIl7IKa473pP1JbqRb4oqhgbBzcAcxeVwmNmiT0XSsnqlHpnuB6Fte5zQZ1zidruOFBxeb8kC7Mh5kV5CMgI3zdEdf7PKNijJWLe_AVabqRGi4hF6cM_jC0M8mX5s_DDk50CCdF6m4gd_gwqzvBR1Lh-awayGehkdGSlfBO7RGhIH_yOT7pNXc9x7e5LLjgQleAukrrLXjCnvItML-WY5rcd9rQaZhwLmJuXGTKhmLvmHTsNSz5axJiwsNZJVmLs-R2ibmYtrMu74X5pN5xR_Ar6qPEMh7ZgObbO15Mnb12JYtN1kj1D0ydLN-a0IpUXGjNac18YaaMrcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pazctHEzsw8T-fXErQhru7DqsoYp7dF_tQuxovJzBjabO1TwEwpUAojp06Q0mzIbMrXBIfkarFNDDpVvlFNncxURGE0QT1tisxHtnjdmkNDi55aZk6GZ5xAkQ8X9rqWahH_O6TQEImjuMXdtSjQFXa_ofDtfELR5DNjllrZcCiZxmbyvy1eKWCQefoWx38SHyU48bEWf9xgDORyBo_CMwmtBxhMDJZXzDAA4GKm1zC7ZmShRGdqmi-a1Ur4-XEOGi-DWr3nxKoJSaRE-oJ_35_uW5lDampa4pGKvc3Ni1UM2DoemvY4IrGdbCahKdpaMpIpaLoD4zPIeTJm7h8q46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1Yu6onXI0ABeX0vBa_Vs1qzSlW8gL-RueXP-yIAsg7YUftpz5p4YuVobB8aIUp8LBlvlBwjlUesZ7akT2-vJmg8QEoyMTVdfu3n3guLcjiEk6QtJkvfkxG4n2aOCn8YiFADu1ATiig_4-74L7XXkpv7Q129YKZXM8fj0w-VBPIw1-_riOV04KXEbXlC2Tg5a8q1arjBMr8eL0tL5v_B1M--Z0OFsKmp-bPgNXl-zeBST3Q37x932124VS-TpkPPYBgjnVXEzMCxd7Y-VxpcdfmNSzzJ0GuP1urfF3tsim0c0hKpnSdtXkIEctPF22t9XsKYZ6yUohJQQBilm0hNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AttWGgF4QlqZg2eOmG9EDMM90N6nutL4GG2vJf_U6ISwGZ5VFA8xbCRWCVC9ufYZQiQeHGCOFoklDqI8yv4HZbhq0QAKIxJ97aV3iaQqvz4RuYicb2BlH4aiDPgryNT6kKnYOVC_8a3h6RCU6ahIsv48zmjx1TrvCCkVuZ7kanl9vMtubbHkkVioNDSE5fQzC01KnJ4iA9MEZAZmcwSeCSryKa2AKxOm0dNuTOMUuf3DGu-7SMJJBmoZF9NxLI0lWfw_ayl6FVPq88Vffg0WpNOi0X894E_Hvp4p_oLURe2kLIQOI9Q5lIefJuC1q35rEpHjcnnB3dJFTlBv15aMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwDtyBj49vWDU4vlR-FvGGbbpo1YCx6PcL-aIf7xWnukgQhVMs4eItnZjRxtmcrJF-_4q_jQtxq24APH0jOoo7F_pqWCAJPvzpUYOtaFZRBMgxBjVPm97ggcN9Cs_NS2oYG0oLqpNAOUF_-c3a6NczDrTSTBYIZWA0lcdd94wze7feXyrpdjVEgLwZ89qTACmJKabArqgyA_ZKiTDcJ8pNq88Nq2jn174W-QyjBR52WG0bla-_c7HiYSd2JUfvkDwghmIdI3kJHToD3JNqtWUluLzkMfYKi1YWm66tN1ZDpzcxk_AiIIz6rahIteBGyyHRL_6EIrhA-pdHHkAJ4BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M25M1qsjL_B2K9zuYYlO2riHjhwXeN4jyx-mLgP6ReQt5reYe7sVwgJVTC8PrGbBpXuiV365p9jRLTruQ76tNcIC8m3wyvQdrP1EkKBVonoBqIIFUYlpPHOLOSGWpSX7e0CoB8GTUcyVJzmgVqde4DzGMbwz2MLSefEuepsyzVEIE68Q-faszSYPz-bUo_BfPn-nl4sFMyAJJuC9qY9aBajVN73nnMf7XlfutIMiPD-FcnHKbU3mHuvIDI9didu33lC8miTkBLPahCZOZQMzCmSRo5QlrxqbL2tzvYvTfuQK3A3cY7eJLl1mq55oRiShzG25XwT0jR1gkjYvLvxshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی روز سه‌شنبه ۱۷ شهریور به رویترز گفت یک شناور بدون سرنشین زیرسطحی نظامی آمریکا در خاورمیانه، هنگام پایش آب‌های منطقه در حمایت از جنگ علیه ایران، دچار نقص فنی شده است.
این اظهارنظر ساعاتی بعد از آن منتشر شده که سپاه پاسداران انقلاب اسلامی از «شکار» و به «غنیمت گرفتن» یک شناور زیرسطحی آمریکایی در تنگه هرمز خبر داد.
مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، گفت این شناور معیوب از «مدل قدیمی‌تر» بوده و هیچ‌گونه تجهیزات سونار یا رادار طبقه‌بندی‌شده حمل نمی‌کرد.
او افزود این شناور بیش از یک روز پیش دچار نقص فنی شده است اما به سرنوشت آن و یا کنترل نیروهای نظامی ایران بر آن اشاره نکرد.
در بیانیه نیروی دریایی سپاه پاسداران ادعا شده که «یکی از مدرن‌ترین زیر دریایی‌های هوشمند و بدون سرنشین» ارتش آمریکا در بامداد روز سه‌شنبه به دام افتاده است.
پیش از این گزارش‌هایی درباره مین‌روبی آب‌های تنگه هرمز توسط ارتش آمریکا با استفاده از تجهیزاتی مانند شناورهای زیر آبی بدون سرنشین منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-a5DY3B6YSjyAeVhVTzw8rdpjvsj0i0LUGqcProo_G-3Kkacxj6Xo02LZU8j4zmc7XnZQR8vPC3uOX8dEmySDw8PurzSaD3CffxsmYHejjsnjzDHyi404v4k5z2vqU9LRe7zQ_ZOLcJGdn95jf0aauVSoYCTT0JWyF3tWpHw9_W-S7I3yNsPI6U1qsW05Nuxjw82DUO_QtifbiMH47lzceNvGqaTKKGDXCPIU7_Nx57zxtl6LAHu0Eo_7UDP4_Dwjgcq7yeVUZC0fUjhWaa8sfGaSOwyVif4fFMxkEtj4Bmlrgm9PssH4_n-v8cOBMxRULtx71QN7xiwHh94_qmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دولتی یمن روز سه‌شنبه ۱۷ شهریور خبر دادند یکی از فرماندهان ارشد حوثی‌ها را در جریان یک درگیری در استان تعز به اسارت گرفته‌اند.
منابع نظامی، این فرماندۀ حوثی را ابوعلی الاجنی، رئیس سازمان اطلاعات و شناسایی انصارالله، معرفی کرده‌اند که در یک درگیری سنگین در تعز در جنوب غربی یمن به اسارت درآمده است.
این چهرۀ مهم حوثی‌ها، که با وجود جایگاه نظامی‌اش در کادر رهبری حوثی‌ها جا ندارد، به همراه ۹ تن دیگر بازداشت شده است.
درگیری‌های سنگین در تعز از پنجشنبۀ گذشته در جریان بوده و تلفات زیادی به جا گذاشته است.
در همین حال مارکو روبیو وزیر خارجۀ آمریکا هم با اشاره به نقش نیابتی حوثی‌ها در قبال جمهوری اسلامی، گفت معتقد است که «دست ایران پشت بسیاری از حملات حوثی‌ها به عربستان سعودی مخفی است».
وزیر خارجۀ آمریکا با تأکید بر روابط دفاعی کشورش با عربستان سعودی، گفت واشینگتن تحولات یمن را از نزدیک زیر نظر دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKVfB-wwZIu41M4Y5hR3bEGdL8-mkqXc6PM3qQN1Qh83FX9G5mSbj9EqkhfAUzM1TMTQoUMXgfPOUyyQgQiquffIugrjXnWYBEkd3d_5w6CuUJokA2aVdt5Ep-YGaeIbFJ9wNWPyh4f-vnytfgTLOWnnDwjU-Wg_mVDVxPS0O1Zot1_eXqgvHeFM57bgKaT6FP7VbAKn3aPFW9rGhhg3gHSO-p4Fbgle6yRxuTgXEP6q2qgzscMDSk0t7I6D-QPzhdjsMRSgsBzyXw2cqisfT2-d3BrGzuOLzhmd6zB8ieoz1DBwIQM_yX6aO6TWUnQUustZVhp4XwMW0GO3pBIYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6uziUzW5jqU22NKAFMO5pvWVWWhvNJkAk9OAdM87GKVvcv4MCK8lYhobNr2pn8lLiE-GwH-mcJ28ZyGcUwK3F96heVdgFoplGwG-YJ03rxnACb5Hl_sXHAsVNFaMp6zHc6HsF4EWJxvNImVive1VSPEQIUYZAXsQseit3TmamiAoep6BJKTQAcF67GY9mDPTxWvYJ8q7wlCVKc7KlnBaOBO71oNsERCw5riXMBW3GFbz95CdsMWiL-vNegQ8x2flwAgi2lo25XMVW9eKOW9fjoFclXxGxeWZLViMBaRsFRP8muf_m0cm23pEzJP3sbC4Hn2f_JDCcnYtkML2-WO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kCgK3G8SSqPKveljTKpWN5oSb81Kg_OYeUKiunHkIhAqVhMlN3_wLUEqF-X0PTFShoSHbeUMwhjkxSf9rWCWTHijjnkYBMuilxQAjSJIAfEsyCIkfj3b8bE6KtoASc4YBSXq3mjl6-UwxD1b5tC9bhzKxiHmp5_nqg-Bo1kuXFruZklazFinUF_FihJEFwvOm6veZQEhnXB2iQKPDTf24w5nvhTQvnab6WuYkein6oabl1eMJjJ1KesraFVYA2dqofWFTv5fiLbrR0XXXwvG5EaGvBcppf1mEeVE0NsrbhOHmka-zomOgNRDbSEZyi9rj6yC9DCzHccdPtmN9v7hZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgwMjuANJ9yUzCs96q6eN17XzVtXO0jFvoX1eEQ7ngzwq3FncLUWpIKzVeN3R70PCWPQ1teOFSgHies7QGJBw1Uxp5ucljSbgT9zZYbH0XUIoDqZL0OwaIw4kFt9MQBU4-DYQzKDBkozK1ErhkkZ_7mNLoHbKuWHuQiBMDX_rWQSytQKIDZZdu5lnNuNxgK0k7jXk8KlhOSV6rsLqdhgJveLpSUO7JsVFGQ6kN_uyzOKpSwWMtFqD5Cq9awbvpWBtqT0C6_X2QQ7draoHwrXo5GCjgwJGbWuGvHtANK9_awDQR-d4_v2v5PHx4tt3-EYx0zdVd-XqRRRdZPJXhTU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KOpGa5ul3cYV3OWvvUKJOupYgjJlkNzkHTmmFX7w3hkhMt4K8B8kSj879D67icY4S6yRkVjM9HoM70JN8KYMxg3_MvDhwqH76PD8X-XuIJ1PdA9dJbDbXV2UWEzDegSZ-h-jpJS8T0CKDoOspKwFi7u_rXix3JUCV7s5vbRLdBV7OjKcaDW27w4W9IkbmWE7RFEma_vOkDY_e_OD4yAPgGMBtoRmMOQ1YawGApMp7xzGt1v7hzxOMSOFx0ErrKvo1RdY6q7XsKzfKzVQovOfCAZkcHoPdOhRhrDUnJbr0CYS5LdGh1aBPyFKKYmiC4ZyypElnI_N-d4eC7pk8E196g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j8WymiYBW8LYWFkXX8M6hP_69vxy6CMaTISFPqYQP84zpqdX8x5S1G6r6mlfz2DdnbzsxLQwvy3JNCwsCZroqrXJ5BY-ofGzSXduRP0pFKW6CL5FD7m-62bWgJ6SqxOcl26_7G2P3K9QkgglTEaf5nLJv3XBnab3srTYNtvLgeKsdxOMj99v02dbyhArAKLHYpfqAswFhBkv7Wj11TevXA3jX4q7b7nZ1tWNqeGsNpMEtM3TUHcnQnTl945oUv0iUefWR8SY21vAKPrSar6nTKAUPs2QPH8bJkh5w1OKkFSYjrC-e26h36T2T9aa6s7RLGKVIedlCkt3yE-npbsUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/urUEtt4GubzGTphlZQ0tL6g0ReCaRmuHfaje0ZpmKkZj7C6PFa9XVJ95XNv8ppooKWJe4VTrZjNVTCJWnolqedEnalLTdQRktpSv2n_79Z4fFnB3jcbfGh2MS0w8XZQNq7pML2chf3BSBMkgfwj4ZomUgH0zskqZmhHLrghiOpIy-iDRiP-llRv6Kl1GT0Ng4LTi1nlvY0enuP13GftlZ97caMUy5_RpsKY2EgmCdWZKqTMrqc5rAto8ZhbztQkh0XeY308zSWWM0rt15DDefRSGXoqyCASvm2JV0EstlE0qnd1Z2su0ssX7ISSNXB7vHH4Ejkc9vMpbZLe-eeOYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MrXz2c4TvaVZ04ANemWaQv5-WkS-S8NSUKwCbnHlIiiixuulsQ7mIbQS6vhETYhvbTmgUwX1drM37XBmefeEpRwXxPVIGC0tqzwz44-zjef4JJViMY4Ph1JkcC2wCzmp-KT9u8BYakakGFg3v3ctcoNXIZIDz66F51fEB_OXgN8s7SCkq2baP9yuhuVucne6WXzxFRfh-boAW3JR8S52tZszbQPg7snc3fGBNfCA3L7QSuFR74F6diGkjkCt_Yljl_bkZSG_TstnYp0gZkxbFrykwoQBrDIfBkUu6F1G6Z_otrllYyZk09p0ttgnXkhMhmRvXdgKh4SCvzjQjYJmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f_3Ftf-zrwkhV7tXR9kcNF9qcIGyW_MvvaUrhCKXcJUB21CbscHIrgD8_AoBizWMMjBDuQRBmQlcwt2PNafJrYyKLG1yQUCpV0LnrDLxyVdsEPFi1OUL9553hguLL_qg6IYdCS5DugY3Q2C94MG7eMZ0514ShrMgR70IxaH96Hvl7NTuEgNrpVwOQhuEm6zQaWnSZbr6qUBeRFVwCUUxAW8IkOKCg_d12c8r1bXDNH7cAHVQVy5y9TCa3oUCbF77OHCKvVjW8Z8keiNHlVCgDlNd5NeYpWlIy4l8d1lo2WOPigeXdTfoECB9Nx-bJn39b8GL70PqODozB3342lNrCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=Hp6FXgdHIbVk_amcb2Wcaf7_dUGaxRPBhCcBdNNgXL5C42GHpL_75L0boalkAqUKlLHHvNrYbmWQ5LpDSMwqRR6oGT6Mp8tAZ3PUEMG7qsfkB_VrdObnnkmVhRakE08TH8ZN58pXzYuxYeu79XuU9XBdPqqJHwho-VarJuBCr6q4X-Wm5U-CER9y-Q4_cG3XibZDFG0y6Ll8iIF-nkkTbo7shiqnR5gTKsYqXm84l7-rgNY3by4E0z3vRe3vXU9m8UY6svsdQo98SquMWA-HN9mhAnh2XYKDAuOi3XR58Si-N4qEOK7s5pWWLPykx6VvZ4dSVuUBjbGhx8aj8QwafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=Hp6FXgdHIbVk_amcb2Wcaf7_dUGaxRPBhCcBdNNgXL5C42GHpL_75L0boalkAqUKlLHHvNrYbmWQ5LpDSMwqRR6oGT6Mp8tAZ3PUEMG7qsfkB_VrdObnnkmVhRakE08TH8ZN58pXzYuxYeu79XuU9XBdPqqJHwho-VarJuBCr6q4X-Wm5U-CER9y-Q4_cG3XibZDFG0y6Ll8iIF-nkkTbo7shiqnR5gTKsYqXm84l7-rgNY3by4E0z3vRe3vXU9m8UY6svsdQo98SquMWA-HN9mhAnh2XYKDAuOi3XR58Si-N4qEOK7s5pWWLPykx6VvZ4dSVuUBjbGhx8aj8QwafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib-0Pic-8IU__wU4HuTBNt7rs_KGik8iT1cCgW0n2sS2qKr3arOH9__LDRlXFR3dArlcXlWO-J4u0zjGWVBCNL7HyyXUL8lWw6hIbtEX2vagVIgltGC5NiEaQA4Rpl55FC6DUGz23YS6ajylZD_WPjhvroZYW5h0TkfOlbvT2puQaUCDIiC5TSCwIBnbBDM-6ETYMl5ued07xdndW4gmVcfsKs9ecPxRC-EnxjVi4TFI5-HOlJyLW6F2tT0m1heF8M7T4WBO45hIcFCkb8gkK73ec0DLyYK9jg38W9rjPb7MUR1I7mJxnGcVx1wFMOmfV1yBcIrCx2EdIZ3c5yQf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ag6NoZSWDynvt-anH06d-SXZFVNdaVGkf6aNJKW56nLV53WC7kpdw5HUC_hDtTKg2V5A4DDDDopVd9HLtC1VP9rBD9vHUvPqXrRiA8P6nVn1SQPTTCki0ml3yfhItt6ShE3z1rOXNYZvA_paLW4zJoKXuCSEFHH_ycjyGrv2SKn34lK1QxVaEV4k71pN45bqrHZ0EZCgcJiYm1Arz1_cA-f1R7hhKbLzDMMo2DW46iRQm2laCInsUwG16JuMCROFU3VB-d28qNnmVq821BijRtR-reuPX751PTSMjqm5tjGvig8otquwZ_Fv3NTKl26HEJ7KTsTB5tuIyPMyZdzBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=gIN1g_iqH-fk_bE5ygmEn5PX0FlB2TiBcm63jXuVWJDXqWLqIDnvCwKXSOQoa9MMNqwVJlwAdzVkHFevrtVW9kFXXw6eVJbxJ9N8LMxwVUUPHcqaWviIXjGCTygXWf7DYk1Im03jie8WN5Ww60lnFOM-TAVbXG5OL1kvaRPOBF_mGw2y_GM_rMqaugcETy9b5LKWhE4whpj3pOQLaypmJemmZ8YN1tJUlxhI8LjYv1Rra_rL8mF4ZG_y5uTDCErEZ5SpAif2lKetRI4hK4cdIa--u37KcIiGReIoGQWsux44LWf1RGEieQE_CweUMgIUgCt6VQZuEJ3HBaM7rPmrdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=gIN1g_iqH-fk_bE5ygmEn5PX0FlB2TiBcm63jXuVWJDXqWLqIDnvCwKXSOQoa9MMNqwVJlwAdzVkHFevrtVW9kFXXw6eVJbxJ9N8LMxwVUUPHcqaWviIXjGCTygXWf7DYk1Im03jie8WN5Ww60lnFOM-TAVbXG5OL1kvaRPOBF_mGw2y_GM_rMqaugcETy9b5LKWhE4whpj3pOQLaypmJemmZ8YN1tJUlxhI8LjYv1Rra_rL8mF4ZG_y5uTDCErEZ5SpAif2lKetRI4hK4cdIa--u37KcIiGReIoGQWsux44LWf1RGEieQE_CweUMgIUgCt6VQZuEJ3HBaM7rPmrdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VFQIoLJKm8t4sShzER2KbwjNm38bhJDgVoh7ypco-z65p3TEsedfGZf7j15-MZKEUdALeQPKfeYRQcZQkEaa1GDBUHb46Qok_q-jJVy3mulZKaX8FRhuXHA3A9dF_mY4jQF4hHHPzfBIQj9fMusLmz2gh-tzydhu0HPZDznd14Fs14ARGz9AU1U_tSsqveTOKOZye-_2tp7rj2JB8cHgUuQrmkDX_5FNim1WGi4qf8iq1UkI3UXzs-M2hA8a_Y_jk6IDZ4z5-xNo17NiPu3x8YMS_aOkjFx9sawwxDtymbtGahcFS9E5eLZ-spLYjVpuS-JVvjM7UQoSBsazsDLrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIp3vkz0t4MKlWAh4AvWaq2nlyfrzwDXb9FObXBvVJ7qaSHWJSJ--VgQ5KVeKWEuV8boLtPTk9gWmbPkJHqS2j_BCdRmNkGMkKQAcZ6nBC8qvMBkaSoywgvPQBp5u2pwM_kM9ljLcu4UrRrpJzoVC4NOmPWeTnxcHBacZc_yHfTL0j9juhCRaFToBHZTuAMfZqwGE3dFVh67fU9JxyEqtD85PO92iZylcCWT_JaJ8Qw-P1TAmMgPO-NKOEOnx4Jx8Os5DTJapxAQaPfkbzqUBi186qvlKAaeIRMBRHHsXpBdSpHarlw-KybLsRZdV3tnosn1tui_nAImT13jqWMx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ah_oGl1nWULncBI52j_9w-7GNWPGfIUAyDylHt4BIrv2IPvX0MXmjU9vrIIEhQ6z1EmleDedf2C_cZpsZ9IXmlgPgn_-VHAiNYK1ULLs9Joj4qljY7OdGM8_A4jcv03_PtSo44DAwUfYLk6mkcmBVCCBKJfVN95aFzc3_36BbF2mttMxVKPjyd5FdUWnz0Yb0PVJ7aHI-7qq1qP8tHu9SbA0lb5Uj8utqOBgZADGsHOnpioy8smOl5wElwM1SsOtBoR0hidBhiJuDjR9F_c1w4ghoCjoPay9ZljgHv_G8rBGtVuCG4lVv1JikKAU4tRBSKJpS2sUiuT_x_eqD8P2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p6zufTwr2TqA8UR7kRthZLeVObYft2ABwneI2SmuJIwnV-RiAEGCJouXwahv4mGKNmVzc10MpIeLcKbnPjCZomesBxGC2xqh9zNSwOUyrFTcAP10senPv0W3NKpOcg2sAF7xIcQaYXcqBXHqVH_wwyooUjaorlT5C01ra_fJ8yJSZXGBslkvor6VUFxWQGKftLeaKJ8wY1_JO-Awa3R9-O7HMPVMxEOMqsyZsKlphrcDX6XpCgGckotOrvVZbTVeUSA2D-LqUZfl5lcjyFgUKV8JKuZ1Gk_XzVHKfN9VgIObUlngAKv4sDX3nNvUMv5GqV2Jq9FydJEeGr-R_uaVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=ijb4876oAFTLvsbziRq-tArnVsfZIGVidfM3K6poCEOY55qq8WlZwX2iH5QdETmdFrQ1uvR1Sh-gQzmQ7RvCiS5ukOW3f5FBbg2Of-yUxSXQWcE3mtL52owxpvuIvoUyT1hOAUcplECDwXTZqPvVpdzzPbV2N0EtaB0eRf5UbeTLtJ1QqrUjdfkeEfYZI46Fv7cPUTXXTqq_fN0JEcdy_H_Zk5JEepE-z29Pn-x5u4JY3vVKIVKrBEHo-dB5kmNaObcXDyiTk3VD9iN8CQCeHaWe8kb8opt44nNzAu6OsqQu4DltDYP6QOeTTgRXZl8vleI3-qUBh7-2yChJh6QdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=ijb4876oAFTLvsbziRq-tArnVsfZIGVidfM3K6poCEOY55qq8WlZwX2iH5QdETmdFrQ1uvR1Sh-gQzmQ7RvCiS5ukOW3f5FBbg2Of-yUxSXQWcE3mtL52owxpvuIvoUyT1hOAUcplECDwXTZqPvVpdzzPbV2N0EtaB0eRf5UbeTLtJ1QqrUjdfkeEfYZI46Fv7cPUTXXTqq_fN0JEcdy_H_Zk5JEepE-z29Pn-x5u4JY3vVKIVKrBEHo-dB5kmNaObcXDyiTk3VD9iN8CQCeHaWe8kb8opt44nNzAu6OsqQu4DltDYP6QOeTTgRXZl8vleI3-qUBh7-2yChJh6QdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6b2SsipOB8eYW4f7xTWt9aLG7W6CYp1TmivRKuqM2sH51T0R42SOgJ3qoZ6SshvE1D0tqFmy6wrUm3eEOm0jveORO0Mt5nbHTySCgJQtbEBnmLrf7AWxMCoj1OUPtu_i6xLKalwJDc3B0I0jdkgb8wU1XJlhamd1E64Mus9GCsZ7VdbVKkZ3mtfA2CzHqQGACw_RA4ZKp05gRqZpDGG8ueC7hWt0409WKUZhDwznNjER2vptXMLlFos743BmmIamhDdoHOxQIaIv2jMKRd5R9J8h-gCeoGytXxzvYHw7Ycu6v1znZn-N4r0nl9yRK-hjRbQe4z7bS9hcUSUdcDplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=SYx9A7ynhDT6faweYi5cKBrRK67R-611kElMBw3ED2I9qQFkyNwMUH46vRa6IHCgMb3LpaPKQFIxNw46t5rhc6Nn7bj7jnQVzB_Pt7IbcLtTSSPPExOsiOtQpYg5GxO48VW7Ffr4w0AqhPV7Br94CW9jwJLGlkr3nxL-OajhlQBq7qKNL5A8VO13mT66WniAxnQqqMk2BrVVNrFn1QZXjSzmtbKroEys9aGUd56V0JSxm7D2QjVveGzHlcsmle155FSvaK7W91JGZErb3rpL4joY0JgTOB_FLBa-f5qEuZAN5D1Bb12COOFNM83S8XAZ-IwRbPZhbpIqOHILmFE7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=SYx9A7ynhDT6faweYi5cKBrRK67R-611kElMBw3ED2I9qQFkyNwMUH46vRa6IHCgMb3LpaPKQFIxNw46t5rhc6Nn7bj7jnQVzB_Pt7IbcLtTSSPPExOsiOtQpYg5GxO48VW7Ffr4w0AqhPV7Br94CW9jwJLGlkr3nxL-OajhlQBq7qKNL5A8VO13mT66WniAxnQqqMk2BrVVNrFn1QZXjSzmtbKroEys9aGUd56V0JSxm7D2QjVveGzHlcsmle155FSvaK7W91JGZErb3rpL4joY0JgTOB_FLBa-f5qEuZAN5D1Bb12COOFNM83S8XAZ-IwRbPZhbpIqOHILmFE7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O5knj2RB2SYTCeUcqmkT06W6G-MH7S4QBQrC9c5JPCm3-LW5QUOz_hN4g7lJECLi3e6fmwLRbVJU057W8mqQqOo5sCwol9K7Kmdm3TBWsZgAGzem2dkpzlWISdp_tyPCs08lUwo4QCfjMt4AwWYEZFy_lwuaMl9d17PMITdPk-d6rwsblNhwUjdprU8I2dS8iQTVMNrhaCTiZ_4YwvTQ60V302sbog9Me0H8vwOGQ_o-HwwD3kb05gHhzwwBfj4pgIfXKyiITLV8RQPG6kI9nwh9FQj5hMVXP3p87MXEyWIAUZ49HLYn4d3hrGXRx2XtvZLKDGNv9ocsCWepmTJICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EIUX18CaR1JjIIqJAulXaP7ZNkbEa9cYyVd4SmMLF7ocd7VJOz7IYedczfsk4wBAqjz21sW-EPV29J_ZJiB-8AiDR4VXCveY5JupW4A_ZkEt6R8XPotBc0auljfgdU3BmlR_IPTpLdYaZ_SywjH1dUG24eNj0BFHn1oMngLHHgc09DJ_ewcm8-H7BE_XtDQW9POVgNPQ0H88LomdESWlLj0VlMeC5yeixXpQ8TWGQ5Do-0wuP67xpN3YbnMXRFmWmUrA5QSMcLohEY8Od7LS1B4EQlDXyaIww3R9hM4BZHgAgq9lJ5sN1P7A-e-OeevjRpDNKZx5A9lUDHzbSAhdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NlDt6tzTZqySh3EpBwVTZoLLoWeFv99ITTP5bneNDElrgudHG1xKMtVNmipI6xnDOXAgoJp_BRNcmvgdAIK29JZbVaCUWMwrzbAIm6OOFCW9SuNNfRsYgv5QIv5Bwug3o6fzwGSguBei-woLyi_KApP6Npmixh1L-lD4R_fX2lSrRcCK5Lar53jRpgbfwlKC571II1-iJo-77E5GmW7WLMfpz4cVkOz1SsqBnfQa5GLaJN1drsW-HHkLfPFbvbZTYRIXgZaAClgMDs9TxfOu6woRe4R_hlwJwX8eTwsZq9cJPBdbjNdng8sdjelGoi98c72dnOhQ3zfky10hdKb-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LNy08-wRupNLIWtVTeMSUfUmqiUY4uQfWXsU5iY8B_3k00k8mwod-S8WTFvcvTBXWOctVLmLBLj40UATgMO6d9q1S6y9rzXB01WqmkDnXu9-IEo483fibfFHZi5h0U06OrdHYIPT7Sz2ko5S0mNzvQYwgGN3lwd1H3slK4DzYCpmwUflxPIn5vbwNpUw2JCYfcTj0BkI4PAws-q-4sk241iU12ERba-imsRmWPvZMZv5ROCORy7rF3szaIBzt0PX5KXvIDH-ExWSOkLsvp1OrJ7ZCO_2YowPX_FUsxBz7EI2m0VXwHV_oIOQgFyOemeSCUe1zi0deU_kmkKMsB9z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FM_roVg9DE_XQQzYLwmkPzzjcWeLHjq5r-TDYK9cT38xU8dDLVuviF10jx_-ZYvN_pNw33tAWQOEX0Nk6K_g1CUvKVEJgj1McSfNtjIAL2vgq1El_1GK08stdT0CF_G7kyM_0663g2ZmcEz3f_yB5gfzUGiHvw-q8DUiIMCWGDXYfLkeICbq9xh4CqGbSWrnZudRI1KXssKBtGSg-9AEOd6Ly0tZAOAuQvWRTWH_yEKOxlEJxg1oGkVcy6ewun2vi9i-todERXMwr7-hzHuVv4qxlYTX2sBOUg2AyVUO3x0HeVndEefAHKd29LXfSr4myncCJzoVot6-EE45wDJ3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VVf1UeIdxze44_VKTzGEX7tpN-9Br6rIHJu_mr6O354sfM3RJpz32dbaMH4SknSOTgomrJ5prYhZLDrK7PWcf82ix1nxQFObOFe3WXLe1iKKTC6iI0Efqkf1FY5eqx9bNNtGI8G17j0az1jqne5wBuewL45ff-oCViGSSZ8_lGjmLWCn3xj2roTGXG5d5D5qiTQD4xWDevgEg836hyzWJo2ZNDw4YwQ3VMhyEX5HyXrp1WR_D-VlAfEgyxcaNGNRVeOfWaHriLjdtZLub9MlGK-oWssIN1Dm0Ln3KtkrcB7dWiabDYXNN414KhoXfEEmJyguficOZEoI5wrHaSxJSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">BadAngel66636
آرمین تیموری راد ۱۹ ساله
پدرش: امید تیموری راد ۴۷ ساله
عموش: امیر تیموری راد ۴۲ ساله
نوشته بودند ۱۸ دی در فردیس کرج به دست ماموران سرکوبگر حکومت کشته شدند.
روی مزارشون نوشته شده ۱۹ دی
و نوشته بودند:
به جز این سه نفر، همسر امید تیموری‌راد و مادر آرمین هم در پی اصابت گلولەهای جنگی، بە شدت مجروح شدە است:
@VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOenC_orqfnxUmAXEBKAMfXuv7vi5-F8scsCJAhyBicq7ftctv38XGXwflkcA7NXJhxT0GibS1JKdjnypzTprWxHmWo6HsHKLr5wiEKWVWAtuHC_Vp3aFdlwhWlBPLp0DiA4dnP8oHZXRmM3BUtlL60XtkYSyiB-E9qY6qedPR9n04duNM8qB5W4XsurQKzqJA_QvXT31MmXQfufxFyGeogaESzy8ClDnqWxTIZ5pEc2eL7DBTUJh2pQ396eKWK-zIpb8Ez5ywRANCJckWQe_n3IUqQ85S88Xckved1vjC0hWm-oVtu_nXMfWKMWSmKwA5HOokI7ZvZQBDDPtc3ftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=vKvo-nzilftsQoQKSsYv4KmInTFkzuUe7Pf0WklyxKj8Pd3UfAZ201g-T9F9_qynfr51E6XCci8QNehpf34Ta9yc2zPXEGEfXhXxs0HfqCuMYJt-H5D66NsET5ZnV2eGMuzrrLyv7Tb87sGD1lzoRkV5h7Hc5t51i2Er-o6c8CFv6hqsyFBgDvUPiqg4GGUqjgn9XOpmhlDlj0RFt2R9cx-W-5QM3s_XT31CU6D_27RVMLLxqfN5jw4ZbrWkT9Hg2v34GlnDFNYPl8AV5Hy5NichAdkP0bYUrNcBtlh10WLwvczdCE2Uu5cHrlgOdfkpIcRJj5dJODs2xVuISzB9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=vKvo-nzilftsQoQKSsYv4KmInTFkzuUe7Pf0WklyxKj8Pd3UfAZ201g-T9F9_qynfr51E6XCci8QNehpf34Ta9yc2zPXEGEfXhXxs0HfqCuMYJt-H5D66NsET5ZnV2eGMuzrrLyv7Tb87sGD1lzoRkV5h7Hc5t51i2Er-o6c8CFv6hqsyFBgDvUPiqg4GGUqjgn9XOpmhlDlj0RFt2R9cx-W-5QM3s_XT31CU6D_27RVMLLxqfN5jw4ZbrWkT9Hg2v34GlnDFNYPl8AV5Hy5NichAdkP0bYUrNcBtlh10WLwvczdCE2Uu5cHrlgOdfkpIcRJj5dJODs2xVuISzB9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H56gwrhJ2lnEhFvfFXzUOyiNXSRXmNVUisqfP_rWw6U0qL3TYBH1tLLM1107lc0M0568MfP9S9FFPNP_QWx8w0XqdA1PRw0a-cq2_dnqJpRiwLKU_9Lga-Ojh504U-6HfG325yzfiMqNwwySeKqvAHF8qYsKX_34cpNsw0HmUboclWY1INbf28Vjrn-FBbz1MNLLpYo3v9CCLbjMTNheTsRT6WnjGy1mOjeu_QqiH1owvv4-N8rYdbnY52vJn3GvPHix5Yw_0BoetViCYmmmkPPRRhuUAT24ILM7WIe0BnzFEIis67pS1vuF3w1aCOmhcnJV4LHGv2pspoHk_0DpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx_dC2k4cpcxBuBZWX5_Tr6zeaJZgrb4V2GnBwgtRiB2-yc5N3cCNUIQDwal5k3Zoi3jFnvhFtoS88gnkCf8gbdsIEqUnP598OW5_DxBjWmo3idUKwqg11psWwKoG4qwNH2urr0ak92KZGGFNequrYHYhG0-vQerzw-2SrZodkKeCCJN6tgVgN3A4FVw-j7d4ZS1d36F_msCkLGXhN3gnLqoDyaXDn7IAmytIxM388y4aQC2lsNr6xEpB3DWzCW5znEbrqwxafEjdoOQRVn_BIRXRIVNPFtGlNavxu3zQibkROnDS9Hhdi7oQGk34ax-dRTvXhOoyigpZeCAEzweLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم نیروی دریایی سپاه پاسداران انقلاب اسلامی روز شنبه در بیانیه‌ای اعلام کرد که سه نفتکش را که از «مسیرهای غیرمجاز در تنگه هرمز عبور می‌کردند، و همچنین سه شناور دیگر آمریکایی را در مناطق دیگر هدف قرار داده است.»
نیروی دریایی سپاه در این بیانیه به هدف قرار گرفتن سه نفتکش ایرانی توسط نیروهای آمریکایی در صبح امروز اشاره کرده و گفته است که این حملات خساراتی به‌بار آورده است.
@
VahidHeadline
علی محمدی، معاون سیاسی نیروی دریایی سپاه، روز شنبه در گفتگو با خبرگزاری فارس، گفت: «در ۱۰ روز منتهی به هشتم شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.»
او گفت:‌ «حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل اراده نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=Vjp6QLrST9hrmDzJp4TAeJGzqtz_wM66OEIP6los7tdwIQPgG6ct1lECprY-wwSk0AquvPvVEz0ccxyPGx_-VjkWGDbO-CQUv3BzRUxG5FuYjw15aWfl7g75ORA7DABRHaDYhuB2bhRDfNjcji0y20bOo8TsiHKqhBnGApxexENK2sGajfJd6d2F99uL9WDDTu2U1N83AdMDKSxDUNouD6OPc-Z3bpJTYXX9BdGqbh-dmlfGF9emAN8AfmZB1bcPEW56alON1tRaAzyk6zk6XvE0lAvkvOM0ovRGGcDw1KhuZqahXUKivsX5N2RWL6IAK08a9qothY7rQxawYrpOmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=Vjp6QLrST9hrmDzJp4TAeJGzqtz_wM66OEIP6los7tdwIQPgG6ct1lECprY-wwSk0AquvPvVEz0ccxyPGx_-VjkWGDbO-CQUv3BzRUxG5FuYjw15aWfl7g75ORA7DABRHaDYhuB2bhRDfNjcji0y20bOo8TsiHKqhBnGApxexENK2sGajfJd6d2F99uL9WDDTu2U1N83AdMDKSxDUNouD6OPc-Z3bpJTYXX9BdGqbh-dmlfGF9emAN8AfmZB1bcPEW56alON1tRaAzyk6zk6XvE0lAvkvOM0ovRGGcDw1KhuZqahXUKivsX5N2RWL6IAK08a9qothY7rQxawYrpOmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giRCZ59Sjcu0hLrV7OD2rLdFm33zOvsmIUxuepArvNsR17yocOAmmgAadCeADyjPCjmCVTfte0OCtYLs-Gpl9irH_jEG7PB6FwWpWDKwlAVXcK-bJPIooIKplthixIWXJ2nPYGpZzOlbXaubYLRuIYx9eYmeGRz_KkTzQZTW9Z4xMzwuizwL00QxX3wjgDkB9e0g7XL-5Aca-69kc1MQYu4et9z8-8E1FC3sCooPFHFEW_IAXUM4duzrptEwFOYm0YlrsDOnTcWvMeoyqGqMqaEu4nyVXBaPgUloludQTRMpEfumEB3sy4Wfva4tFVnj2mtycaNybhELZ1nStzODag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWMW_R4QmSWTVi42c8sw8YmtVppcQL4uLat94S-_nlTn4Pgk0lNDJ5jl2iCzydPhSSvBb2thjYT0egGLXwZji8FygwnPbIUCoGHs4EATPOAEs3oWMjLCJbzBJter3qfzHVeJSLErHSbuv2JMwLXcInEuC1aHWGXmxN_nAqAlZ_We9WlCJoACcNm-gksGRJlpieUfWnT9C0WjEgPyeRkVg967nm3MmqErBm3wgOzTPLVxtU0yix5_veYddEvoXF2Odiwa2mtm4YG1oyFazrxfnPaXb1_WtUJ46sRC_iqXX_Of8LmFwEGAsG8B6v70gUvm9pgQqZzqud8l5yBCT_Ai9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pV5hoD28ZB0l-a8PCv9ppc10gr8tCCBYkvwlhtV4SjdlAAFEcUB9EsnJ-yS9uscIZlMGZcn6j5okPw37xTqUPAWz0ksaf57Bk8VD8G_J2oCBptDvik3DSF_74GrgPCmSbS76BS_vmY4QvZ2Evx1DYcClBFCuzmWf27uLZdn5O8uBNgITI8LArP47FE7elP-_FxcTt_uXrJrSQeTeRHFmcGuFRMpBXSyTloRPclgt5TFkE77pT_blxA3-3ifG4PW4Yms87xtism3gC3PjqsvQv2iWUaz9dXhQ8c_yYu1gCFJJw4rIcnlzFWZOC0Aswq2CHFySqDWgoN2Vrrp3bnmZEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❇️
مادر دو معترض جان‌باخته، در لاهیجان بازداشت
🔹
مادر دو جانباخته اعتراضات ایران نزهت میرراضی، معروف به «مامان نزهت»، مادر علی و عماد شوش، دو تن از جان‌باختگان اعتراضات سراسری ایران، روز جمعه ۱۳ شهریور در لاهیجان بازداشت و به مکانی نامعلوم منتقل شده است.
🔹
نیروهای امنیتی نزهت میرراضی را در حالی بازداشت کردند که تاکنون اطلاعاتی درباره نهاد بازداشت‌کننده، محل نگهداری و اتهامات احتمالی مطرح‌شده علیه او منتشر نشده است.
🔹
بازداشت این مادر دادخواه یک روز پس از آن روی داد که او با انتشار ویدئویی به پیشواز زادروز یکی از دو فرزند کشته‌شده‌اش، عماد شوش، رفته بود. خانم میرراضی همزمان با افزایش فشارهای امنیتی در استان گیلان و جلوگیری نیروهای اطلاعاتی و انتظامی از برگزاری مراسم زادروز هومن صباغ بر سر مزار او در لاهیجان صورت گرفته است.
🔹
نزهت میرراضی در دو دوره از اعتراضات سراسری ایران دو فرزند خود را از دست داده است.علی شوش، شاعر، بازیگر تئاتر و نوازنده اهل لاهیجان، در جریان اعتراضات سراسری «زن، زندگی، آزادی» در سال ۱۴۰۱ جان باخت. هه‌نگاو می‌گوید او در جریان اعتراضات در اصفهان به دست نیروهای حکومتی کشته شد.
🔹
عماد شوش، برادر علی، نیز از اعضای فعال خانواده‌های دادخواه بود و بر اساس گزارش‌ها، در جریان اعتراضات سال ۱۴۰۱ سابقه بازداشت داشت.
🔹
عماد شوش روز ۱۸ دی ۱۴۰۴ در جریان اعتراضات در لاهیجان بر اثر شلیک مستقیم نیروهای حکومتی و اصابت چهار گلوله جان باخت.
🔹
در هفته‌ی گذشته نیز جعفر پناهی به دیدار مادر این خانواده رفته بود.
@MahmoudianMehdi</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=Jzf87Zj0ll8PrinMDFZo8Tm1Y7qzku14khzsxnGlQ9mIYeJyDJxYy42Hn_slWLL4_d_Q16xLmeM0H3b5dWlCJXjrRNT25GfyQGQuGpsjytsPH-nEDLgLBALU26UruK0LV-KsSxrQD4TjPRuw50B7Why2hIKvvw-KKka1nZvt0s_KxnVYWeXXsY9ubeId9zpkiBiQE4DdxGslogIe2MSVWVq5DDLw7IQpSQANqnODVyoYCLo7gk7a2nx2d-IcYvS_k-XiQd1PV7fL69oxUykHXSokR9R1EPO5a2SgNoa1quUgpaq0QiS7W0Q4VGiJXWDpaq6bBYh7fvEhr-FtnM9rRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=Jzf87Zj0ll8PrinMDFZo8Tm1Y7qzku14khzsxnGlQ9mIYeJyDJxYy42Hn_slWLL4_d_Q16xLmeM0H3b5dWlCJXjrRNT25GfyQGQuGpsjytsPH-nEDLgLBALU26UruK0LV-KsSxrQD4TjPRuw50B7Why2hIKvvw-KKka1nZvt0s_KxnVYWeXXsY9ubeId9zpkiBiQE4DdxGslogIe2MSVWVq5DDLw7IQpSQANqnODVyoYCLo7gk7a2nx2d-IcYvS_k-XiQd1PV7fL69oxUykHXSokR9R1EPO5a2SgNoa1quUgpaq0QiS7W0Q4VGiJXWDpaq6bBYh7fvEhr-FtnM9rRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت سنتکام:
'
سنتکام پس از هدف قرار گرفتن ۲ ناو جنگی نیروی دریایی آمریکا توسط ایران، ۳ نفتکش سپاه پاسداران را منهدم کرد
'
ترجمه ماشین:
تامپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) روز ۵ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی موشک‌های بالستیک به سوی دو ناو جنگی نیروی دریایی آمریکا در حال گشت‌زنی در آب‌های منطقه شلیک کرد، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
یک ناو هواپیمابر آمریکا و یک ناوشکن مجهز به موشک‌های هدایت‌شونده با موفقیت از چندین حمله بدون تحریک قبلی ایران گریختند. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
پس از حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران،
M/T Downy
در نزدیکی ساحل جزیره خارک و
M/T Stark 1
در نزدیکی جاسک را به‌طور دائمی از کار انداخت. نیروهای آمریکایی همچنین نفتکش خالی
M/T Kylo
(که با نام «Noxen» نیز شناخته می‌شود) را در دریای عمان به‌طور کامل منهدم کردند؛ این شناور پس از آنکه به خدمه دستور داده شد کشتی را ترک کنند، در چندین نقطه حیاتی هدف قرار گرفت تا غیرقابل استفاده شود.
این سه نفتکش ایرانی بخشی از یک شبکه سایه چندمیلیارددلاری هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ ابزاری برای دفاع از آن‌ها ندارد.
دریاسالار برد کوپر، فرمانده سنتکام، گفت: «پیام به سپاه پاسداران روشن باشد: اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه کشتی شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و در معرض آسیب ایران را نابود خواهیم کرد.»
CENTCOM
دقایقی بعد در پستی دیگر:
«پیام به سپاه پاسداران باید روشن باشد: اگر به دو فروند از کشتی‌های ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه فروند از کشتی‌های شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و آسیب‌پذیر ایران را نابود خواهیم کرد.» — دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
پیت هگست وزیر جنگ آمریکا:
ساده است: اگر ایران به کشتی‌های آمریکا شلیک کند، ما نفتکش‌هایش را نابود خواهیم کرد (و غرقشان خواهیم کرد). تنها کاری که باید بکنند این است که شلیک به @‌USNavy را متوقف کنند.
ناوگان نفتکش‌های ایران بی‌دفاع است — ایران نه نیروی دریایی دارد و نه نیروی هوایی. هواپیماها، کشتی‌ها و زیردریایی‌های ما می‌توانند همه آن‌ها را، در حوزه‌های @‌CENTCOM و @‌USPACOM، هدف قرار دهند.
PeteHegseth
خبرگزاری صداوسیمای جمهوری اسلامی گزارش کرده که خدمه دو نفتکشی که امروز از سوی آمریکا مورد حمله قرار گرفته بودند «با قایق‌های نجات به ساحل منتقل شدند.»
براساس این خبر یکی از این نفتکش‌ها «خالی و دومی حامل محموله نفت» بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZ6lb1P2rqrlm4Pp2zScRfdjqESr079VEQI4NXS0TJjn-Dk5Ur3YQ99ELSBfkvDCVpRBO_BPS43_33i3FQMyZME_RDWKAXeGSSMzbso9tiXIcHKiBTTRAU7b6UbHd5x8Em2RS9OZZA9s0XjsnxCS3lONvozzbJNXRV5ZtYslxRtTWl1_h7N3vB314-HEWBaPaftrOkjWU6y9DR6e_MM1pOm37UwNldYz-Rj_A4Ag1GDM4S7W04xcIBHy72ZpNvMtxwVd22fqXSIs7QR9VGqJZKc9Lrnb660FfOE2aSJuWEm4Ln1nM03aprbwNZycGnQ7K5jLu5RWH26arM8U_Axf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز شنبه ۱۴ شهریور با جهشی دیگر به ۲۲۸ هزار تومان رسید و بهای یورو نیز از ۲۶۳ هزار تومان عبور کرد.
وب‌سایت‌هایی که نرخ غیررسمی ارز در ایران را به نمایش می‌گذارند، همچنین بهای پوند انگلیس را ۳۰۷ هزار و درهم امارات را بیش از ۶۲ هزار تومان اعلام کرده‌اند.
این افزایش مجدد تنها یک روز بعد از آن رخ داده که عبدالناصر همتی، رئیس‌کل بانک مرکزی ایران، کمبود جدی ارز برای واردات را رد کرد و کاهش شدید پول ملی ایران را ناشی از افزایش تقاضای «احتیاطی، سفته‌بازانه و خروج سرمایه» دانست.
قیمت دلار در ابتدای شهریور از مرز ۲۰۰ هزار تومان عبور کرد و طی دو هفته گذشته به شکل مداوم افزایش یافته است.
این در حالی است که همتی هفته پیش گفته بود ایران «به‌اندازهٔ کافی» ارز در اختیار دارد و بانک مرکزی در صورت نیاز آمادهٔ تزریق تا دو میلیارد دلار به بازار است، اما این اظهارات مانع ادامهٔ افزایش نرخ ارز نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78240" target="_blank">📅 17:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFcTHLs_WrlFA16fAoUZfVxmR_PgDkqy9fP8FWOSs55M6MnJ16NftsDr7t2nBCLj1ONv9xmJh9InorMDjAwnZT0e15pnsqVhsn6lUSItBnKfZMAxDTHHqzgTrEVZpfg9M0nflPoD82sMqo5N16QgMo1JNy_9_-DRDH1no1EblZB1RBhTPnmDxZSdbzTIhwXUHqrbSZHxcLt9aHEBMu2oYyFZgzHsoX7khnhsM3tfQobA8ZMncwoxcjo7shJwzVLxffc08NW5cQdu_OKr36nQ7sOOXbctIPqdLZ-TksbpEpE8RZ_GngKNxhrgwRSTFBt0KNW0UbESLgi7EggrTO6xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده روز جمعه ۱۳ شهریور از موافقت با فروش پنج میلیارد دلار بمب، کیت‌های هدایت و دیگر تجهیزات نظامی به عربستان سعودی خبر داد.
این وزارتخانه اعلام کرد این فروش، توان دفاع هوایی عربستان را برای مقابله با تهدیدهای کنونی و آینده منطقه‌ای تقویت و هماهنگی تجهیزات این کشور با سامانه‌های نیروهای آمریکایی و دیگر شرکای واشینگتن در خلیج فارس را بیشتر می‌کند.
عربستان سعودی از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران بارها هدف حملات موشکی و پهپادی نیروهای ایرانی و حوثی‌های مورد حمایت تهران در یمن قرار گرفته است.
وزارت خارجه آمریکا کنگره را از این معامله مطلع کرده است؛ این فروش برای نهایی شدن همچنان به تأیید قانون‌گذاران آمریکایی نیاز دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78239" target="_blank">📅 17:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19446f537f.mp4?token=Mh4jSdnOQskZM2-bkxLgLWr-zC9MjeDfnJ8wDs8-0dVuPH-vNg9XjVXKl3vwBiPLYv7l6Oq9gQNtcdqbyJRCg54cm-mIAmS3FgjknrEIwRkSq-RqxMW376vEmFyA-MJCkPEQJ_6nj56S-NSIDO-Nixkm7yoY_gZvWc3QP8JCknpxpKCIqZmjzFLYS65IuCrG7jJqBs4m1_22P4t9z0CafpmQ_mlbAl7GIwJ0U2dsg26h5NUOvXghVB2Yyu9nippPgh5CGTyIj2JmK5WX3u8yCxH_aEemvA7FaZ8FjpJDnBmZ8HOCJ9yfzKjhpnNW1ZyLCiKXig-k5zzTRY_vn4_vrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19446f537f.mp4?token=Mh4jSdnOQskZM2-bkxLgLWr-zC9MjeDfnJ8wDs8-0dVuPH-vNg9XjVXKl3vwBiPLYv7l6Oq9gQNtcdqbyJRCg54cm-mIAmS3FgjknrEIwRkSq-RqxMW376vEmFyA-MJCkPEQJ_6nj56S-NSIDO-Nixkm7yoY_gZvWc3QP8JCknpxpKCIqZmjzFLYS65IuCrG7jJqBs4m1_22P4t9z0CafpmQ_mlbAl7GIwJ0U2dsg26h5NUOvXghVB2Yyu9nippPgh5CGTyIj2JmK5WX3u8yCxH_aEemvA7FaZ8FjpJDnBmZ8HOCJ9yfzKjhpnNW1ZyLCiKXig-k5zzTRY_vn4_vrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های ایران از شنیده شدن صدای چند انفجار در نزدیکی جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و هدف قرار گرفتن یک نفتکش کوچک ایرانی خبر داده‌اند.
خبرگزاری تسنیم گزارش داد این نفتکش صبح شنبه ۱۴ شهریور در شش مایلی جزیره خارک و در محدوده لنگرگاه، «هدف قرار گرفته است.»
تسنیم می‌گوید این هدف‌گیری «با چهار پرتابه نیروهای آمریکایی» انجام شده است.
به گفته منابع محلی، این حادثه تلفات جانی نداشته و کارکنان در حال تخلیه نفتکش هستند. وب‌سایت عصر ایران نیز اصابت چهار پرتابه به این شناور را گزارش کرده است.
خبرگزاری فارس پیشتر اعلام کرده بود که صدای انفجارها از محدوده خلیج فارس شنیده شده، اما نشانه‌ای از دود مشاهده نشده و منشأ صداها مشخص نیست.
نورنیوز نیز به نقل از منابع محلی، گزارش «حمله موشکی آمریکا به یک نفتکش ایرانی» را منتشر کرد، اما آن را تأییدنشده خواند.
خبرگزاری دانشجو هم ویدیویی را منتشر کرده که می‌گوید مربوط به این نفتکش هدف قرار گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78238" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=d_S-tMz1Gwxc8ToBqjw1qtVBF2EqAFE4oCyYG8LVq8gVLM1Oiokpz1uqu0WqYlP5_3ys2LIY-wN_vyQXQJBcELymh0jjGTEzgkqJs3Xl2x0lutQpEHWhaTkZIrMkPwV9YCDjPF1niRl6ARCMpl94fwsVlSPJ4LEmCcXUBBzTDezBxMBu2tNUm5Vb6Tww8KljDccc5O6kDisbqv_yqiFYOvuRRRlgYCjXI6RJ5Hv2VcDhQ1WfrLx6b2vqvyPtugCIbcuRXwqc-3QHbz78ZKUdW09cove6jn6rNeCoh0jAJOkkPWXMqBVYF6IRE6CeRsR7H_sCfwdUMWW0NwyW39U9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=d_S-tMz1Gwxc8ToBqjw1qtVBF2EqAFE4oCyYG8LVq8gVLM1Oiokpz1uqu0WqYlP5_3ys2LIY-wN_vyQXQJBcELymh0jjGTEzgkqJs3Xl2x0lutQpEHWhaTkZIrMkPwV9YCDjPF1niRl6ARCMpl94fwsVlSPJ4LEmCcXUBBzTDezBxMBu2tNUm5Vb6Tww8KljDccc5O6kDisbqv_yqiFYOvuRRRlgYCjXI6RJ5Hv2VcDhQ1WfrLx6b2vqvyPtugCIbcuRXwqc-3QHbz78ZKUdW09cove6jn6rNeCoh0jAJOkkPWXMqBVYF6IRE6CeRsR7H_sCfwdUMWW0NwyW39U9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتین خواجوی‌نیا، دانش‌آموز ۱۶ ساله رشته کامپیوتر، شامگاه ۱۸دی۱۴۰۴ در جریان اعتراضات مقابل فرمانداری شهر قدس، قلعه حسن‌خان، با شلیک گلوله جنگی کشته شد.
مادر آرتین ویدیویی از جمع‌آوری کفش‌های فرزندش منتشر کرده است؛ کفش‌هایی از دوره‌های مختلف زندگی او که حالا به یادگار مانده‌اند.
مادر این نوجوان کشته شده، نوشته است: «از اولین تا آخرین قدم‌های تو را مرور می‌کنم پسر قهرمانم. از لحظه‌به‌لحظه بزرگ شدنت حالا فقط خاطراتی برای من مانده که هر ثانیه از مقابل چشمانم می‌گذرد.»
«از آن نوزاد زیبا با آن لباس زرد در آغوشم تا آن مرد بلند قامتی که باید برای دیدنش سرم را بالا می‌بردم، تو همیشه یادگار مادر شدن من خواهی ماند.»
او فرزندش را «قهرمان جاودانه من» خطاب کرده و نوشته است: «هر لحظه و هر جا یادت جاوید و راهت پرنور.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78237" target="_blank">📅 17:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/toJRrN-7M4RFnIiTKfnCoFVfeb9eBfBcqmSMfeXu7vDAu1V2cZXdVZUXhw3teFBb_yhTwAy4trFip0qgSYMWbuvYsWDUiG4S2KACcClikqhgMK4m46C4Ap1omKgxWO0fB-hesL4BiVcypNBj5_NxKyvzQA2HtGCWIQuaSIdTvqg5sPoSYSlq_Nycs-I4hUvCTy0Nq9m6Cwga1RcZFxfSemcWGqMbAEIKeSAmECqcAVeBIKOflbLV67VBxrkCXefiVYncMb04_u1zPAbyCsSqjblR_agAavpz1A_ntTS3089q-eeaQOsACKHx3EAcdlWAFXUVhrxwPhH21unfstoWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdOuWtv5UmlhhrLunlywWLM3NQLnj1-ui8z8w23Tt3KPKUxAdWM4KnZ_w0ZGV1OeZGhidDlF2y3rdwNTZuJg8AvmBh1vVdI8wBQIaAo9rHettorFNpQC0uSenDOxDSAiYbF3IuBWAON-fro3KxjbVR12AYnm_dF-VmR_dDYXqds0CgJvcuQjH9GwI56RCh-aWj5hAFRDziD1gM6dhZvbXZKDDh66kuBp15FaPtnUxYVevTnGTBrW8NaHZIRNOue0POXXgtmGjiWdqtAVVp3BOsonWaR3tpWDa7JLjyKoLvgA6A_1TH2OorXRyRNG0nyTf7bCmyqQ06PeNLWor_y1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JXd35j7zCe2ZQ98ja8ffy60bBSvOz9YK6flu7PMGEjjnvdb08p5Jx2rvhHxUzmpnrAMIpIKjvyarpq-Y6UoDk-d-cuVnN63Z_Qhuh0K7KifpAcWw5oiFUAGUKzlFYAMglY4ZgCSVdD59XtI8FWCj8veTqS2EmSAE7_u4DGSKnA63o8o6I7aApjZHFukdm-XpuR9PBQE6AqEpnvZ3c7GM90qav9hi0wg1azhsurcfcfbQHjJLSaL-Ubfzx1YMXBN75lNmPuRBu9FQilmgSKpk7YIS3jlGR-ib7ZNTEqsPYgH4dKEiYEhJy0N4ZUy1pUOksjJ7-BSnB74rs6cWoId6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا یک بانک مستقر در ترکیه و دو شرکت وابسته به آن را به دلیل تسهیل انتقال ده‌ها میلیون دلار برای نیروی قدس سپاه پاسداران و فراهم کردن دسترسی جمهوری اسلامی به شبکه بانکی بین‌المللی تحریم کرد.
وزارت خزانه‌داری آمریکا روز جمعه ۱۳ شهریور اعلام کرد «گلدن گلوبال بانک» و دو شرکت زیرمجموعه آن، «گلدن گلوبال وارلیک کیرالاما» و «گلدن گلوبال پورتفوی یونتیمی»، در چارچوب عملیات «طرد اقتصادی» به فهرست تحریم‌ها افزوده شده‌اند. هر سه نهاد در ترکیه مستقر هستند.
وزارت خزانه‌داری آمریکا همچنین در حساب رسمی خود در شبکه اجتماعی «ایکس» اعلام کرد این اقدام بخشی از عملیات «طرد اقتصادی» است و هدف آن قطع «شریان‌های حیاتی مالی» جمهوری اسلامی در ترکیه است. به گفته این وزارتخانه، گلدن گلوبال بانک و شرکت‌های وابسته به آن ده‌ها میلیون دلار تراکنش برای نیروی قدس سپاه پاسداران تسهیل کرده و دسترسی مهمی به خدمات بانکداری کارگزاری در اختیار جمهوری اسلامی قرار داده‌اند؛ دسترسی‌ای که امکان جابه‌جایی بین‌المللی منابع مالی حکومت ایران را فراهم می‌کند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، با اشاره به کارزار دولت پرزیدنت ترامپ برای قطع منابع مالی جمهوری اسلامی گفت مؤسسات مالی همچنان درمی‌یابند که ایالات متحده در اجرای عملیات «طرد اقتصادی» جدی است.
او افزود آمریکا امیدوار است بانک‌های بیشتری نیاز به تحریم نداشته باشند، اما این مسئله به این بستگی دارد که جامعه بین‌المللی به سرعت حمایت از حکومت ایران را متوقف کند. آقای بسنت همچنین تأکید کرد ایالات متحده به همراه متحدان و شرکای خود به اقدامات علیه شبکه‌های مالی جمهوری اسلامی ادامه خواهد داد.
بر اساس اعلام وزارت خزانه‌داری آمریکا، گلدن گلوبال بانک برای فراهم کردن امکان انتقال درآمدهای نفتی جمهوری اسلامی از چین به ترکیه ایجاد شده بود؛ درآمدهایی که پس از انتقال به ترکیه می‌توانست به پول نقد و طلا تبدیل شود.
وزارت خزانه‌داری می‌گوید این بانک همچنین آگاهانه پیشنهاد ارائه خدمات بانکداری کارگزاری به مؤسسات مالی جمهوری اسلامی را داده و از این طریق انجام تراکنش از طریق حساب‌های تحت کنترل نیروی قدس سپاه پاسداران و شبکه‌های وابسته به آن را امکان‌پذیر کرده است.
در اطلاعیه وزارت خزانه‌داری همچنین به شبکه «سیتکی آیان»، بازرگان ترکیه‌ای، اشاره شده است. ایالات متحده این شبکه را پیش‌تر در سال ۱۴۰۱ به دلیل نقش آن در انتقال صدها میلیون دلار درآمد حاصل از فروش نفت مرتبط با نیروی قدس سپاه پاسداران تحریم کرده بود.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، جمعه ۱۳ شهریور در شبکه اجتماعی ایکس نوشت از زمان برقراری دوباره محاصره آمریکا، هیچ محموله نفت خام ایران نتوانسته با موفقیت از تنگه هرمز عبور کند و به چین برسد.
او افزود نفت خام در کشتی‌های گرفتار در داخل تنگه انباشته شده و امکان جایگزین کردن ذخایر صادرشده وجود ندارد.
بسنت نوشت: «مسیر حیاتی صادرات ایران در حال قطع شدن است؛ نفت سرگردان، ظرفیت محدود ذخیره‌سازی و درآمدهایی که به‌سرعت در حال کاهش است.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78233" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYF-45MgEqdIVuAwNIO-UccJS3tpAPbhWfEBWzvYwpAmCb3APqWxZvMY0mG4pxN6dGjGU6B5s-8bhGMiCS14vaVufG3YQJkfrwQ2zKensAw1Jo-RszSfBwYcR6EhVFia5pE13FFH9_UqFU2QZpLRihwYx3Tmeo1OAN0FhlKSFYwVUdjGvgu_mClaFYCdaKMy0trsLA1yBXPDOdubX65Qx2HyLp8Y7PVckALQOgRT8m0osj8S7j8yjhcVXxpjkwEMhKG277IRR89bogrBBw80KcPsqYXtvtPXut8wNn9Gecxbxhk4Bc0qUAHj92oXPaNHEIDJJl_pEL5UTbrWgzr2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
دیوانه‌های چپ رادیکال، دموکرات‌های احمق و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ جنگ را برای آمریکا ببرد.
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه ما پیروز شویم!
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ چیزی که گاهی از آن با عنوان «سندرم جنون ترامپ» (TRUMP DERANGEMENT SYNDROME) یاد می‌شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78232" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byNFRBhsJ_cZXS0BKy13fkcSdyqBzEjXrhfEUS2mytVOrQjsUdmmLQyeiPYmFXIAGBwp0HDesjgbshYZzyN6LHb05djvH-nej4-JPJNBKMrxEoq1ThlsTo06Nk0_W8Qjv9Ze0EHtVb_dHtOD_Us5QYGS7HCCpAyJLf-nnZnMRZq5fcEr-ei9GWwIW2w_eMApSeiu_MB7APhohtBhJFol1s1sOU2vb7YlekCCSYBJm7bBoTeucc_9UOYXuXiohA2UjrSUXl0bOENaczAjnDKisfxzb88wkFt3aeWiNdvkDTM9tz4mzJXw_XaTJTpG7F7P1ICw20abDN-XyJDv3KaMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «فایننشال تایمز» روز جمعه ۱۳ شهریور در گزارشی اعلام کرد اختلافات میان ایالات متحده و جمهوری اسلامی ایران بیش از پیش بر سر آینده تنگه هرمز متمرکز شده است؛ چرا که دولت دونالد ترامپ بازگشت به یادداشت تفاهم اسلام‌آباد را رد کرده، در حالی که تهران خواهان احیای این توافق به عنوان زمینه‌ای برای کاهش تنش‌ها و ازسرگیری عبور نفت از تنگه هرمز است.
بر اساس این گزارش، تلاش‌های دیپلماتیک برای بازگرداندن طرفین به تفاهم‌نامه اسلام‌آباد که شامل توقف اقدامات نظامی، بازگشایی تنگه هرمز و آغاز مذاکرات جامع‌تر بود، با مخالفت واشنگتن روبرو شده است. آمریکا اکنون خواستار توافقی جدید و فراگیرتر است که علاوه بر وضعیت تنگه هرمز، پرونده هسته‌ای ایران را نیز شامل شود.
در مقابل، مسعود پزشکیان تاکید کرده که کشورش آماده است به محض بازگشت آمریکا به تعهدات خود در توافق موقت، به تعهداتش عمل کند.
با این حال، واشنگتن بر اهرم فشار میدانی حساب باز کرده و با تقویت حضور نظامی، مین‌روبی و ایجاد مسیرهای امن، سعی دارد ثابت کند ایران دیگر نمی‌تواند از تنگه هرمز به عنوان یک کارت فشار بر بازار انرژی استفاده کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78231" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAR1rVCXH5KMEEzFsFBszLDm0ZL2vfKD2hMtpC28PBXEgDAaD3pdhHBrNZDBNW0PxCaspnAyPcvSseDef1eEZTEiuV01pQWHL8m5x_dy7J5Zl_nkcbGQjcTjTZM4PU_kz43zO9FnR0dXvu0yCIgEVzyIW-3D-Pi7smeepRPzsDWvnkhYBosDqO981NMs-tI0UCsLh2IQjrAjGsvecrYLHatef0ZhVhbo-hv3HWdlWN716qaK4fb2QsxH0zussJP52C4wPfOnjL13ZFw2LZmvgV1WnUiYjK4jtER_ztD6tleFLmNmaSiX7MAEmZhJpDD1H7L-Pd9cf2ik1zOjC8IjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گازوئیل در آمریکا با ثبت رکورد تازه‌ای به بیش از پنج و نیم دلار در هر گالن رسید.
انجمن اتوموبیل آمریکا روز جمعه ۱۳ شهریور اعلام کرد که قیمت گازوئیل در این کشور در حال حاضر به پنج دلار و ۸۵ سنت به ازای هر گالن رسیده، در حالی که یک سال پیش قیمت آن سه دلار و ۷۱ سنت بود.
هر گالن حدود ۳.۸ لیتر است.
انجمن یادشده این افزایش قیمت را ناشی از اختلالات در حمل‌ونقل سوخت به‌دلیل جنگ آمریکا با ایران عنوان کرده است.
گازوئیل، سوخت حیاتی مورد استفاده در حمل‌ونقل جاده‌ای، کشاورزی و ساخت‌وساز محسوب می‌شود و بیم آن می‌رود که افزایش چشمگیر قیمت آن، نرخ تورم را افزایش دهد.
قیمت بنزین معمولی در آمریکا نیز چهار دلار و ۱۵ سنت به ازای هر گالن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78230" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amvXggeITBVzIZNzsSBlFUEzz3Xdtd8OKbn-nQfas9X6YX4l0Fg_Mc2YbulvRgTnZDhb6nNgUZG94e64by63mXrg1wptFPgSunUdTLJsiXbuM30aNisO2fHVR6KtNmmv0uaDLkXQkZmG2j5okGl3Nk4KXck_THB4ta7nOeRbORDzIGQ0lkke8_YOXtEaK_8jmGVOf7Oi1P1sRMSOGOaHfn-c8rew5Fq3vF5skY2nZYElI_JGpGbcMfX7mVlHOzHzVHdVp8__T6_H-yW-nKhWP8HAN9DigdM73Vu37LhhyatP_p72e0O_7gELdzTZV5M-qk0WLHvhMYP1TwpvnGI45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌هایی که من دیروز دریافت کرده بودم:
▪️
آزمون Pte  زبان برای ساکنان ایران لغو شد
▪️
موسسه‌ی پیرسون هم تمام آزمون‌هاش رو برای ساکنین ایران کنسل کرد.
امروز صبح روی سایت اعلامیه زدن یک دفعه.
مشهورترین‌هاش برای ایرانی‌ها امتحان مدیکال کانسیل استرالیا و وزارت بهداشت عمان هست.
و امتحان‌ زبان PTE
▪️
ما جمعی از پزشکا برای مهاجرت استرالیا تلاش میکردیم و هزینه ازمونمون ۳۰۰۰ دلار بود
الان لغو شده بدون هیچ توضیح خاصی
دوستان هتل و پرواز بوک کرده بودند برن هند پیام بدن الان میگه نمیشه باید کارت اقامت کشور دیگه ارائه بدی
خبر:
موسسه بریتانیایی «پیرسون» که برگزار کننده آزمون‌ زبان انگلیسی «پی‌تی‌ئی» و آزمون ای‌ام‌سی (شورای پزشکی استرالیا) است، در بیانیه‌ای اعلام کرد که به دلیل تحریم‌های جدید آمریکا علیه ایران، آزمون‌های داوطلبان ساکن ایران را لغو می‌کند.
پیشتر در تاریخ ۷شهریور۱۴۰۵، تعداد دیگری از برگزارکنندگان آزمون‌های مهارت‌های زبان‌های خارجی، از جمله دولینگو و تافل، اعلام کرده بودند که این آزمون‌ها دیگر در ایران برگزار نخواهد شد.
پیرسون در اطلاعیه‌ای درباره لغو آزمون پی‌تی‌ئی آورده است: «در پی تعلیق 'مجوز عمومی G' توسط دفتر کنترل دارایی‌های خارجی (OFAC) در وزارت دارایی آمریکا، از ساعت ۱۲:۰۰ بامداد هشتم سپتامبر ۲۰۲۶ به وقت شرق آمریکا تا اطلاع ثانوی، ما قادر به برنامه‌ریزی یا برگزاری آزمون برای داوطلبان ساکن ایران‌ نخواهیم بود، مگر آنکه بتوانند مدرکی دال بر اقامت اصلی خود در خارج از ایران ارایه کنند.»
در ادامه این اطلاعیه آمده است: «آزمون‌هایی که در حال حاضر برای داوطلبان مشمول این محدودیت برنامه‌ریزی شده‌اند، لغو خواهند شد. به‌خاطر این مشکل که برای آنها ایجاد شده، پوزش می‌طلبیم.»
سرنوشت شمار زیادی از دانشجویانی که قصد مهاجرت با هدف ادامه تحصیل به کشورهای اروپایی، آمریکا، آمریکای شمالی و استرالیا را دارند تحت تاثیر این اقدامات قرار خواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78229" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=rxnVToQ6JvLyR88ysLx7hofzTcTMr3E9hf_JS2qAERHUTNtwzExyzTQWnMl4G0VAzkwFqtaiN_4OfuUG1ds3erXsJqjAzi9arGfxjSPBK8KnZbvYnxgtgHbqwb1fJ8znu9-xmCuTFQ5jVc_a2rX3JPeeFlQ5H0Klg2HTpVcmJ3RAw4eW3nY-NjrtkFi0fXAIm7Rdg_M_M5pFYzTZeOJlBHzcPkFfjpyID0mtxBA8NWTXXmyqKLelNH6AhpsnMhZeqpms1GJtKnoW8krQfMF8ny8ba4X10cbeenCsYJw5KCmes2hBSo6utmygerkTWCoLAGqpW-mi9hosn72W-m74oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=rxnVToQ6JvLyR88ysLx7hofzTcTMr3E9hf_JS2qAERHUTNtwzExyzTQWnMl4G0VAzkwFqtaiN_4OfuUG1ds3erXsJqjAzi9arGfxjSPBK8KnZbvYnxgtgHbqwb1fJ8znu9-xmCuTFQ5jVc_a2rX3JPeeFlQ5H0Klg2HTpVcmJ3RAw4eW3nY-NjrtkFi0fXAIm7Rdg_M_M5pFYzTZeOJlBHzcPkFfjpyID0mtxBA8NWTXXmyqKLelNH6AhpsnMhZeqpms1GJtKnoW8krQfMF8ny8ba4X10cbeenCsYJw5KCmes2hBSo6utmygerkTWCoLAGqpW-mi9hosn72W-m74oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
الان از اصفهان موشک زدن یه دونه
سلام وحید جان
ساعت 7:12 دقیقه از اصفهان موشک شلیک کردن ( از سمت [....] اصفهان)
همین الان [...] اصفهان موشک رفت
19:13 از سمت [...] اصفهان موشک زدن
همین الان ۱۹:۱۲ از سمت [...] اصفهان
فکر کنم [...] بود
بالسیک شلیک شد به سمت [...] رفت
از اصفهان همین الان موشک زدن صدای وحشتناکی داد
اقا همین الان یه موشک از سمت اصفهان شلیک شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78228" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k8VyYGCOdOWFWKWe6kvuvwc3CFQL_p9jW7xrTv0uENKZ1VSL04PG7Krmf-aMlaDIaKePU2kefnefCLfY1jF-ixJzX0kiZ3xONRhBgnccvGB8XjHqcFYV8NAOEi3NS7ZEBacQbTvyLMYpTOQ9u1merGUPB0wwWFd8ci9_S0PZehJwb6o_i26_Ddm3HLuVQXELIybomXgvhJt-Aj4HO38jK9B9FykWXzvY2gbQ93huCuEuwc3MzIPcBMjH_xKXmtp7MgzJ4enuXPGqwfRseLAHQFXhWC9d__OSf4Q_ddPjI7zIn7znty_qRvjhIw0Eh1PYYrgOX4YFVWIGtpJopJiKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O9qv9jt0gogg5IoClRUkFZhdCqw_NM7mcB6QmHYRfwrTJCZGTH1D86LEvRhJgs1AY5kPPcpShGwBUt-o02c_VrsxCxQ3MCulM_xDNtm-b2H3ALBmntKZG04IuOj7KLRT5mU8Nf3P2W-SHn7RwXW5EqIrHK4ngK0kNC-w_C28M27JTC7jfXvnoLcHNSO6WV0MkE99KckE6LtnGo0Xdo2zF6J81iW6wZNeQupTywBAK18DkTwPGsNh7QCrvdLjQrbUv5zk8rKb9E5dc2WLnvxizxGzp5zgXr1CMUCYyKzWhZPQPobYrWaIozVY897u6KtTTD8NenmfUjb5KVRKEJPGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVuqgpOnVMrygrFwqgOfnmBpwIccAPmL0ec8y6XR6ohkJ8yuxZMaUWGSp_IpVLR9mlskQDGWjWQsNoc386o5mj9IAyAwAG3nFp-pO7bYAkBWIpJV4yhWDfAknv5nqw8DVW5V0tc2a0AGCQlSFqniN6SEyHB0pKx31neSNb9znT01BQytsLrKmXHble5u3-YFx9ZXClvkeclX5rS264Hp8Eu6yHSceA1icHZiW8mcfiqhkJiXI25XjmTdbWZOBIdX3C6YNSPQIFkL_Aaes4RlGb0seK8wOkYfVKxPCON_gP8K81q9v4uKj-Y8SXZQ0biuB7WzF3YlFSl2Fy1adsHQLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A6wGidt-erlMFVXTbM5snY845fs7CZh9tSXqJwfOjPVj3WP34DYmwvx9DRgYCKGjgwVFQbSxhrAeoxH3ViFubTYqtH09kDb4sJSIdkD8QHOIdP9jBDkP587nvvbdwLU8c7_29gwXFwhP3Q9wKLNaT5HNFCn3r6Vkv3RRHlu1ULobIi1rgIdZY90gJWNTXu5h78k85uAtWQshdf_EhbojhhMMuOFP7c2Za8oqDsPkgQGOd4thyH5-Re1L9urYYuR5RHj6UdgozbqkmIVtkyWVAIhhiOdDZ4BYcdNuPcagatzb2ieTZz4P8N3w_8cr56gsHTUeI2bz59IVT1wiTZZk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a2_XNXvTeSPeGdeA39VOjPpXk7caL03wasSk6HugGmzaBPt_G1px1UiQYKiVLamrBtXy6OauinFF1JskjlO6ziwU24jN9P8UHu0YQdI91hFpwPojy8iL1YWY8kTa8hDqH5RBRQJ3xOhR24NFG1NHFXj30sfWfIYUR1r8iRune_zkiGnB-kFtdexlUe281uKykVv76Uts-xe1veS01gYw_5mWF2iCZLysG_QfJ_vip-dcPNBj8wPve0StJ5Kb92j2x3_iPyacSHTomnCDvgWuMVcb9jVq6pg5CoYvcLR6lafnwTI54KCT26Lkm2AlIwQPpD1jgn1ofRpAOdYsjEAlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K4I8CZrwOE7p2N_mqnBXKzYhnO_hv8ZQJwfxUXVjxi0Ns7t0ca0Bnemg585xjpNKTCGkiAiE9USr6FYF0e97TqByAcXMsVJvRrkDcBExnFMOlouvj-GdXm10eiwT3I_d7tddQmdEu_Wm6zUv5YGi6SWPF4zU8bVcCrctvjoODbzbDUNBkt-Gq3s_opfuco0aadfaVEKUSjorGWq8ygR2yo-KLOSjl3FkDYdFbrLNb1-Q4pUQGUHxI_vIp11CWUcwCHpD9syjYsPgkqmuQAvYdWXAoo09XQylAzereti5wV4iIQ_BpBb_bmqCBYupDsKSvhmS8r9kt0kwlUWEsvxrHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCH672_bhYOBchtd0P3V91YkvXlPRS-QpdAdfRTovW79l9pOJEo7dg9kVQhL9F0hzzs4lQzr2cSUbbBjtuUI-yNXlHSZihT0NnN-4-3s3pNsUiULahcCZpl2ceB23ITESP_nG9PC3MH6ZQofWznj0K_JDc_3yl0FWLWGyYg42TCMbpSdQsrQkYr0WqVARRbI3tqH7nTJL2ZqbtruTR3u4PJottbmsicxvqPcXMnNDRo88WcMIQxi0iWXkdC_rHzn6oWbXdL9W94daiU4jsv5y75244SV0GS05g_ZYkdf0NC4LXhA8pMnf_RIRBkV_Ck8JaYeFc05IgtS5jgRwmOpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twhatFmn-l389oKtkCPaBijaKhZqqxubsS9og1zQMQJpk-fPkdY7pRP3YoSKDvDbLNkB_nI0BLw57D300E2TQ-osbCCVbc31sy_0PS4JfcqJZcDgjo3pS6mYd4Aj9x1JEqdjsdEcDB2FctaAGtMDdXKTvSJvtn-bX44-382J0EKFKAB3h5REW12yvZSXmEx_YHBLV60_FlNy1NKEv2u5cvGOxyLw0j1OOeysj2VqxilpYD2HN1dzp9-_EEmtT0ZyfHZlhXQLUPFHHHywfd5M5fnccmP3-ZbXWBmZ4XsJafCyI5tfvpNsa9XX_l28ptUQ6EQ1E-9ZErQ0TF06ZBBSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
برای آن آشغال‌های خائنی که حاضر نیستند درباره عملیات نظامی ما در ایران گزارش دقیق بدهند: ما عملاً مقادیر نامحدودی مهمات با کیفیت متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنچه بتوانیم در این جنگ یا هر جنگ دیگری ــ که وقوعش بسیار بعید است! ــ مصرف کنیم. علاوه بر این، ما در سطحی بی‌سابقه در حال تولید مهمات هستیم. در حال ذخیره‌سازی و آماده شدن برای هر وضعیت احتمالی هستیم که ممکن است پیش بیاید. این مهمات را برای خودمان، ایالات متحده آمریکا، نگه می‌داریم، به‌جای اینکه آن‌ها را به دیگران بفروشیم؛ اما فروش به متحدان نیز به‌زودی دوباره آغاز خواهد شد.
همچنین لطفاً همه بدانند که دولت بایدن بسیار بیشتر از میزان مهماتی که ما در ایران مصرف کرده‌ایم، مهمات را کاملاً رایگان در اختیار اوکراین قرار داد. صدها میلیارد دلار بدون دریافت هیچ هزینه‌ای به اوکراین و ناتو داده شد؛ پولی که اروپا حاضر بود بابت آن بپردازد ــ اگر فقط از آن‌ها خواسته می‌شد. اما ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
از توجه شما به این موضوع متشکرم.
رئیس‌جمهور دونالد جی. ترامپ
truthsocial.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78217" target="_blank">📅 18:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cB3JhYaLSAlQnlgqeqtwp_auQ-JF2bzsSVNxg0Cqi8yhykc4ZQgJK4vpoOOMHY2hzIK-Wvs-TVjMtgnsfI11XxYjKSww9Yg93cpMaoEggvSknlvCXAZYlRdz_5WXXJClqnUihdo6cmLac5PFQoyjjPVaDz8yYzvakqVGeEInoo5BmbYAR4Iyk3dHuk8e3GsCsd-7drpeXFvrEqUJJoQGQvHq-YABGfDnX4Q5v-8sOZi7Pw4Cw-IutZLN_ksGmWCCxetCfcETm_UsJv6C-HpP0Bux69gh_z8KyLG5O5XCxKBm5vIyZiGZLRvrFOK1PGOluVkAhZMZQKMrPOKN_1Qjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رئیس‌جمهوری اسلامی ایران، روز پنجشنبه ۱۲ شهریور هشدار داد که «ماه‌های تاریکی» در انتظار اقتصاد ایالات متحده است و از مردم آمریکا خواست اقدام به ذخیره‌سازی سوخت و بنزین کنند.
او تاکید کرد که «جنایات جدید آمریکا»، دکترین دفاعی خود را به تاکتیک‌های «نامتوازن» و «چندلایه» تغییر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78216" target="_blank">📅 17:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDayUoyUKtgynzcBAfJT0rXJbJ9nTNX1n8_Ke3u5x1QQl8Zhh_RMLLyYiKlsQOm8qibRuW1lzGoAOUCwaorVyc53n5SGlskUAXK36254iKkoVjVrZOR3Aj_2cL1Ufpce6WTQVCjBJHQ0sYX7DppJlidpcVK6ch1u6kOd4RTGjI1N03y5UOmIlGO1YIBOJZ2vp_hyga_6DtndWBeTJ6YndFMfa7H8fyqRpYutvHxdTXLSgjq0r5eGPFLrWFMcy0EFWLbp9wNXqBJXDBdV1HgaJiFtl0xtBVOjBe9URODqA45YwOEFSpIsX3TRjVJ6qgtrBZJPHHCAtz1-BXmt3OiUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">916208
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78215" target="_blank">📅 16:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBAjWnP6Udy9Zq8NrEb_SwiJY46HXX56EdhVhhQNLDr-K2ZqNsak-R1hQJnHNe3wm-u-JpT9E4ehILa1k2y-V4vfLjLyQ-cOlIc0ZR4_lB6LKh-XqDrZM-n4WBXphZLTKSRq9Mqq1qrqNKTSybeZCuM5-RCNQZoXRfv8TUfJjwuLCzEhtv8myEByxrdyZxtrE83TOMOg6ABc4Edi1dXHZH_CdVqtdGypmLplkqbPW9h32g7Tij5p1mONRJBKc3tCRzbwvkNHOG6Gfe21F6AsyC-0KIk8FZ8T4Z9hgs0jLaF9AIvBmTgwEy4sX_oDkYRQ4j4sRRafot3c7Ep_deNvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا با انتشار تصویری در شبکه اجتماعی تروث سوشال، مجموع حجم نفت و گاز مایعی که پیش از جنگ از تنگه هرمز عبور می‌کرد را با میزان کنونی آن مقایسه کرد و نوشت: «حجم نفت هرمز بازگشته است!»
ترامپ در این تصویر، مجموع حجم نفت و گاز مایع عبوری از تنگه هرمز در زمان پیش از جنگ را حدود ۲۰ میلیون بشکه در روز در نظر گرفت و میزان عبور این مایعات در حال حاضر را ۱۸ میلیون بشکه اعلام کرد.
این در حالی است که سامانه پیگیری موقعیت نفتکش‌ها در جهان، میزان عبور نفت و گاز مایع در ماه گذشته را به‌صورت میانگین ۷.۵۴ میلیون بشکه در روز اعلام کرده است.
بر اساس داده‌های این سامانه، حداکثر میزان عبوری در یک روز، ۱۰ میلیون بشکه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78214" target="_blank">📅 16:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/beDK_WHqHb5jryG3MkO_epSUdubRyVuemZAm8uTreijnUdKXRxuYsIALnBUwn7-vAw9Zl_WemUMsQXcec9LHOJ4tL6ttuUUXf_UE-Fd_aUrKfOh0tAR5Tp8hjG0zJDPR6Pod4W9h6mTa5cJxxNZ6aLdW6SVXZehnytPecuZawhZ5XfshHLWlBSOhvyBO0hZfPJ5x9iDp2D-AaaFrpOhBhmQxgBtcNIPZ0YVT-gSoDPwYDrHGJV4GwUpmaF6XP3CBsYC079ax9qNjq9-3Bqagp3QqcW4I2CZ13leQKcOojlQnYXATPhQFNNLoav3OfAjc4e2FGGUC9Yf5W6HtiH_D7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MwWZbufuL_7AA0sa_GzJbPHPQ2OtF-vp33sqGAcPGCP1orUkQ4tDBMaVxQ3kUErz-nWnb4i9TGZlDoofVaqLip7UCJg_Vt158hDU0EJTYv0dHJbP_jugrcok7Xkh466f-bS7H8j3CGjdLZ0dO96Wz9nWv6T1wwnzBw0yM0ePxqjn3hBLr_xN9GvB8wRWbNfdLkXIIydAx_oZII1-igS8GweqbSFb9CExOpZH9kUo4NfSDlUhJHH7DCAbztthgY9_WkS0bOlMM20TMXpgwEuTMq2f2evRgvzY-YCdPV76GccnmsMT6W8vPVg0wE0fF3kjja_lrDrYE8Ih37pNieFcZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=MsvH9tteSw9uFO2sm2k8VGZcN65Y49cP-y0BuGVjwo2Xb4cftLcL2uMqo0NkHNORIIMcfX9WVR5m2jtxTI9hkCKIXd5FBYJ9RuptQ9ibq9V_vgde-gH9x-dpjHKNdjiSYUTzEmauVkaGTKNTPdQj6o5dDboE0zQ7UXHlWhf8jQldjaUOTDObCLT8dB8rg7zBgwELnc_Tvgi9BiP9DYo1cuXL2touU7kaGisWtYuVcArAKNJ5BjNoe2DHwf4hewFJt61VYSVAefUmLVwDWn4jr7NRVC-4Ta0z1ePWXepYK03djXZ-_NVoqFD-tCxXcHLXXxzEwf-blvml5fkZi21eCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=MsvH9tteSw9uFO2sm2k8VGZcN65Y49cP-y0BuGVjwo2Xb4cftLcL2uMqo0NkHNORIIMcfX9WVR5m2jtxTI9hkCKIXd5FBYJ9RuptQ9ibq9V_vgde-gH9x-dpjHKNdjiSYUTzEmauVkaGTKNTPdQj6o5dDboE0zQ7UXHlWhf8jQldjaUOTDObCLT8dB8rg7zBgwELnc_Tvgi9BiP9DYo1cuXL2touU7kaGisWtYuVcArAKNJ5BjNoe2DHwf4hewFJt61VYSVAefUmLVwDWn4jr7NRVC-4Ta0z1ePWXepYK03djXZ-_NVoqFD-tCxXcHLXXxzEwf-blvml5fkZi21eCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">dadban4
:
"امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه.
شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند.
ما مادران نه می بخشیم و نه فراموش می کنیم.»
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند.
او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد."
abelbalb
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78211" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4iG8aDLpYOPaHbl7L5qXbMDO-045keRCyqVdHl6G7PWqt3UjjObvduND2dYI4J5IkbsHUQL5ogHBSWvz1wqf0Lr0PPC-8lD53dtrwy8jPnfLw1Q499FecicbOj8_TC1dDQtNBSi1e7Bk1X7IogEs7euQd5TD594REaK1fmZAYxyrOJhiOpBEd58BrP2jEykMwYk941to6SMMejyXHYSdOiD-F9WWA4s1L51YzRLXeuI6pE7UGnfUiyldKBIWaC2seYTjAZDlE4hP3JmZZ6n1n4IrLB66qfzcIOh0-E7wnIz-nWXyaaeQb_Yy2Kbsy7DgpR2xVKkKaCnfDnyDDR8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، از کشته شدن سه خلبان ارتش جمهوری اسلامی ایران در حمله سه‌شنبه شب آمریکا به ایران خبر داد.
این خبرگزاری با انتشار اسامی و تصاویر این خلبانان گفته است دو نفر از آن‌ها از خلبانان نیروی دریایی و یکی از آن‌ها از خلبانان نیروی هوایی ارتش بودند، اما اعلام نکرد در کجا و چگونه کشته شدند.
با این حال، اسامی اعلام‌شده سه نفر از هفت نفری هستند که روز چهارشنبه ۱۱ شهریور اعلام شد در حملات آمریکا به شهرهای اهواز و آغاجاری کشته شدند.
در جریان حملات شامگاه سه‌شنبه آمریکا، به‌‌گفتهٔ مقام‌های ایران، مناطقی از جمله فرودگاه جیرفت در جنوب استان کرمان، عسلویه، کرمانشاه، مناطقی در استان خوزستان، شهرهای چابهار و کنارک در استان سیستان و بلوچستان، سیریک، لاوان، قشم و بندرعباس در استان هرمزگان هدف قرار گرفتند.
سخنگوی وزارت بهداشت صبح پنجشنبه از کشته شدن «۱۸ نفر و مجروح شدن ۱۴۲ نفر» در جریان حملات اخیر آمریکا خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78210" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOwluHyukEjMYVN1leczX4uUJZ27rgwFjQxgMO2E8TzQZKuBFTr5WOy7iGa7lvFR1mYzRu61iWH2bUtn_QPxoMRYMTqAfZQwjF3KoKJm2zup0ZSHuUmI937T1L8N1xkKTyOO2IaSqsWrtwS0pQesG2IDDqApgqlEiAVsd98SRahozke0WXfZctOAtwhZn2adAu6nQOMP5bDP9_iDd1hWnvtC0vtKI7OmlTJWnA-R_bCAHEeZL58Zk2pJO8Kx7tjOcLDCM8rijr3uVBta-JA_zT_5JA5jR-aC6osUocMsw-hWyMyRuLPRmEQenGHlxfssZ754yoj-kDsc57v-G9UEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78208" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oy7rYdvRLf1clrOYUVHrntRDwu0gxFskWH3Jkk8qxhBkrEBnTD88S5vEuALv0JHrSfN0iy7nczIGA5eyW4JwsY6YdmAoGU-sOTL4NFYxJxuKc4sZeSX9tB8Jri1W4WvH1VusKLwW04c8C6Gwll8K4KoXwwvWW9t8rEN8D4aUZAWiSOmodPwOru6_TGS4li7cpLfrfwyTY05B_DDS4Tx_wfR6ldFNJTcIDvRZ0VNYrnx0qqSfNeQ-2HeMSSprHVMc52usUqZus_4mnpM2z7l2Hb-9rw9xsqYx-7PnyOnhQpjzoWx7TUunkZ1Md1WGxEsaodkXbpk6hQ2aWGbzLnOZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، پنج‌شنبه ۱۲ شهریور در مراسم روش هشانا با کارکنان وزارت دفاع اعلام کرد حمله جمهوری اسلامی به این کشور، اسرائیل را از همه محدودیت‌ها رها خواهد کرد و این کشور حتی زیرساخت‌های انرژی را نیز هدف قرار خواهد داد.
وزیر دفاع اسرائیل گفت: تمام زیرساخت‌های ملی، نظامی و غیرنظامی، از جمله زیرساخت‌های انرژی را هدف قرار خواهیم داد و ایران را به اعماق عصر حجر و تاریکی بازخواهیم گرداند.
کاتز همچنین افزود: فشار اقتصادی و نگرانی از قیام و سقوط حکومت ممکن است جمهوری اسلامی را به اقدامات از سر استیصال سوق دهد.
او گفت: حکومت آیت‌الله‌ها در ایران به‌خوبی می‌داند چرا پس از آنکه دو بار ضربات سختی به آنها وارد کردیم، برنامه هسته‌ای را نابود کردیم، خامنه‌ای را کشتیم و به توانایی‌های راهبردی آنها آسیب شدیدی زدیم، به اسرائیل حمله نمی‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78207" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhmmOdbGT4fq9T_6QwkE5dn_iLz5piRJK7J02W8GKAR6AHGycvEJ07PYg153oW0c4ULQZMbj9pwCaJl3buoFUhbXSlsdzO5NLpmHamJQwc_GW4_clmwNIirf4QfpTspo3i35WEYXoaqiBvTcrkhkL_Zivsr_VT7xTT-atiYOdabrmrvLY2bYmFBPidCDn6l0bgOYOFYRewu9_vNuk74XnkS2n2Zi97I-NhX7y3-ev200Cpi-tLBYWpEjqSpdwoB0F3GlkNGskCjUlhaNguMhF3nhk9p1areG93SFDg8xL9l1LFDUWmfRbeymboebqpDrr2JqgWCnXB4ewSOfXjsz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خودروسازی سایپا، روز پنجشنبه ۱۲ شهریور ماه و چند روز پس از آغاز ثبت‌نام طرح فروش فوق‌العاده، با صدور اصلاحیه‌ای رسمی، بهای مصوب چهار محصول عرضه‌شده را به بهانه «افزایش هزینه گواهی اسقاط خودروهای فرسوده و سایر عوارض قانونی شماره‌گذاری» به‌طور چشمگیری بالا برد.
بر اساس جدول جدید منتشرشده، بهای مصرف‌کننده «کوییک اس» و «سهند اس دوگانه‌سوز» هر کدام ۳۳ میلیون تومان گران‌تر شده و به ترتیب به یک میلیارد و ۳۲ میلیون و ۵۱۰ هزار تومان و یک میلیارد و ۱۲۳ میلیون و ۶۸۸ هزار تومان رسیده است.
در بخش خودروهای مونتاژی و وارداتی نیز قیمت «سیتروئن سی۳-ایکس‌آر نسخه وی‌یک» با افزایش ۱۱۵ میلیون و ۵۰۰ هزار تومانی به ۳ میلیارد و ۳۸۹ میلیون و ۳۲۲ هزار تومان و قیمت «چانگان سی‌اس ۵۵ پلاس» با جهش ۱۹۸ میلیون تومانی به ۵ میلیارد و ۸۱۹ میلیون و ۱۲ هزار تومان افزایش یافته است.
این در حالی است که متقاضیان در روزهای گذشته بر مبنای نرخ‌های اولیه اقدام به ثبت درخواست کرده بودند و حالا این محصولات با موعد تحویل ۹۰ تا ۱۲۰ روزه با نرخ‌های جدید تحویل داده خواهند شد.
روز چهارشنبه ۱۱ شهریور، بازار آزاد نیز با موج تازه‌ای از گرانی همراه شد و چند خودروی داخلی دیگر جهش قیمت داشتند.
به‌طوری‌که تارا اتوماتیک با رکوردشکنی و رشد حدود ۱۰۰ میلیون تومانی به محدوده ۳ میلیارد و ۷۵ میلیون تومان رسید. بر اساس گزارش فرارو، در همین روز دنا پلاس اتوماتیک با افزایش ۲۵ میلیونی به ۳ میلیارد و ۱۹۰ میلیون تومان و پژو ۲۰۷ اتوماتیک پانوراما به ۲ میلیارد و ۹۸۰ میلیون تومان رسید و محصولاتی نظیر شاهین اتوماتیک پلاس و سورن پلاس دوگانه‌سوز نیز به‌ترتیب در سطوح قیمتی ۳ میلیارد و ۳۰ میلیون و ۲ میلیارد و ۴۱۰ میلیون تومان معامله شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78206" target="_blank">📅 14:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i8EXxC5XdT5uj54hfiUBKx8zrrLuEY2MBaeSPOZHIMe0ofoU0jfl5HaF28pCqkTcravt_9Bd54oa8Gy7OZC6fCaqR968bG3_BWrUyz4hjpWfQeJEORH_-FJ8kpUr_hYEJ7tE0SJ7DftxEzSYGJgjnWZtVdhGQGucq2fazxJwrKeTM_uvDZYF1HQ-KktAieCBolV92CCEOvmaG7lcpdIBriPpja4syhxdGeV6fwS96-Qkyw83onuauSGnnv-OfpqjMSZaHIFUw-8QkVId_BBIVRBa2YhOPGi8Y5M2sgIHhzFr5blDutFEzXKbMXgEUYjqBdT3RneL_uGrRSphVUGavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین شریعتمداری، مدیرمسئول روزنامه کیهان، پنج‌شنبه ۱۲ شهریور در یادداشتی نوشت که ارتش و سپاه باید از «اهرم» عبور کابل‌های فیبر نوری بین‌المللی در خلیج فارس و تنگه هرمز برای «مقابله با آمریکا و متحدانش» استفاده کنند.
مدیرمسئول روزنامه کیهان نوشت: «در عمق آب‌های خلیج فارس و تنگه هرمز یکی از شاهراه‌های فیبر نوری بین‌المللی جای گرفته است. شاهراهی که بیشترین ارتباطات اینترنت، تماس‌های بین‌المللی، تراکنش‌های بانکی، سرویس‌های ابری (iCloud) و حتی ارتباطات هوش مصنوعی و دیتاسنترها از همین کابل‌ها عبور می‌کنند.»
حسین شریعتمداری، نماینده خامنه‌ای در روزنامه کیهان، تاکید کرد: «سخن با مسئولان کشور و مخصوصا با ارتش و سپاه است؛ خوب نگاه کنید! کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78203" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NP8zONZXMvludZukkapUJK2VqWXSD4qtJxTL2tvphLOpzZxSpQB2vexw7DQfVyEjaNsGimZZ82Q9cvtF8SsA8Hey6TeXMDQZr7J1vhcQDQzHqs7TUakK5GabMOLJsLHxmLTURW3EKXQ7IXmpBAXV9sWGlspkjcOIXCk1ei2yuFwhGCCng5TJsq8hqXRM02F7KO6yJ36PUU-uBOG9MOM9mcf9obajsFVbqMmvErdpXlPSvaFdtZRihFAaER1uMElZs37uj6UJ-OH35hZSFL0-7K1EaAXPOG2b2IDUl-8QUesytwacHatYkvBe1dplmDTu_3ZjqRTkMwY0JjKTf1OCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه افزایش نرخ ارز در ایران، قیمت پوند بریتانیا پنج‌شنبه ۱۲ شهریور در بازار آزاد برای نخستین بار از مرز ۳۰۰ هزار تومان عبور کرد و تا زمان تنظیم این گزارش به ۳۰۰ هزار و ۲۸۰ تومان رسید.
در همین حال، دلار در بازار آزاد با قیمت بیش از ۲۲۲ هزار تومان معامله شد و قیمت یورو نیز از ۲۵۸ هزار تومان عبور کرد.
قیمت سکه امامی نیز از ۲۳۵ میلیون تومان عبور کرد و نیم‌سکه به ۱۲۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78202" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTXC46wSXiP-B7aN7-cCQQdniQTiA5YBbDxXHYsgG2W8RgqoNcFvRP4NWFX-Uoycfceq8UoSjbkw0SZgAjdsFi3NhNqGcEPEFaL1093Z-0MVaj-LG1tyfQMGHgiO2hchvDhr35hQaebIYrE44aNElP_QlsUH6jRlRniMz82bx0NSCoDugL9SoeHK-syZTcAxe0c7U9g1CGAakfGztacSU8xSsDJCCgb2shSHqOIMPj9oaC-nDs4aNTgg82zzR6s-2CJeUAI3FpR6ohaL3OxpP2jCz_ZBfWFXfDAdWVgeFRH1_vQeOg9s6KJeChGAETg4kY7zDTSM3A-uePwwvh4Uzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور حکم ۱۲ سال و شش ماه و یک روز حبس، مصادره تمامی اموال و دو سال محرومیت از کافه‌داری برای صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای «ساعدی‌نیا»، را تایید کرده است.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ اعلام کرد این حکم به‌دلیل حمایت ساعدی‌نیا از اعتراضات دی‌ماه ۱۴۰۴ و تعطیل‌کردن واحدهای صنفی زیر مجموعه این برند صادر شده است.
براساس اعلام قوه قضاییه، صادق ساعدی‌نیا به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به ۱۲ سال و شش ماه و یک روز حبس تعزیری و مصادره تمامی اموال منقول و غیرمنقول خود به نفع دولت محکوم شده است.
دادگاه همچنین او را پس از پایان دوران حبس، به دو سال محرومیت از فعالیت در حرفه کافه‌داری محکوم کرده است.
قوه قضاییه انتشار مطالب اعتراضی در اینستاگرام، حمایت از فراخوان‌ها، تعطیل‌کردن کافه‌ها و فروشگاه‌های مجموعه و تشویق کارکنان به شرکت در اعتراضات را از مصادیق اتهامات او اعلام کرده است.
براساس کیفرخواست، صادق ساعدی‌نیا با سه عنوان اتهامی شامل «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های مخالف جمهوری اسلامی» و «فعالیت تبلیغی علیه نظام» محاکمه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78201" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7CK3qqZmqcJpdTZNci1qupw5MOmTyB4b6OhaRRZRJZW_f7QoNBKwUIDVSQJMXomNNIaKIAOTP0WnFStRIVjrFvY_qjask1wnp389LHsJD4M36qwExMOsRzJrHOTFiONPgHOwQUa3c4HTfol6bE18OiyiltWR5YnDF6tDWbvKqmw3x0RmjdyYcN3dhy1E72Y1l4NyRdeh044Z7V6nky6MWW08qug44PUumZBiS3kKWVTZSkRYaCbof7jjseOwmbqsDkDIj6HHUlREj47xOHkpcP2Gu_QTU8Al0t4ECBkLzKHBqhBT6DSMv3gfIBOlXolqqsmRXF3Q7sZ2KnqJWF0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pv32dvt--9zIsq-ZbE4DsNNoQjYcTHp6mzEFHIYooIUhDFgq1Sg2LtZGyIdFqhe0eYiZ21-xgmvniwCGL8t1PlzXtBhKFXzFhKTnirTFu86ILjC7TICSQE0Wh1DK78HVD-1bu8PM8TCsjG6PiTXoVi_AOi3iH0YZXaEiUvlQb2y96jaLZXD5dyhK3CxLspSuBKlUe8Cs8jZNivFWofpCXMmi55kHqri3szusglcPvCX3PdI94ZDd72rVy05I128tFZ2zsY3s2eZhyl4FqxX2cfiFTmIgZZ0EKRa3MbyaUJcqWGJpiVmK5eMjXi8WAlueFjmB9aYvRBwuTO9fjazobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=qcNvnYSRJiufouigmfHg3WcwJByvZLQA-E_YCKxUt80TYZKYwxkvyYfYFKDf6H59fJmcjxG_KXoEvXDs5hXlDN_XxlYawFPt1ZzkE5cOvrMt_dr4YM5Mx-PpeQ-kUxWOS8BewksEd7fvcUKcjVZzbmCLdACo6K3NjlbYVBddmrutyYN4wtwI36YzimkCXqi3ok3hMofSne7yKgy2t4dsCODVKBf8Y1xdq3SAOq98s9WeJfmBlNnfPrvpKNwxyalscGBNEXrH7pLlTvLbYwYotFIsX1_Ag5aK76N5gu0O38Fu-pExjC4x_6LeBuGieloZpIAg2W6mgSw8AP4WFqoUxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=qcNvnYSRJiufouigmfHg3WcwJByvZLQA-E_YCKxUt80TYZKYwxkvyYfYFKDf6H59fJmcjxG_KXoEvXDs5hXlDN_XxlYawFPt1ZzkE5cOvrMt_dr4YM5Mx-PpeQ-kUxWOS8BewksEd7fvcUKcjVZzbmCLdACo6K3NjlbYVBddmrutyYN4wtwI36YzimkCXqi3ok3hMofSne7yKgy2t4dsCODVKBf8Y1xdq3SAOq98s9WeJfmBlNnfPrvpKNwxyalscGBNEXrH7pLlTvLbYwYotFIsX1_Ag5aK76N5gu0O38Fu-pExjC4x_6LeBuGieloZpIAg2W6mgSw8AP4WFqoUxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفت.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
آپدیت:
حال‌وش روز چهارشنبه ۱۱ شهریور ۱۴۰۵، به نقل از شماری از شاهدان محلی خبر داد که پیش از انفجار، صدای دو پهپاد در منطقه شنیده شده است.
این رسانه، علی ملاحی، صاحب خانه و پدر عروس، را یکی از شاهدان معرفی کرده است. او گفته پیش از وقوع انفجار صدای دو پهپاد را شنیده و پس از آن، ساختمان هدف قرار گرفته است.
شماری دیگر از ساکنان کوهستک نیز از مشاهده یک پهپاد یا شنیدن صدای آن خبر داده‌اند.
منابع محلی همچنین می‌گویند خسارت‌های واردشده به خانه تنها ناشی از ترکش انفجار در یک محل دیگر نبوده و یک یا چند پرتابه مستقیما به ساختمان اصابت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=FvZ6PCx5-JFXN5BXLIdZEXutQZ6P4jtLlzFsS-lNVOR9I1TyuNPMp-g-e_ywSYiBFFLN0duCihNygumCOujq8ZpasFyYJhI0T2RLIysKcZysX2MsYtldA_cbfLmnQeG60fC3VDyW976vLmCVjFKdEg7ZGpC4QjJ-KLyhwgfzJVWUes7jvFfjBRe55NwuIsH-mYD9L7xoUuz8LkRBq-kX3ve0suU1_vibWTIT27A_wwuzTjPc4XFbDV8YnSDewqhIYjB1OrR1hnQtLpU3eL2uieGWeJyeoR-UxeDlA0Q-A0SHmB5U0Vmq7Nvbs_OPrZ5axvlFJ_-J2ZYHjydEMjzI5a6mt40uKcsm9SrI04CtyqN1HkK1T1iRoFarBU7AEAg3KXLyfxQnWkQ3wX90qOHl_nGtuOc-qcyzkUf5z1BuYvVbBJWXzCYn21pMtzv4iUS3N4zdrxS_OlTKDXL7GlstVCf1pvHwy4h34bEzJ9oDOJJ4I79WadxxmaOoclRgnV0Mc4KvgGSXWg0L-ky8ITXJirNxrB9adXz6GbxGLPLhSjP8CIJre589KeSULuewQCxgxac1tqlutjBirhkM5DPoo4OyzejZ5Tl_uK6qGqG50gu8MjWAKy-bf6itcmh7Sak1dWtPa8zlGHjWM_LLF4sDjWQcK-ytnur8TTnYNVq_ts8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=FvZ6PCx5-JFXN5BXLIdZEXutQZ6P4jtLlzFsS-lNVOR9I1TyuNPMp-g-e_ywSYiBFFLN0duCihNygumCOujq8ZpasFyYJhI0T2RLIysKcZysX2MsYtldA_cbfLmnQeG60fC3VDyW976vLmCVjFKdEg7ZGpC4QjJ-KLyhwgfzJVWUes7jvFfjBRe55NwuIsH-mYD9L7xoUuz8LkRBq-kX3ve0suU1_vibWTIT27A_wwuzTjPc4XFbDV8YnSDewqhIYjB1OrR1hnQtLpU3eL2uieGWeJyeoR-UxeDlA0Q-A0SHmB5U0Vmq7Nvbs_OPrZ5axvlFJ_-J2ZYHjydEMjzI5a6mt40uKcsm9SrI04CtyqN1HkK1T1iRoFarBU7AEAg3KXLyfxQnWkQ3wX90qOHl_nGtuOc-qcyzkUf5z1BuYvVbBJWXzCYn21pMtzv4iUS3N4zdrxS_OlTKDXL7GlstVCf1pvHwy4h34bEzJ9oDOJJ4I79WadxxmaOoclRgnV0Mc4KvgGSXWg0L-ky8ITXJirNxrB9adXz6GbxGLPLhSjP8CIJre589KeSULuewQCxgxac1tqlutjBirhkM5DPoo4OyzejZ5Tl_uK6qGqG50gu8MjWAKy-bf6itcmh7Sak1dWtPa8zlGHjWM_LLF4sDjWQcK-ytnur8TTnYNVq_ts8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=llSyiLST5LjN3LTytLGqdIdS4L4VLL_XFqY9j6Y6m0PpJLZQsp15XAllicqn9s0wdoIvYuQ3Wsw7c6KTIWveY3-2YNy74UjkA9o10KlRbSBd0XwkR-cx8IDMdlhNVbiJ2xaTAJRh5Mb_tvB44OCG6juZs5rNegurY5jIH-e4tjbZsIEEtCScFU4ay5DytXeuKM5F7YYUlAPaSFKOg1w29TWzaGlKF674tLHiSMycMcJipZad97PC3sP0PghFSGEkkSI3hZ0ibtxRCiY7VVxWYvpVgMTxY9TPjtEokZXiymDrK8__CoV1hZGzM2vKzNp7Bc7ye-lSPl5j_q_wMdR2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=llSyiLST5LjN3LTytLGqdIdS4L4VLL_XFqY9j6Y6m0PpJLZQsp15XAllicqn9s0wdoIvYuQ3Wsw7c6KTIWveY3-2YNy74UjkA9o10KlRbSBd0XwkR-cx8IDMdlhNVbiJ2xaTAJRh5Mb_tvB44OCG6juZs5rNegurY5jIH-e4tjbZsIEEtCScFU4ay5DytXeuKM5F7YYUlAPaSFKOg1w29TWzaGlKF674tLHiSMycMcJipZad97PC3sP0PghFSGEkkSI3hZ0ibtxRCiY7VVxWYvpVgMTxY9TPjtEokZXiymDrK8__CoV1hZGzM2vKzNp7Bc7ye-lSPl5j_q_wMdR2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، و دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، روز چهارشنبه توافقی نفتی را در کاراکاس امضا کردند که بر اساس آن ایالات متحده کنترل اکثریتی بر ۶۵ میلیارد بشکه از ذخایر نفت ونزوئلا به دست می‌آورد.
این میزان حدود یک‌پنجم ذخایر عظیم نفتی ونزوئلا را شامل می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، این توافق را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده است.
بر اساس این توافق، آمریکا به ۱۷ میدان نفتی ونزوئلا دسترسی ترجیحی خواهد داشت؛ تأسیساتی که برخی از آنها پیشتر در اختیار شرکت‌های روسی و چینی بوده‌اند.
همزمان، شرکت شورون نیز از توافق جداگانه‌ای به ارزش هفت میلیارد دلار برای توسعه دو میدان نفتی دیگر در کمربند اورینوکو خبر داده است. شورون می‌گوید این سرمایه‌گذاری می‌تواند تولیدش در ونزوئلا را طی پنج سال بیش از دو برابر کند.
وزیر انرژی آمریکا پیش‌بینی کرده است تولید نفت ونزوئلا تا پایان دهه جاری به بیش از دو میلیون بشکه در روز برسد؛ حدود دو برابر سطح تولید در ژانویه، زمانی که نیروهای آمریکایی نیکلاس مادورو را سرنگون کردند و دلسی رودریگز قدرت را در دست گرفت.
این توافق با انتقادهایی نیز روبه‌رو شده و منتقدان دولت رودریگز را به واگذاری حاکمیت ونزوئلا بر منابع نفتی خود متهم کرده‌اند. دولت ونزوئلا در مقابل می‌گوید این توافق به این کشور برای بهره‌برداری از ظرفیت‌های انرژی و جذب سرمایه‌گذاری کمک خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78195" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nL1WyFgyix8kKs6KsmDP2KqxTgQd3Qg7aJOKUZ6Rux7zpXZxFsvY4kDL5xtvfwJNNbx7L0iZXLDQ1yoh9EYeNTzts3hyOi8GNWq-BJpqkiX9zeypAHrpJroQnMNcIydWNAA9_cBhMS297x77aHtp0vLVbUlO3lC_zq_Vf9wY_U4-YgWmPVVqhgF0c1J70owssndAymqRM5uRQGJwgE5UBQbjYY-pttiVvWWZw0q6Xz_AZoROOiZArEU4FDR1MX08APTvVE4U5QCgkCe_VHbVQWwXSsElQxv9NEmG3vF6QnI71DNHRc4uwm8pc2GYpKnzhAH6n_OupevFFIOunaEhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=taX4ofoEw55HmcjdJv59K2eFO04NyRBj1b0mBPoCLwlqEXFfTvWrn7OpL2rt-Ei6CFLFV_t3hSYPZkaRMHJc0H2I9KViY8WFqLUxA650xS7Jj0C6DnbZoXOtUe9NYv4W2J7WS_49Zp42-0cbnhlsMgwVClv1CdJbzWc8ahVdjGEI_OTa4ozDuzepBFXbQQwkT2cmug_Gwezc5DQ-ACsCHt1aZZg6xJgr_-i8-jqU8cc9wQpDJp1OoQKMDQmQKUniSJtM2RyxNEeVQx1eO45pO_LeneP7qvVKHjwjWkkpGFCSNgfTO1jDkadyPE465FnhAr-zbMmsAj5m4hoUXx2hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=taX4ofoEw55HmcjdJv59K2eFO04NyRBj1b0mBPoCLwlqEXFfTvWrn7OpL2rt-Ei6CFLFV_t3hSYPZkaRMHJc0H2I9KViY8WFqLUxA650xS7Jj0C6DnbZoXOtUe9NYv4W2J7WS_49Zp42-0cbnhlsMgwVClv1CdJbzWc8ahVdjGEI_OTa4ozDuzepBFXbQQwkT2cmug_Gwezc5DQ-ACsCHt1aZZg6xJgr_-i8-jqU8cc9wQpDJp1OoQKMDQmQKUniSJtM2RyxNEeVQx1eO45pO_LeneP7qvVKHjwjWkkpGFCSNgfTO1jDkadyPE465FnhAr-zbMmsAj5m4hoUXx2hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با شبکه نیوزمکس گفت که ایالات متحده لزوما به دنبال فروپاشی جمهوری اسلامی ایران نیست، هرچند تحولات درونی و قیام مردم امکان‌پذیر است.
او همچنین به مخاطرات شخصی پیش‌روی رهبران و فرماندهان نظامی ایران با افزایش فشارها اشاره کرد.
بسنت ادعاهای ایران درباره کنترل بر تنگه هرمز را رد کرد و گفت با عبور حدود ۱۷ میلیون بشکه نفت در روز گذشته، کنترل ایران بر این تنگه بی‌معناست. او همچنین گزارش‌ها درباره وجود مین یا برخورد دو کشتی با مین در تنگه هرمز را تکذیب کرد و رسانه‌ها را به بازنشر سریع ادعاهای نادرست ایران متهم ساخت.
وزیر خزانه‌داری آمریکا، با اشاره به تداوم خرید نفت ایران توسط چین تاکید کرد که تنها حدود ۳۰ میلیون بشکه نفت ایران روی آب باقی مانده و این ذخایر نیز به‌زودی به پایان خواهد رسید.
بسنت روز گذشته نیز در جریان سخنرانی در مجمع اقتصادی جی۲۰، تاکید کرده بود که فشارهای اقتصادی یا به ایجاد شکاف و دودستگی در سپاه پاسداران و احتمالا مقابله مردم با آن‌ها منجر می‌شود یا مقام‌های تهران تصمیم می‌گیرند که به میز مذاکره بازگردند.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با شبکه آی‌۲۴ درباره حکومت ایران گفت: «نیروهای ما می‌توانند هر لحظه در آنجا باشند. ما این حکومت را شکست خواهیم داد.»
نتانیاهو درباره اینکه آیا منظور او از شکست دادن، سقوط کردن حکومت است، گفت: «بله، سقوط خواهد کرد و ما آن را سرنگون می‌کنیم.»
نتانیاهو در پاسخ به این سوال که آیا رومان گوفمن، رییس موساد، برای سرنگونی جمهوری اسلامی فعالیت می‌کند، گفت: «همه دستگاه‌های ما تحت هدایت من برای سرنگونی این حکومت و شکست آن فعالیت می‌کنند.»
نتانیاهو گفت: «در نهایت با سر اختاپوس، برخورد خواهیم کرد، بازوها را قطع خواهیم کرد و محور شر ایران را هدف قرار خواهیم داد. این کار را با قدرت بسیار انجام دادیم؛ خلبانان ما آنجا بودند و هر لحظه می‌توانند آن جا باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78193" target="_blank">📅 21:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueEaSNNsHxEicFwaepEXlYwwHLGr0Q2CgYTqTnHHzUVN1_YPm9QwNNkzy6GskuCn5G9uEERvUl9Gz8njYJPJ961hVmwq-cwH4Katw3GTj1EuYL7FoVtWDJnzZC15D_m-6_H8ZUVZq9MsDWCO-UJZ0AOog9GoNoATMqJLbqf7qDNW3p79c2InT_88yZjZmfVBV_yP6KJAfm-F2xDG0lcQP4WSPo0PtENyUqZq_Bt5PQaAeCYgUJXGt3BMK6mJ_7OSyyb3An_mXv-aF5z_0kJDWUi2TkYOmtaX03ZNd8hgKDymTVkvp5gHFl9IKLnQsgKIt-v1P9uMecGH-YM4T9lH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی جمهوری اسلامی، با هشدار به ایالات متحده گفت تهران در جنگ جاری از «راهبردی جدید» استفاده خواهد کرد.
رضایی، چهارشنبه ۱۱ شهریور ۱۴۰۵، در پستی در ایکس نوشت که تلاش‌های آمریکا برای خروج از شرایط کنونی نتیجه‌ای نخواهد داشت و افزود: «به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، پایه‌های شما را درهم خواهد شکست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78192" target="_blank">📅 19:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bsNq0X_qDcPohYg6yvT0h2FbR3QsfU7gusEUPNcaIu9iBtx6zeLD00Q3XXERq3U9pA7uDQFg1lWnlKcTU_9J_CxTYPcChsbsMBAPKsjy-U0tN73Y0D7wiq6fZut5C-eH_Xdvov68DgfCmfAkFbKDvQmXRe4qIQuXJwgvTIu5VyiWst-5y1F-jPtybpI0J7UXaPISa6JHFVu_nPRce8EpCN1ozp90HaaGSSQeLQ8NfW-J_O1y8GIrZ2xIYp7ouE9Q7FYs1-hvRaK0VAIZ_-vhrbYksf1JXNX2E1CYE_IiAEmijJAPAlI4jX5HuSWQEoKfQBOMWRN7Q51BWfxa4PA30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حالا که آن را تحت کنترل ایالات متحده آمریکا درآورده‌ایم، آیا باید نام «تنگه هرمز» را به «تنگه ترامپ» تغییر دهیم؟؟؟ درست مثل خود آمریکا، این تنگه هم «داغ‌تر» از هر زمان دیگری خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
Now that we have it under U.S.A. control, should we change the name Hormuz Strait to TRUMP STRAIT??? Like America itself, it would be “hotter” than ever before! Thank you for your attention to this matter. President DONALD J. TRUMP
realDonaldTrump
در خبری دیگر:
ترامپ در گفت‌وگو با پادکست «دن پاتریک»، درباره حملات سه‌شنبه شب آمریکا در اطراف تنگه هرمز، گفت: «ما اکنون کنترل تنگه هرمز را در اختیار داریم. ما آن را کنترل می‌کنیم. دیشب ۲۸ کشتی را از بین بردیم. ما آن را کنترل می‌کنیم، آنها چیزی دریافت نمی‌کنند و ما کشتی‌ها را از بین بردیم.»
ترامپ همچنین درباره حکومت ایران گفت که جمهوری اسلامی دو هفته با داشتن یک سلاح هسته‌ای فاصله داشت. او افزود: «اگر آنها سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت، خاورمیانه از بین می‌رفت و آنها به شهرهای ایالات متحده حمله می‌کردند. چون آنها دیوانه هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78191" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oX78YgTFIX9ksQgzLngqjsX6N-hYv0rq6ZoppfJ1SElI71pHHYkT_qfu-virUi10zea8XnMEAgiSGuQpJMLRZtaAIbDHoMHrW3sHjVY20vMi1ZZuijDKXaPfDj2ojRsB2eU_1YnB3BT1sJKuc3KsAxwHo6gkDGNxDDranvl0T8TVQfpCsMBCKF8B7lnapt87BzDZx6kmXpq51i-KLVV5rs77NUfg-cmIf85kbIAc8kpApH4FRSE6rdR01m3HD0A4w2TDab9QV23HK79331hXH1GAK3sSynzgHowfIx464rmloLPL7FBLttgBI3Ar2UCGcGbBYxx1fkQmiXsFvE7Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی گفت: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
محمدباقر قالیباف، در دیدار با مسئول ارتباطات اسلامی حماس گفت جمهوری اسلامی مذاکره را رد نمی‌کند، اما آن را «ابزاری برای مبارزه» می‌داند.
او گفت کنار گذاشتن مبارزه با آمریکا و اسرائیل به معنای شکست است.
او افزود جمهوری اسلامی در جریان مذاکرات، پایان جنگ علیه ایران و متحدانش در «جبهه مقاومت» را در ماده نخست تفاهم‌نامه مطرح کرد، در حالی که به گفته او، طرف مقابل در متن اولیه ۱۵ ماده‌ای خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و فعالیت‌های «جبهه مقاومت» شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78190" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KI2bHJHGgkMiCY3yuaCBUTNw4sH2RB0no7SVa7_gdRLu2DX-Q612CTVr1PQ1wu1cvGCZAR1g60PoqCHeema-ifVYlFxseSPJN1Pcw7LarLJlJip2gFDoFApiBPV_VRtIubn1-orFicVlRjufZLjc_-QCLURg9crqhvP8x9drYaB-d8X77JLt9SNDr5NJj6qKuSxMzysYyfkXU2_WPEZju6kPjInWLffRHAJxNB3RY0MQ4BMi1Nrrr3afUIeNNgn-HBIjPPAAuHuuYwhcY1vwrx9m34pMXOgjpoFdxIzfKWtiZCL7ywLLgsxdVErGeLSP-xL5QWiorw3CA1iflenbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آمارهای اعلام شده از سوی شرکت ملی پخش فرآورده‌های نفتی ایران، میانگین مصرف روزانۀ بنزین در نخستین هفتۀ شهریورماه از مرز ۱۴۸ میلیون لیتر گذشته است.
بر اساس این آمارها، بیشترین میزان تقاضای روزانه در ۸ روز نخست آخرین‌ماه تابستان، بیش از ۱۵۴ میلیون لیتر بوده و در این بازه در مجموع بیش از یک میلیارد و ۲۰۰ میلیون لیتر بنزین عرضه شده است.
کاهش شدید ظرفیت تولید در ماه‌های اخیر در اثر حملات آمریکا به تأسیسات نفتی ایران از یک‌سو و مشکلات دولت برای وارد کردن بنزین از سایر کشورها از سوی دیگر، باعث افزایش قیمت بنزین و حتی مطرح شدن احتمال بالاتر رفتن قیمت این فراورده و افزایش شدید تقاضا برای آن شده است.
مسعود پزشکیان رئیس‌جمهور و شماری دیگر از مقام‌ها تأکید کرده‌اند که دولت توان چندانی برای وارد کردن بنزین و بخصوص عرضۀ آن با قیمت‌های قبلی ندارد.
دولت ایران اما در عین حال ادعا می‌کند که تشکیل صف در برخی جایگاه‌های عرضۀ بنزین، ناشی از هیجان و بار روانی بوده و مشکلی در تأمین بنزین مورد نیاز کشور وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78189" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l016Vk-wwEJ1O65ljWUQZW5bZYTgLiuL0h6NhJJA4wAi6U-0ccUs4KHC55Y39BPvkX25pPhuXW4zXu4g8ZfH4MOL1-f7yZevYNn9dURtxfIn8Gru1FQhK6utAfBAQ2iVkeVuQgfAvL32q9KsKcdl2UylceVVC-ZbRn5pAfrHBYoCqKyNBdBB8UsKv_KM4uWGz5D2KJUdU6BJQrv_zCY4pK0BLo6prIcz7wrTrn8NGoe-r6NlmVXro2xnzEYCkMeho3LPbVNTufpkoqZ9C1zp_no5swQBqPXYzN2nVASZCdJ9BCtxMTTmk0UWldQKug04ik5QyyMFUWLKcez68OjMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در ایران بامداد چهارشنبه ۱۱ شهریور و ساعاتی پس از دور جدید حملات آمریکا، رکورد تازه‌ای ثبت کرد و قیمت یورو، پول واحد اروپایی، برای نخستین بار از مرز ۲۵۵ هزار تومان گذشت.
وب‌سایت‌های اعلام نرخ ارز قیمت دلار از جمله «نوسان»، قیمت دلار آمریکا را حدود ۲۲۰ هزار تومان گزارش کردند. قیمت درهم امارات هم به بیش از ۶۰ هزار تومان رسیده است.
افزایش قیمت نرخ ارزهای خارجی در بازار آزاد ایران از زمان اعلام امارات در قطع روابط مالی با ایران و آغاز برنامهٔ فشار اقتصادی آمریکا موسوم به «عملیات طرد اقتصادی» شدت گرفته است.
در دو هفته اخیر پول ملی ایران در مقابل ارزهای عمده خارجی بیش از ۱۰ درصد دیگر از ارزش خود را از دست داده است.
روز چهارشنبه قیمت سکه طلای موسوم به «امامی» هم با وجود کاهش جهانی قیمت طلا، ۲۲۴ میلیون تومان گزارش شد.
عبدالناصر همتی، رئیس‌کل بانک مرکزی، روز ۱۰ شهریور ادعای کمبود منابع ارزی و احتمال فروپاشی اقتصاد ایران را رد کرد و گفت بانک مرکزی آماده است برای مهار بازار تا دو میلیارد دلار ارز عرضه کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78188" target="_blank">📅 16:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XoUf2NYgR9cWPL3hVJ-a3er1cMEKXlO1hbWxgJmdbCyYKL4MwG8gneD1d24-XvZ0JSuKdpdojh9u0Mns7Be3Zvptc1Z_pOTkqwncd0pFf_RWK4hkB7JLksWrb-cPqISNMUj_4Bq_pYph9GOs-CDbkOlqnboSDP9DDCVKGh-JNZD6ayoOLdwL0zBfYJ2XFDmy1fzuy_pdvqoeFQdFPZO9KWA8_v6-7khmW1fUTs8lgYfJUHpfnBQ-JO5DUo2mjIvQbXQ0MCWyyntBddW9CNeJskLa9zwqEaRnwEwy376PxvcqmRBGqVyMcnyKQJP6r1aQys_BhF8IAC9h30pvgob-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد که ارتش ایالات متحده در جریان موج حملات شامگاه سه‌شنبه دهم شهریور به اهدافی در جنوب ایران، «دو نفتکش دولتی» این کشور را نیز هدف قرار داده است.
بر اساس این گزارش، این دو نفتکش در نزدیکی سواحل ایران و در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند و پهپادهای آمریکایی با شلیک موشک موتورخانه‌های آن‌ها را هدف قرار دادند.
فرماندهی مرکزی ارتش آمریکا، سنتکام، در بیانیهٔ رسمی خود پس از حملات سه‌شنبه‌شب اشارهٔ مشخصی به حمله به نفتکش‌ها نکرد، اما در تصاویر ویدئویی که از حملات منتشر کرد، صحنه‌ای از اصابت موشک به نفتکش نیز دیده می‌شود.
اکسیوس می‌گوید این نخستین بار است که ارتش آمریکا نفتکش‌های ایرانی را نه برای جلوگیری از نقض محاصره دریایی، بلکه در واکنش به حملات ایران به کشتی‌های عبوری از تنگه هرمز هدف قرار می‌دهد.
یک مقام آمریکایی این اقدام را بخشی از سیاست تازه‌ای موسوم به «نفتکش در برابر نفتکش» توصیف کرده که به‌گفتۀ او دونالد ترامپ برای بازدارندگی از حملات بیشتر ایران به کشتی‌ها تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78187" target="_blank">📅 16:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAbajTOFkRiSq_Jtt2-mTiZn5t7LhFdm6P5Z7e9qpLi_aoATgQgLw0uxJH8_ptep4je8lt5E7COMuNw4gkXj9vwv3xBEli-84_GBcgRmVyqaJX2K07USTisHbEADFQIS6sDD_jTZnHpDhOUoVECPV17VMef4E0ifdZmiuM5UVIoF9zuPJVFtwYwj-aE2D2grbfDsbNHZeE8xR_JpYu_hJVE69G0SA_7wzuD8a_kob4aLTvUN88ezb_dDdXkPOscTk1WClmJQlY5ZqNiQyBKNPC2FKRPDQhdi2ZYXoNIdKUkFRKKO_bWL6DLmPN6YOgL9nr8I5ra9X0RS4vTsV6e-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujWcQ4UUFw6wsNQly6njDvPMQKzsBmvInXXxeOIF2H6xH3obYNwB8OpinHC3fMGk2jQBNMwTH19ibDoxChx6b3i3S_dtKDjXqliXfriMzD0A_pFd3CaXu-Zy1536VGl66AZOTYxFHp7SMSarNdOyCzLG0ZwKf-NWI7xn_2zT4WWCHgJ_80q7OjrD9qu4HuQhIuJkg0JSPAwki3_Jqj5heLRIjUxFdAiUkDxOdoqoShybQRho7fRbMbVp2gZpBoqfCI-fWs8bUlG8qgZMCuZxmtHZnYjJEtwCVrujzlwwwBxgWNhWYgXT75RMpo4sYCd5e0fwG4s3gkrTZDGflNjHlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=PjllafmfuL6BjL1CO9pebGuhTNT-I_MAvQMrnY1_lE-ZmexJqQ20yh7TFRA9bEDZWotU5C-2VIEZGJd2Qeibq4FQAMxDKQoM8jRdZpEUbH380nY66j_8BBAzGDb7n6zPWjYs_tpRoaQ1jJj_wFBPLAQEyXg_ZyS4z8teI4RIaNW-qjnkgBboiMdO7j_EJUqhOq3LGyHF8LDZ0MsOt06SBvegbG2m3oyp4MuTz5sBjP5o1JyjE7-pP9_yQZsGSvhUCWYVcAFHFsPKCabjmCMK-jk2nbNCJIU-gD8M0HjBqjW79WIk4Cso0wErwYXDKPsBdZYP-Pf86mMIYMPwHXuozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=PjllafmfuL6BjL1CO9pebGuhTNT-I_MAvQMrnY1_lE-ZmexJqQ20yh7TFRA9bEDZWotU5C-2VIEZGJd2Qeibq4FQAMxDKQoM8jRdZpEUbH380nY66j_8BBAzGDb7n6zPWjYs_tpRoaQ1jJj_wFBPLAQEyXg_ZyS4z8teI4RIaNW-qjnkgBboiMdO7j_EJUqhOq3LGyHF8LDZ0MsOt06SBvegbG2m3oyp4MuTz5sBjP5o1JyjE7-pP9_yQZsGSvhUCWYVcAFHFsPKCabjmCMK-jk2nbNCJIU-gD8M0HjBqjW79WIk4Cso0wErwYXDKPsBdZYP-Pf86mMIYMPwHXuozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح چهارشنبه؛ وضعیت چند منزل مسکونی در کوهستک (هرمزگان).
@iliaen</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78183" target="_blank">📅 09:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05113c6026.mp4?token=IJYNw-u7vCJez8Z3oRjexJ1bQcsLTEpsHJ44NRyNkCqPLO6XMkRKwBYWGoAvJSCoYuwQWrCzr_45nxEEUVwBAlXQrPW_1etABwEcrlsCoUSWfjpM_EXAR3M8doo_umyN4iJm2WY2l9mb5LW0gSE-r96Vne5qzhrmIOI4FC2p-dAGS1vwSIyg-t3M1NLIPlTOT11BL1oBSojMjv__YE40yAJbn7tgH4zUMw13h2Ynh-hqZE4g2ahW-4wjHiVTDXu3abIHVIR0xbmruMA68hRd9flEMau2iKRcBSUdj6HIPDwaqcqsf21KUHuvPCOpNjTffTa66kB2jCcH16ReJGBT5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05113c6026.mp4?token=IJYNw-u7vCJez8Z3oRjexJ1bQcsLTEpsHJ44NRyNkCqPLO6XMkRKwBYWGoAvJSCoYuwQWrCzr_45nxEEUVwBAlXQrPW_1etABwEcrlsCoUSWfjpM_EXAR3M8doo_umyN4iJm2WY2l9mb5LW0gSE-r96Vne5qzhrmIOI4FC2p-dAGS1vwSIyg-t3M1NLIPlTOT11BL1oBSojMjv__YE40yAJbn7tgH4zUMw13h2Ynh-hqZE4g2ahW-4wjHiVTDXu3abIHVIR0xbmruMA68hRd9flEMau2iKRcBSUdj6HIPDwaqcqsf21KUHuvPCOpNjTffTa66kB2jCcH16ReJGBT5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روستای کوهستک در سیریک هرمزگان
ویدیوی منتشر شده در منابع حکومتی از مکانی که مورد حمله هوایی آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78182" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPmpAa996dcpVGdwJr15oxLI2FJMkiK-uz1NPTyPzO0sXawIp-Yl0TtaZpPBy8du0ih5dgMNU4F5q_W7o3G4oGPu-JmbjkgCCVnOEL2OdDufw5Ro6JvHCxF3FRnq4i1lq-nDCUwDowPuSl0O390fwzJ7_hAI1GeDsgG8yCeWaylEjtk5TVbfpErX4L2z1iyUH4K9wwHCFJILgblAAgTTJ5VhGEBaGAIG7n4JNmpxUoHl0vddlsMbXg96yki0o6M5HXMrTLgFQtBg-BlTL0CG5SaeLCfeqU-ce8zTsDUNRjyvfdS5ytydhKUAlARovC4eOiPLC7p7y1hBy8vF5DAcIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من تلاش نمی‌کنم ایران را، آن‌طور که ABC Fake News گزارش داده، به پای میز مذاکره بکشانم.
اصلاً برایم مهم نیست که آن‌ها توافقی امضا کنند که برای خودشان هم ارزشی ندارد.
من موقعیت فعلی‌مان را خیلی بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در ایران کاملاً در حال فروپاشی است.
آن‌ها فقط دارند روند اجتناب‌ناپذیر را طی می‌کنند.
مردم ایران چه زمانی به پا خواهند خاست و خواهند جنگید؟
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/78181" target="_blank">📅 04:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=RA20EsIiLrL8EOWob2RFj82-OVVMP9RjCLSTCFtq541UV6-YwTpoDZf8Arv4oMReFEDUAq5gCZLuEuWW8z9I-EoMVQlDtKcCVOp-uOToAfdgxq6PYiaKROiJCo6cpNVw-KAlPVLkUn0gutKjl6eMH26VOL8BKDPIJbKBEXoPUFtLnIH1JB4vQRaLRRvv5Yb5bTKq953gypOPPoH-yMOlBMXLW3cy9dzaTKoMzgEgPfABxJMuAdlwUAJ48Rna6uYkMfNLexAjEb7-o_0MPfPul_oIYpXYAqrLO2tRWNdGCZ_z_sU2bM-hbziunzFkvkFF9VY39sOrU80gAxmbsdGsdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=RA20EsIiLrL8EOWob2RFj82-OVVMP9RjCLSTCFtq541UV6-YwTpoDZf8Arv4oMReFEDUAq5gCZLuEuWW8z9I-EoMVQlDtKcCVOp-uOToAfdgxq6PYiaKROiJCo6cpNVw-KAlPVLkUn0gutKjl6eMH26VOL8BKDPIJbKBEXoPUFtLnIH1JB4vQRaLRRvv5Yb5bTKq953gypOPPoH-yMOlBMXLW3cy9dzaTKoMzgEgPfABxJMuAdlwUAJ48Rna6uYkMfNLexAjEb7-o_0MPfPul_oIYpXYAqrLO2tRWNdGCZ_z_sU2bM-hbziunzFkvkFF9VY39sOrU80gAxmbsdGsdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شروط پکن برای سفر قالیباف به چین'
حسین مرعشی، دبیرکل "حزب کارگزاران سازندگی"، گفت: خیلی روشن به ما گفته‌اند که
۱- تنگه هرمز را باز می‌کنید
۲- عوارض نمی‌گیرید
۳- با عربستان سعودی مسئله‌تان را حل می‌کنید
۴-  با آمریکا مسئله‌تان را حل می‌کنید
بعد قالیباف به چین بیاید.
قالیباف در اردیبهشت سال جاری، با پیشنهاد مسعود پزشکیان و تایید رهبر جمهوری اسلامی به عنوان «نماینده ویژه ایران در امور چین» منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/78180" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منابع حکومتی:
روابط عمومی سپاه:
🔹
مردم شریف و انقلابی اردن؛ یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن، اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78179" target="_blank">📅 02:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=TedutDBtzQSiu4Y0FNN9Vj4MIWzi4SrYITnxmWW29VmU6Sxcin5sSXEGTLv_CIqaRUJJDz67x-fknqRjse_2SdqhPzw4NfPRwAKJk0S-1lwAxmsM9LQxNzaY4e2mQFeUdPqWRdJUP0LXuswRHf0rBF2279wOWJWapwEHA16_dedSEHxu5zGSegfzdDpScmVPreTlkD0VzNYfDGh8pYtLmi7BiTK7kgqkshikysOuOIn19klFZG9QyfmqTiSYj56SeznYsd4jXNkpSipI8Pdtan6gf9BnPW3iwtZBuwoSoR3i0OvpHiMNFJN0P5O7PofhUnlJIRJo-EqGZdDh1GoTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=TedutDBtzQSiu4Y0FNN9Vj4MIWzi4SrYITnxmWW29VmU6Sxcin5sSXEGTLv_CIqaRUJJDz67x-fknqRjse_2SdqhPzw4NfPRwAKJk0S-1lwAxmsM9LQxNzaY4e2mQFeUdPqWRdJUP0LXuswRHf0rBF2279wOWJWapwEHA16_dedSEHxu5zGSegfzdDpScmVPreTlkD0VzNYfDGh8pYtLmi7BiTK7kgqkshikysOuOIn19klFZG9QyfmqTiSYj56SeznYsd4jXNkpSipI8Pdtan6gf9BnPW3iwtZBuwoSoR3i0OvpHiMNFJN0P5O7PofhUnlJIRJo-EqGZdDh1GoTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متنی که اکانت سنتکام به همراه ویدیوی بالا منتشر کرده، ترجمه ماشین:
سنتکام حملات به اهداف سپاه پاسداران در ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، توانمندی‌های مین‌گذاری و مراکز ارتباطی بود.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتیرانی تجاری در تنگه هرمز و نیروهای نظامی آمریکایی انجام شد.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول فعالیت هستند و همچنان هوشیار، مرگبار و آماده‌اند تا به اجرای عملیات‌هایی که فرمانده کل قوا دستور می‌دهد، ادامه دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78178" target="_blank">📅 02:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/wCWeloKKWiAMV1vS19KWwoZsxPGJ_1S0YEmhaqjEiJ1-vr7f2ZA1xetYWrziIAwD4DWovztFLowozuy25vjnWYW115f0Q9mnmRCOaWuAN9e6XcSMziERcqt93Z-NYEm6CSOA4lq_z_pMRFEnqRh7z6B9nNGrD6M5d0VAe0HOCsugprxkH48rUEwwTWmJKgX5aXIQdad98HlrEPHiL39iT67ywfBZmpNpyvg150qaO4ORGQTsxluZfEkoQiPgQ0kkkGuVwXhLoLXvsNh_dWEY3-nTtYYMpEgaF3pppSKYlmyycU_X4Q2knWiFTH2RwLycCA6f56sRVw5dgv62QLFTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EknEaLK6OzTQ_VcPZD6kpGIKzzQOKhziL6OETKf937xEDXHBNTDwFluxPin3JcUZgaVKQ1ADsIKEPfuvSxZiP5DwmSUYb1NeOaCtZIU977qNYMTrCGQu3eU3n-ioI7SduhzQZDkU904YOOY3oeaysfVb_4zzTKpMZMd8D7F3-hERMhA1MzWunpvXxKbQPs5h7t6DiN4puAPQLElf3Mb4iyZRRRjcb_b7xWOZUA2-0DAZY4p7wahCtnCR69jB6LpMZOuzKXROo7oTQHvDOL1Q8V3bSWmoUymeDysLPyAcU7zU68TeT4DD223H4GGhpI24VVBEdCqlcsSte4gc2qUEFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">"ستاد کل ارتش کویت" در فاصله چند دقیقه دو اطلاعیه منتشر کرد که گویا دومی فقط یک کلمه بیشتر داره. ترجمه ماشین:
اولی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادهای متخاصم است.
KuwaitArmyGHQ
دومی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم است.
KuwaitArmyGHQ
ادامه متن:
"ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، این صداها ناشی از رهگیری اهداف متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی مراجع ذی‌صلاح را رعایت کنند."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78176" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=HUbEziMqicitjThRtdCrDKPKgSX5uYbEF238XXpOcXYWaFfehM3MowqfAmVNoJ24cvwk6qwU3izlHLU5zdWxSIwErCMv1EDTXD-HlGBPZFg3OA15gLKVKScMsvMVWU7BnrzlmDdSIY81CZ48o_XYUXwot3CQeeVPhX6yNMNRuQjvIivmSQV6fUlM5Wq59kSTHhwhPwTc35tryf2JYJExcuujCnn6wPDbDuMPm_vzko59RilKfuENOZFXJfJ_fNjaRyI5zkcRQc13Ss1U-gciJYw-M23IQUwa9N9f1YZtbJw6t_gmvDKsb0JAaoPoEACgRE2ss4BE9nMBWrpTnRB6og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=HUbEziMqicitjThRtdCrDKPKgSX5uYbEF238XXpOcXYWaFfehM3MowqfAmVNoJ24cvwk6qwU3izlHLU5zdWxSIwErCMv1EDTXD-HlGBPZFg3OA15gLKVKScMsvMVWU7BnrzlmDdSIY81CZ48o_XYUXwot3CQeeVPhX6yNMNRuQjvIivmSQV6fUlM5Wq59kSTHhwhPwTc35tryf2JYJExcuujCnn6wPDbDuMPm_vzko59RilKfuENOZFXJfJ_fNjaRyI5zkcRQc13Ss1U-gciJYw-M23IQUwa9N9f1YZtbJw6t_gmvDKsb0JAaoPoEACgRE2ss4BE9nMBWrpTnRB6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان ویدیوی دریافتی از شهرستانی در استان ایلام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78175" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HDL7pSoctyR0_khPya_szfG1USVl6_gcYK3NoQIqqQ57ngUIN5A9Xbj4Sl02-L8RG3ssFSjz8cD9zwrFhRlLPVWrdY1AUt4wS0kccG9Z_NQfrik7qFLTai-jloSYBhREAcmCdo9knS17jvIJeum9pvCE5jNlL9aLh8G58P7YwiB1su3VAhvyiL2VIFFkzaUUX08psOGruUGJgcnK0kjU36Iuvbcc-ZQ28-zdNessl5G8joZ0vIY2-yDa61IlIKcI43p1F4zxRe2VqFg2BF1K0GE-NEE98ufFLFdaV8cRLUGgWivEhpKpEZUquQpqTQ1WY5pJYMy1drcC5PZFzXETnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار در کویت
ترجمه ماشین:
هشدار: خطر قریب‌الوقوع
............. تهدید امنیتی .............
همه موظف‌اند در مکان‌های امن بمانند و برای تضمین ایمنی عمومی، از پنجره‌ها و مکان‌های روباز و در معرض خطر فاصله بگیرند.
دفاع مدنی — وزارت کشور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78174" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=vMOOA8CrtsoAnvqGsLKFIkkJteh05zEghpq_MQsEfnJ-4LYKBKx0wonLkUJ1LYCQ1HFZcqFHGJyA0NTap9Mhk6O50kT_EhGee8yL-RbzG2oZ7RnUnBLfUbuVBaRBuy904-rSkO5vwxd1V6bApz2EuSi4ba_sBa56_ien3tarN7dOVU211Dfr0FoM2I4Gcf1c0Ui0CSzuArzoUGiHDeg52FFwkoOaRl3DP0pzjiXpdgZTieUWmptjZn4M0JvWhRlfnqKF0sxsHtO1bHrlVprmx6oHSNJOvtC9JoetT_VACCf1F_WsQud-Q6pLkSsfFgnLF3RFOYB881gGsVImJ4-q7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=vMOOA8CrtsoAnvqGsLKFIkkJteh05zEghpq_MQsEfnJ-4LYKBKx0wonLkUJ1LYCQ1HFZcqFHGJyA0NTap9Mhk6O50kT_EhGee8yL-RbzG2oZ7RnUnBLfUbuVBaRBuy904-rSkO5vwxd1V6bApz2EuSi4ba_sBa56_ien3tarN7dOVU211Dfr0FoM2I4Gcf1c0Ui0CSzuArzoUGiHDeg52FFwkoOaRl3DP0pzjiXpdgZTieUWmptjZn4M0JvWhRlfnqKF0sxsHtO1bHrlVprmx6oHSNJOvtC9JoetT_VACCf1F_WsQud-Q6pLkSsfFgnLF3RFOYB881gGsVImJ4-q7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس راهور جمهوری اسلامی ایران:
یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/78173" target="_blank">📅 01:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=JgPoKOkUNZh6VPo1vy5N_Ty9ADFEvvNxeoy4bDonNFNU84lUJ1hgGQpU2ZPUrhkZAmWWrU1VCMhPMk54Z3JwLMwx9ZiNBek3aLxP5Szy1LzbYyzlxRhIBbojQsQDWWCLL3rVPeiXLBfSiLK-pXVDfi1GxaqMtcJrvOPXWg9fOzJ1O7Zv45CCIfC4F2qAnsr_Z2mwEaWPfHCD_TJKCGIOP2eFDmhFEvUQLFnrLdkKfW-z6aJ3Zj8FN6y-jWNnDIVAV28I7XpSn_3wZu1Ds2OHqySbeJObBTnaKF00fjX7CCkz-pWZWWNkhW6MTVTjRFZHAbRvNFcloD3cmw-pDEm5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=JgPoKOkUNZh6VPo1vy5N_Ty9ADFEvvNxeoy4bDonNFNU84lUJ1hgGQpU2ZPUrhkZAmWWrU1VCMhPMk54Z3JwLMwx9ZiNBek3aLxP5Szy1LzbYyzlxRhIBbojQsQDWWCLL3rVPeiXLBfSiLK-pXVDfi1GxaqMtcJrvOPXWg9fOzJ1O7Zv45CCIfC4F2qAnsr_Z2mwEaWPfHCD_TJKCGIOP2eFDmhFEvUQLFnrLdkKfW-z6aJ3Zj8FN6y-jWNnDIVAV28I7XpSn_3wZu1Ds2OHqySbeJObBTnaKF00fjX7CCkz-pWZWWNkhW6MTVTjRFZHAbRvNFcloD3cmw-pDEm5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پیکر بی‌جان
ویدیوهای منتشر شده در منابع حکومتی: یکی در
#مشهد
با خودرو کوبیده به تجمع بسیجیان
سه‌شنبه ۱۰ شهریور
Vahid
دست‌کم چهار کشته در برخورد خودرو به تجمع‌کنندگان در مشهد
دقایقی پیش خبرگزاری‌های ایران گزارش دادند که راننده خودرویی که به میان تجمع‌کنندگان در بلوار وکیل‌آباد مشهد راند، بازداشت شده است.
خبرگزاری صداوسیما گفت که در این حادثه «۴ نفر کشته و بیش از ۱۰ نفر زخمی شده‌اند.»
پلیس راهنمایی و رانندگی مشهد گفت که یک ماشین «هیوندای جنسیس با سرعت بالا منحرف شده» و پس از آن به میان جمعیت برخورد کرده است.
گفته می‌شود این خودرو به «تجمع‌ شبانه حامیان حکومت ایران» برخورد کرده است.
هنوز علت این حادثه از سوی مقام‌های مشهد اعلام نشده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 505K · <a href="https://t.me/VahidOnline/78170" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ueRrmeI6NNcfvDFM26k8uFECr7I6JSYcbWYJPNqybbWvxwIpcGONEZaEv2SPv0rRa5wQbQLwBa4SLvChYmPE1RwF_Z4v5q4DD_OR875gX6eq_GtrTX4T2EzI1owQzPb4aZf30c3hU_ZqR6rIN5OgtL-pcv38ivBKEnSvps107Uqivinz3QvKkryhtTcBHrEuh0fdJ1_4gA3EwsXa6sx376lIRxvu1fPLRJCp-j-kFhATlJIvgMjaid_hEPiKMgFdiUeVcC_D-7Lj3nmd9Jt4-RCrFAHBa4uDhPwrEkTvgz5k3dRdHJ8_ksqxTDqwbixxYVpWqLH-r9HuThFbdo4-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dGWXssxPuVsChXfmxJ_dlPtmfNrW4YFGsEC-jt7EU65PQHzuK-sQ1froCml9AgW_j4gzijay0Vx6Ykj4CdiKCPM70hVZXQyktqWj3jeq3VQYfM5v3aDVTo4bdtdazdKOKn9meDtzEl3VhcWROaRSNA8yDLMDNx9xd3AvR676EIuu9k8cNuBoYou7hmTN6wK2vQTDeSQHKUMxLYq--7owVzPJDgPY86bLrv2Yx7SI1lPk7_D_ZzKGeZN1DwAi7I1ha8Io10Up-paxzPnNUgv33f_o8wPTz4PtoPfWT_XM15kXDYywrnXbH4YwIenAmnSB5OPY_MJ_UsbMlIDs_LlMDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت دکل مخابراتی کوهستک که در منطقه مسکونی واقع شده بود.
@iliaen</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/78168" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=l7TssVfmTacxg8fDRSQnUAWv33qfT3ngZMW3KxqmPQ5Nj8gRP_nx6oSGGn1W-vb8o6jP8910v0LRthpDV-D7mrOFOv-5BF1ztvqumDj2XYioVa3jOlUXMf1MsKeZcC5s5DUojjv7tZXOaaiDQDl7uU9NS8T02BpX71bQj6Sscmt6YVq-5xjQC1TF6XfNUTdIvZZYsUzuBieW_eRIHl0KfJZZk2BKKfDtBIULTJMw3MWIJFFg3-f-Nkpmsw2DzOCa94eSjq1kDzA7_UdrYTO9Ni2jvyeX6JlGhZAca9Xd2FytL4qqLjv02rESNbKsnRjomQ_O9QmTpt2aZCcCPveC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=l7TssVfmTacxg8fDRSQnUAWv33qfT3ngZMW3KxqmPQ5Nj8gRP_nx6oSGGn1W-vb8o6jP8910v0LRthpDV-D7mrOFOv-5BF1ztvqumDj2XYioVa3jOlUXMf1MsKeZcC5s5DUojjv7tZXOaaiDQDl7uU9NS8T02BpX71bQj6Sscmt6YVq-5xjQC1TF6XfNUTdIvZZYsUzuBieW_eRIHl0KfJZZk2BKKfDtBIULTJMw3MWIJFFg3-f-Nkpmsw2DzOCa94eSjq1kDzA7_UdrYTO9Ni2jvyeX6JlGhZAca9Xd2FytL4qqLjv02rESNbKsnRjomQ_O9QmTpt2aZCcCPveC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: '
در حمله به سیریک ۴ شهروند کشته و ۶۵ نفر زخمی شدند
'
ایران گفته است در حملات هوایی آمریکا به بندر کوهستک شهرستان سیریک، چهار نفر از جمله یک زن و یک کودک که در مراسم عروسی شرکت داشتند کشته و ۶۵ نفر مجروح شدند.
رئیس دانشگاه علوم پزشکی هرمزگان گفت دو نفر در محل کشته شدند و دو نفر در بیمارستان جان باختند و «شش نفر از مجروحان در بخش مراقبت‌های ویژه بستری‌ شده‌اند و ۲۶ نفر هم در بخش‌های جراحی تحت درمان قرار دارند.»
@
VahidHeadline
در همین رابطه یک منبع محلی به بی‌بی‌سی فارسی گفت به گمان او هدف حمله هوایی «یک دکل مخابراتی» که در فاصله «چند متری خانه محل برگزاری عروسی و آن طرف خیابان» قرار داشته بوده است.
@
VahidHeadline
در پیام‌هایی که من دریافت کرده بودم هم نوشته بودند هدف حمله یک
دکل مخابراتی
بوده و در اون حمله شهروندانی در خانه‌های اطراف، از جمله در یک
عروسی
، کشته یا زخمی شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/78167" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=dNcGbb-R77xPRVNIoEIxrUZmzSzE55qMLPOCUT4oKm95LjMR1TYpsZIYK9paHJkrRfUG3ZxzBonCK6w-4zf-lOG42f7Agguz8G7Nd_eSNuAloR4RPUn4-tpZXwdD2gTCvHCuJYfKW04U_oQOloDLp0Pbx4ZLZc6YBirQuknMV_hPzIM9NoJDMITA5mmnkTI8nTxECbh5W6TGsaO3EucKZhSubMsTQFcbeuWivGdTX4ZWC4lzw45_Gynfthz_by5YMIswMYMcyOa1clxjLvl4Osk6AcBAekrKM784fiY6CmLUpGgCifydGEv3NvRfYG02Xo0HeQTCEEYBvOnfFRCqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=dNcGbb-R77xPRVNIoEIxrUZmzSzE55qMLPOCUT4oKm95LjMR1TYpsZIYK9paHJkrRfUG3ZxzBonCK6w-4zf-lOG42f7Agguz8G7Nd_eSNuAloR4RPUn4-tpZXwdD2gTCvHCuJYfKW04U_oQOloDLp0Pbx4ZLZc6YBirQuknMV_hPzIM9NoJDMITA5mmnkTI8nTxECbh5W6TGsaO3EucKZhSubMsTQFcbeuWivGdTX4ZWC4lzw45_Gynfthz_by5YMIswMYMcyOa1clxjLvl4Osk6AcBAekrKM784fiY6CmLUpGgCifydGEv3NvRfYG02Xo0HeQTCEEYBvOnfFRCqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از بیدگنه
سلام همین الان از بیدگنه موشک زدن
سلام از فردیس موشک فرستادن
سلام وحیدجان
ساعت ۲۳:۱۳ از سمت جنوب مهرشهر کرج صدای بلند شدن موشک میاد.
سلام الان از بیدگنه موشک زدن
از کرج موشک زدن چندتا
از بیدگنه ملارد بود احتمالا
درود همین الان صدای بلند شدن موشک از فردیس کرج اومد
همین الا از ملارد بیدگنه موشک شلیک شد
همین الان از بیدگنه چندتا موشک شلیک کرد
سلام از ملارد موشک زدن ساعت ۱۱:۱۲
+ ده‌ها پیام مشابه دیگر از این منطقه پرجمعیت که نمی‌رسم بخونم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/78166" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان از کرمانشاه موشک زدن ۱۱و۰۷ دقیقه
داداش کرمانشاه پردیس دقیقا همین الان صدا اومد
همین الان از کرمانشاه موشک پرتاب کردن
صدا انفجار شدید کرمانشاه الان
وحید همین الان از کرمانشاه موشک فرستادن ۲۳:۰۸
کرمانشاه الان موشک زدن
کرمانشاه صدا جنگنده میاد وحشتناک [صدای پرتاب موشک با جنگنده زیاد اشتباه گرفته میشن.]
10:08 کرمانشاه موشک رفت
همین الان از کرمانشاه موشک فرستاد ...
سلام وقت بخیر الان هم از کرمانشاه صدای شبیه پرتاب موشک اومد ۲۳:۱۰
کرمانشاه دارن موشک میزنن، هنوز ادامه داره ۲۳:۱۱
موج دوم موشک از کرمانشاه ۲۳.۱۲
آپدیت:
پیام‌های کرمانشاه تا پنج تا موشک ادامه داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78165" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
الان موشک از،یزد زدن
از یزد موشک زدن الان
سلام وحید جان
همین الان از یزد موشک بلند شد
همین الان از یزد موشک زدن
وحید یزد همین الان موشک بلند شد ازش
الان از یزد موشک پرتاب شد
🔄
همین الان دوتا دیگه
دو تا دیگه از یزد زدن
۲۳:۰۸ دوباره از
#یزد
موشک زدن.
۳ تا موشک دوباره یزد بلند شد
سومین موشک هم شلیک شد
ساعت 11:08 دوتا موشک دیگه از یزد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78164" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mKbmFGXrA2dBTqzqU-XpWYH-OxWPRhfi2LzIU4i9sPQw9J2XuJoZ62M_XXiovwOXaixyKoAnPeySEcCAlqJ_uAhOfrBWKzkL-4W6CpY_8vAneAzoTEnTiQ0qAE_wTkxnLwrRbnGWyCelGwDxW72RUx2S936FosWOY9xxAZ0V5fl1mE5tA43jHHMN0bAVYAtdrl2AdhjKugcZJzHgvkuSTePU_wda8YM56OvGEpb7rrRwsMhJfuA-1I8bgPhY0TPiaCVI-iYkvWwGOsIfBs4M4MqjLb4u74s_AR0can7QqMtXGpsYisaoy7bW6P3F6HVcKGMgrGprSm11d7JrhCjq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CuL7fWM7r2UW0SmxxidKXqWO6XpBBJ72qrgqAZjdXLc6ODh0tmU1ug42ItUhl20VNq_XHLtsF0_NY1hUn9YH-NNXWmiMuJu98N4FsxiMuUP5t3CPpBqrXxggg_GeVmte6M7xkiOJ4hD96WV72kP3Qujr-yr20YOwP9bj75boZ3JY5ufFX6VslTK2CnyWns6fVTM8_z9IupzWN6Xbisejy9tH0-St-5Qg19zhnhx00Zei1jsK5IuJq8QTS-m7gHC01hxPsLaGIvi_XlOHFh6d8twE_ipIQAukjS3KUGcyPKQT7EZMxmQARYHmqOn-E81UB8mk3ic6FYyC4aDedkIgGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=JmL8uobtv_yZwXqMwlzjh0yWDKz3h9yqzP_xnj7lTM9k0E8P62JpijpZHg6p7DO924cIApckfHN4muSW-Hy84lyZ4hC5DbBoIXVMj4KwYtnogOkm0DlxQau9rPJ85d8kreWVS8s99k3abMeJ9SumfydYxkLMrCixNw_RhgSRPB4oWvHwtLNrY55B2IDTq6bs-1jOsOBIJcKPPKnWVvJdYHIz57WQoO3p82KyNuNuAlbbEEL-4paLVT5K8JcG2c5tmeId-xJdjygxSj_RANqCdhnZsGASZlBIHZdIXorG5tJUmL0NGBZKPJm4Q8-SR-rh5dncxIFeWQ0MVcoiwPBIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=JmL8uobtv_yZwXqMwlzjh0yWDKz3h9yqzP_xnj7lTM9k0E8P62JpijpZHg6p7DO924cIApckfHN4muSW-Hy84lyZ4hC5DbBoIXVMj4KwYtnogOkm0DlxQau9rPJ85d8kreWVS8s99k3abMeJ9SumfydYxkLMrCixNw_RhgSRPB4oWvHwtLNrY55B2IDTq6bs-1jOsOBIJcKPPKnWVvJdYHIz57WQoO3p82KyNuNuAlbbEEL-4paLVT5K8JcG2c5tmeId-xJdjygxSj_RANqCdhnZsGASZlBIHZdIXorG5tJUmL0NGBZKPJm4Q8-SR-rh5dncxIFeWQ0MVcoiwPBIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی: سه موشک از
#خمین
پرتاب شد
تصویر دریافتی سوم از آسمان ازنا در لرستان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78160" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=atwaw-aabGx434LnUcOqDPqyzDVhEmI8xTVtK91sHMhkc1nnNfZxtbuC-Hidv3l4NLjpcvo_X3a8LoXb7m0UPKZQA4MzviTvfxe1fQjTcq8pOHfsQyDMFh8d52QZIEHXRraVj4vUtS3dlzdi90HD_VQhDjvKSFtGxpQHab_us3xChmThq5J6cyeR-Dsr9zkdx3J6SKJw6kFE8gioYVA7UEHEMLYCDs9oRaIVWUu0fMfu1s38dBbhUNInMg2_qD7zqwPrcSrMqGj1Mw5KKu6uU1EcjqWY1LASFrfIu-RTRXEiG6MMBEg3rUA8uK5aug9RianU3cgafb6VJYpVQ4nmpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=atwaw-aabGx434LnUcOqDPqyzDVhEmI8xTVtK91sHMhkc1nnNfZxtbuC-Hidv3l4NLjpcvo_X3a8LoXb7m0UPKZQA4MzviTvfxe1fQjTcq8pOHfsQyDMFh8d52QZIEHXRraVj4vUtS3dlzdi90HD_VQhDjvKSFtGxpQHab_us3xChmThq5J6cyeR-Dsr9zkdx3J6SKJw6kFE8gioYVA7UEHEMLYCDs9oRaIVWUu0fMfu1s38dBbhUNInMg2_qD7zqwPrcSrMqGj1Mw5KKu6uU1EcjqWY1LASFrfIu-RTRXEiG6MMBEg3rUA8uK5aug9RianU3cgafb6VJYpVQ4nmpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
خمین همین الان دوتا موشک زد
سومی رو هم زد
سه تا موشک از خمین زدن
سه صدای شلیک موشک از الیگودرز - احتمالا سمت خمین باشه
شلیک مجدد موشک از خمین، بیش از 3تا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78159" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
