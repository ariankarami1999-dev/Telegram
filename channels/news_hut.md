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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 15:21:00</div>
<hr>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 620 · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQsmBj0xYdXYni8GcA0QRnpuTBSeLNLLXUIQl7OM1HZpFIaZwQesRkS-yjTj7_1ZHD_uRhtsNggvcHpOFh0Fz8kVru6qAf9Z3E5iz9GCD4xxfCJVLmHXVmuCs8OXGoQTxpknbHoT72GmdHvWR5th07tuhn6yoR8WhoEgvV1AOh-qAGGaWTl9vPBOlyI_H9gEToVe4kyTNCvzTX-IHQMYzYHaDU6EnLZqGNh7apcPwwlYbMS0KPTT2k3b10EnkO8S5Kg3jrIOjcsVDSBi_r2f4DcqCePySaZiTTyrhcpnLehWM7cFZSaDIChw2d5EAdIos9bt_uwCjaXipMOv_99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBhBfOZ2RHAlWjwbjxviJYLYlYScUGXRiWGPYRjyuJfkJJwjtEPeOFSakrseImM-rcX02dfi3QiSCHgYtAPEE0cy3mipNpIOhJ2-Rgw7nntcqy1iOa5_YcbMxGRYaNZ_LSbys8Pove9nkvu-CJhsIuEiVxL5NaVS_oM0IzZiUMTvWw5KFIhVJ2e9hbBAK_p53_21Khq7AXkUFQEXRpQkvBb_OKVHssoQLmPeU1ZD4PJfrx36ZxYlhNNFNbSbvsKZ6ryGW0MdoZZg1TX1QHsDCDCV4teYoq6vGBaQjNFJen9ngw7w4zNB3yxDdJIlZu7xOgnk9caAXbrrg0tcrHSgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7LhBOFsWniZLYRpxwdj6guOJuWwsza91uhlwpxzUiv3kKLdABJ8KooPvYtgy5KwFBmxpvKjrE1XAU3KifajSDtXzQECLPjU0h0lBEjTMpvrnfXEp2cWcWd7BDNpftRnCnv5bFPixKN18V68Am1dSs8YcDj4U8_aPL5KlzpN0CmOLx8vpcjF_BMCuemhvvL5_BA2Hij2-nXMZq-_SNLcNhoSCZX4aR7JgFp7PKlk96GROmCGjKfUQ_kFXgRRri8Boj8UpPGTaUKhpnlMrQcU6ny_EhKJTmAARM5Q1MtgkOFLOpp6KuxcKAFduKifVW2QuyIiNBGxjvnMkauihUPDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-bB7Um9I0KKrCYrGKMWa2lth2iTkTi_Sx3PUR24dMsXUgqtL7JEZi_KCUkdsVbfuAU3XcwWSWRQ6P4wNCjwW-qLALsiGvtZvlsQ4ifzPJjSVTlEdyvgSPGmwkHEW_iMq6pencaEbcInWHZ3E02BPYo6h8d5vtfGMAHdsHpT4qFopiaDa3FmJ7NjYR5q4SZ25WTbVEVGHrh_T2t7pq9VW1yaeH1MBJK89QPBBLFaiHRdJBjC9OYV6eY7U0w9rzjJRK0c3MWTpY-XouBgzAR3iA6QfKCtUpTVFG5GuvDO8rPQWlHpdxcCyKoDvy6bE82Ug1Y1_5elVuEl5o499fL49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0hSuQicpecqXwzUfzH5r44cD98jx-sjsVXBeEEx0QkmdwkNOkXP5vqyzMZmfTPvSlF2YBxFfkFp1qYZyXjHQTLS3jOgf89y-WhiFR8OwTDsO38-eg6A8hETQ6HW1bGX_6Tcu8tLvoclqwOMV80Cej1ljJTz7IW81ksZN-_hSrVV94kxoLp0DWiWwCUWmg9SWHpB60e9phFZ2nt7uzdwCrOMzACZ-pZiqrIi8uhNVt-1k1Ul6Fc4mSG7OCsQl01wJZw9_-c_nB9f61tYv7jYZxaxfaOH59c-E0OsGWlx77_y4ImpzMhjwUVGcVT04LVA8bucyvcSKv9PqNW1fGawUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVuhIjdao7I_bCwEMYc8SEsIrqnS0-9ABpzUHzN-TXAuiwQymijx26L-L8H1gWz6nFEUOg3xhqw1HOJOpNXJOdzL2WEnpZ6uBOvpNQAWgvAfhqlvlToi-IE2IQxibeLRBi2dkrSjIPtbmjrvH4LFMS6x9b7ooSPbRNNjrmZSH6CuD6tkDFxeGKhkvpu35s_wFqqiSgBR9KQj_oCJx6DHd_-qCHS1aXdV7LNZGLRoG5wwDddoDo-nonDV7Ll5B0KjdklBmO5kzkc5iNNbBNuf9hbbZU9X0j1of3EOQ8IsBa3vaTuFtQdLgCfjQykcGvGtMsju7ZyA35DlvTxOghDiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEKKPgpVfNiohvlrOIKKsE6SFovQC6modYnAoGvuSJqOJF9U37nkuegJq6HKJyB0PW5Lfo7SNNt6_gBIMHNv0A2oqoOVXtshb0aWB_E0pLy1wadPkygLwpUGfSWcLYKorF56gZqHpBy6Wimx5F2wMowLtNJU59LOn1Q05tCj1rrPMLjKLKtKYU0cnCJWY8olx20vOvyvEnvwtKTuFAILVKAuogOs8nq8pq96l-SHMwBHjhkZJv4Uveg2a8CGxKdobM7IEjuxBz0OymffSALkVubn2mCQV7BzXSL47CI9ocX6tgsyhzd7WXawnC_-suc4eHSjhNF_YjX0z_8b8TTc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngD7gv2NuqPytOC3djYrzBoihiXRpapJNhCqplkkJuoGzlMhBab2u_8TVDj91mufuBy21NkDdJmzjZBBOXJHd_fxdEngXkkbT1zqW0AGu7u6pj4y6DYjO7vwVn8HSTavaZ_JNgGRxGRlyoSiFmd0VKigg7vHAqec0N-R2MeX2xDsfIQb10DKMKOWqUOBsoFY9VEVtHuRyNNQN57TGYbBABbOxUtNhKwfb3_c9x6qhfcSoKugePK-3l0t7Dl_4lbZrzaReqUvSIH8nx7RxWfaXNG6AbEU-yN4woVMqhfF82HjAr91IRF3eW7YbjnKKKgdT4fAQd8ncZKZ9mu59WJSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUvol7mj4B93Y3sRuzxzXiiMe_pcgrDYPeFMDe414Mc2Ndhl4Yzm1qCEfQrZNK04TCt9QsgArdD_RqKcgwgw9a1HFWl5RbRkxA0nIPQen1NeJlYPzeaeiiyPXNxYT919qozrHrD9LFBHWVXI906hDcn-gVfoyUXoFd1hpngxJaX5A6nP4hToCSS-XlDMFvJ5Od7_8BjdWsQ3STJMe2ogzBwPQnTTvygqchhJPK1gCemIkHlX-2NiifJKCPqpBDmC2So0M-go7qotWFv56K2ZeB0flfUb0g4OPGXVD286GQpuTD6BmZQ9w5B5uebspKqvQmRIn4nnzc0m0Y66XteyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilqS4mK9spCg1frgzqmRfQ_k4pfwq7lsdq24jcLdvFEN1W11qZHhsjSEEQlZ5ftYK_bHqmuTMAAlCHhQZZ4Tcaq9PbiwNBGbunEq1m9oSyCQ_DCPXT5ZTzNxJFAtoC1peC8Iv6WqDbDw9BVfFYs880G0mtSdJM7QmQofbc0GQJy15zNsIGMtRyDRvlSxVikNHy-s5HFGa3FfgVCEbTxM8uhlQkrQx47wRM2YajutOVHMLxHarfdYEe8HWLMh-L1ybpH8Fu8EHzE_YJzcbstVg9HGLz37iiAjgT2xknYdFB3Mwg8_tHFDqlnU3bM562zPVzLMc_O5bq0X9TjpFmGhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqL-uHuLIFAl9nTsPHXDM15qBymH2M1HHdGpLDe0NRpCz0Y2k9SmaqPSN042kps_s6eWiINFmkWXovm8uVJ2DahZbMhFHwv64Xjb2SJf027zndRXDN0gviSNUAVZ4V-q4RT8n43Low5taOy0VjoBXzVV8_aUAjBqFEwo2IlKGT7NzeTfvBdslpxShMGQ87NCoBtsF25qhmWaA3cWIhyD6EVoLibQE2695vir0KNKLkJXR48wUfVw8XswEqYPAfEgFT0GINTCVguq3IULoRKvTAttvftKqzWQWLuSdZsF3LdcHTg_ph4bxH1sJHh7sBC8PisntIwS4MkCbxSRHy-QgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=UURxX4-FFLzhlt1wb62isnNDL-M3HCbIxQgTGfUqiN7mc6E2vKwX5ckbFu1etLdiGutkzeXXhrVfnt0Q6e3xXwlJkLhBrweWmnx4R2fMuLXz2IjNCqNTdfBcLuDqDF1-m16ihtprqxe3ePvMmONYrLHJ9gYatPwSHCBwa25eyAQ1Ek40yEgU7J4XOZdSpbc-n-uHjdmfCVVFMqAO3LMCAVhSfidyUICD0IJNnVe9twQgf4Z4UXA0X1lOIt1oDj1kw0KKLkS_3R41tPviZCAXjqCj3tKQu3uAz9x0lK-FX_0vRQclEDXNxYZ0QAfkEDnpJz0X4zi07GOGPaWMnPdfZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=UURxX4-FFLzhlt1wb62isnNDL-M3HCbIxQgTGfUqiN7mc6E2vKwX5ckbFu1etLdiGutkzeXXhrVfnt0Q6e3xXwlJkLhBrweWmnx4R2fMuLXz2IjNCqNTdfBcLuDqDF1-m16ihtprqxe3ePvMmONYrLHJ9gYatPwSHCBwa25eyAQ1Ek40yEgU7J4XOZdSpbc-n-uHjdmfCVVFMqAO3LMCAVhSfidyUICD0IJNnVe9twQgf4Z4UXA0X1lOIt1oDj1kw0KKLkS_3R41tPviZCAXjqCj3tKQu3uAz9x0lK-FX_0vRQclEDXNxYZ0QAfkEDnpJz0X4zi07GOGPaWMnPdfZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=cCHjwiSoXXCvl6EEQxbC0XufTgeQsLumDyOoZA-jiNnGwQjCOsdRmrjJ8wGnVatzg3VSB3YDQESpn06fb9FeTc1xhNSK0gKd_9xrqVOR3IzOMnEj6CzQxYnkiqUqTA-z-VPZYnCWaq6-h7GhIXPlRqg9J__IUmCeOrQZuSg3iE1r2xDyWI4i3Y0NiOqgVQHtx72q5-P1aG-y48m-6vkg-ONuEn473pz9aPqTC8nVM5zmJw232-3KBzc9xBk86PNJgh-SoBa2SOGiHflLDMkYGO4iP03dBeVvH1oDcztLuIDlJ9vW5lS5cAuMFt9hB_N7mTHFO5DcYyYNFVvQJoGmNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=cCHjwiSoXXCvl6EEQxbC0XufTgeQsLumDyOoZA-jiNnGwQjCOsdRmrjJ8wGnVatzg3VSB3YDQESpn06fb9FeTc1xhNSK0gKd_9xrqVOR3IzOMnEj6CzQxYnkiqUqTA-z-VPZYnCWaq6-h7GhIXPlRqg9J__IUmCeOrQZuSg3iE1r2xDyWI4i3Y0NiOqgVQHtx72q5-P1aG-y48m-6vkg-ONuEn473pz9aPqTC8nVM5zmJw232-3KBzc9xBk86PNJgh-SoBa2SOGiHflLDMkYGO4iP03dBeVvH1oDcztLuIDlJ9vW5lS5cAuMFt9hB_N7mTHFO5DcYyYNFVvQJoGmNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbe_dp7zHRFNNDnTBZoHT2eXPCxYqwcRkwVE3_syVHsYxhr2BQ5dFPyQGCF6m64fDTfodS1GXjneaQU1mG3YrgM9kklmfRkk-QfjazTWlFh0PeQieiNpSy4nuKC3CcSkOPbXbyR86pDRt8HVY2jX8gvC1j3scZBsHw5Z7pCqW4rcaISCNzCHc1YUY_YRWT0LmtuD6nrEd8h7shxr1HjSHdjBqTAKuzi5Wnp8uS2t3LElCT4foA9mzlfbVLF8lRdvWY34tJ-Hu3_WwfrygrQ2J3ExOAG_qTfUkvFXUpQXYOxPnZF9mI_VEuGX8kYBMBSIAfj-9H_Xrn_Dm5llSFe0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haAOXZh6kWDgS4tboQ7Y8OnvDm8OAhUHGr-qf-SYXCn2ejHfk473Jr4uYD9-p8L2E8oOFi4wK4c2W9IGDXLYrakvNF9wFGmameBpL78BVOgwlHaeU1J07QDw5zIv2rhADGTTswaFiJ1RpHzOcY05q_u7lYPMCtfAnPKbF8bu58iBlj1Rrqz14hdecyXhw2R9lZwidr-KFrXcYrd0gpa40nPqwyO7hwEK_Jt0ki17CtZYTQD6DK2d_PTQ4v9Vd66mkHVNOIWCnlUkjjPT2IvbrY0Sa98O5--2xuUYAKRuyEb2WVl3W4ClUjr1Zl-A-dvCTFIn-arJlSaahjcSlL8lzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7BtDyfp6hSElikThoYJTG665AzxTHeyqYWMv_h0pHAOsp47XvC-lekX5EHYxmE0oaRohxntyir34ebSjuqU76gdqd500g4Gz9-dBvAvGMjYIZnJEt7O2ywOOYw4J9LEVA4nZc-8u-v2nRTCBupsCeSsywjK-_CXGGr6fx-ldC5ZTzBwjQAIEQ0UTo_BHjNRPs_v2hn9pngb7cbR08cpSkS94BHHQJbcmST6tBhDj_BM3PNPPPn2zQhKgVeKqZiGZR99S2Rx1eP4Zns8ekFr4UYIKspxufyX1zbbtjkl-APw59TBI8XP0ZTzcOZv-eXlsRRKn2kEc8dLbTeS7fOwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=mOtiYGS-fmXXsV1tAG3rru9CSbr3o_1fXZmC3cC9f6MpEmGzLx9N0C9vCZLoLdzSvfMW9a6i-_-_xO-5Hy1fBMmw03D-VnrnfVSdt1CJYICHfTfu7h9w7UegZ8PODscObnVk0R2tddrjwBiRHJvTvXF9eSHOTgcNRoMllv9WEqKAHsPqT1BanVssmt-5gX890uUkFRMPqEhJnSK4-Lu4KpLkMd695eJJASkSJZKbIzujolQ6tQbCd5gPRvN_3OZrTqeLaLMNvuM33S5KTTEngFl0vUYMgTp9bUhwnkgzXeQ5INqht1D-c6S8pv0bSdEZ41k0PLvcmxqpf8uFEGFn1UmFsZI_dcyOWQ5sZpsOzZj8oJhPV1gxtfX3fKHUdGddDATUYyGM9Pweu4RG5F5tz5h2uCimFSUT2b-T7QfoLZiRDiyCjjpP24uNWQUSUL0u_iyk5Bcjb7d67YlBvU_TiaYzm2lZ1YfRnXC4ihURyIky_3C_by8uH6RV43xl4cIqavb6h7E4MRDZoyZK3wNjVpPe_nFF7R6AJUmNezvsjtN-S9F6AMDucPRSReZM7Gnbm-agRC_jdh9lLr1mDLPV5Aim1bJ7otuoVDZ9dEFiTf0i3A3T9fFjP8QYYP_K2q8ldON9r9lZFStG0PONoKT_xcKv4et253TC_N9loCmwRWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=mOtiYGS-fmXXsV1tAG3rru9CSbr3o_1fXZmC3cC9f6MpEmGzLx9N0C9vCZLoLdzSvfMW9a6i-_-_xO-5Hy1fBMmw03D-VnrnfVSdt1CJYICHfTfu7h9w7UegZ8PODscObnVk0R2tddrjwBiRHJvTvXF9eSHOTgcNRoMllv9WEqKAHsPqT1BanVssmt-5gX890uUkFRMPqEhJnSK4-Lu4KpLkMd695eJJASkSJZKbIzujolQ6tQbCd5gPRvN_3OZrTqeLaLMNvuM33S5KTTEngFl0vUYMgTp9bUhwnkgzXeQ5INqht1D-c6S8pv0bSdEZ41k0PLvcmxqpf8uFEGFn1UmFsZI_dcyOWQ5sZpsOzZj8oJhPV1gxtfX3fKHUdGddDATUYyGM9Pweu4RG5F5tz5h2uCimFSUT2b-T7QfoLZiRDiyCjjpP24uNWQUSUL0u_iyk5Bcjb7d67YlBvU_TiaYzm2lZ1YfRnXC4ihURyIky_3C_by8uH6RV43xl4cIqavb6h7E4MRDZoyZK3wNjVpPe_nFF7R6AJUmNezvsjtN-S9F6AMDucPRSReZM7Gnbm-agRC_jdh9lLr1mDLPV5Aim1bJ7otuoVDZ9dEFiTf0i3A3T9fFjP8QYYP_K2q8ldON9r9lZFStG0PONoKT_xcKv4et253TC_N9loCmwRWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=R7dsRHonoV1F2YcxgQYDPwIQlNBitS9FahcAT9mYuomze7Z8TJfJU9kUf2h92-qtEMQhzOIueWA-Js2sIQg7zqOK1225Xwndazjpg6JEy5B_jpyTVOtNDWcwv-BXZ-oMAcJnBq_y_wiezP4KFbjvF6A2OxBxXvCwi6elhUE4fqkoDQE-CjFv3AxuGc3jAHG0ZN-axZOKPibAEoIkwn3bDh2MxM9vAR1VAPyc-GP6lvdOsk7gsT9h89OEXSZ4N7LIKjy9YUtuP8-klXMaAq2naaMp1FljyOU7Z32_qet2Bw0g4vMAlbZJdaImavYUoLNz50ORLLZkltqKj7jnq9o_ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=R7dsRHonoV1F2YcxgQYDPwIQlNBitS9FahcAT9mYuomze7Z8TJfJU9kUf2h92-qtEMQhzOIueWA-Js2sIQg7zqOK1225Xwndazjpg6JEy5B_jpyTVOtNDWcwv-BXZ-oMAcJnBq_y_wiezP4KFbjvF6A2OxBxXvCwi6elhUE4fqkoDQE-CjFv3AxuGc3jAHG0ZN-axZOKPibAEoIkwn3bDh2MxM9vAR1VAPyc-GP6lvdOsk7gsT9h89OEXSZ4N7LIKjy9YUtuP8-klXMaAq2naaMp1FljyOU7Z32_qet2Bw0g4vMAlbZJdaImavYUoLNz50ORLLZkltqKj7jnq9o_ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6CWjiypXGzXQ5QzshZNDrTTDfvnLDnBREWPQtl_K0ND5GWZ62M0-eX5TjPx4_okDrs74X8QP17ElWcjOuoElWqtJ2lCj_v1ze0oY8A-cextDVzro-v6ymdeWd1TQO50z-5k5o5d-DU38ckWctPZ92Jp2DqE08ditJIBAjn8eWta8QOgsNDwjtj2G3MqZUXS06qUcCRgo9quDPwXK6LiVntS9bdVsRDifHQJwKuj84WeaIXMkF1xSRHLnfNO8-MukwIP9bk88DMZxQVjonvZTy9EIIph5F87N2HGZZsGS8Bjc-XMFXiLxTXVVp-ad-SYwaqy4lBLwOviCW0VbW7SeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=PsfKuHA4AZUGm34GOLL2s3750G4b5Iq3iY1NVIPvYgQJ-HqZvrpNKJHvancArS2WUE3mSuaJaKuihSgASA4umIAmRJp5KxyqrL3Escb9dFbWbXoxYcFVVK_wspPba3wIgLq3qQkHIb2WoN_QRjzXy1HRYLFk1myvDwYxRoHz7ETVIKagwMjIDdbIoEjfvMxXYWa5xTZUITUn9ezkFA_lOrux9Cg7gwLFtSNI1HloCKNFZdMVBRZi52yk-gFdsLEY1rqjmVXa2GLC5gAVuoRg2p5ZCasTOuBlLbkwhAjSijVRQxEw1vGqIhRUHICzuQCZmkFaW1s1xznORU4V1X-fEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=PsfKuHA4AZUGm34GOLL2s3750G4b5Iq3iY1NVIPvYgQJ-HqZvrpNKJHvancArS2WUE3mSuaJaKuihSgASA4umIAmRJp5KxyqrL3Escb9dFbWbXoxYcFVVK_wspPba3wIgLq3qQkHIb2WoN_QRjzXy1HRYLFk1myvDwYxRoHz7ETVIKagwMjIDdbIoEjfvMxXYWa5xTZUITUn9ezkFA_lOrux9Cg7gwLFtSNI1HloCKNFZdMVBRZi52yk-gFdsLEY1rqjmVXa2GLC5gAVuoRg2p5ZCasTOuBlLbkwhAjSijVRQxEw1vGqIhRUHICzuQCZmkFaW1s1xznORU4V1X-fEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=XqAmi17ZUTB5a1OeLbdbnMDaGTTL7mCYMeFO_rntYjkaqF8I52o1Fl89CeeHDxbU8jrria02S_Pxbb1u6ySvrcnP-jCTHaxoEQmivmkRerv20IewHcfqq_drViRn4G2WALIgBMd7WAKpChSJF1toi7WCAimYtsYJzCXTJNWs1Hmjm5Z8A9j12XoN26BFWofHdU4MjAvI6mSfMcnoinEWfcp8hiuIAdkQV6YwDAM_gFxzD57wHWy0VEZ-4QS3zNne5EpfACNt_UyaL0i7c7RKQAgZovnTBtfYrnu-fN0HneH-mY5pkF2c8OVWRTAAZ6GRlpzzEv4nJUsqZ9lcF-PRvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=XqAmi17ZUTB5a1OeLbdbnMDaGTTL7mCYMeFO_rntYjkaqF8I52o1Fl89CeeHDxbU8jrria02S_Pxbb1u6ySvrcnP-jCTHaxoEQmivmkRerv20IewHcfqq_drViRn4G2WALIgBMd7WAKpChSJF1toi7WCAimYtsYJzCXTJNWs1Hmjm5Z8A9j12XoN26BFWofHdU4MjAvI6mSfMcnoinEWfcp8hiuIAdkQV6YwDAM_gFxzD57wHWy0VEZ-4QS3zNne5EpfACNt_UyaL0i7c7RKQAgZovnTBtfYrnu-fN0HneH-mY5pkF2c8OVWRTAAZ6GRlpzzEv4nJUsqZ9lcF-PRvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkdCj1yYCq9dnoO8h9aZK-F-AY1VIa5d3snoXOdymOZx3dsxYfUG_fZFMFl_vntiHwXifLs8bhn_N0zX4vaXn-yFJ_wEpD_nWYEv_nhZsqrE1HbQldBZ9bb_CPsKOFpckTocHXKYQ0V_GS5eeUSYoYngfKTZCvMtpP20IqB28_olSIeC-nS-eXCX5PvPvnFQPlYoCjKBVCaAXowHcB_cSGvXPUfQwUr1DDhA_4QzN-DPU-QQTUsWmwl-qjxV4RHEdwwA_t8IefWZsrwMyM0dDsPUPY7rdcFdujRaM9RYjbmdPTLPuu4xTl5pkfBN8XpxQCeE92uGoO5-dJo1nhz81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R73cotSOaHuvCfo9BUjBwlKWxEmTABV65rzyR6DiSkKF5hVOvTbhRC_b3iCj3czNcCGmyiqRocgoFC-b0X24Ew4DJRq5ySyDnBKczN79kJtC3fFXHx0whk3C7GVPBnboruuplQSDbBE73sA-027DuHG9ak1SfgH2_WwTMvAE5G5R6IhAfI5j04R1pPNK4woDA1MVXQ5QbBjQMhjtOxkzkjAMZsYv1wI-c4bzNl-00ScmChdEmFRMttbAr8rjmeZlgmG3yq271tJgbvzJw2_e1ZakzrrhrKnFNp-LHCzAFuxlQkqZyVFHvuMxmW59c6gE5phVQoolJ9WeIDMBfMYQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbHtDvpmHEvi1AMeUSD5MDxw_NPJi7sEJET1yrxsSyGkJUnw540nQkIfYH5YddH1lCKiJ7_FQPQsjxE9yYcJL2BHKIUjFh4hNS6MoxvDUYuW8iaO2YlxrC1dp3gTAgacobl9RIAc1zkBAOsjFtjkArDV0ME74nM9Ct8mihyg9lmFHrGGx6l5-VSnRc57o70JbmQrtGrk3h3s9Gicr5DaMb0m1PDVwRG4_b0bkvnZbWw0asDjcKZGM-PG901R3dxHMlsYzERp9MRGFuE9DpFZfX9nDbUR5QpWJ6cUwR3F049B9AEfZbeG6TNCy1JQXYgrtgQ7ab9x3FiaLxOIkXcQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmOxFKTGWTP_ImVZXbuKafd-MdEeDA9OP0LTlvxoiS3xJWXiLTHt7lmwPBh9dKG1Hc_moX_28NXyC7ZtTd0qNsvxyFrcuZ-FH_XlqhBamVb8iG_zg58FaiT7p05wguWGuWDZksK5swS4Ka8c5fqvMyeCWe6nqEHTdUAV_MR8zeqYvYYTIQQ1aF1svr_yKVIfVKNsPFqgUIESVSgULn-4oePxt2WZE383r5Z3D82IY_SVS15nqwfUZqAylLnXSTqdIgwTnGLSOcH_hRHuK54NJZhUlbJQ5MDBpnWFR9wUl0PgMTlxthqnvY44I5_MiqJSB_erijqQNiJE7YLAIqFrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=J0JdcZHjAIWpxA2DBW7SOOzYK3iYtAQL4OjeN10EClzEKZJJhCkklNmdOtAUxHY8GtgUvOmsHx-MwYeZvf5rGlPshKyQsS-TbNtbA5vT_3xgReEkfM8nUUOVMbrnzsSZPc3XiEEQAed_7YoPQUB9eerQ1NC6KfcTEVckQcHNJ4-DyAdXvXDz_5Oe5a3SA0xKz6HN5YK_biywotj4eVbsYgK3yi_XvR56ObaUm1tX3PCV2QS_ulM7tmrhH8NSQgqfrhG1b97_JaT85u7LQlivZqauqLJCsEnB4DVg6bhCf_KCynk0TGbIS4yJxAfUWqnuQEQXwun73_9KZOdOPvSsfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=J0JdcZHjAIWpxA2DBW7SOOzYK3iYtAQL4OjeN10EClzEKZJJhCkklNmdOtAUxHY8GtgUvOmsHx-MwYeZvf5rGlPshKyQsS-TbNtbA5vT_3xgReEkfM8nUUOVMbrnzsSZPc3XiEEQAed_7YoPQUB9eerQ1NC6KfcTEVckQcHNJ4-DyAdXvXDz_5Oe5a3SA0xKz6HN5YK_biywotj4eVbsYgK3yi_XvR56ObaUm1tX3PCV2QS_ulM7tmrhH8NSQgqfrhG1b97_JaT85u7LQlivZqauqLJCsEnB4DVg6bhCf_KCynk0TGbIS4yJxAfUWqnuQEQXwun73_9KZOdOPvSsfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M64GctS9v9DYt53wOZVudVt704dxvlz_hDEVYKuDRW55h6YiyykFKzFnCbPD51UDv3tCUKfZpo7hZAIG7pcROnjChiJFK19b3SOiBZVCv8xCJvXMFFVX1luMgIDTGeGKcmyDVPwBxX24IXOGftc0XtHoNYabceknI_2zLi9Kd07dD84e3_MUzT5p6LKEAMzHWxVY034xJs_oEKLfIl7qOlm2Lt6qEc35ofNMhFDy8PRKsxIprH7c-Zot45l-yFHk5XUAJm0liwmMOX_cy9ZcSwlV9koI8lcFLKx1-wHVmfcsDpkCDNsv13IoirCjJhMXYZDFSA0so8LNzKF4zC9F1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=phIEtL7Gw78Ik58sOKR-4NzYuttTohxputGUFIWzidWkK7Gc_GDhcb3zOjQftfkYae-l_D2ZcQtt3XuLIzY9J0ehGQGtkUz-jcXISZ9fm8NeKUT2moIsFenK5GQ9nmxl577-q2-vWJTlJ4avlRPF9lq7uH33huFBzvjGKHbs5uf9wJysw6827sERI4cWjiQSz6uZCv0Ak8joWAFwoO0zD0S7Vygf8Be-Hc7jmgbmpzyPfbogLrDg7clht0jjKLzjs5H5RBZoT696ek8_hUYHMKQPI_1AMCJS5FcNvG5Me9M3bzzomTN-1X9IyfR5riYw8zrYHp7WglfYGUzuvrsclA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=phIEtL7Gw78Ik58sOKR-4NzYuttTohxputGUFIWzidWkK7Gc_GDhcb3zOjQftfkYae-l_D2ZcQtt3XuLIzY9J0ehGQGtkUz-jcXISZ9fm8NeKUT2moIsFenK5GQ9nmxl577-q2-vWJTlJ4avlRPF9lq7uH33huFBzvjGKHbs5uf9wJysw6827sERI4cWjiQSz6uZCv0Ak8joWAFwoO0zD0S7Vygf8Be-Hc7jmgbmpzyPfbogLrDg7clht0jjKLzjs5H5RBZoT696ek8_hUYHMKQPI_1AMCJS5FcNvG5Me9M3bzzomTN-1X9IyfR5riYw8zrYHp7WglfYGUzuvrsclA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=Giw_4GwGsJOb84mmm7MvegDswPJ5GJVRRrLM6sEKPPx4SW1UyQdp4DR6Xl0Y6Sqv_rx4lNAtCrtN6EDqsjVLZHsl-HLaaZCy5X2xS6EpgGWM9D-t-mgjuLYmKephUot0Q2guejbRquizChjOYXr1wdtjTMH4mBdsGePwla23ae7GLlhw50LpWp1Uka-d2MW_BN0etTtWnpgs9ThgewpV7-67kMtjgJQv06wcJty55pxVv6v_-Ou-RlKP4PtaLt25qd0dwHKAko00Hpb1jBmKXwTf8I3oNcQHSMkRnAa7qolbF5Tj0wDXS39xzkWjfaYRgRIdhyI-QhlxYFRiLx3F1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=Giw_4GwGsJOb84mmm7MvegDswPJ5GJVRRrLM6sEKPPx4SW1UyQdp4DR6Xl0Y6Sqv_rx4lNAtCrtN6EDqsjVLZHsl-HLaaZCy5X2xS6EpgGWM9D-t-mgjuLYmKephUot0Q2guejbRquizChjOYXr1wdtjTMH4mBdsGePwla23ae7GLlhw50LpWp1Uka-d2MW_BN0etTtWnpgs9ThgewpV7-67kMtjgJQv06wcJty55pxVv6v_-Ou-RlKP4PtaLt25qd0dwHKAko00Hpb1jBmKXwTf8I3oNcQHSMkRnAa7qolbF5Tj0wDXS39xzkWjfaYRgRIdhyI-QhlxYFRiLx3F1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIzUb--KgkMj_fx6M2hYK-YmUiOjtza2TUBgXNkMGj0_0bGgq6jlz5LG1mdIue6zqnkp0x7SN2lDFpy2R3bxxwjN-3ji6AtTV4ezRZcXuDLLeVYjvR1a5WRU2XxuVtCFk1QJ2dqhY17zvz35IX8LdIq2AYyM66thGvQpUmSomMY9vYV2xQOHFLZCdvrknGIkJv9H3_mSHuWDn6bnEjdUrixT394a-YxtAj8sTMOj8cSqL2RrXZxAzQAvi0QQryxCyJPDklRTEUTVbUNR0QNScdsJ5xE-_FASa9VkQsG8JhrwrqtF4ZgkWnAi_1p0tlW1XityuPn-KBo2ygp_9UAM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=ZJDL5qgN9A0Hp5UaSpz-oRzMe58Nm0Xd2PmoKZuhCeImoV1wQSsWmfrtVnpoBsh1T_5KjTS9MvFSw672cgHng5sjKCw2x0fk6cOGUMqCULO2Y9MG8aySiVwHorLFTU1Hq2NRhYjUcE8Qz_8J3AGmOsrW2MzDdTTJQ47EEjaB1FfUcqZXdcCYmm3dkSW460lKUHGoEhIH-tZUBTCDNNOZFOxPqQhgvnBe5vdIa5p8pxZ51eqLSQdyfRowMyTn0PYNge1rdHdl8dVf4JAULNg5HYezlMiLcRD5GQx6E6DeAJVe62wrJgwWrN0gLlESfwz391gZ6c36tTDt_DOlnWtpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=ZJDL5qgN9A0Hp5UaSpz-oRzMe58Nm0Xd2PmoKZuhCeImoV1wQSsWmfrtVnpoBsh1T_5KjTS9MvFSw672cgHng5sjKCw2x0fk6cOGUMqCULO2Y9MG8aySiVwHorLFTU1Hq2NRhYjUcE8Qz_8J3AGmOsrW2MzDdTTJQ47EEjaB1FfUcqZXdcCYmm3dkSW460lKUHGoEhIH-tZUBTCDNNOZFOxPqQhgvnBe5vdIa5p8pxZ51eqLSQdyfRowMyTn0PYNge1rdHdl8dVf4JAULNg5HYezlMiLcRD5GQx6E6DeAJVe62wrJgwWrN0gLlESfwz391gZ6c36tTDt_DOlnWtpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTv2I4U6Ij3coqyS32LAnehObBctKJhPMxfNOenxfCFRPo0BFroTPkfhgyyeHAsCqxhZuz44lBCCK8YpK23rR4OMW3VTf3-Awkv28Dr_tjXpbcxeRJIDJf0RVWQ6GjqgVKH2tztmPjAMyTnSTFqCd7ks4XQsluYbrvKMy1F1SuKDEWB9uU182EqoaXs1Ldkvi9erGnFjztVU-kM8n3vsmNBJPa1noBTXwu_yQ3G-Xnr4Zgz9t0w8LXFmyT9p-TubSER0omyMSGvLvCkrfTVqFD1cAR51FqCPRuLhk2Yos6hZfnnEzugBiOnvGaJuhLVOtb5LprkEw-Aegq6vH1bz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC8Kn2xvn58V7PaQp-63ODc-0FupJQAJBhCbQglfBKz79gaY4YluFlrb9y6JxOl6MI3_-ZHYpNXbMWOD5Nw-3jdcpB0rnDZWZYNjDWAJT1sHEwmtwuFXkbD9TVuLSMZczcNBrhjfKgSRyRv3orxMplyRuiLnnOP1Ba3qrLw4U9hlyf9xldo6vQyWSbWYvevjaXFwtDzjxpUelBbveaxn7oNQUx7ft_NFs6XNijaUiDGJC9PZFaj3IuNgddHcza-V_8gSLjpYCzT-3F2gSP3fy3W6-Ho36Bc15lRVWKfTB1QHrAC9berI8KStrXIzVfT-qVenbfBUipswqnT01Xb0zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=ReGnaO4CWTclaPOYiCNfzTjQqyIDW_mBDbTtYhDmORApx8o6oH9c5U1rSkqj_dbRj2NMX0vT-3QyahCy_6bNMHwWrbgBY63nre5bwjdmE0T-JA90dgPCnk3ETOqSPNj5zk9yX4bRimVp6lDSoUwoyHzD5H2Q6i-EywKuvzc90NCTGWbHzKFTLy4VXqDORgpxskXTGorY--pU6-gHSrX_S_wc57kIBO07fXIviYOsQms1j8d-GsxO8c3SMEtl5_7xhJ4agQhoJXra6aRK4dlKNZJa0mhN01GNKI1oUALD12Ay39vOh_W5Eo8zvTUmq5HWqOInXM02lswXFMawojhf3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=ReGnaO4CWTclaPOYiCNfzTjQqyIDW_mBDbTtYhDmORApx8o6oH9c5U1rSkqj_dbRj2NMX0vT-3QyahCy_6bNMHwWrbgBY63nre5bwjdmE0T-JA90dgPCnk3ETOqSPNj5zk9yX4bRimVp6lDSoUwoyHzD5H2Q6i-EywKuvzc90NCTGWbHzKFTLy4VXqDORgpxskXTGorY--pU6-gHSrX_S_wc57kIBO07fXIviYOsQms1j8d-GsxO8c3SMEtl5_7xhJ4agQhoJXra6aRK4dlKNZJa0mhN01GNKI1oUALD12Ay39vOh_W5Eo8zvTUmq5HWqOInXM02lswXFMawojhf3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxXmbcKipYNheJ5NuGpVTpRmhWIobDkm09Sx_6_Neu6oaIEySu3vysBFYHEGrqHeufQmMaiuYn2qJWJ5RXR69ivI8Mi2f4iXbyys75eXHr1YPAFjgR7ETk0O94ls0xj5w0fMOnN3qOApxWy2Psu2Q7GtPJAjM5dVMATdV-PDqLAgofuUflJzYVTQh46Lkay7yDQmJN63vUvob-KwUanKeqIVK6P9KzO8flZPkmNdMXU8aVakGiStbLUo_RpRFRf1zzNRC11XcHke13Q0PJtVMA6uPWmcJXOu2xtaCqQDMhr5Dem5ZEok6GrZ0MtE1CC0F6h86_0WfWXfitPoxNrVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhBypXvvp8JoB0uAeykPZaTbfrdUHdHuGJRc0-4oNrc4b_ajBMrWafkllkEXGCOWlnesg7y1cG3sE6fNs2U3YLMC8jFAUw08U6Y2RGCL-3oZxubN5rvauzumBbHCEOAML5lsdri6-foqOJ2b-s00XYRZp3G0DQGCBZmOwg9ozGPUk2fIXjjUJ_1j-X8wwVMLB9ytGgDQwUaW9XIt1SQeAmPDi9fcIWXRHsUrYpxte1pifrR82hSuZ5tZcGQ4ER9jxi8pr6Gf840p9qlRGVXF66lTcPj1XtQWYr6B2Kahg3C0ORFUwwfrwajWVBKK5B5LsHf8MUUzpvNRomanWrL95Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=uoDJq-dsgNms2_lruMbyvUQmMQ-BWiG0gHhv-1m45hPnCJM9r-5G9OBzjvcz-nzfHoxy1nv5nUA5mWwfrDHOTrw9k-ecNAixRSN22iPNekJn38Ltb1wPYoUOZwhLu9a8uj0k_qqxc1123-vxrYaxpNLnfr5-qZRHHeZ3fLbJimZewGAI4vJhxq1RScybhRjl9dzf6jOPwKqCbWnTg8AuOVacdT5i0zwq-7Lvmi0LSYnwlZH31Lzv4HS2Tt7YFWUUXq9vXdS7jLOKyt_oASET-4gkbtfFRl8u9sLdi6yGcyT4_zQ5jjIsAB5pQf-0yyCGiW05jb7lEjuxTOTA_KyYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=uoDJq-dsgNms2_lruMbyvUQmMQ-BWiG0gHhv-1m45hPnCJM9r-5G9OBzjvcz-nzfHoxy1nv5nUA5mWwfrDHOTrw9k-ecNAixRSN22iPNekJn38Ltb1wPYoUOZwhLu9a8uj0k_qqxc1123-vxrYaxpNLnfr5-qZRHHeZ3fLbJimZewGAI4vJhxq1RScybhRjl9dzf6jOPwKqCbWnTg8AuOVacdT5i0zwq-7Lvmi0LSYnwlZH31Lzv4HS2Tt7YFWUUXq9vXdS7jLOKyt_oASET-4gkbtfFRl8u9sLdi6yGcyT4_zQ5jjIsAB5pQf-0yyCGiW05jb7lEjuxTOTA_KyYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=PvDPHKLHTTto7cm7TP232EJdNKEpRg3r6FKcqsj3jMoayDltsQx9BReBE9DSKxT3bwvhpp8E4lMWXkcQMGSAsBKkSGFC2e7eaL9yNVT706mLVan-NlIO-y-vPZhB_v2f1f2JeYok7QiyNPbbLudF5tBRmi4El66zGKOD9w_6rAPJf6Hubcjdr9XzSqiE1FiUcnjGt35vKwKuizYeFx6qoIpmHqA5hMPaRmYKusD6V4gXk2qnDiXcIfLORPicUwh0Gh1d9SX0JFdquPq7fRK-FF6Ewr2JMAOggO1EFy5vU9hNTlQiLHfBVDxpvPJThEMmoRqMtJD0FPwX3b82iMHHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=PvDPHKLHTTto7cm7TP232EJdNKEpRg3r6FKcqsj3jMoayDltsQx9BReBE9DSKxT3bwvhpp8E4lMWXkcQMGSAsBKkSGFC2e7eaL9yNVT706mLVan-NlIO-y-vPZhB_v2f1f2JeYok7QiyNPbbLudF5tBRmi4El66zGKOD9w_6rAPJf6Hubcjdr9XzSqiE1FiUcnjGt35vKwKuizYeFx6qoIpmHqA5hMPaRmYKusD6V4gXk2qnDiXcIfLORPicUwh0Gh1d9SX0JFdquPq7fRK-FF6Ewr2JMAOggO1EFy5vU9hNTlQiLHfBVDxpvPJThEMmoRqMtJD0FPwX3b82iMHHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drgePGD5npRJbUzv3OBuYI6Vvq64UfGSzn6-BRMi-aoZIMgfryGcmIbo5sFJpYTR9r8GdmtPwRp7v6fcHKyYbtS13-40GtSJDwu6_3KyG8a7WTpB8d5yQw-ufNemHz83A3vBOJdLpO97uepw4ugk5z6nxDafGHmFRjQG9gECBhYTcOwKoiSZ84-refLrHP6ChBr2O_qEsvuyhnBMDczdm5fy4YzCUI_Qv0cpT3Nt8HLKuGyVQOCGTD4xILC69YXsMCiwCQ-4gZzYW8TgSpKCk5pLZJZAhmBXImPnDbFah_Bs68_JZ9midqw3P9VvaFRKPj-kVB1s61h8KNbNh1eVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=m0rmw_ygiW86WSFo6gXj5470-OoslU-GvqLDZzx6pNnQsI0-mQXS5e8N7qtgTGW2QPxrKRM36jqErlD97PlJXbfXrW3sm6oTcWSo3e-4j2SKOZklprOwL6lzM3Ug18hbLC21tlcR3J1-BoXUsoBkPBerZxodO69-JK5unyCW_rnhy6xvlLJXOtMfLVAqh2UP08um1inI3U6bOl6LVgWz7KNlyPxVT3Sa67my4Hi0bsNmeO7ODwTFYYrSeflqmJbd9B2Ay3VnBvEtZVKtXOQx94-z4WU3OhYccZcCR1tjhFXlUhxFKluwvEr5sfuwXYtv3AFuNXkIqvVPLwHOQAdk_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=m0rmw_ygiW86WSFo6gXj5470-OoslU-GvqLDZzx6pNnQsI0-mQXS5e8N7qtgTGW2QPxrKRM36jqErlD97PlJXbfXrW3sm6oTcWSo3e-4j2SKOZklprOwL6lzM3Ug18hbLC21tlcR3J1-BoXUsoBkPBerZxodO69-JK5unyCW_rnhy6xvlLJXOtMfLVAqh2UP08um1inI3U6bOl6LVgWz7KNlyPxVT3Sa67my4Hi0bsNmeO7ODwTFYYrSeflqmJbd9B2Ay3VnBvEtZVKtXOQx94-z4WU3OhYccZcCR1tjhFXlUhxFKluwvEr5sfuwXYtv3AFuNXkIqvVPLwHOQAdk_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=hKir7V8ntF7BSV2ddJf5SPujG7k3ZauramHS-uauddaZHN1gVhmGmq-iDzN1LigTqaLT8o7tEDkEKjtxS0pNSmC617xEVTgIohDEzZCZuELJk-04o0tI0RX9nDZGvrxKXpfIIdgx2wo5eshp5sE41JUUK1qJTDDxAe6DGBPAwS8Sx2nBsiXpHEx9Fz93yrqXwp6pyBf7AZ69Nwybl3P-jd4P_xPJcADOvmpPolnIbMUp70vu-RJNE11HLJvX1MGZqh7i9ykbrtPEzRer1iKEzyWFUcpP-znNrgG3QT-dR6YxWfvudRg1R9RQXKwcbeBdPO8aB1Ycnmolm0XpMYKxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=hKir7V8ntF7BSV2ddJf5SPujG7k3ZauramHS-uauddaZHN1gVhmGmq-iDzN1LigTqaLT8o7tEDkEKjtxS0pNSmC617xEVTgIohDEzZCZuELJk-04o0tI0RX9nDZGvrxKXpfIIdgx2wo5eshp5sE41JUUK1qJTDDxAe6DGBPAwS8Sx2nBsiXpHEx9Fz93yrqXwp6pyBf7AZ69Nwybl3P-jd4P_xPJcADOvmpPolnIbMUp70vu-RJNE11HLJvX1MGZqh7i9ykbrtPEzRer1iKEzyWFUcpP-znNrgG3QT-dR6YxWfvudRg1R9RQXKwcbeBdPO8aB1Ycnmolm0XpMYKxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=daRu1fS7mhIa5FoW5bNtC9Zh4NP-cAFQfDD6faUPwmsv5Xn4W0VSDxdE3yUwIjGSlNgkic4vzcL02vOpXKjfX3nzaRTjU-0G495mKlflM0Zix7p0ly45jT42hLyB5nF1y_aT1ez3qgobAEXvHol6AbpTOLxSNgaaww-gvugCB-gXtSFc7RakPj6Y2IwaBr2A14UUmifJbuC4nEaxTyyQVOHPzQUs1gupi4zXWGrSh1bZJu3wLtHb5ktv2BiLuZXizY7_lKzYwj9R5tMo0cRiN_siy4SqzSgMD02Sdju5qtegyo-gAEfTCmW3ynsLgXhP-UbRrd4yguHjy773fiNUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=daRu1fS7mhIa5FoW5bNtC9Zh4NP-cAFQfDD6faUPwmsv5Xn4W0VSDxdE3yUwIjGSlNgkic4vzcL02vOpXKjfX3nzaRTjU-0G495mKlflM0Zix7p0ly45jT42hLyB5nF1y_aT1ez3qgobAEXvHol6AbpTOLxSNgaaww-gvugCB-gXtSFc7RakPj6Y2IwaBr2A14UUmifJbuC4nEaxTyyQVOHPzQUs1gupi4zXWGrSh1bZJu3wLtHb5ktv2BiLuZXizY7_lKzYwj9R5tMo0cRiN_siy4SqzSgMD02Sdju5qtegyo-gAEfTCmW3ynsLgXhP-UbRrd4yguHjy773fiNUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=P3LsyIalE0aoxBkOTsLy04qKRUffW9o9n2OHLIMGQgIqDcbwpLDqquoVLensunxnR1N2ERW5AGY1I5ON6PKDSU8nUCsgnLopdSokAi54JYQBL0xO16Sk_mERRzpWmIvXArpTCDj3RgwL1pUxUILVZV7UOtXPov4BXPZ2xFnXS8t36wverti7BmHz9766Y0aCL6vW4wGrXPoczelb8cVk82S2IxHqZcofNPnbv1W9I8s1VKpQSnkICAUzIAC5Dn7TOo1fJNEJ02VBN2blD8emfMPWTGdeHRV2U7Tr0vOjqRpLCBivtp6XcwcR18Vb64pxO31NPXzt1uBcQJPiPOs8rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=P3LsyIalE0aoxBkOTsLy04qKRUffW9o9n2OHLIMGQgIqDcbwpLDqquoVLensunxnR1N2ERW5AGY1I5ON6PKDSU8nUCsgnLopdSokAi54JYQBL0xO16Sk_mERRzpWmIvXArpTCDj3RgwL1pUxUILVZV7UOtXPov4BXPZ2xFnXS8t36wverti7BmHz9766Y0aCL6vW4wGrXPoczelb8cVk82S2IxHqZcofNPnbv1W9I8s1VKpQSnkICAUzIAC5Dn7TOo1fJNEJ02VBN2blD8emfMPWTGdeHRV2U7Tr0vOjqRpLCBivtp6XcwcR18Vb64pxO31NPXzt1uBcQJPiPOs8rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIjg-WrcwUN-wlIVzsCTExaseTgGECjAAxBexeBAua6GzQ6Yl9pK0NA1btJWvv_oP1DKCvp_LEfdJ_p1f4BHUzz-T3P8z1G9xSN6TuHctZvz22mSNTJk9yGYyz3v61zxI8hjPnXpKtB-q_8BnOUBSm3K2LXe8BDa_rBzPGMq3uPVe-qFcbCHz30EsN-R5pFQXpgvs9aAai-qg-UnE1mzvxkGB5-Plzf3WSbex7jvlYsNExm69N6WR_bE73i_Uxf0V8UtF0asu-asu7-ACUNgAv4gCsv-hglIDVr5JFj96J39Jkmqzl4RUOT6L_d_Zh22w6ou8uH4UMZ81vU5iAnm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9eqllS6IXzG8We6435t1AiZKFK1K45Gx0qN4LHeyxgfXeVUmMyK5zOIfkBBhyvcty443BLsnAFtLRsKzMvfXWLE_rUYlsYTexc2I1bK8siMdnpm1O7EaOFmiFadyycfPXAfrS6p_CN6BxVaBcCQ1Siy2MCqhvb2cNJ4-PSv6KRGm53E2Cbh3_i0PSUO9jLUmRkBIr1hsUXBd6rpTMJLwSOtU79g-NUvJCdlKSdVzOOx61gTMK6WYLymceUMCqhHCLLe8nVQlKoqlETU54IUCACyq44ODt2kB3x6zQ9YUDQmqaRhuXTGkIaBZ7XTiPN2bRfZdW7JiBsMZCDXQuZZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=RaqbQtji4MIIcmBKaoejhVeFCCWz8OERrfHHIxiLvonWMnfsnZ6SQCSIfM5CLNQfAScpXaVq5HfYq7-UTeSCyonr_iu1-DQL1i661iUfofal8bfmMEfv_3AiKJGYII9G7vTqocWTV_Zdqk1ki_A3eaOQgeY89IQAzEZVcJvV4j3lxSBb2gywDegCeUFo5Qp6MgogaBYh9mFMSU9y0EiYFy2pvvtrao4zNJjJaBq3JfmAFxZz1X3Qs9WbTsD6q0nWy5eUupVSA_rOMDgmDUqMDgCg8zj8Acxo57AE_UgVeve9KW1rlqbbHJqS-jRiQemWhOOvteW_a3RheIiHOOIi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=RaqbQtji4MIIcmBKaoejhVeFCCWz8OERrfHHIxiLvonWMnfsnZ6SQCSIfM5CLNQfAScpXaVq5HfYq7-UTeSCyonr_iu1-DQL1i661iUfofal8bfmMEfv_3AiKJGYII9G7vTqocWTV_Zdqk1ki_A3eaOQgeY89IQAzEZVcJvV4j3lxSBb2gywDegCeUFo5Qp6MgogaBYh9mFMSU9y0EiYFy2pvvtrao4zNJjJaBq3JfmAFxZz1X3Qs9WbTsD6q0nWy5eUupVSA_rOMDgmDUqMDgCg8zj8Acxo57AE_UgVeve9KW1rlqbbHJqS-jRiQemWhOOvteW_a3RheIiHOOIi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qker5auKScG2CVLj9ysyzsc2HPO30eVV574w2cQ1kt6bgKOkt5KbqqJKahlijVavrHmK6J5mSTH15mkGkx9-T91RMlQPmmHhNWgNAiaYTeUqhG7nAP5VXd5BXbQiujcgkDTDTsy82ZByyvIoxcbQEpJkhwpTQpcYRhpRRfaFn2gd2RoDb7GasRNHNyTdCchM79I9sKNozOtAgdcALMfcfmri_YokSbDLequ5BkjwhT9ar6fCLfqU-yu3BCaOEZe3EbIe9wcZBKFmpcxasMCoy9cEVy9gvUcMO1p8JyAyIb-LFFn_xot6BdUiDZqKPfqNPIu-oiB_HK5FxEXL_3zmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqvKzjMNL66Bcss9jaVw6AHsFAsmPApEBtXl_U5Y8RQ5gbfBZ_ULLL7zV2IHn4Q6IcgaeoIjMiDmEDjr1_s2Cxp6GNktbBGN0wZXNh1QQLp5NTKiZ9yIdcMah4Q1hjD4DqTH51Zhah0ChiRydtb8VR_K2-JQv2ZC1ofcTprP0soGUnK24HyKi1-flcLA1zMcR7AiiN8hozpnCJ6N5BWbZ1cPeDohXU1XT8WH7LHWqwyqrflKD9O3OnF4zJq8_GE24sbaxBt2gleoLObEbRC5wqNr7FehHiWr_597bahpxVxpPmRB66szz7jqIrV1p1G0lq8EA7hQKFwsFbFU43stbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YBhZ8Cj-DBRILwfmvMcVtCCeKTp9lmC6DVyrbxbbOqDCbKcCXASrYVlHLK5FyjWzGdorkI6Qp9n7Kgt7jIa5SImZEer3T-4DHOO69hLaaP_FbPWnUvmzau_8d_JCvc8KblTM9SboQcFUX0dEmv_lTbSKGiwRyqUHMB0785eqPoFOl8Y0hnoMkL3C1JN8pz2cbwPy0-wSosb-nbijEKxxXYABRVtspWLIvlUxTCQEME7dvVy7xJjwn7ceQCuESUBTKkAKWOyBqsvAZ2uPm3v2mZVOs6MhwxgDxYKd9h9jCYycFJs1e_jtaKos8RNmAvEciwRVEqDUyVaWBTtimT23AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UmG74RcB6S4L2-CuEUiP8aTNETJhUxFaypSl0zB1jB1GQSgDU1v1g-cSirVLAfpYcc5w2yg9R7RtgwcKIoR2j4euP8v6FUDO_jfh5w2KDhXiVgLUtT909CpHz6TU2ww8hxVhoURaWWL7mYiNP7X5FGMyi5itqtqza_Qs48UUXbe_wiaPZYtEXUNjJTz4xDh6Afei5R7DLdnlRg3YHyGrmIpeMieGGViV66Uitx_gG0iulvPNUKJMtLTUtpadJmuL7PnVh7hTcT2z_KgPfbOVxsrCq22SP7zDy4wwmtT8TWkceaoNoLzTJiC2qoY5fL5AD6KRczw9Yk5M_lFjJ5p_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=DjDHGACOmJ5bn6UjaX37aP26skqhGezIl00AvP2NrZdMyPy8C_PcTznhniyCrma7GamewyiwhSg39CT77couURF1vzvuXrPDg-wrIZoA1JYQXDs3Jat79cRaCvESYzdIXRitjdhrgmJT2ZInPwmCzWZ0QlGW7PTrxAh89s3maWoG7dM3QESCr6keRvuWxklUOfwaW4RA77x4bjmq-1gDO3s0mvzsNF0hvxFkZme9pZOoz3m1WBP-mVcxZ2IYNHOZX1AImvvWarwxQJjTYKl2pJrUuZcUkWlR22zvyXcw7pk3DMUn2RMmwNTEScQxVew1pwEt-OIZk4ukiy0x7WkCPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=DjDHGACOmJ5bn6UjaX37aP26skqhGezIl00AvP2NrZdMyPy8C_PcTznhniyCrma7GamewyiwhSg39CT77couURF1vzvuXrPDg-wrIZoA1JYQXDs3Jat79cRaCvESYzdIXRitjdhrgmJT2ZInPwmCzWZ0QlGW7PTrxAh89s3maWoG7dM3QESCr6keRvuWxklUOfwaW4RA77x4bjmq-1gDO3s0mvzsNF0hvxFkZme9pZOoz3m1WBP-mVcxZ2IYNHOZX1AImvvWarwxQJjTYKl2pJrUuZcUkWlR22zvyXcw7pk3DMUn2RMmwNTEScQxVew1pwEt-OIZk4ukiy0x7WkCPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1DGtXr-bmUrRDlN_j28sGIqDCdpZGuNByamd63neQjYdJEhDojgweeefDQMQn4w9oH2FwiOsb1GYWRwLEvmGKXysy1e_ux98XnEEKmB2PT_2BM6i32nMY1Z7mjVKXbq8hmpHdJltMNmOjl2n69kmSsoMVS0lR9Q8jFuSjFTSfLWLCNm5tOH-Q8YQjl2h68tSX6S0W-oo5rGu5g0x6yXiPDGj3PFclM1klpoh3XUcX-W_xkb0KvcO07bmLm97i8YfsEzR3wdRyzC78jPOZyHW_ZnOJupjS9RR_gfGwgKJs94xiM8vax-myqKGeLD3d9CQSreoRrkghEPOo8wBHvYPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=hOeFK1iBT4x_FaVfQ72KXyHNhVivOIu2fmri-b_SEGj58nqJUlRndfvC4LrtlLMWH0YeBRk9g7VgYVssD6hSmvPbgnhsg25PWxbMnbl8erP0MWCrmUbsSF4cx5v0ZE-NPclRdUP3UxOe5QdJ7fSNg7XW9B6vjlVmHoKiUD0eswPgnmspRwa2JMwO-9q40Vq6lnixBNLA5SVBp33ksGLGNpR_C6p9LIBOs9qtMQGibQ8kC34rJABmrbO3uT7dNMvi9sFcS2LLP-9gVXTZrXcBT-MNxJmQQb3EexIj2MRdyYf6No0bs5B3vtcLDoVpD-MNPxgLevx53p4cL_0sODMITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=hOeFK1iBT4x_FaVfQ72KXyHNhVivOIu2fmri-b_SEGj58nqJUlRndfvC4LrtlLMWH0YeBRk9g7VgYVssD6hSmvPbgnhsg25PWxbMnbl8erP0MWCrmUbsSF4cx5v0ZE-NPclRdUP3UxOe5QdJ7fSNg7XW9B6vjlVmHoKiUD0eswPgnmspRwa2JMwO-9q40Vq6lnixBNLA5SVBp33ksGLGNpR_C6p9LIBOs9qtMQGibQ8kC34rJABmrbO3uT7dNMvi9sFcS2LLP-9gVXTZrXcBT-MNxJmQQb3EexIj2MRdyYf6No0bs5B3vtcLDoVpD-MNPxgLevx53p4cL_0sODMITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdpI9vfn5Ugce3I-osNChA3YtAzHMb4b-2j3m5HCziR3yM5NWpAgfN4V9aUBZw8AIKeyfYyGdAuC3S6EYtmQSMIKx4P-U7JdThqLycXTfqUgR65_IeHfDaTwzyN9B8cpRf3wJZCvKTMQI0D0ynJ_nNfDCX5YynUqzphlbWdMZ0jehbAcgzbn_Y2wtE_bELw1xcLf5cq3Y_ho76dtDHX9qFv47cadk5YTrP_FozXxodz_VR0bn7pAnaM9ys3QBDsZKtgHjqwwBMBRoNeTMikcnWmXHK4qyd49Edx6XSfzJG70grJTknpBpqOV4kzbaPPR2Dp9d5S7kORcpzhQTxucrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fO5r-8hTCrkYjbvtXLmP-frGwpDApOY8cjZilz9P9Cu4dqjEuh7Ny2c_K3DRxg8HO_WgtLYp9CelhGz3AjyF_Ocr5XDLnOMGrr2FyGDYMd0Xj8ALQPdpMXD7N38YJnIHdXSShmfvzGLFkWr6bfewszPBaw4Qn6XEPyGfAx9LjqwTQoOccUi6JQFXw-rmlO7mHr7JMGQksaOx7R65hz1jyFi4CFXoBvkAndeL84RyQNTtCwdOqMNKpoCCGoHTiYyhBf9jddU7Vr59uqLEHKE6TjTEqieZYqK5OoOFGZBikj3LW1JdzH56F-0Lxqx1jiWOZrIpNhUxQtDv3ikpq0gpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=mLPE0tw0_xyUHYgMO5Ht4fOsJN4AQs9ypZTuTvfogTwJLBkJGSyi3KRevjsseN6tKKPrH1o3z_2PkTCL9vpHVeBRXJ79ZnUn4HsllHMM6FO1g2FODiS6wFxZGALcNo0XzGQkK8bcE9Jy_SVB2b5HDd8pP0VSfV2hqHldLuj08b10TBYyI-b0ZgraHLQIwx56ZGP_n6Rb9h8L7UH-rG5Z89m0tDC29uqoNNxYLoGQEghZuhB81gXyt8GYCudEqyIba2QY-0_Z4LLzmEM8C6S4QBXwP22iRTRgQctqR1F7e63GrusHjgn65HSTFD26ckJ2aOvCgqrWDGUzlS-pKQ0ZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=mLPE0tw0_xyUHYgMO5Ht4fOsJN4AQs9ypZTuTvfogTwJLBkJGSyi3KRevjsseN6tKKPrH1o3z_2PkTCL9vpHVeBRXJ79ZnUn4HsllHMM6FO1g2FODiS6wFxZGALcNo0XzGQkK8bcE9Jy_SVB2b5HDd8pP0VSfV2hqHldLuj08b10TBYyI-b0ZgraHLQIwx56ZGP_n6Rb9h8L7UH-rG5Z89m0tDC29uqoNNxYLoGQEghZuhB81gXyt8GYCudEqyIba2QY-0_Z4LLzmEM8C6S4QBXwP22iRTRgQctqR1F7e63GrusHjgn65HSTFD26ckJ2aOvCgqrWDGUzlS-pKQ0ZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIC3fgsdX5fgeeKnTgoGG8IixPuxWe00AsfYGUZLytmT0sdL7SRPFXmJgtdFtyljMnOFMKPzhU8ItKTpbdWZC37nI55VBROFXjGlUyuub6L8GwcNA8lYNqG0WXnQCRl9-ISgdHZTwf0NRlC0qCz4O1K3EeqyAMf4A2o37Y7El681IgQV-92Iff0SWqM5WLBMU71oHbonjTVZUKf6VnCW3AMHzST2xKGjjVBcUXXzqTFPGMbgc4C-zpfFyoLEwCY3-9MbzK03T1_ujikXoeFfrujdi5piKEvejSJX1yyYJw0mWKknyT1n_O5sepFO-b2NsUZfsfAG-_KV5xCVZF5gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=kgUG--R3UeYMqPdJWyFV3-cTRCF-dzGs810RGYB-Sjhnyb93YI5YV8edSG364qFnFOiZes93-bweriwWjlzWcea2A9RtRBrvdE5WNh36Z7-XOXDMAiR5DyVBKFJpYBqPUnFZopTbDC8a27SEtVt66vSb4PxnaK4p5IL-kkRUGq8ervAauDZ3IyBMag_e7ksOJl5LFbRrt_8zu8lac0VQ1bF1dFBC5sYJgWDiznDNwKqZPzUrmu1Olm5VCZuuqHSTyYuANSx09QUezBUxmf8RuEL991A5LH3HhqUyV0HecqHLKihTURvdJIZsmmZtjieUYYDLo5N0Fh5XDrtot_rHX5jErg7D1UBTQxuQJ-12GOtoWFo0DoXUyLzdXVLl902AJ08FsrYgQsoYcSR3LEXSX9v8RTP3yFSAkD4GIC1tpcqnx2xm2YpmxryppbiqXuATrWyuxviSB3bT5sokx4r8I8jt1ATycqNSrzyM2yb0Q0cB9o9jvz73O_94B1pyR9Oex9sLL6j0OUEU0bHnFAzBkf69-fKIbWCkSRXxC2uWNezGeXDx6mMVxImJbtwUWUS1US46-19e21mQvdy_t-ETrN5og1BZEyHY2wVrjDKLyu4j47W_EL8rbpjRYi3cwqt9nsBs72LAiNQkwEzNGSIjX6GVI0yUutVeuXgebShS-uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=kgUG--R3UeYMqPdJWyFV3-cTRCF-dzGs810RGYB-Sjhnyb93YI5YV8edSG364qFnFOiZes93-bweriwWjlzWcea2A9RtRBrvdE5WNh36Z7-XOXDMAiR5DyVBKFJpYBqPUnFZopTbDC8a27SEtVt66vSb4PxnaK4p5IL-kkRUGq8ervAauDZ3IyBMag_e7ksOJl5LFbRrt_8zu8lac0VQ1bF1dFBC5sYJgWDiznDNwKqZPzUrmu1Olm5VCZuuqHSTyYuANSx09QUezBUxmf8RuEL991A5LH3HhqUyV0HecqHLKihTURvdJIZsmmZtjieUYYDLo5N0Fh5XDrtot_rHX5jErg7D1UBTQxuQJ-12GOtoWFo0DoXUyLzdXVLl902AJ08FsrYgQsoYcSR3LEXSX9v8RTP3yFSAkD4GIC1tpcqnx2xm2YpmxryppbiqXuATrWyuxviSB3bT5sokx4r8I8jt1ATycqNSrzyM2yb0Q0cB9o9jvz73O_94B1pyR9Oex9sLL6j0OUEU0bHnFAzBkf69-fKIbWCkSRXxC2uWNezGeXDx6mMVxImJbtwUWUS1US46-19e21mQvdy_t-ETrN5og1BZEyHY2wVrjDKLyu4j47W_EL8rbpjRYi3cwqt9nsBs72LAiNQkwEzNGSIjX6GVI0yUutVeuXgebShS-uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=c9xBnWILM9y-xOTCd6Oh0jhEfu450UkE3IyPeQ_ZSav8c3uSzrklGaJr3siS-izi1Yn5g7vfGxFk4jHLi9yciqxxhe-qxGfRINuQKfUOOGz8kyBO8ZHUX3dISrkZqxXtMjmeVQEda2HQPxlIma5JVafETKRZvE30_zLDyt9uzHfujEciDupFdYKKTvVsvY7DTO1jOsuORv_5PpgIEzsAyCheeWP7L54lSfHozEYSi6l7dU7LacmM9V_ZEvN6jldKnKYC2Fsvc5f0MhvjOLkszn3-XbLEUbePbQgnRAuYUQ8-39W-mkZkK-2B0DLvQ1qi3jpWJGnJQw6_B1s1f1QpBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=c9xBnWILM9y-xOTCd6Oh0jhEfu450UkE3IyPeQ_ZSav8c3uSzrklGaJr3siS-izi1Yn5g7vfGxFk4jHLi9yciqxxhe-qxGfRINuQKfUOOGz8kyBO8ZHUX3dISrkZqxXtMjmeVQEda2HQPxlIma5JVafETKRZvE30_zLDyt9uzHfujEciDupFdYKKTvVsvY7DTO1jOsuORv_5PpgIEzsAyCheeWP7L54lSfHozEYSi6l7dU7LacmM9V_ZEvN6jldKnKYC2Fsvc5f0MhvjOLkszn3-XbLEUbePbQgnRAuYUQ8-39W-mkZkK-2B0DLvQ1qi3jpWJGnJQw6_B1s1f1QpBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k34jTw1C3hR3pELmCgXX505mRpzxOVHbUK4gfs3E01VRIi5sOLjj2p1zbWog40sdtpDHGRj6RLRriKhh5t8aH0Y5YiaccXmxvzLpys3zW7AeECDNi13Wry1WubiyvGnW3Ac4j3qlJqyjMi55gMCDYiEakuPzaBsWJpWBruj1KJrm9j3bLfmw-u491kML_K7ud9RKrNLimTScRUhqAckWWVb3IwhnUdMuljhnuuknKSIAN3FdHJ1kOqrVoE7s4lcYSYEa0XfBr5_jLF7iBVjxQI0nUGz4kDQeK3QOQZ2TcjbYtwqaNs_h-evkJ-VXlpHNWyEbdvNXpXngmEmKJ8NRCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=NXfw9Bq7TLWEEyXMMtF3aldv1FjCTUFbs2ooJzoKhWG6qG_Fkb43l97SYfKdu4dQvpk6kwGaJ_yhEvqPgonFv7j13nBk3po-OEM1J75OBoWjqMhPATAKvI1TcLhX-xWz7egrbwo1wBaEzqeiDeXRsvM1Kxz6r0UMPRkC8z5wskXNmj0xaEKsEYZyXVSTYQPRPF7nnqEyPEZCUyorWryO8gOUToOcIUiKG_5UhWG3R16dQgjn1_O2gngHl828uNsQotms5ujq14eTGcTuRIyRo8enQqn4GfDuHgZnwimEOuYcK6Yg86m-XpybEaZQT7VfJbJNSaduY1aUthtbOpgDMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=NXfw9Bq7TLWEEyXMMtF3aldv1FjCTUFbs2ooJzoKhWG6qG_Fkb43l97SYfKdu4dQvpk6kwGaJ_yhEvqPgonFv7j13nBk3po-OEM1J75OBoWjqMhPATAKvI1TcLhX-xWz7egrbwo1wBaEzqeiDeXRsvM1Kxz6r0UMPRkC8z5wskXNmj0xaEKsEYZyXVSTYQPRPF7nnqEyPEZCUyorWryO8gOUToOcIUiKG_5UhWG3R16dQgjn1_O2gngHl828uNsQotms5ujq14eTGcTuRIyRo8enQqn4GfDuHgZnwimEOuYcK6Yg86m-XpybEaZQT7VfJbJNSaduY1aUthtbOpgDMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=h4GUiWKbKGfWW7AKWvRzpupwYWngj4CBfheK89uMOkgx9ut2FhTn1XJLgff2IR9t2PYAYN72A_zWNZc8lFOvzSf7awiWxAGgEGakWYXJfGt_WUXhDagJLV3zeewXesApbOV4cNfkyWhhWReIZg_oez5fWg0AXUb08hKpnIpJgxMVzUOCwqpxgUNs300zI4HXzfUbVm8QohMw98RbtLDHQghXxlGBMgwBJG98KcmBQ-gZ7C4qwFz7hIUEr3xpRfimJT_nBfq_2EPrTWtClZaorrFq1_nLKDQ9VSHm1XOe15dDhbiCDTQxO0mKwmFCNvHk3DofTxnvzdjNBp6jYij_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=h4GUiWKbKGfWW7AKWvRzpupwYWngj4CBfheK89uMOkgx9ut2FhTn1XJLgff2IR9t2PYAYN72A_zWNZc8lFOvzSf7awiWxAGgEGakWYXJfGt_WUXhDagJLV3zeewXesApbOV4cNfkyWhhWReIZg_oez5fWg0AXUb08hKpnIpJgxMVzUOCwqpxgUNs300zI4HXzfUbVm8QohMw98RbtLDHQghXxlGBMgwBJG98KcmBQ-gZ7C4qwFz7hIUEr3xpRfimJT_nBfq_2EPrTWtClZaorrFq1_nLKDQ9VSHm1XOe15dDhbiCDTQxO0mKwmFCNvHk3DofTxnvzdjNBp6jYij_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxuaqbWvvWpCO9Xc9pawYQglJhMoic_P9VNTGMd_D3zAoYxrTG-gtfOfGID6Z7ve0djDa5d7aEaihGnqP6j0EtHLpPz52s4xXGC-wO3I6UqtsZaMaLqkcV0aTIWjAXyuEqnX6YndnS9lfSDQlAiODghpgX1zBtrReUlGYf3kA-Cd09qtCFkmfc7WYdVC8RXKtS-VX7tgvJMewup_9_YEhUWHMTkYUHgEwh7F4cq5si2G5i58bTe5BhEZMDWuU1TA6JvCjNMScM6utWO71uOQBp_o0htQt-7o1KdMNmb-erGHy1t_QzU328pFHr37jKkUeTbUhYYjEcA_iA-VZtiN1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=Z9409PTrOdldlP78z4lmBuR_bDMxW3u83v9QvNASIt37mXZRnJj3pMaRcEx_EibbYQ7jSXYHDm2lb9byheJQJnQadjOYqXnDWt-hM7NuYuOQFLGnmat77IfqOlMN9WUjO9rwYWAyV-1p8UitUu_cBM_LReB6ZTTTShLVW5w1CtgbiXhwL7N3ZZBKuym3gu40fmeSbkJPQHVwj3F-WBxFSONVoVxIqbC-5C2jZ5sk6DBHUyp8uUnE0LPIPwq51W1yJpf8RM_vHMGefyHq2fyQ_KnKawcO_ej5YZxy47InxZP8sXnptOUAhxHarZT-W3d3Z1Dm_mufHLuwaOWMtdHZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=Z9409PTrOdldlP78z4lmBuR_bDMxW3u83v9QvNASIt37mXZRnJj3pMaRcEx_EibbYQ7jSXYHDm2lb9byheJQJnQadjOYqXnDWt-hM7NuYuOQFLGnmat77IfqOlMN9WUjO9rwYWAyV-1p8UitUu_cBM_LReB6ZTTTShLVW5w1CtgbiXhwL7N3ZZBKuym3gu40fmeSbkJPQHVwj3F-WBxFSONVoVxIqbC-5C2jZ5sk6DBHUyp8uUnE0LPIPwq51W1yJpf8RM_vHMGefyHq2fyQ_KnKawcO_ej5YZxy47InxZP8sXnptOUAhxHarZT-W3d3Z1Dm_mufHLuwaOWMtdHZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIb_uTZ6xR414DYOtJMwIq-BG3JkGAbKNpxrNNulCH2rsFBabNGigv6np3XIfUonlS5YzBj9y-jM2hBdlfTJZukI0qdXcidHpvB_gkLvFlF7O6RytrT2tdTbHKTbEV-6Y1QaIP4-QCQ_tRwgyQN72EgVAFZDz5KJpVERsPpXzFcEqxUb9nHEpODN34pGeOyMw3oypyegIPBVwAU4T28m3jmaoho6UgnH0bJ7oIA_95CuAe8TNm9tpG-rbPQC6HLNvrQj6TnwAAIdiKmoze404_KxI9-KZJUB2e0B6ReZvcnyy-R3Dfkz9Q03Czt_VXBgw6L_GP36ru_6iXSp7r0-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N60fl0dFRYeKChcI_fClKc0Am79m4IAh82YHF6q9CYObWwJySFLqHtsUxOh67_qg2oK_v6HznUq6pEogjXBOx0ItzDQ0bViWYlRU2TYuDZqxsCRWMipnLvFJoJDbwanM1ZwrkcMyT1PDQw1eEQnvdBiKAs2JB-GLaKBHOY74eE_2XW0UmwuSF_yidTvOVf7qJsFS3vaaFjDOAAvn4sEzN7krALMPTdAlbnpcZjOtND2SNG44AXyCjzPkrrfmt-Pad9tlSjkDrYDj9jxDgA1eyxG6fj1EIPpY2zCc7LYX5Qy74OLJPwhTkR_A0LM4ifKJ5rnd8ADJ-eQUbfQppEt2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPtSbLbkDzgfPxfkVVtzHCYVx1USCZwUyRKlgcyNO-MyyN1KCFZQzVKd292_855IC3xqPv7pw0z82j8O0jCxNAApFOjc5JuaqE5Af8ocSnXksNZZKIAbotxX-bXyG3eYrSmk868XDNb5qHzuJ4x6nV8T0UlrfQHfRWTL-HkWheLukm_hYco7Hb5Of3605nSe06565ihu_OefxC8BCJPCmdUfpCXah5qYbwh0sfHjPVCOrVPrQlKbLbxasnNF8YOLmPduip_WYLra1CbEL8DUEqwgD82VQKmCDH1fQKqSE_Hhv2OcdbPxDNVfo2Mdf7NW9-Oarm79Iog3UlAOTUl1Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU9tquzhpqduQJnxye4Gw12p1BlonW3qUIt-BRziRhRRTrHgnyYwg7pAPcr94prkQkw11rH1O4KBfhSbLGeKZMNr2xJig6vYgPyZB3kBNsD1E7G6YdgcGhAHFTimCbvXdRoZBNMquhSeyFp59-LiVPcC6PZ5XKu8GPKFzdtfOb_iPEuspmzFEyVAb0j53af7wqCRGLB7ENU9s2COH4SQe95B_x-HoGuRGu7ZtjczKMt-2ROqM5uwNf4OhZJxq6rQ7TzwXY98kS7n9YY18Ux8-U1mRAd8et67Cf-dPZE7PRtKezlIciqgRw_UpcGZTmzUDrotDO2ffn-mCqwyv7NbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=m2iwmaCANjoBC8MEky8c3GZzeCoI_f7KBz1_6bQhNRh7_vEwme_6xt6UdRDkyr3tklRNvvnpF4eYkRpgyOEnYB_5r6zm5zAwseg6Zh_Zrt8trV_IOys4Toxn-rBKhYM0Bb01OBdKudUuwtmEzQlSk665EDYpcBzVyZPaNwNMNW37sOEfwJsjvwpdBESnosFTXnFZHZ0hoW16wJprsD0THPtNPSzUKVD2HhVOfXJRluVt8XHvTrFoF9vIHw9Ggz7J3Ge4mbTcUwuEIumfTJEpbPr8bZUw1fyhfy6d-Kj6dj0KNnqFJmdASLPueCD-A1cRnYqNJgBnBh4yF86avBXlYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=m2iwmaCANjoBC8MEky8c3GZzeCoI_f7KBz1_6bQhNRh7_vEwme_6xt6UdRDkyr3tklRNvvnpF4eYkRpgyOEnYB_5r6zm5zAwseg6Zh_Zrt8trV_IOys4Toxn-rBKhYM0Bb01OBdKudUuwtmEzQlSk665EDYpcBzVyZPaNwNMNW37sOEfwJsjvwpdBESnosFTXnFZHZ0hoW16wJprsD0THPtNPSzUKVD2HhVOfXJRluVt8XHvTrFoF9vIHw9Ggz7J3Ge4mbTcUwuEIumfTJEpbPr8bZUw1fyhfy6d-Kj6dj0KNnqFJmdASLPueCD-A1cRnYqNJgBnBh4yF86avBXlYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK8q_8WTASx0SdeZsJVEW4BFwIvWSVtx7Ar5msP3ZowMVs3UBoBnhlNYNwI9LFYDvOPSDC0gNUWXBWTbJgXw3rTTlJvk-RFU63ejBonkY5dqgtuoMYVQG-XPRIGbm9lZYZl8CVhG7lE17-eC0h0k7VygWTnA3DynVJJPXLhzeaOLjp2gC8efDyoEVEA1DvjMR69eSmYLrfwYNSRbaiaw5XlbnzrvgHKUduG3mwwAl5vs_9hT9H8IxIC-V9XaYvVr8ARBKwSNfGKZngCb4pxCbOD3CBi4xBTFMWyyARL17t1D7P8jipjNGwwGF4QbgDpiO20KtBMhfYFTE7SAvf8LWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=uxtU-8_YXV1n5zPcIvrsrq2pjHZfQw7ex51Ra9A3V6ZdU0X5gu2DyAx0lnoG1-5wTxgfyX-oaCzWVS5es-c3LZNjovm5huER3jGG38gUoYZUUaymfSUQoMCI_AZ0uLun_Tkrzd5rz-TXknpB_t6WqZ4RZqI3auu2x7j1UJYzFWqlo7QcRnvb2ilzns6KjmvGMK_Z1jQPXxDX4FZ6szxBKYMEU9Iby09kx4c0MBbH9MvXo48CplyyGoR1Z07GEEdWswVLOZlSRR-VfokQpjVnEBf6JV1HdKS0MujJ8UZrhXX0T68NfnXZC-sBHhqgH8IviPTr72Gd1uDUeZDpYL80Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=uxtU-8_YXV1n5zPcIvrsrq2pjHZfQw7ex51Ra9A3V6ZdU0X5gu2DyAx0lnoG1-5wTxgfyX-oaCzWVS5es-c3LZNjovm5huER3jGG38gUoYZUUaymfSUQoMCI_AZ0uLun_Tkrzd5rz-TXknpB_t6WqZ4RZqI3auu2x7j1UJYzFWqlo7QcRnvb2ilzns6KjmvGMK_Z1jQPXxDX4FZ6szxBKYMEU9Iby09kx4c0MBbH9MvXo48CplyyGoR1Z07GEEdWswVLOZlSRR-VfokQpjVnEBf6JV1HdKS0MujJ8UZrhXX0T68NfnXZC-sBHhqgH8IviPTr72Gd1uDUeZDpYL80Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y773Nwm3hNckr5OVZ0Hq1_ElFSCArBYIya2xnuhyyQj378jMUuiTJU4HDWIBu1dxtxbQ-uziMn_T_qyfTIqXSiFy091iGwL1UsCoaPXxxh5sgstCKNCn0zhbXSZvjYHTg1BO7t2Okftmua2nnJC63b4AcWNdj3pz9Ozp59L9EJAkXCOAN3t9_W0VOVOPgA0b6l3bpqlIhRageRnrli-PDKwgj_iYhPp2adD-mxhph_zo7iNKgdoe2g1HJzw33yL2PPDW0I3GLXtbgilPgmyOtzlbUr1MMkRY25hY_mxL6Lidf0oelsdu1EQEo4IgXWfpdvxGy4tclzxBVWJqwfCB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBQTCFQKaEjp5zQstctLv7QoXkh26cnQoNSDqhZbWvrsN0bOcH9mdod1h1xcEgYHdvJH6Scwi48Sf--RohBlueH2qhYgszBXwHnxvjv8o1Jz2MPHeGN2FVOGv2gTwwoVspQmUaRv0r2wLf6XKxCb4s9V9oDlhvQt5A6Wxn-eTOrE0-LMk0ihBmzIfi9E-aYrr0HcgkxyzF-enn2y1Z7GQqZ8c9L_ZiVYGy90jNbws5UxEkrFIFO4gEAf1Drsm-HIS8-ZhRU2CbOukXvUO0xenZJGpWFovrYoblRPOyAP63JTxXv7d4c_VGJFh9trz4887EIFwaq9hAGoD02fiUvP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oi9DW5vri0fbS-YwxIwXJJxs60NBJmFPzhMpcHuAv_LRtbLM9_QgQFKyDwsMz5YR5CcFYaXAYG5BAxzjMqI12rrGvA9oYWsFmBKPRCD87cg3EKw1g1QfD_EpWV1U4cBajP6uyasHPmMteYGA8kLyaljUHIImBl14X1LpM7VhLLkEz7Y2U_azzd7uYnNW-KxOSGbVdXHHqQkMuJJJaKTBmGZIFCNi0VsBXcNVGicRuk3pOKdRSzUdrPQQxwdLsR6otcXvIkcWe2YEvp4ngXItxco_i7esSnZxu-W-0YSXFeyOGsgG9hDV9n2lz9VME-qwfxvm_EgYOVrJfG-okizGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOe-NeX2HV9g_Lau4R4TMzz3PmDTJ7Rtjx10QdU783jRwb9r3Aqc6b62edE5ziJ9euUSCdBXQQNpQQKELXX8IKCoPQeDSbqYuuUxH1Xz3XT6k7VlzXJWLcc36fcRRlUjExO7GnKyqnLnPiy7MvvIElNn1ASKU7gfw8kdK10J9Sfzi_ma2njEDU4BXEkhyccCZFFD6lRVcdpVeoDyaKRJkSRY-kWQsxZ9vwT9yeAI99yGyHxnZ0uyUqRzG1azW2iRiTrwpYj9rAIEDWB5dQIEBWrHPlVQA3Q30ZtIV03nmFcFhzmuitJnuA3Yv5lLm5WkNkMeFroF2etAW0yLdOakVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXULmZo1Jis0zCWemQizhBeyhKQRfcaEw83ZpkaIqiRpH7kOXG_k92HRFsK1aSZNNhx_E_jXPgVb9mUJrGwGmQhC_l7C2SDuDOTqJJ_RFGa9AGLUCEUx5PSlvtKVm3AdYWQ3lIER0omYHGhV3f9JogvOyqH5qKa54KFY2GP95DIzAktM1Ia363cgGTfsJxPGmYJHMLJBT6_lQ6mnfPXX1Y_fpL7zEplrbsr7eQBy5GOv2zGjeanjl5eZGMSdEy3GZ3L4PULWlRwuJ0CE6N-3jYd8R6BYo9kui0yTRjvE8ih3Po9Vc8SjEenfjC02vLb9FDOL0-IGO-V2HbEab5FvpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
