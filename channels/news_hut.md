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
<img src="https://cdn4.telesco.pe/file/s5lKNLKN_QUChbChMKQrt6y_rMJIgKRsieIlWeXi1R2DVBGMU_baC25V12IJ6GLOMgfAui7Vo2kNXjOMBMGupdKDFpmSM6z3GFYegW8tBoTMyyZx0KvtyP1FxBq1temqZ7Leo6na8bOG4sduRPXwFCkxpZm08nQQRpUbOZ13rXhfvGUHWXHwt0PW4j5DhJUw35ezan5SHlBtAloeH3vWq3nYMbYKLbvlGZNMT01v4fl5E4vPRMzAKrtAEHLOSSAqy_c_PPj_7aEmD_HuC0HYCzQOa2jVPL5CHB3sGNukvIgkkkloTG-pMgH0eMuWfKhNmPxg7ENvoC_UM3v3aTKsyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/et-fccib55eslOMEVbD73D4-Z8-sk9HrN5QGPetS7Sgacck-K3VwY6xkQ4lXJNzoExH52T5rHRbhh0mnE3vGyhW3Pt0FaH8yHOfxyVaEgq_VOvOLhmjOt6G7qEzOHgwdMTjGpB4c2IcbH8UWVSLIHGwkeLQap8pFooiPvB0HEsN8VPfmIJ2ek3gsvL_Cvpqw2uIHLXDNtMHLsV0rYYDt7l6Y6CTr0k_dN9WzOSHi9K0BqN26VUUPaH2WDD4fUZ7CiAO-Y-ytwc1lqWCnr_9paV0ICFYLOC0G9U-e-EJHEvoZseUIcEBKP60wn2HZut6470ic0m8IcPB5x9XrTLrLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQsmBj0xYdXYni8GcA0QRnpuTBSeLNLLXUIQl7OM1HZpFIaZwQesRkS-yjTj7_1ZHD_uRhtsNggvcHpOFh0Fz8kVru6qAf9Z3E5iz9GCD4xxfCJVLmHXVmuCs8OXGoQTxpknbHoT72GmdHvWR5th07tuhn6yoR8WhoEgvV1AOh-qAGGaWTl9vPBOlyI_H9gEToVe4kyTNCvzTX-IHQMYzYHaDU6EnLZqGNh7apcPwwlYbMS0KPTT2k3b10EnkO8S5Kg3jrIOjcsVDSBi_r2f4DcqCePySaZiTTyrhcpnLehWM7cFZSaDIChw2d5EAdIos9bt_uwCjaXipMOv_99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBhBfOZ2RHAlWjwbjxviJYLYlYScUGXRiWGPYRjyuJfkJJwjtEPeOFSakrseImM-rcX02dfi3QiSCHgYtAPEE0cy3mipNpIOhJ2-Rgw7nntcqy1iOa5_YcbMxGRYaNZ_LSbys8Pove9nkvu-CJhsIuEiVxL5NaVS_oM0IzZiUMTvWw5KFIhVJ2e9hbBAK_p53_21Khq7AXkUFQEXRpQkvBb_OKVHssoQLmPeU1ZD4PJfrx36ZxYlhNNFNbSbvsKZ6ryGW0MdoZZg1TX1QHsDCDCV4teYoq6vGBaQjNFJen9ngw7w4zNB3yxDdJIlZu7xOgnk9caAXbrrg0tcrHSgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5tshjScOqoxyy2zCmi75fZHUfeHJTjRbOC2GRgs57mnboHqXA5Ha1b_-fSYbuk76EnfqI3VCKMsIWbkg_pi9CwQ9CFAfaKn7OZ7_BiiLmcR4Bj7MIrRfvrLYmojRHbFupFfS1oGIB7elrYF0WS_yefprvILM2_TM9KJDxOF1gITNXLex2pQ4S6HAnwSn6p6ecu744XI3OnPuQ3S7tztbhiH-jxO1mmSRDsG2NZe6O7qtlfjZ1O57-TKQXKr5AIkWUoAbDVMBXbUAPq0uJEYsgVVWVo6RV8JoPJPZ3HzIXu-8JNDtCrKI74v2Ee8g4r8KbUEyZTLukBSKagwMIzxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7LhBOFsWniZLYRpxwdj6guOJuWwsza91uhlwpxzUiv3kKLdABJ8KooPvYtgy5KwFBmxpvKjrE1XAU3KifajSDtXzQECLPjU0h0lBEjTMpvrnfXEp2cWcWd7BDNpftRnCnv5bFPixKN18V68Am1dSs8YcDj4U8_aPL5KlzpN0CmOLx8vpcjF_BMCuemhvvL5_BA2Hij2-nXMZq-_SNLcNhoSCZX4aR7JgFp7PKlk96GROmCGjKfUQ_kFXgRRri8Boj8UpPGTaUKhpnlMrQcU6ny_EhKJTmAARM5Q1MtgkOFLOpp6KuxcKAFduKifVW2QuyIiNBGxjvnMkauihUPDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=OubzCpTMU7c__Ege2Sxd7WRS-4zGU_wcPV5hH9-IL34l18ceDQUuwA39dkDvK0g1bNrasa4dJFPUdP1j7fqrarVtM_gNtHrsGdBsR6emVU5UuskZ5mPg2f4ABFqFKv1oFFU6N8q0Dw-F6zu5BCGCoEIde8hnvAXbJPgf-Copcy01DThppOTTCNMVRYKBR5a481y1AOcgpeJ5q3cnWJvTuhl_iKxiRVBmr0XVL0tO9wqHe19zaj3ynp6JCOW2FF7cjGs8thQ5GM8vZ4SHGIDaR-pYqzmt_RLEpV302jQXCMQYEzoca7dIZ_J3Cw2DQ_HzaA5L1p3KV1mXoMD1OPTCsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=OubzCpTMU7c__Ege2Sxd7WRS-4zGU_wcPV5hH9-IL34l18ceDQUuwA39dkDvK0g1bNrasa4dJFPUdP1j7fqrarVtM_gNtHrsGdBsR6emVU5UuskZ5mPg2f4ABFqFKv1oFFU6N8q0Dw-F6zu5BCGCoEIde8hnvAXbJPgf-Copcy01DThppOTTCNMVRYKBR5a481y1AOcgpeJ5q3cnWJvTuhl_iKxiRVBmr0XVL0tO9wqHe19zaj3ynp6JCOW2FF7cjGs8thQ5GM8vZ4SHGIDaR-pYqzmt_RLEpV302jQXCMQYEzoca7dIZ_J3Cw2DQ_HzaA5L1p3KV1mXoMD1OPTCsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Ihcpw7gMXPRV-q-P3rnju31_75xjjS4ncNRg246ncbNH0vRhlOe2yNilslYmUAyx4e8fidXxBlfzmlVtlkP0aoP9oA5ZLxBqDL8t5oJLKKY_M4QJ5P6L6bhqGQjCTqp6INlcGPN1C19E_uoXXMOfISAQ6GN5rVZ5NmtyJi0qmbSDZkh0L1FAMq3VQ2fyPGa1RPYD_e6j0aizRh0pG8rxVw7Iq8XEpD7ss3Vr6j01O163k1ShIhaWPiIJeB18VIb2sv8dsxyl-LYbgXN4174_XBOIeszzHVp46m6YPqF6GZriHUa2i69D5MbbPr7oaJny1-zUNTWf11l5aV5iHGcCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Ihcpw7gMXPRV-q-P3rnju31_75xjjS4ncNRg246ncbNH0vRhlOe2yNilslYmUAyx4e8fidXxBlfzmlVtlkP0aoP9oA5ZLxBqDL8t5oJLKKY_M4QJ5P6L6bhqGQjCTqp6INlcGPN1C19E_uoXXMOfISAQ6GN5rVZ5NmtyJi0qmbSDZkh0L1FAMq3VQ2fyPGa1RPYD_e6j0aizRh0pG8rxVw7Iq8XEpD7ss3Vr6j01O163k1ShIhaWPiIJeB18VIb2sv8dsxyl-LYbgXN4174_XBOIeszzHVp46m6YPqF6GZriHUa2i69D5MbbPr7oaJny1-zUNTWf11l5aV5iHGcCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kiO49vuwQRLCeKCn_BELVoFGp3FR1XPfGBcep42A7N0Dy5rl7voLpoKL6fJM1fybqOfaFfa--1wSkm4CunCiutKhKutoZ6tdzxuQsUWDp_kDw7eTt7ZVIKdcJfDvp7zf-66vLfA-oNhP6VCrMYlSO07aYDBEjF2W2GUVXZNfTJHsfdh9fhiicsdFjfhZ5MIEyiwgZq1E7ajqE-6NUW7fzXEtIPedcmsTpUWksBvW44giRhCfki-IXMdPBvl0E-NyqmFU7qujwy3V6vGEV9HPLq_PsQ0qHF_DUcX4wM25a9iKjQDsBnXkWbqzyHTSy09G1JkHPrhuDAlQhwA8zh-6JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kiO49vuwQRLCeKCn_BELVoFGp3FR1XPfGBcep42A7N0Dy5rl7voLpoKL6fJM1fybqOfaFfa--1wSkm4CunCiutKhKutoZ6tdzxuQsUWDp_kDw7eTt7ZVIKdcJfDvp7zf-66vLfA-oNhP6VCrMYlSO07aYDBEjF2W2GUVXZNfTJHsfdh9fhiicsdFjfhZ5MIEyiwgZq1E7ajqE-6NUW7fzXEtIPedcmsTpUWksBvW44giRhCfki-IXMdPBvl0E-NyqmFU7qujwy3V6vGEV9HPLq_PsQ0qHF_DUcX4wM25a9iKjQDsBnXkWbqzyHTSy09G1JkHPrhuDAlQhwA8zh-6JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8rQ_HRArxsY6fbrhdc4REoSjSAhH2tPG-bwuC21P_49UKaXSglJZUKTixe2XUY9QdHzuon_TwsKrPXM1pvPoXVTFS3b-d2YStMmUbw8HyX4lcXUv0maWbAUV1WMXUt7-nvha9U6jmQ7CGx6eFMETKZyxuUwyES5ZzDnoxoZPK1kg-FUR76Wwen15EfFPyyeVC5DfrEYoEoIE6TtE98zhdrggZ-CS9X_9P5wUV7Mgwdxhm1pbazz5zna93q2sy0v_DKiy6zMctfPbCTK6IU4dDsiNETu5cnFaAs8cJ99o3fz4QQwgyN-tBZiefiUQCoWxMsM9ZIwt88R4CR8bL_trA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0hSuQicpecqXwzUfzH5r44cD98jx-sjsVXBeEEx0QkmdwkNOkXP5vqyzMZmfTPvSlF2YBxFfkFp1qYZyXjHQTLS3jOgf89y-WhiFR8OwTDsO38-eg6A8hETQ6HW1bGX_6Tcu8tLvoclqwOMV80Cej1ljJTz7IW81ksZN-_hSrVV94kxoLp0DWiWwCUWmg9SWHpB60e9phFZ2nt7uzdwCrOMzACZ-pZiqrIi8uhNVt-1k1Ul6Fc4mSG7OCsQl01wJZw9_-c_nB9f61tYv7jYZxaxfaOH59c-E0OsGWlx77_y4ImpzMhjwUVGcVT04LVA8bucyvcSKv9PqNW1fGawUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFuLOw66rbKw4ftKe9ixyvAHOZk8YzxUJ-SOAZIwk_e9w3A4ziYYm1ynLgSJ_IDlsMtTFzln2yfYtnH5oYHw8YGJT-8wIKGThCv-HH8vxEKn6yNcOLedIln28B8Noq9qXsbC8QdVPuJyCn6jNXuPEbhuHaL8oJFNuaplp4CmzVtge8Yc5OIdw6Xw7J1A_GkPUDPDK0Gn_z5K8MCLtZJsTaa5v2g6FxbDvFFlSRxHIaQDdDROIL8kOQ9_5zWIawokkp9_owNg2YqG_ybLyzQ1F4bRKUPE9gjHfIkyG37x9Q3IFQxAvH9rNt1fTerCE2CHxEZZL8XO_R41AO05ASI5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEKKPgpVfNiohvlrOIKKsE6SFovQC6modYnAoGvuSJqOJF9U37nkuegJq6HKJyB0PW5Lfo7SNNt6_gBIMHNv0A2oqoOVXtshb0aWB_E0pLy1wadPkygLwpUGfSWcLYKorF56gZqHpBy6Wimx5F2wMowLtNJU59LOn1Q05tCj1rrPMLjKLKtKYU0cnCJWY8olx20vOvyvEnvwtKTuFAILVKAuogOs8nq8pq96l-SHMwBHjhkZJv4Uveg2a8CGxKdobM7IEjuxBz0OymffSALkVubn2mCQV7BzXSL47CI9ocX6tgsyhzd7WXawnC_-suc4eHSjhNF_YjX0z_8b8TTc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngD7gv2NuqPytOC3djYrzBoihiXRpapJNhCqplkkJuoGzlMhBab2u_8TVDj91mufuBy21NkDdJmzjZBBOXJHd_fxdEngXkkbT1zqW0AGu7u6pj4y6DYjO7vwVn8HSTavaZ_JNgGRxGRlyoSiFmd0VKigg7vHAqec0N-R2MeX2xDsfIQb10DKMKOWqUOBsoFY9VEVtHuRyNNQN57TGYbBABbOxUtNhKwfb3_c9x6qhfcSoKugePK-3l0t7Dl_4lbZrzaReqUvSIH8nx7RxWfaXNG6AbEU-yN4woVMqhfF82HjAr91IRF3eW7YbjnKKKgdT4fAQd8ncZKZ9mu59WJSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUvol7mj4B93Y3sRuzxzXiiMe_pcgrDYPeFMDe414Mc2Ndhl4Yzm1qCEfQrZNK04TCt9QsgArdD_RqKcgwgw9a1HFWl5RbRkxA0nIPQen1NeJlYPzeaeiiyPXNxYT919qozrHrD9LFBHWVXI906hDcn-gVfoyUXoFd1hpngxJaX5A6nP4hToCSS-XlDMFvJ5Od7_8BjdWsQ3STJMe2ogzBwPQnTTvygqchhJPK1gCemIkHlX-2NiifJKCPqpBDmC2So0M-go7qotWFv56K2ZeB0flfUb0g4OPGXVD286GQpuTD6BmZQ9w5B5uebspKqvQmRIn4nnzc0m0Y66XteyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilqS4mK9spCg1frgzqmRfQ_k4pfwq7lsdq24jcLdvFEN1W11qZHhsjSEEQlZ5ftYK_bHqmuTMAAlCHhQZZ4Tcaq9PbiwNBGbunEq1m9oSyCQ_DCPXT5ZTzNxJFAtoC1peC8Iv6WqDbDw9BVfFYs880G0mtSdJM7QmQofbc0GQJy15zNsIGMtRyDRvlSxVikNHy-s5HFGa3FfgVCEbTxM8uhlQkrQx47wRM2YajutOVHMLxHarfdYEe8HWLMh-L1ybpH8Fu8EHzE_YJzcbstVg9HGLz37iiAjgT2xknYdFB3Mwg8_tHFDqlnU3bM562zPVzLMc_O5bq0X9TjpFmGhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqL-uHuLIFAl9nTsPHXDM15qBymH2M1HHdGpLDe0NRpCz0Y2k9SmaqPSN042kps_s6eWiINFmkWXovm8uVJ2DahZbMhFHwv64Xjb2SJf027zndRXDN0gviSNUAVZ4V-q4RT8n43Low5taOy0VjoBXzVV8_aUAjBqFEwo2IlKGT7NzeTfvBdslpxShMGQ87NCoBtsF25qhmWaA3cWIhyD6EVoLibQE2695vir0KNKLkJXR48wUfVw8XswEqYPAfEgFT0GINTCVguq3IULoRKvTAttvftKqzWQWLuSdZsF3LdcHTg_ph4bxH1sJHh7sBC8PisntIwS4MkCbxSRHy-QgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=HWj16JLxJOSRgwOrJRVNuuC5arfMzPWT4QetZeDXsgs18a0yHs2liiKrYakRmRyAPyKM0_0CnYsViel0KzIpah111r9VQP3BA9YYpHYVm_2tCp-BKKh-NXByE9y4MPTnqhUo8JYCkNKBekNvdQ300q3jBvtCtyvqBEkyukcKblGvJ3T6uA0p_FNG8T6Bq8VFXXJATpvn9cK9c-HBEfKbyBrr21TcVAOxVs4s0gR6WEQCGPuRZM0HjXh89U7v46_LzA1n5sfVoHxmKLFyfLJcrqOTyNHTwjeVcRuS6M-kQct17B5vpZmyfNKot6C-E4SICS-F62qZJNoL14ZsuHmDUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=HWj16JLxJOSRgwOrJRVNuuC5arfMzPWT4QetZeDXsgs18a0yHs2liiKrYakRmRyAPyKM0_0CnYsViel0KzIpah111r9VQP3BA9YYpHYVm_2tCp-BKKh-NXByE9y4MPTnqhUo8JYCkNKBekNvdQ300q3jBvtCtyvqBEkyukcKblGvJ3T6uA0p_FNG8T6Bq8VFXXJATpvn9cK9c-HBEfKbyBrr21TcVAOxVs4s0gR6WEQCGPuRZM0HjXh89U7v46_LzA1n5sfVoHxmKLFyfLJcrqOTyNHTwjeVcRuS6M-kQct17B5vpZmyfNKot6C-E4SICS-F62qZJNoL14ZsuHmDUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=iTu6EdIm8SEtimHvMO-dyLf52Pzzi0itaEGFBwKN2SVor6sofD_-vINFjXMZ3P3cxREAliTSZZMVx9IZow2QiVia-etbSy24LDXNBSHWwsaAloVlIkfiNaMo1AFiGZ6rB70jpGB0giWbfldGeJ8KwT3flayvIU-CaJYSn3fWpPGYO1rvIY_0LUAl6c2WVJWZle8snLAJed7TDQoXwNq6Bh4pKheNOhsKyqCqM2eT0a0IahXpDCXU784uAtaEdLZl640exb2MfnQsp3mGVJ1zyeP8lttFFKiAxsSa0Eu3mzGCTkdr30574wFDqgm5sAm2E26CbTX3WRwG-a_jlp2LMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=iTu6EdIm8SEtimHvMO-dyLf52Pzzi0itaEGFBwKN2SVor6sofD_-vINFjXMZ3P3cxREAliTSZZMVx9IZow2QiVia-etbSy24LDXNBSHWwsaAloVlIkfiNaMo1AFiGZ6rB70jpGB0giWbfldGeJ8KwT3flayvIU-CaJYSn3fWpPGYO1rvIY_0LUAl6c2WVJWZle8snLAJed7TDQoXwNq6Bh4pKheNOhsKyqCqM2eT0a0IahXpDCXU784uAtaEdLZl640exb2MfnQsp3mGVJ1zyeP8lttFFKiAxsSa0Eu3mzGCTkdr30574wFDqgm5sAm2E26CbTX3WRwG-a_jlp2LMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=f9u1Gwom5KOJONPTz87xmaRn4QKIC-3tOHidc4hmWfAGZIJA55BnOol5x-BkEwdFOOVH_j0zrJpg7FYhAsptqfXcNNdyDy8Mqtt8Rdv-VdblErnVdLElFWTRgRjUBAROu2fjzYdFt9Az3y01r7npWliF3uT7Xuht2tpksEMhteFV9WpjZpfwx2UM5iJMvZRJl82F4lJjk_-FlqdbjhBjnQXH4tVZpHTPk99VyzuhQwrgDOaQy7SR7R3gM71YtVL_9yyuvbTh8ghMUIluBRYSjvUDUfeK8OJFX767biQF12WGN3o8M8O2Tx4uY09W1LgWMBlZqm1PGAmSE_nqMTjkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=f9u1Gwom5KOJONPTz87xmaRn4QKIC-3tOHidc4hmWfAGZIJA55BnOol5x-BkEwdFOOVH_j0zrJpg7FYhAsptqfXcNNdyDy8Mqtt8Rdv-VdblErnVdLElFWTRgRjUBAROu2fjzYdFt9Az3y01r7npWliF3uT7Xuht2tpksEMhteFV9WpjZpfwx2UM5iJMvZRJl82F4lJjk_-FlqdbjhBjnQXH4tVZpHTPk99VyzuhQwrgDOaQy7SR7R3gM71YtVL_9yyuvbTh8ghMUIluBRYSjvUDUfeK8OJFX767biQF12WGN3o8M8O2Tx4uY09W1LgWMBlZqm1PGAmSE_nqMTjkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=BwaK7kMq9G_LCVlqnv4OHccUzVbh3tWLOeIe-6tQxgd5MlOOMLTr0kqByuLl4gxCdYsMNMgIuB-EGnOeLPtGDiMiaBWvFWvEdCDneTZF546HlVeka1i5FIJ4CnuD0RoVFUKOol6fiUXk3OP7NkfubpBTwpafwo7amTZWu7WQxDYTJ-VCSJIKDAKalei-a-uR29042cCpfSo8wwPaAA4k7-TKmtmzbsZCq0lHHo2c-yI4KWZBI8IR2ws6V41AIFdOodhl_WUBZsgocaca2UvUYax-BLxwHQ4JR4GLey4K3fF-BTvJTgcYMAJhPmLn6YfpmVs6YT4gNqoN3MELN2eKLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=BwaK7kMq9G_LCVlqnv4OHccUzVbh3tWLOeIe-6tQxgd5MlOOMLTr0kqByuLl4gxCdYsMNMgIuB-EGnOeLPtGDiMiaBWvFWvEdCDneTZF546HlVeka1i5FIJ4CnuD0RoVFUKOol6fiUXk3OP7NkfubpBTwpafwo7amTZWu7WQxDYTJ-VCSJIKDAKalei-a-uR29042cCpfSo8wwPaAA4k7-TKmtmzbsZCq0lHHo2c-yI4KWZBI8IR2ws6V41AIFdOodhl_WUBZsgocaca2UvUYax-BLxwHQ4JR4GLey4K3fF-BTvJTgcYMAJhPmLn6YfpmVs6YT4gNqoN3MELN2eKLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbe_dp7zHRFNNDnTBZoHT2eXPCxYqwcRkwVE3_syVHsYxhr2BQ5dFPyQGCF6m64fDTfodS1GXjneaQU1mG3YrgM9kklmfRkk-QfjazTWlFh0PeQieiNpSy4nuKC3CcSkOPbXbyR86pDRt8HVY2jX8gvC1j3scZBsHw5Z7pCqW4rcaISCNzCHc1YUY_YRWT0LmtuD6nrEd8h7shxr1HjSHdjBqTAKuzi5Wnp8uS2t3LElCT4foA9mzlfbVLF8lRdvWY34tJ-Hu3_WwfrygrQ2J3ExOAG_qTfUkvFXUpQXYOxPnZF9mI_VEuGX8kYBMBSIAfj-9H_Xrn_Dm5llSFe0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkivMRuh1MmB-efZq6rR5wySaqu9HPQqrgCAZNABlSjI4rgxg79PCRSIL06zfRDdol0C4k4-ui88nKWd0Af6cAu5NfdPVLaCKFBXA-hXxrLZkl5bZJJLhWMyOCh45NmGoorYavS1TQrFJzKSq2gDjKbDkq6FA6NKZatls1srhNfBfXA4KPgqAA0NqiWzj1oHkmb584fH8OQ1i7E3iWz6L0oU6YLJ15qno2yGv7nPysq-e41Nyh4-ZUqxBsdb_zTs0JMwjP4SVz06c7ypz8eVBx0hfc2FtpXq5gU_w-XvPe11lT3k6TTXL-_3zeIu2EPvGNqVA1YaKw94-GXso_ybIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7BtDyfp6hSElikThoYJTG665AzxTHeyqYWMv_h0pHAOsp47XvC-lekX5EHYxmE0oaRohxntyir34ebSjuqU76gdqd500g4Gz9-dBvAvGMjYIZnJEt7O2ywOOYw4J9LEVA4nZc-8u-v2nRTCBupsCeSsywjK-_CXGGr6fx-ldC5ZTzBwjQAIEQ0UTo_BHjNRPs_v2hn9pngb7cbR08cpSkS94BHHQJbcmST6tBhDj_BM3PNPPPn2zQhKgVeKqZiGZR99S2Rx1eP4Zns8ekFr4UYIKspxufyX1zbbtjkl-APw59TBI8XP0ZTzcOZv-eXlsRRKn2kEc8dLbTeS7fOwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=R0AyWadjlzp55isiktm_jIAngw3hJroiGjy36wFLxWmNGer1ezG5kaGPQgwxgYn7irO7wg1yd4d0Mold4-MLsj8gx8htUpllRnlnPKcW47d49LBEwYVGlpQllr_G-4rVtsU3FfcG5t18YB7Blm9fET_dkMfW6YiyHMV40ZRlVcTI3fzajy7NCYl4SKIYgFPTmL-fnu-NjbcpHStgBGaEvvPUlYT4DRZ7lnI1s2B61Wl-j2lUepu3ORKZHrGAiGeL9tLSfY-6scZYg0XGeUe_vLr-eaFQTuazPt_p5lShQkc8eDUXRVtLA91PaJd58Ah_8RBDnOuAYNjp7vIVSrWoLJ-hGuum6sy6eQQkQLGv57BcGiFfeIK5yz-rjxC-NLUvYkKeDKZ2eG8XOV5R1kxNSEK98hZ3GB4MHfufgWYEBAyJl4tDnTfVvkT9RJpitVwjgkuTwG1-agWSRxQ3coRqQSHrzd_57E2Eikbgsepc7VpHBh_UynEI2mpIfu1GH5yB6BtVlVfUXr0-nxvMdWSrHyaiyRfLrbAZHMvxHLA-vf4JhFn6p25JpA3cfeyFa4UnGjGlx-wStYF8agRDBye0-WSO4EkA9GQYJ-UzQG4vaVGWnnubQ9VTnvKcGvx4PYxq5m79j9QUQkMLJI5pl-RTD7fJ5GG4JVsxPhfM9ak-wUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=R0AyWadjlzp55isiktm_jIAngw3hJroiGjy36wFLxWmNGer1ezG5kaGPQgwxgYn7irO7wg1yd4d0Mold4-MLsj8gx8htUpllRnlnPKcW47d49LBEwYVGlpQllr_G-4rVtsU3FfcG5t18YB7Blm9fET_dkMfW6YiyHMV40ZRlVcTI3fzajy7NCYl4SKIYgFPTmL-fnu-NjbcpHStgBGaEvvPUlYT4DRZ7lnI1s2B61Wl-j2lUepu3ORKZHrGAiGeL9tLSfY-6scZYg0XGeUe_vLr-eaFQTuazPt_p5lShQkc8eDUXRVtLA91PaJd58Ah_8RBDnOuAYNjp7vIVSrWoLJ-hGuum6sy6eQQkQLGv57BcGiFfeIK5yz-rjxC-NLUvYkKeDKZ2eG8XOV5R1kxNSEK98hZ3GB4MHfufgWYEBAyJl4tDnTfVvkT9RJpitVwjgkuTwG1-agWSRxQ3coRqQSHrzd_57E2Eikbgsepc7VpHBh_UynEI2mpIfu1GH5yB6BtVlVfUXr0-nxvMdWSrHyaiyRfLrbAZHMvxHLA-vf4JhFn6p25JpA3cfeyFa4UnGjGlx-wStYF8agRDBye0-WSO4EkA9GQYJ-UzQG4vaVGWnnubQ9VTnvKcGvx4PYxq5m79j9QUQkMLJI5pl-RTD7fJ5GG4JVsxPhfM9ak-wUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=U9I1olfl6s1vedgeyLQXLP8GMbRaCoEFRx2qsIyQjX74q5l-99c63LgRK3ppXMV0Ep5U6nc7QCVxRZmRAkHiH92RV5Q3J8ZKviGITpcrmM2LYnHNpArklSHqe4wEScZ6vKWvTmfN4BIB1oOaabZnxLc3PSrWfI55trCVG842BYvUnJwYgRFnIcHx7Qh-66ll-ZS8vkL5QKWbACCZP6vijQS2LZHVdLgTgyPlDuVWVVlM1LK9_ebLGjIt6U9EL5cY9e996288fVrIF-16jJ1D0DTQtAwgYIjiC7d-s5UqrqXLDj2X4nyU55CGf-Dn0RwHPZCsyvLaSIYM6CjcVdTmjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=U9I1olfl6s1vedgeyLQXLP8GMbRaCoEFRx2qsIyQjX74q5l-99c63LgRK3ppXMV0Ep5U6nc7QCVxRZmRAkHiH92RV5Q3J8ZKviGITpcrmM2LYnHNpArklSHqe4wEScZ6vKWvTmfN4BIB1oOaabZnxLc3PSrWfI55trCVG842BYvUnJwYgRFnIcHx7Qh-66ll-ZS8vkL5QKWbACCZP6vijQS2LZHVdLgTgyPlDuVWVVlM1LK9_ebLGjIt6U9EL5cY9e996288fVrIF-16jJ1D0DTQtAwgYIjiC7d-s5UqrqXLDj2X4nyU55CGf-Dn0RwHPZCsyvLaSIYM6CjcVdTmjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSAVmgTAx0dE8XxYoc4455hZl62RizUnQ-U891xWA0pQqoB3h61xq-c7VtTgwuh0OUPmtEIMQzkYgXe_IbHQLSaiHfJIjZZdPnOaq0OZsKeFSAHIL0uncaE1zey19V-1MDMTSlKR-5pTwqBFD8gW9AcLmWqnC-gAAqwR0OzE0up6ShFpNq4jCPjcqPUxcNzDPorAql7QkJsQROmJr_LvEO52ZPu-aciX7GOJQ9v7RLmsPONWrz6YdIPEY02CGeLjP5TwJmphH23YGz8vZooLtCmlR-54SszyNrSdEtawgaIjHZFG1uXWw4BxSjAI9l4W7zHnI6xH6HFu-SK7Xa9ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=QiwcY7Fm0SQn8eD7YoMMZ41kHQc3J1SVF40aAoASBV1oMtoWxR5VU2J8SbOvAyFbxmsvorGYKfPGmTnjRqk-RtQR-w1LHpMBsSoUea9Px_IOdxNnW6TK_awY6oRdavDLev5V_U5eeC8FWcIpHt0u41UtC_0AKxtxavgLhapgBpmagnMeq0GmhiiumycGphhrLULEC-7WdCZDeikgAvrLeDAzz8YBW5m2bIO_V8wFcyLKppiBkiiXBJqrl9BdcXo_3zpH2q8NBR9VKfJHwlPw3fr7z3XwMJvOlvyPIy6-N0frjAtdZ2IupjgMlyAXQbLH8iy1n3MR2l-Ms66hFbPXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=QiwcY7Fm0SQn8eD7YoMMZ41kHQc3J1SVF40aAoASBV1oMtoWxR5VU2J8SbOvAyFbxmsvorGYKfPGmTnjRqk-RtQR-w1LHpMBsSoUea9Px_IOdxNnW6TK_awY6oRdavDLev5V_U5eeC8FWcIpHt0u41UtC_0AKxtxavgLhapgBpmagnMeq0GmhiiumycGphhrLULEC-7WdCZDeikgAvrLeDAzz8YBW5m2bIO_V8wFcyLKppiBkiiXBJqrl9BdcXo_3zpH2q8NBR9VKfJHwlPw3fr7z3XwMJvOlvyPIy6-N0frjAtdZ2IupjgMlyAXQbLH8iy1n3MR2l-Ms66hFbPXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=KBeQ7FCnECG_ZhY0V5Yfgb9jaRBjmnXXZEg44iBrgz4GS8Uu5SVyxlJS8l7spzmhBi-aw0nZcTQGefBhZxrUmmvrao-BY9cYDiFthe4_0Er4HgJQRhJ2L0N01X7bT8Gg670q1HrjeS4ZUZqJ141Tpd7WyqwMrIXb445qwy_iwPs80pF6cqy1AHMlhuoF5Ci5XVC4NdunIvfWqusBMGq-dchBObVuMw_uys1-bOiVl-oQtfHSHbosrsr8ayyTp9gRVAQ73yGQjodljQJ5bKs2RFvtjIsFdZwAAAbAbPnIIuX1YCXZxB9LBnxOyHGuyXuBhXnCODRWPLAGN9rjOkzk6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=KBeQ7FCnECG_ZhY0V5Yfgb9jaRBjmnXXZEg44iBrgz4GS8Uu5SVyxlJS8l7spzmhBi-aw0nZcTQGefBhZxrUmmvrao-BY9cYDiFthe4_0Er4HgJQRhJ2L0N01X7bT8Gg670q1HrjeS4ZUZqJ141Tpd7WyqwMrIXb445qwy_iwPs80pF6cqy1AHMlhuoF5Ci5XVC4NdunIvfWqusBMGq-dchBObVuMw_uys1-bOiVl-oQtfHSHbosrsr8ayyTp9gRVAQ73yGQjodljQJ5bKs2RFvtjIsFdZwAAAbAbPnIIuX1YCXZxB9LBnxOyHGuyXuBhXnCODRWPLAGN9rjOkzk6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUu_r2BeYw2vFThhv1PJ_A3C1OjWsb4RIZUoIkEzWnq_wmZAY0ycup2ctb_TTwH7U_oblOFoO647s1FQEnDdH1AXNBs1mhNCe5oUTMJMsQa-vDIeCmx6YCoiYnb_2vVpxM8mP15_gMEoBCB3UU6xXfKJLnlwU1OmMFwnkaYuBVm0mB6wZMsG646oJWa0W_thdUcGpyt6i2hEmwPBum5osJ6GtbuGoRzJmA5A0zlts3bgcWRAGYB5M5rzDHbckgZj2NX1EEUMXz12JxJK_rg9PPQIT3qomINBD4jkN7BH_wLjAx7r3LcAg0Fix3NFiuEWueOJgrEb7VrA32KUZb28Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY7Wx5mIymwajYVwzisvpfgYxR8T6X44uoNo3458aAQtLol1EWN_ZlYWaEkVuQSrDVtSGyg5GzBLbeyeHy4O7UsEooupXy5DnUSf1CwBP7gWJF5U5-6sxRyJZIisIz4Qq22BgK5ZSTQdSMzSXvastJjzLGryFo8an2RH0lj6xuV-LWFlKE5VAzDQL_iAE-Ws5a8-cx2NsvmJdk0rpPhW9fGiszb8VkYFoDRfq1bJMPdPJcjWu0wJ-x2htDTWK42I4oFgEbbWLzKbNga-tJgzbe5vNpHeiCJ5QebEu6XGP9mP2mthpQchjxxMNeg0KewU9P0ukAYvr3WiZU30rZUTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdtuFgQVM4xvYWR9t8Ncyu6ktYg5mLCxOVTRsna4ZD222NULcQ-WPuihHBlLkhbTZQoOcCl8LaIBKKBfOBpAEVkTV5lwXFnjxGfwNSv328-7--Za6yNaHpMowHNxmMEI1SzyTkOAden_3JbkXWkLPjwDuO40s8T48xk2OfmaJKAViugkAAK2RwgbyGhcpOnq5kitQOVmx9GdL-cWkiMrEFJ1d-s0HEX7zyEH6dgGFPPdHgC9hcTHRWu0K1EC2LYdns_GieAl6SG3pOBGLinlBkLX4lIJGsuiCwSrGuzAibN4gAwNU9Sikf7uBbtff-LfdyxdWplejJF8rhqZRYF3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZjUYWwrWlOsHhpVqb5rt6dJQRRYE4IzBv4K16Ui4P72939l7m-4lz_wrusZ8r3QlQHNyQTlbFoNaQvlIfNmnbP35tvIqjSqG4AsY-Le6gKUjxT8HPlpncKntevTPTryT2phTKVgDXPSc-I-9c1qXSNhUSicfERJE3Rfht83NrmE58NuAVIJQUMdG1jSgUdjLsBLtPZYgQ-UG7_rcSIssFeMli9q6vNKW0khZ9d5AVEv4bgKmTeHm3ZN750UCos5zr0dcOV4wGjgBzalhcfXsxywIG1nJMJVlENs69ubKujfjuPnvb-oju_FqQN8fiHnvf-8TH9LajwnBiK4zQKY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=GGQRTlCHjhcZVdySgVXa9ni60jHwMoWnv_v9r7MV_fjs1Tf4o1bgXjcG_JYgGTiFXHVwRQfn8IF09Q9_v7pmkbzkHyMjlXmV9EK7V94wI2sC2S6lIEf0aSpLnnAN_IZSCJ55-6qU3Dyjk_rXf_fC4vIaevDvAnnqpkGmh4UL7b1YlZVlP22jqQ3Pj3iaWG2RKRv1wTaU9QJlWAu2mC14YRbKRV2x-PHi75Pjq1Re4UYfWTzJq8mn7eXCLPpEU7L0YAcKlY1ALvRXkO_pU8-Lv0p6G_T90gzFAQHm9NRQDhEG72Yov2BO2XKKZAw7XDKL4IEIrmJLONgBLxnX-mvoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=GGQRTlCHjhcZVdySgVXa9ni60jHwMoWnv_v9r7MV_fjs1Tf4o1bgXjcG_JYgGTiFXHVwRQfn8IF09Q9_v7pmkbzkHyMjlXmV9EK7V94wI2sC2S6lIEf0aSpLnnAN_IZSCJ55-6qU3Dyjk_rXf_fC4vIaevDvAnnqpkGmh4UL7b1YlZVlP22jqQ3Pj3iaWG2RKRv1wTaU9QJlWAu2mC14YRbKRV2x-PHi75Pjq1Re4UYfWTzJq8mn7eXCLPpEU7L0YAcKlY1ALvRXkO_pU8-Lv0p6G_T90gzFAQHm9NRQDhEG72Yov2BO2XKKZAw7XDKL4IEIrmJLONgBLxnX-mvoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6jz-V1Z3aOk5zExtpUrls76TIFSOEprS8GiElXVq1ikDr0xWjU38e58VqHMqUpYo-eC4PNdhl3f0sM9kgqrXmSbR6UzewpbmpXOnfkD-uLJ1hB537C86wfFPTYNeB-NQU2AxXStXvjSXxfIHHzBzp2DOo8Rngft7oERztmbCLyo11LNPD26KDQtCg2EYJOkGroicrotIykzr4ilYug7CQiD7Qq9qZPrh7GmI0yvGSel4DWoUVErhE-P7BCw6sN5kIDGlV4gZcTmAC3s0TkyZi4lFiivGHhF2NZqbKQef4C2bMXKj4zgZAr5RCK6mPH_CEyHgOUKAhAGZ7lCyhYZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=P8m9gsT1J6aHQGhEvVxtBHcKrYewymdqxgSyet-KDqm3zJv5nnp5bB3EfnHZJFhRFMsLu8IUKfjbaZ8hjJf1r6uKyFD6mFjArIirGtx2FFk4743kBitl-Me7X6TyiNNVCjAAy7Gjy1DhESXElEWKgRYeShEjwsXY1WKSV5GwgroXN4oDpiD7TvuYq8TALQ8AysrcWR0_LDKwVxVK_2IKpAPO9HED8jb0K0PTqQCMjQcRPJTu3d3o4A6VzyX6Fc5vbNXfwF5VpMtrIFvnnAgx0OSz0NURAXvFZm7X0OJB9zc1GvJEri1SR0YeJ9JWtHiC4IRZsP1LjxhD9831rEA8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=P8m9gsT1J6aHQGhEvVxtBHcKrYewymdqxgSyet-KDqm3zJv5nnp5bB3EfnHZJFhRFMsLu8IUKfjbaZ8hjJf1r6uKyFD6mFjArIirGtx2FFk4743kBitl-Me7X6TyiNNVCjAAy7Gjy1DhESXElEWKgRYeShEjwsXY1WKSV5GwgroXN4oDpiD7TvuYq8TALQ8AysrcWR0_LDKwVxVK_2IKpAPO9HED8jb0K0PTqQCMjQcRPJTu3d3o4A6VzyX6Fc5vbNXfwF5VpMtrIFvnnAgx0OSz0NURAXvFZm7X0OJB9zc1GvJEri1SR0YeJ9JWtHiC4IRZsP1LjxhD9831rEA8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=M0t6J96XCRiZuB6qm5Bv19NDe6LIYY-TdsXmnO1Wcd5OrGwPGnqOP01gwAXAfVWVNRTZRHlJpYAKSL5pHe5NWR7_MuUrXzpBDuT-m-BDSYqyEJEqOfX-qShhTaowjy6JGGjqXR9jgif9kY6uAygPhdGC_waQuJbSkJ_Uj49onorPcV998gC0yktafAUlwD77bl2JkDOhUkWC6pw2sxHVRCtubz7z6pA9CZHfTHC04XF-Md4f9XPVcuUt3QXwTa7gzcBCFTvKHmU3ZllM0_2hV8ScUQZCMLTaH-BhXmHi9XwiWUNmSAge4iNCW7HzVWRmaoHh-6lLOethbpep5k_qJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=M0t6J96XCRiZuB6qm5Bv19NDe6LIYY-TdsXmnO1Wcd5OrGwPGnqOP01gwAXAfVWVNRTZRHlJpYAKSL5pHe5NWR7_MuUrXzpBDuT-m-BDSYqyEJEqOfX-qShhTaowjy6JGGjqXR9jgif9kY6uAygPhdGC_waQuJbSkJ_Uj49onorPcV998gC0yktafAUlwD77bl2JkDOhUkWC6pw2sxHVRCtubz7z6pA9CZHfTHC04XF-Md4f9XPVcuUt3QXwTa7gzcBCFTvKHmU3ZllM0_2hV8ScUQZCMLTaH-BhXmHi9XwiWUNmSAge4iNCW7HzVWRmaoHh-6lLOethbpep5k_qJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRFECvQKXgXAcChFLCt4tZaKe8bdrmuMago2bF9GA8wTFi9WB12xIrr-hAM96UtxdKdBvFQJbvQqdIGVGy4L1rrnf2RthgD8-nI5mAkpcjpeDYrDmISIVEzw53j8XELYGt-qm93Bk3A2w7gu0cxwNyrICwzVdhnsQ2zK_DEeIVDcyczRQMjQnhtnxOU5eSxXwF8k-vYm3aVjnuqmKh7Wevon84gePJTV0nPH7ZfsREhl_cuE4AR8H7QEXRf1b6cNZMKbT-H7drIvzSuP6WmZWKaggW3gqyqR3ZF430c0EhZQ9CS-KYsn87xFwmnOG8I31dnbSaCd2i44OYfXZGe4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=vhWzkmIKFoJo6TRrHkka4mJgfGrNQ7Np5_sR1dK1nANMO2wn6Jy-Jo49x0RdEsDO3ijZUvBh2tQrUQ8mo76QoTpdPRBOjkWM_oX9XVhe1ROT8Y0HQzMsJ1AkMMRS1hHq0StWPnhS1OnkN54RG9ZsyILX_iCKWdjwHlhrLiDTMrUFU74bM_TiugcGqXtelvEZ4HblgIraC8G7jEi-9xjGu6OtHd8ZmRXz6U0V0903j5hwz9vmAN0tizEuDwjul10R6l0M6CfuuFHndf8_ESBdY5Y-Ujo7WOGC6laIQM-MCF_8V0fQmdBRhzqysGQYQ18yRTUFE5ZFB96CqxAOJ9czNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=vhWzkmIKFoJo6TRrHkka4mJgfGrNQ7Np5_sR1dK1nANMO2wn6Jy-Jo49x0RdEsDO3ijZUvBh2tQrUQ8mo76QoTpdPRBOjkWM_oX9XVhe1ROT8Y0HQzMsJ1AkMMRS1hHq0StWPnhS1OnkN54RG9ZsyILX_iCKWdjwHlhrLiDTMrUFU74bM_TiugcGqXtelvEZ4HblgIraC8G7jEi-9xjGu6OtHd8ZmRXz6U0V0903j5hwz9vmAN0tizEuDwjul10R6l0M6CfuuFHndf8_ESBdY5Y-Ujo7WOGC6laIQM-MCF_8V0fQmdBRhzqysGQYQ18yRTUFE5ZFB96CqxAOJ9czNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1G58u6VLMUwmFjC4M8zZNmIrGgrsIq_deY16DFo4Jpv99yfRAwKl-4jhtct1g7mARNVmrkAAh0ZIjZ29REZuw8YgwW1YLBwb0Ux8-wSmQboWFnByfBfcOu95fd_7AAuCB9kMnaaRE2UNmFuGkNGrNRwlHNFYVUI71esHjVRkL4to7Rvx7TH7fM-vYVrlj9WUR6O-iuIU7hc2wiKG7GXDpsV7Wlww6evNJIpDHfqWyCt7Hgl4XSVXN7mcLgiCrxZRwzGZTZgf4ByeBOmK58-g5dHDlbUDp7w5mX509fhMA7wyZxmRWl5sdZ_E-XZwoDSBwhzgzng8vbIC8O-HCYdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trTAviqpvt8zt7FShKDr6ZaWPlp97J7RD6d2p-lJXn2sOWuEG98c8HMhRYNbqMt55NgsFJc4hFS_CGLaXPSiqrKSPQ2--YstD2gbOBQ5zmeWdNO5Hj2z_fmvwp1wyoBEXe1IbXwbmu0KmGopNLk8l3ctyFf0bsZJfxInnGRjWdG-mJtBoIultKLwD0tCVnfJqqCYinx8ba2TChkf758Pj_g451kvLGkgzvEJ3B2BSbIcwfH0yxjHVTLiMcU5oipFCx6T1_LwkblTA4THsqzTUsxf7l9d5A9BdnSJzFohRFgNIDKvbC7aRlJPx3S6rfDJDBS3NitHxu7ddyjc6ygi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=Q8haVY1XrtXp-NueecgB5YU1rqLbNmwtEfgNefDKxlwjBgnr4TgLVUSzaiCQbYSxVx-TxOiaEJJ3aHv9yLANM7EoR0IaTaSRtVgXtqLK2jMUH55RolAGIOBnKtwmlwiw1HTF7VsHgQ5ik9J4set-OsVUG5fA9MQaZJEOkbKphYbb9U1hTUTHmq-Ew8yTOS4RJsfhTJcboqZRwz5JTCm2Dz9h21lPKVtxiApIOMoRejJkDY6TO6mUy0y4K_o5XhoADZgnabSVAlJ2WD8Px7W_NhYdGVgKuYkecnROXuEemoIH6QcPpRdyPxp772QI8PlQrTw549Se8pTcQDW5ufXxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=Q8haVY1XrtXp-NueecgB5YU1rqLbNmwtEfgNefDKxlwjBgnr4TgLVUSzaiCQbYSxVx-TxOiaEJJ3aHv9yLANM7EoR0IaTaSRtVgXtqLK2jMUH55RolAGIOBnKtwmlwiw1HTF7VsHgQ5ik9J4set-OsVUG5fA9MQaZJEOkbKphYbb9U1hTUTHmq-Ew8yTOS4RJsfhTJcboqZRwz5JTCm2Dz9h21lPKVtxiApIOMoRejJkDY6TO6mUy0y4K_o5XhoADZgnabSVAlJ2WD8Px7W_NhYdGVgKuYkecnROXuEemoIH6QcPpRdyPxp772QI8PlQrTw549Se8pTcQDW5ufXxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISo0GTD0mwrkazhMsKk_JjJSQzhyszOZUSzHd_qSpbec7mz_JZHpAPuCm9It2b7rgDrJ12Hd-lgINtceZAwt_qsR0iQbmZajfUmmu1jhsBUmkkl2Ok9nAD3Ub37p0wY-k8C0fC28Z6OnFTclKMAn-P1XjC6jZDOUrTf8tAKbgnFIgJutnc3G6CmdvmDwWuCfmSuhgYcJF6bJqO522J53nIs8DSVxrpbhy2l0k8_yxwuSHumzInTYll3tm_ZxFue3JWDi3v3aJgc_SAHDWYGC5bAGP-XqHmOKUeNadsE-pcvAeBPfxQvciOGdgL8KM2KqRLIKo91RFcYKYN3Wvscn4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIsAGvTm1TvvyuyLzeeY6DIJOT_E3eTF06J0v3wV0T9oP_h4gMzq0Rl0z1pqspI-gl8BqmPHwjcLDt8NZiq7TnvLV7PpYyKYLYMCF_Bq4W8yW0Jk7N2dLOtN00ArlO3s1nd457oNJ9UnVrE5sj20RW8DALxvW-kK-4gZCkSiYmDwY-BDHIrK3MeQdMiXAkDuMEE2iA3pTHKVRUjN3aHl6zZ7GjFeqftUYOvb255AKjTxhqs5ZjCW2kfji34w-yUm1rErFsPQwAvU4XhV_Dp0vlXYW9oPJuclhx0o3fqgWAYTY0AvzQKN00ejvfiI_i21zryz_9H2EBY63fpAmSQGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=e_Ji6JyA3rVQCzPaAFCrmZAhkCZ9ZpRmdSNJeLi10YrrtrDkdG6VdNTILHXQXLj2w1lkZs7Xzq-ZhHtxEjd4-j8CkhehXrFKUP1HhiI2-5O0ymQnfvCLKRDQtm_4f8u3jgeesiFh5HWmBXRZEHQ-SL77D1bEhRb6JmWE9X7iGjDypHw2j0g4gjyJ70fGPKbBxjqAR9oQy4yERaAZYMpaOoaz60mErbAzyB910P3jC5lblDGA8E15V27NpZcUkUb3nFwogBCrxWyJwCanX8HCqS3TPcWPeiRvCIg1iG-uwArFsC2KqMvxYNqRhCbC69V2z8e0ARQktJqOelz-1PnEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=e_Ji6JyA3rVQCzPaAFCrmZAhkCZ9ZpRmdSNJeLi10YrrtrDkdG6VdNTILHXQXLj2w1lkZs7Xzq-ZhHtxEjd4-j8CkhehXrFKUP1HhiI2-5O0ymQnfvCLKRDQtm_4f8u3jgeesiFh5HWmBXRZEHQ-SL77D1bEhRb6JmWE9X7iGjDypHw2j0g4gjyJ70fGPKbBxjqAR9oQy4yERaAZYMpaOoaz60mErbAzyB910P3jC5lblDGA8E15V27NpZcUkUb3nFwogBCrxWyJwCanX8HCqS3TPcWPeiRvCIg1iG-uwArFsC2KqMvxYNqRhCbC69V2z8e0ARQktJqOelz-1PnEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=gRcWE86Lk3BNDOybVWYHOgqO-RhulKIztYre5LqwHZUjIFz5gRj3Mr3rfnGRM2lhNIOukp7Z1N5zZRibi9llk2lKORIihokv3gEy-HAPvaBobkEfbuiEGkFZhNltQCI0Q86JXLcgBUBdg2H_bB_ILudZWd1TU_CD4hN6WRX-6MhJD3PXKDtRNfGOq7XxWMOw3jAYa0b0bJAITNn8CCVFcw3Fb38WVb3npqtjWxPaTv40hOs7adgeb8VIaSPdzynWEVSSTIXv85ELhUPpambN9ynszgab4LsClyWwzn9vg3YDIxn_ANNYJnwIZ7l1Zg-EpaFzcILUnpBWJnSefz3CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=gRcWE86Lk3BNDOybVWYHOgqO-RhulKIztYre5LqwHZUjIFz5gRj3Mr3rfnGRM2lhNIOukp7Z1N5zZRibi9llk2lKORIihokv3gEy-HAPvaBobkEfbuiEGkFZhNltQCI0Q86JXLcgBUBdg2H_bB_ILudZWd1TU_CD4hN6WRX-6MhJD3PXKDtRNfGOq7XxWMOw3jAYa0b0bJAITNn8CCVFcw3Fb38WVb3npqtjWxPaTv40hOs7adgeb8VIaSPdzynWEVSSTIXv85ELhUPpambN9ynszgab4LsClyWwzn9vg3YDIxn_ANNYJnwIZ7l1Zg-EpaFzcILUnpBWJnSefz3CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upwirMwFxQ2MyhlFhBTqTIhYUbhG9TQepVSR6cZlyIBCs1PhFvsnuIJ1-zEP9tb4zNvOv_2gCQgrBqJORlu_vcBbLP8dqzAcSVWZKZBdOpgXsyBkPyVjvALiBWjT8G4j3xz3ccq0UB_J7Mci8Ez45EUjgSXWt9jpThQdjVLBeoMh5s17Ep3pcWWtyCADtcRHdgMfRstkuLXGFW6wGHXKPbfFuu2s4CypAUHhPYfIdEO_pZA3NhQAojpJg8PYfw7ytl1sQik6l6gX6-mOIH70CeKWk8VGGwMsXwqIgzDbR84PbK5Bo_JmcRQwaPkwvOwx7RWJFL0uxAwJYRd6eRpFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=f9gBrim0iAs0A04pWSTGF3XXTBxue0qi-S2ZRyovhEBWrmfU-A5hf2ZJqh5rzrYX4BL2QOAKpAuVOIUKb6PbazPwwtaT2kGZ-JHeMR8v_mtmOg9UoUktI6-8lx82lN1zyK_MGsCiKJGFDdSbMCa4XhAqmiH9H6tfgEgLkUINR91mBZvXPtP-HeKlGbACGFrI3HiW9rIxL8lpvVm0JOFOSm2q1mmuIKlS7mTxZQ31L4XsAgF6QlifFT5-suxf2G-UpKlyNGfxK8zzQGYzC2dPHCE3RFvw9--f21vej5E7wEh9FpGMeYz_3ott0n7xV1ir8WuAVo-AnMBVP80wEnMlYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=f9gBrim0iAs0A04pWSTGF3XXTBxue0qi-S2ZRyovhEBWrmfU-A5hf2ZJqh5rzrYX4BL2QOAKpAuVOIUKb6PbazPwwtaT2kGZ-JHeMR8v_mtmOg9UoUktI6-8lx82lN1zyK_MGsCiKJGFDdSbMCa4XhAqmiH9H6tfgEgLkUINR91mBZvXPtP-HeKlGbACGFrI3HiW9rIxL8lpvVm0JOFOSm2q1mmuIKlS7mTxZQ31L4XsAgF6QlifFT5-suxf2G-UpKlyNGfxK8zzQGYzC2dPHCE3RFvw9--f21vej5E7wEh9FpGMeYz_3ott0n7xV1ir8WuAVo-AnMBVP80wEnMlYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=A3DzjBcA2yqtNtaj-VLALqXPuU8wsAjCB1VI59K-wDj60F7GyvRwCPFfsw0RfPSWZh0qmcbueVYhaMqoyeXd39voQlW_FZvaCBXTsS_tz8fjHdNAgW1HDnjZTpcSmadpQhCk-Lz1CZJgVXwNTxI-xLfSCJQ-BiV4VbCY4pQtIlg9AJtQxOoKXGF11FPsd7xuTjTQ-1VoHdArBD_PaBPlisfQjVT5Rk72ugKMjFILdZn-V2nlhYfNOTU9bBkaSiy_ElkgPTLcZEPJVhOfF9-ZRQq294IrGid7aeCcH0Eoj5A_ynXnoT5Lg-XL7Foi48rFB0dLa7b_dmY3WmfRLUJe8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=A3DzjBcA2yqtNtaj-VLALqXPuU8wsAjCB1VI59K-wDj60F7GyvRwCPFfsw0RfPSWZh0qmcbueVYhaMqoyeXd39voQlW_FZvaCBXTsS_tz8fjHdNAgW1HDnjZTpcSmadpQhCk-Lz1CZJgVXwNTxI-xLfSCJQ-BiV4VbCY4pQtIlg9AJtQxOoKXGF11FPsd7xuTjTQ-1VoHdArBD_PaBPlisfQjVT5Rk72ugKMjFILdZn-V2nlhYfNOTU9bBkaSiy_ElkgPTLcZEPJVhOfF9-ZRQq294IrGid7aeCcH0Eoj5A_ynXnoT5Lg-XL7Foi48rFB0dLa7b_dmY3WmfRLUJe8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=eWZ6bVvfV4OAbdP8lQJriWR63ZY3pAQsZaUcflcbN3TJjduvB1eNTEEBpj0yFym3A29kDuWSv5i3QqeyEwWmyEZ6KOOcYJ5-Xvo_lhi52usVc-IGap9K9OvlMcZw4JNn-YY1zC7kkG3hJsN41GZl00Y0CWc7uwTEFxQRF6G49h2Cssx9ejwz07rK0AlbErmhOuT1M0MCnvIXmpgy3NBcwT_X6xMi8OYEngHm0cxK7xg6a-qNqtaNyi7JY0OKFzhZ9HMkd4PgCkxQTUTdoaHLkzL9bYF1YVOQzzb2G_WeW6gR_OjI0CALvtS56jSl_ia-Y3gofr6W1Yz6zRmstn5T1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=eWZ6bVvfV4OAbdP8lQJriWR63ZY3pAQsZaUcflcbN3TJjduvB1eNTEEBpj0yFym3A29kDuWSv5i3QqeyEwWmyEZ6KOOcYJ5-Xvo_lhi52usVc-IGap9K9OvlMcZw4JNn-YY1zC7kkG3hJsN41GZl00Y0CWc7uwTEFxQRF6G49h2Cssx9ejwz07rK0AlbErmhOuT1M0MCnvIXmpgy3NBcwT_X6xMi8OYEngHm0cxK7xg6a-qNqtaNyi7JY0OKFzhZ9HMkd4PgCkxQTUTdoaHLkzL9bYF1YVOQzzb2G_WeW6gR_OjI0CALvtS56jSl_ia-Y3gofr6W1Yz6zRmstn5T1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GWH4V6QsUmy1FAkqWfvcSaWowB7_ClYZcrj9KvlXRY6eNwCbl1AGtzBjg4OThMJQfkcCdLeDN5hn1c0Le5kHs-8n5OsgqUQTCOIMjRVlrut7s9pPgJpcS8oFRHVE0RUm3zdCzYjEAF3CspyiC7QA41vUjEJ4ctRrtbQXT72jceMLpW2s2WqSs1eLiTfx2QLzNDc4vCq6Y1AqogV3yF-PrMeXNLR648vZLF4J1qLc8GrNRj84WXuqZiI9Vb8n1J-xeYxQ79XO9ihAygFWVpssBqeGcwUKC38Z0SY6owUdH6cPt_m-6dLVBjiDP7vZ3uFdvLH4D21a2Xa8YGdgmySw-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GWH4V6QsUmy1FAkqWfvcSaWowB7_ClYZcrj9KvlXRY6eNwCbl1AGtzBjg4OThMJQfkcCdLeDN5hn1c0Le5kHs-8n5OsgqUQTCOIMjRVlrut7s9pPgJpcS8oFRHVE0RUm3zdCzYjEAF3CspyiC7QA41vUjEJ4ctRrtbQXT72jceMLpW2s2WqSs1eLiTfx2QLzNDc4vCq6Y1AqogV3yF-PrMeXNLR648vZLF4J1qLc8GrNRj84WXuqZiI9Vb8n1J-xeYxQ79XO9ihAygFWVpssBqeGcwUKC38Z0SY6owUdH6cPt_m-6dLVBjiDP7vZ3uFdvLH4D21a2Xa8YGdgmySw-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtFDvg-Q6TqzcXqIrStyPJtP8jj3g5HVqYJxvo_QLIIgqgmmnZ5Yj45hfXGHl2-ISop-quNgcToL2Sv1Ar-aHlCTSVVCxCrt0YOCvja_AiRm0Wf12RfrBRI1ERdJyudGmzzaIrOw6g95-4MpX0Z-I3PhivIR5sw7sg53M5Qc0jH__dmGdlbNsqTPT1QvLyPjUabwFw5dWdEPB1nR-XWfTp9d-Sxfm8g9L1xhRRXUdOJ8z-CzSTUWs1-RjsLmvKVrevrP5Cod7o2-z80lvLO0IDbC0qwzT3GGhYw3uKjw2DCaQ_Adao7p4XgQ3JhQC2kgmlsZDJKlmmKA_yDF9SitHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH40J8m8xPbmrzCsmEOljBkg4f6_jFF1TeVfkM5vVMMJF0qmsSVG5aw3whiCUHVQaZm9bg4W7gFPbY3XdgUkE3G1yGs1ewg_lvyNh0FDFZaQExXIKBLQ5tdBi61lYWiwPZS8Mr4I00PK5e1fB5cEu2V9G1jEuEJ7IuLbKFxr4m30UN_oTu8LWTGcmjFF5OpjPBogdvC_Qp1ZyxvfGbBnnE_VjsE3QKk_QrN7Lgg5Pcd1MM3XxtSi_Owp2r8QkhkurKuHaZWLAQz6DcVDPaSdu-SjodPBRbPYaYoAY1XoBVgNYjinW0Go8P4_X6zQxGQFkh9c4iLKRm1BcZDC3a7_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=l7Smcte0FXctbxk-9NUCurI0c3RhEkXKm3JeRz-IWWvanFofG7yGjxqIU4L8HAk2nmZnSsE_sykcJ_4wH34zbsfnn-GWSPQSCWmHflL08t3uQ40L3sFkCEDa3xvSZkCfdm2oS2ewftBqKiyKjvQzxq6wBVkqc1TUqUj7S_oPgzo0pgPaF5HbZWOJfyUcip2pWgEhwAbloVOGNu2K0gBPX8_M97rkFg_ckxMDButc4RKpLZhDNX8YhchAc0sXYZj0oMalK28gV6jepY7-EXFxQ-FjBTmFfsBqkIeMqjvEIM8TX9u0bFC5PCnXx2kVsqh_E2pdDoqUEkcGmenyx00cqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=l7Smcte0FXctbxk-9NUCurI0c3RhEkXKm3JeRz-IWWvanFofG7yGjxqIU4L8HAk2nmZnSsE_sykcJ_4wH34zbsfnn-GWSPQSCWmHflL08t3uQ40L3sFkCEDa3xvSZkCfdm2oS2ewftBqKiyKjvQzxq6wBVkqc1TUqUj7S_oPgzo0pgPaF5HbZWOJfyUcip2pWgEhwAbloVOGNu2K0gBPX8_M97rkFg_ckxMDButc4RKpLZhDNX8YhchAc0sXYZj0oMalK28gV6jepY7-EXFxQ-FjBTmFfsBqkIeMqjvEIM8TX9u0bFC5PCnXx2kVsqh_E2pdDoqUEkcGmenyx00cqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0QuWZv44JqPBGInCcXkJXs5WbesXby5gVqhcC7hsMaVXaN02XAVgEGVqOABvxYDqOtqwJP1kGyyfgZ7CnLz8wdqqBlaRPXZTMHNYyfNW7Hs8r8gsACDbywQuUMft8Ls7cymIhvGfjwUWDe7iFePOdFrKF_Jb26NWlELg2KZngBPerP--7GmumTNaywikNLPPJKtpFFxk8eHoExjks6RE1DePcmNh1q-Vym3saD1TSYCaRdZH5GSZZaha3srCQiNCXM9BpZnI9ayXXGsoGASbjt9uH5N-zk0_8jyaMeq_9PCuO5TVScSTOFP56gqH2W-ns15S5T7x2wahq2NT-OlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWFiSXnjlpfj7A_Zj_DzlHjALK4MvHZ_vtgRwXdmh0I_ijWBkiLtpNmn9ENFxHc41fbnCMsXBbNj3PrzsnjALB5pt0JzYC6q7i6ILRQ_CVheHefMaiSIT0ydJ0VNJackZB0ZOKlW0QQg3z3QewKvb4o3bZRPISui4AQF3DipxKdaMQb4vgvSwUqPoZKGlkhz6CRIat-2d8R5D2IQ0H3_3ar_Bl54ws-5w2dZP2boVSs-1kHCuI3o692R-QNkIkB9e_Lmnd_5Fwa7EJSN98vdduP-N6s54CVw4QbSNoUWk8_4DQgPcFy2CwVt_-1QMLHX0o8nOEs152vVE4O2eg2ayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izEgkQSA67cwZ3PFILGo4A_AereynejtRNCBpywEN5X9St_fFr8n8If9WFqz_HPzSq9ONrgyNphxtVfgES_dyVqX9xs3Bw1TjzVcJK-QhmkNm2psdcz0uMGz-LH6lyksOWGneC9aOQCxn6uuR3MV1hozJcn4DAzfXFUIrtsCzHX2xN9bKfq99f5Jdznvy6iNclVOpYdC689Elf3sutBeAAAg7tDElKpfxOZ8DXwnIf2oOEXV23LnoCND_fx6ONlaL4jCAeKmJIlmuMIvLsPgFwViCphQud-Rb62lxF09_JycbEKtVrO-gTeQLZvYChYjYuxmM8UNluF_z7Cge99OhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MBufE0elpudQdcoRy56m5KyBouv9ceMQ7Pk-XQ_OsqOFwsaPTTWb33qo5YUZIidCq8Rbm4ue6jqxUbfx9LwEpTrgzHnEBKZ5fmLXKdNCypklnjcKciEBz7Y9GJOuB4aDpTCIVp5AnN66mXOZhQ-Sx3DodA59x3FpQdtjaomoH5Kbxs9O-6_pP-FTwJomSs8vWp4dt0rrC-q-EE0HaElWhsXOPRHcTuxtJbR5h-8KarqCHs8Ka1xHMMs805B2toT78A75hSPY6kr4eqObvBnKIyiNqHrx5OheO4SZJzc-wUoNUBh-DirIhHeVq5e_8WB9Bk4AdMiWDMbIZUihcmGOVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=fnsqPLzB65oYSi9stON9Zz4ZISNoAsPm_aOIMKF-ryK8ir_G0TUJVUW0mdcf6GRDQLSBxg459f69kmjXJ62cbP7p-BDINzC_piRDKvHiw3g4Atf8LpTkJ_yu2PNRNslXYCtoWhJz_kzYacScGiFuWb9X6yj0DF8H_zld_rA39vom5MyPQ2NEUWd5IdPSjq9RNDNe0hO3v5pAE4xTJYfGJv8FqgIvdKFOk1mDuXPYLcRPrsrms3o4pA_T2zttGJcc0_vPJ0cdc5xFabRfm6cVXP-5FVw-3krIyeQzvbulf19ao3rRdlnZPPzQd5VMcokxq7Fg1GPR_PXOhOHLo2_hwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=fnsqPLzB65oYSi9stON9Zz4ZISNoAsPm_aOIMKF-ryK8ir_G0TUJVUW0mdcf6GRDQLSBxg459f69kmjXJ62cbP7p-BDINzC_piRDKvHiw3g4Atf8LpTkJ_yu2PNRNslXYCtoWhJz_kzYacScGiFuWb9X6yj0DF8H_zld_rA39vom5MyPQ2NEUWd5IdPSjq9RNDNe0hO3v5pAE4xTJYfGJv8FqgIvdKFOk1mDuXPYLcRPrsrms3o4pA_T2zttGJcc0_vPJ0cdc5xFabRfm6cVXP-5FVw-3krIyeQzvbulf19ao3rRdlnZPPzQd5VMcokxq7Fg1GPR_PXOhOHLo2_hwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FBKqUyerGgZ6f4Q4VwqL0rJ5llPkwYaavfqcTc8n-Ova_xGW9fqvlfchPAi7RbgqoaJKRckuI3k6Br7YaKxv3WShN87Qx0yTM25VipuyaxSgXpJS7FWYFC0weodkt3v77-xZnvCPJ7Fktzr-wqCeArTm7knermzelFAya81kvmg8QjT7Q3BnNuVLGCxNtnv-7JC74r7UTnkuuxCxwTlBD8EUia9oVOa7KnhBIf2dsNPCQX14UxmpOJzRY3wsrV1tQJnKw2cS9BetP5Ucg1DYkg6PyN5HyDgbaw6ipIYnyb2j9rzny1DNYswaqX1INf5gHZrPx2l1_iAJgrtlSVAWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=mU0AwnmzgNl2L1QdSl9r8-31zLPZVd7JboWtc2_HwZBGs2P6oHlsscMNkrktSt2WvmPZOmFHviLyQH_DGWx5dkACBsNCxP_IQhvZUl_0QqtfJ0kHlfgV_kRaFWOAi7P_0GYXYFSJeait-ZEOOcwv2u3aEwloUDbQKUWUM_c1FQcXQCI5sbnRUOO7bWH2PmU7T7fogkjA9_R9WsClJFFbTVlh2jZS_oeX7BJPI3Zsh2MAk8_ImjjsZXFxUXoTmoWYhchMLt8uRZW45jiS39e64fyMhx1KntomMAOWqgteWlt5eVhUTHpzbqzZgUvYsFgaMfoN8U6ZKy_wwPzztGsZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=mU0AwnmzgNl2L1QdSl9r8-31zLPZVd7JboWtc2_HwZBGs2P6oHlsscMNkrktSt2WvmPZOmFHviLyQH_DGWx5dkACBsNCxP_IQhvZUl_0QqtfJ0kHlfgV_kRaFWOAi7P_0GYXYFSJeait-ZEOOcwv2u3aEwloUDbQKUWUM_c1FQcXQCI5sbnRUOO7bWH2PmU7T7fogkjA9_R9WsClJFFbTVlh2jZS_oeX7BJPI3Zsh2MAk8_ImjjsZXFxUXoTmoWYhchMLt8uRZW45jiS39e64fyMhx1KntomMAOWqgteWlt5eVhUTHpzbqzZgUvYsFgaMfoN8U6ZKy_wwPzztGsZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-5st9r-yfYeFxzq8Rn2WVwBnat0Fhd0OsLmSaRQ0G-IK1z3OKH9uEDTKJUfgpk2K7_cZ-SLHOtyflE0rIpjbg2FrQw-FQqwhCUxBNkSHqokmYdfRHL2RPv5bovFYJ6GvkvkNqJvgCugoHwITdNJW8W07hxuyDiPau6-4KvccEKrTmj9sNht96dEDnUQ-wb264QD7AEXgqNpBVwd91cJbXfn3bBBv-f-kkyOxBC9Ru4dnBhxQums1RQCqFRHkaeTYR-Z6EoKf8v4T5G2-bxbY-igveXQIGAgcdlS3owo9DTSwdFjZcn3whh8LDnycclX6tC0JUZF58FgYjcDkHViTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu-VX_ApxxxRXWCZPYiW6pEByIwPpvVY7fk5bP0RLd-KfvqevVFVdetVHQGa5vZDbvnfSCyvwC3LHqIJnpmbkkLmxKTWEhhJkjoQ-QW-I_SCa1xd9N74ww3jtKQQ403YTYyd56hg57ednxLwkSJeewcli6qYZp0KTdJy_5x8G7FEe2KBtKVdfn35uYA8HPntg1pYeoLXpc1vRPsQZqt-yGQRRphfqQmUjVyA52TxrzmSQSgSHNM7b3L-DHpr4n6VqqXwzMfNNDcX4JxdmsYQjo_xxoCb24U4L6J8mJJLioBEvPIvonYkMgxIJ12-wIK2bnNKhYDjEOd7EG58QkdpWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=dN45BgSmVh8Fegds1_7xJ09gmIG5Uzj-ZXQsaPsE2KmY8t0pvZPg7yK0pZW88s8SenfX2t7uq6tUhS9WKbxg5WytKUnauJV3BAPo5FM5RmKjxPgy-WKsNftDXopQZj2meleCL3K57-wWKl0ZK4XIOjeSgqeBUXNlSpSP571Ko212Ab1GCjdsDaICMS3NSo8hSjGS5fs_ZMHC5FRudho25QQazL9J9JTLMMfDb0s-igQCPCUay1L_H9Du8S9RO5NAjynweyQME5z7_4KDZ1MrRu3zJQQW5LW0puPN1so9QLBLBV9nuzbox2PoSEcRfnMB_a3f5_BUIfrHY_MelX4UBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=dN45BgSmVh8Fegds1_7xJ09gmIG5Uzj-ZXQsaPsE2KmY8t0pvZPg7yK0pZW88s8SenfX2t7uq6tUhS9WKbxg5WytKUnauJV3BAPo5FM5RmKjxPgy-WKsNftDXopQZj2meleCL3K57-wWKl0ZK4XIOjeSgqeBUXNlSpSP571Ko212Ab1GCjdsDaICMS3NSo8hSjGS5fs_ZMHC5FRudho25QQazL9J9JTLMMfDb0s-igQCPCUay1L_H9Du8S9RO5NAjynweyQME5z7_4KDZ1MrRu3zJQQW5LW0puPN1so9QLBLBV9nuzbox2PoSEcRfnMB_a3f5_BUIfrHY_MelX4UBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCMz5PAV_KpBmagDqTvw-tSPXfHHADTYzeF6u_Ax9cvUzx6CXTZwkVHj08RI7QymmJJM6af_ISyNwOSoKuBV2b6yOK-4sT_dhSQ18e_AX9Xsz_sU3LuYv7CVfCrTaQ8HTPHuXrOYeQuEIafioBjdGrAqM716n-QlnJjrr8ZXX04wFwq-AYVmvNwbR096CXRpyPYHO6de_zXNAIr_VciJlr7v7pjx8DpQFd4OQvdsjOoBB0D9Yf3wmPYLC8myNHhOLwBfn_gqDmXdyy5jtZeou9ADmZpufvNFgdPvfLv9f_yjwLHotXszyRE1t1TH3ynBwo56ZKEjJDkRxztafExtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=hx3t7WX3xHNmAo7sCnEe_aDE9MFpgy-jQD6QNybb5gNLAv7jDO6v-GVmVI4wwm2ejLs-PyVl8c_RbpdNCS0drwHJ7UV6qx0f-n-c1yq_OMVIY-iJ3u3wEhB4r_3VerDoAuZWWX2ni5B2Z0l4FFv9zeLO5VBIRtIBJ0lNYkoL0yvm-Mdt0QlD1_IFkNBeeFVn3QJvbDTMsIl18FSQ56yccCgoxSFR1Os3D5SZo8mzp1RFujQ9gY4qG17ue0HVvfSWaITGwFomkkL6d7Aqgws-UIVltNCgIy-BfNpo11KiM6hKT6Kdi1f541PAJMXRyMR1s3HMfOciL5UIIMq3ova5mhrevDUOCxMzTIhL4M0c2fk_JCqFadYYv7R-nFF43QvuTPj0VHUSsI4Ns1TekacMPxtxYlc0i5LhE6gA7Eo-Qx90sIGVPfqJcdeDg4JSKLyHAiiSIuNz_C4-zEIXnUSFc90E1nM_KrIkjxwA0PcJFzy0g1Iy8pAO0DsOaN-dt8CyHILD7riTdWr-A4cKzKXrIxBIRhdbXVwOqqUrAxxvzqWVZaa0DnAGit6NpJ3iN2BhBNQPw-i7eMBrvqanJ6GpJ6fMeG3fTFc44Dhr_fQyBX2Lt9tYSedZlbecfExO41EKeptT-bLBUmsNVqEeWbRACHDSYHqI8AXVKsiJiaBBt-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=hx3t7WX3xHNmAo7sCnEe_aDE9MFpgy-jQD6QNybb5gNLAv7jDO6v-GVmVI4wwm2ejLs-PyVl8c_RbpdNCS0drwHJ7UV6qx0f-n-c1yq_OMVIY-iJ3u3wEhB4r_3VerDoAuZWWX2ni5B2Z0l4FFv9zeLO5VBIRtIBJ0lNYkoL0yvm-Mdt0QlD1_IFkNBeeFVn3QJvbDTMsIl18FSQ56yccCgoxSFR1Os3D5SZo8mzp1RFujQ9gY4qG17ue0HVvfSWaITGwFomkkL6d7Aqgws-UIVltNCgIy-BfNpo11KiM6hKT6Kdi1f541PAJMXRyMR1s3HMfOciL5UIIMq3ova5mhrevDUOCxMzTIhL4M0c2fk_JCqFadYYv7R-nFF43QvuTPj0VHUSsI4Ns1TekacMPxtxYlc0i5LhE6gA7Eo-Qx90sIGVPfqJcdeDg4JSKLyHAiiSIuNz_C4-zEIXnUSFc90E1nM_KrIkjxwA0PcJFzy0g1Iy8pAO0DsOaN-dt8CyHILD7riTdWr-A4cKzKXrIxBIRhdbXVwOqqUrAxxvzqWVZaa0DnAGit6NpJ3iN2BhBNQPw-i7eMBrvqanJ6GpJ6fMeG3fTFc44Dhr_fQyBX2Lt9tYSedZlbecfExO41EKeptT-bLBUmsNVqEeWbRACHDSYHqI8AXVKsiJiaBBt-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=u-KeqXH5V1FMDmYzcOEOhVsg5fr3lBN2FhcXZy6DeXBX1Iefja1ksChn-4FNThGVhPeEzxo3qufgLP5oUuRmnSefOa7cI4qkMVzegJjyPj5g4vX6GyvkiYXuCZljQEH5X3DSquLnMt2N1-4gXBaDvFUqpZkKH9F4Ks2mLj7CtIVNhQlO6PrRakRNy-111z5RRaTUCYJ0Sa4ajxFOBs-N1lG1s-37m3DuhCdlIRr2e8ENBlGd_Tkf_lsjdvqeHOVFXxG1GiT3dTQ5XE57230WKz22s3owhaGc_CzP6eXu_x8Ls2ldVIUWrDDJouJAwqasFvIzspKOFFkH4WHxMdFowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=u-KeqXH5V1FMDmYzcOEOhVsg5fr3lBN2FhcXZy6DeXBX1Iefja1ksChn-4FNThGVhPeEzxo3qufgLP5oUuRmnSefOa7cI4qkMVzegJjyPj5g4vX6GyvkiYXuCZljQEH5X3DSquLnMt2N1-4gXBaDvFUqpZkKH9F4Ks2mLj7CtIVNhQlO6PrRakRNy-111z5RRaTUCYJ0Sa4ajxFOBs-N1lG1s-37m3DuhCdlIRr2e8ENBlGd_Tkf_lsjdvqeHOVFXxG1GiT3dTQ5XE57230WKz22s3owhaGc_CzP6eXu_x8Ls2ldVIUWrDDJouJAwqasFvIzspKOFFkH4WHxMdFowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxkcBG8Zoxim1HUyRLw3yMBCfSVxHRYUkT1Xbk2t_fbc-69ADbC6JhfA5ohqy3Ha7AvGBRHfuHSL9Dyo-DaW_iGCco16dJ6QnWtGyCh7jiYU2n2Y-vBbBJjg98peGR0nBWEFhJo2kxzg53BhdOHlTkwj5cyP_3afCxmAKQ0grkkg0St-gdAH6QPCxtBF3kuRIUOTDGbkU5cEDtycvOZT15tuaQZLq98I9s-bETDGQeHARewVgjEEx9njXUYfVMHllERWbDcfun-UhbwoB9higd3t1OLWzEDkZWSRSvhI3BKFeB8AoP1KgaN3B6_K337TdmsKdAq-9FutZaMyXf5raQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ljkdhjqf8Zk2S9LBs1ZepaeHwChYi9p-_kCfZaqPzWVcWmcyMZeAShK-7cUjV3E6--wMV9Rg-mgpCjyJHOgvlw4GYOCWkeZ7_5Der1d-swPCi9UuC_3jWebkdqw-c2OhKLl9qSoQGNOOXUv9kvCJwcsjYU14bCFgW7ymgiW3VoV_HEVZlfq9-9y3K5tI2GGCtvxA67iQv_Wrg-bzO2pGOCRv0HCFQRSVQtnULRFxLum9cPirH_gIPWvZFtk1Ij75dQqpzvka-7_Ff4lMyohed8SzJVKncKE2W3ccblHhyleLtgO490I2PDyW4gLeRobwSt2lIWzjOEMzx46hlPQy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ljkdhjqf8Zk2S9LBs1ZepaeHwChYi9p-_kCfZaqPzWVcWmcyMZeAShK-7cUjV3E6--wMV9Rg-mgpCjyJHOgvlw4GYOCWkeZ7_5Der1d-swPCi9UuC_3jWebkdqw-c2OhKLl9qSoQGNOOXUv9kvCJwcsjYU14bCFgW7ymgiW3VoV_HEVZlfq9-9y3K5tI2GGCtvxA67iQv_Wrg-bzO2pGOCRv0HCFQRSVQtnULRFxLum9cPirH_gIPWvZFtk1Ij75dQqpzvka-7_Ff4lMyohed8SzJVKncKE2W3ccblHhyleLtgO490I2PDyW4gLeRobwSt2lIWzjOEMzx46hlPQy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=vbqZoXajfJ3p0PfYNjefPlWPDsGbLbGf-L9VHb7Aqn-r-nIsEkeMciSpYqu1uYF2Njd4WGuNMcdDK73W6W0ND8nvkMlFhraXFAmN04egOoSMIeIJboJlG_Ceath-Euzj1HTiU7HLCfeyQL8LXnaaAws7NP_si-EZLdX8d7yJEclZoCjXbgFyj5rBkQiLwU11iO8dr4F761DVtHO3IjTbvffBfDqum0flVRZlPrkJZk8j-cQpSwvjgArju0XJPSKIUylHFjcSTpBeml1Mpb-MPMgIUkjTEEWeqsQCmXiFvgf7Ki_0REs_8mTbVO2C3h96UwLPgV10F3mpCblJTwro8w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=vbqZoXajfJ3p0PfYNjefPlWPDsGbLbGf-L9VHb7Aqn-r-nIsEkeMciSpYqu1uYF2Njd4WGuNMcdDK73W6W0ND8nvkMlFhraXFAmN04egOoSMIeIJboJlG_Ceath-Euzj1HTiU7HLCfeyQL8LXnaaAws7NP_si-EZLdX8d7yJEclZoCjXbgFyj5rBkQiLwU11iO8dr4F761DVtHO3IjTbvffBfDqum0flVRZlPrkJZk8j-cQpSwvjgArju0XJPSKIUylHFjcSTpBeml1Mpb-MPMgIUkjTEEWeqsQCmXiFvgf7Ki_0REs_8mTbVO2C3h96UwLPgV10F3mpCblJTwro8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQWHzQMO_DvXwJdOQaNQmsRngrvWicYnFBnB7otvOp-apYCKA6oBz67K2Z92uKYGg3A8wd43vBpB2N3eqjLisZAI00jLHLpTcPevAePmlfiDB08ytATgrtOZp1NVQ0w7-UqWWrixmMAacGaQfBrnlFnGHV3knl7AHWPqnpXza7v1hy9Ee38AhKorMNt0Rw_ZrEGvVO5T-3XNPPyvRJDxusmgAk6bQL4fBwjNsqTGNM7tRQhqb_YzgKvuzOIiNpU07uqE2KoMVvsqlXkTljX7PNDRjAESWm_ckSlatfSf_RnxYBqBjWRjqxtXnfQMA28U3YxeWNT-wt_RlheDq8iFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kdgxuNjduMcmupigMLDJEYxfxvyYZ_0aGI6Y5mI-Xe20vem3iEWBOBBz1GuneSTKhl-3ff-v4AvOxfShOv-zvheufZaC4RP_2XElaKacQ-3kpdCcd9SNf6LXYZvePlAevgVxkRSkpZV9pXW0eapEBXNOavD_hT4k_K0XKz4CyobIcK9iUXwumXGAbm8JptW0IT2nvDvmu31JJ4Jy9gIW_o0J4ioYpFXWyvscnw9hAFOZnd6xmgJsoz4aHo_M0DmwNhXlSLEZafuBNH6ATGY7gcBOa1leL8rOBd5-O1VZgML9-SwwTsa8t4u8v95_23ZIIqnu94aJ_e-oo-HUcHHVpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kdgxuNjduMcmupigMLDJEYxfxvyYZ_0aGI6Y5mI-Xe20vem3iEWBOBBz1GuneSTKhl-3ff-v4AvOxfShOv-zvheufZaC4RP_2XElaKacQ-3kpdCcd9SNf6LXYZvePlAevgVxkRSkpZV9pXW0eapEBXNOavD_hT4k_K0XKz4CyobIcK9iUXwumXGAbm8JptW0IT2nvDvmu31JJ4Jy9gIW_o0J4ioYpFXWyvscnw9hAFOZnd6xmgJsoz4aHo_M0DmwNhXlSLEZafuBNH6ATGY7gcBOa1leL8rOBd5-O1VZgML9-SwwTsa8t4u8v95_23ZIIqnu94aJ_e-oo-HUcHHVpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC3ZruclqXTa7LPO8ziE9LUn9RsSLqkp01Kp9OOadyIS9cDkGRzGSvTQSOx2055u9jnaLG3zu4z529aiV_RXP0QCqzQ-m2NZRDohKHolRGglb-ABxGkrv44TCDclyzCbqBdTw08i4JzBJvYRnSkwGQrNHGDs7RbdiX5-dnWOYzuqj94kKCMszhaFWl7dapC2aifLqpcegy9vZQa1CaF4CZYQaR2LetXkvgukJH2X-CjPr4GDMXGuBq9z4kC1uN10pdTOMMpc9hWAqXB-rxaE54xGGlupzLFIIGvYymM1cC4Q0Rh_ncnruze2YVUQ6k0fGC15m0I-NqH2vDTrsp1kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0G5TVnCoyNS4kqz1XFs0bxMeersRg_v0_Yf8OQ0IM_vKpwB2pF8xg8NEs0w1_vyTSNAg-p8oa0hk4u9g2pLDTO1lNyWm3McxzMrc_WWiChT44gVGfQFAFfIfg2prXyaytoOuCj2KuCD5I4pARuMh_6hvLSEd-5aBy0l-gKHzmksXR-mxod3F_3V3-FVpUs4GAAsruxaUYgAx51ZF4twZnZAbFGORa0uHgiWv7fKgTtwpVcDs6QizKHBZ8kdTjncRinEYej7RKxtQ997q4v7G3F9gTgzhR39vbnH35t25N97bVjYftDd0sUc0-GpVpBUDAtnzqfzrtzZMYTcJsjP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8kZ-PDT-_tZAGVo9o30AVpVutpwGVDk6ivI4fnEu6Qg-45WC7VUFSjgTp76GE3x_v-q_tjSq3uEcOJwU0dFATVENwsgxuo7y5ALzq9PaxNbWchPz1WKAXxR649V745kCan-S9_ob4jLU_76VLG4U9gYt2OUOmPJFks4eQhbhEIjU2teSnVD8Lw5mn96Mf3fExGoqa_V8Jk-wfBR8e5zoRdRg4UHD67R5n1BaDorVZNDyBhY0-3Q3eKf91TYF8p_pff6f-gD2u19s5vAzzQD1-7tomIccAkdkC-6B93wPOo3IQgqV3OY4LVaMnep1R6infhCtukucd82QNL6kE2ODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWByzJtBio7VyRV9DSWRKfRpOJ9zltuCJTGIQrwftEAwI5Cne_3E8on72ZtA7BoYihtpPpLfXYh6EmKBlG_GPamSKu1NNOHXExHS4GY5XJ5xyZ_DPVrTgaJ13Pudcyohpetw_XnaAC6bIiqTF2h8xdSopyuqffjd7ikUoIPJHV-D7_ZCw73N21wyzVpKPySipduQrrD6-Dazeclj9MdCVCVML78eHsuxnQ_3HZl-zgGBY4-QotV6dtkTIprjTrcuAGmnZXGd-qEtfliht8D-ZWusSGEQud_lZq-ks1EBDNH7hPV1Bx6cx6rUL8lRKPPbHC0ntJ7KISnGQdpWiIDT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=sH3gbasa1eNUTuh4OzoaBB5Kbq147b332pcYLv1tewzSGgzOl0B4N-IaKMTJN2Y8dPZKsaAq6-h_SiURYAh94rvCkb-kd-HRCpDZnQK6kPVy5mC2LnBskLyjF1hCvGcfxAmnGdvnFjaXvbmVQRj7aSPk0cnn5_y7MH52Xjm1eY7WoMWNDqJUbgdspwOp1QZdz7rFxQeu-Oox6rxXSC0KvyReph3dwopWpJ9tv6615i8iJAvEbqHTc5j5ZQIi9wNVxVdDRgUFYFON2DvA69J2VhKN7aeGtyW0b4TWKgsZSyY-D7TdhkUUlYSW1JVF3C9sS_tlJtPpBfwE3iz9RozLyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=sH3gbasa1eNUTuh4OzoaBB5Kbq147b332pcYLv1tewzSGgzOl0B4N-IaKMTJN2Y8dPZKsaAq6-h_SiURYAh94rvCkb-kd-HRCpDZnQK6kPVy5mC2LnBskLyjF1hCvGcfxAmnGdvnFjaXvbmVQRj7aSPk0cnn5_y7MH52Xjm1eY7WoMWNDqJUbgdspwOp1QZdz7rFxQeu-Oox6rxXSC0KvyReph3dwopWpJ9tv6615i8iJAvEbqHTc5j5ZQIi9wNVxVdDRgUFYFON2DvA69J2VhKN7aeGtyW0b4TWKgsZSyY-D7TdhkUUlYSW1JVF3C9sS_tlJtPpBfwE3iz9RozLyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZx3FC8k_e2xJdE7X2fIb-QAbcSbHISUIW6UX-czI8-O_RpR3-RkMhhryYr7oPfa-BnUz6T9K3eeTnBpknqv-hwgFpC0MXvXBSCuRZS3xp7HybxG-cToXbjWItMrKIPOtcpo1ijFe7cVWjG4KCuWPy0zKcYE4gBGup1y6Q5ofU7Sl1QGnQz_fkn8YbYt9rGfGDVDVE4dTGBcdkRgho1ONCcRjpm_gb5ELLXMf5OYHmQXfHveTlMX5W3W687H1me_HMcbwOcoyB5sAeqKhDQhYTO_hSJcnuYq9KQ6Ex-qwWJVrY4m59l1Ig6HzodR8WIAmT34EmhhgBzthOHwSeZ2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
