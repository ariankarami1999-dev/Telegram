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
<img src="https://cdn4.telesco.pe/file/kmqVdmv_W0POiirb7oTCLSt75G3UT-bHbk_Ek4AO566FNcRNq3KbQu7-HFZVIiFupW8mwzsROQJ0aQNxrsesJxYOaLfuH4GExlDV8Qk0SPtcFbDR37sT7p1sBT6GD5MWgFymVroJBtRA-ZFj3sTmWtERcAkWJ1YHmqd_qUQk1dDldrkXrj_VpJtVnpbf06ZmFKtO3OsB_qt4z-z2dxSGLGECp-3S0YgYnIVJlOGRbWM0BRbDCUJsG-N3lCLkcHkZZ0GMltNZRhiTINpLDIu0RThW4XVVfRzFLe_6kYHiAYzeJApr_8wyDzAHrkmrf2l1OaUYFypft3xSmW7umG9m-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-673847">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
گزارش‌های تائید نشده از عملیات  هلی‌برن نیروهای آمریکایی در صحرای البادیه عراق
🔹
برخی گزارش‌های میدانی از انجام یک عملیات هلی‌برن (پیاده‌سازی نیرو) توسط ارتش تروریستی آمریکا در منطقه صحرای البادیه واقع در غرب عراق خبر می‌دهند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/673847" target="_blank">📅 19:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده ماهشهر: هر تیری که آمریکا بزند، ۱۰ برابر پاسخ می‌دهیم
امیر حیات‌مقدم، نماینده امیدیه، بندرماهشهر و هندیجان در مجلس در
#گفتگو
با خبرفوری:
🔹
ترامپ آدم دیوانه‌ای است که اصلا تعادل روحی و فکری ندارد و به جای آن‌که در بیمارستان نگهداری شود، در کاخ سفید است. ما با دولتی مواجه هستیم که هیچ اصول و منطقی نمی‌داند، اصول بین‌المللی را زیر پا می‌گذارد، نه دین دارد و نه آزاده است.
🔹
هر تیری که آن‌ها بزنند، ۱۰ برابر پاسخ می‌دهیم. جمهوری اسلامی اکنون در موقعیتی است که به‌طور کامل می‌تواند پاسخ دهد.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/673846" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJN_lgOKcby05UuIc8xOS2U8j_DDhNDA5BKHPlNoeBzcwtUjbfJtDQx1nEM2dgn2wEowbcogI08ACQyX7xpE6ZHdR_YFqGvei2ldMQEMsH6sqPigz6L67X0T3iiSzAg1ZSALoBRA6eATJe0p3h_T1Cxj1_FHxzSguSmeoBVC7Ik40CS7QbKcbod2tGJ_UplW7OKTbDBPzlPwHFUOtAZVY_-PsK9JYPdnShXIVd2dk6teSTHDpMc1TYhfdZ-pcjncr4Te_x0BZ8__NJhCqA8maxWmyUHxev1Ta5s2H94RyjgdVTjJ02aIqwHYy_KTKML6n8j5eTrdtiQJ1hydW1amRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقتصاد دیجیتال؛ پلی میان دارایی‌های خرد و فرصت‌های بزرگ
🔹
اقتصاد دیجیتال امروز دیگر صرفاً به توسعه فناوری و ارائه خدمات آنلاین محدود نمی‌شود؛ بلکه به یکی از مسیرهای جدید برای مشارکت مردم در اقتصاد، خلق ارزش و افزایش بهره‌وری تبدیل شده است.
🔹
سعید علی‌عسگری، مدیرعامل «میلی»، در دومین روز همایش «چشم‌انداز اقتصاد ایران ۱۴۰۵» با اشاره به روند تکامل اقتصاد دیجیتال گفت: پس از ایجاد زیرساخت‌های ارتباطی، موج جدید این اقتصاد بر توسعه سرویس‌های دیجیتال، دسترسی آسان‌تر به کالا، خدمات و  اعتبار  شکل گرفته و در ادامه، دارایی‌های دیجیتال می‌توانند به بخش مهمی از این اکوسیستم تبدیل شوند.
🔹
او تأکید کرد که بخش خصوصی در این مسیر می‌تواند نقش مهمی ایفا کند؛ به‌ویژه در شرایطی که اقتصاد با بحران‌ها و محدودیت‌های مختلف مواجه است. به گفته علی‌عسگری، تجربه روزهای دشوار نشان داد پلتفرم‌های دیجیتال می‌توانند با حفظ تداوم فعالیت، بخشی از نیازهای مردم را پاسخ دهند و به افزایش تاب‌آوری اقتصادی کمک کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/673845" target="_blank">📅 19:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673843">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f93d277e.mp4?token=fcm4OgR1jGr_Eif2kVl6ncwemC8HibRqG8jTGb-r-uVqxELPFUDHYF9SEAHYijAESRb3RRV8CnB_j6xiXPNudupVNjqpa4KAjmVFg0tIbe5CZZj_MbPZqP0OyjRnbJvXFIp0AulMwtQjPWWZfxHL0hzzOatO0LLRtmwtKjPkk0rizvxDPeGT0mHqZ-25x0Wj5RsirbaSQ9lYY6A5B30ty44mokIFzGIFw-kn6CWd5-HN6oiK72yMzgLhDtl_eC1YZXeWFDhX7GQEwfnhiKVQVPOIax1sOKHmiCbWVobBvas0IOw3RT7BFkYlWIcMAzmZjnKIeu_4jFOVx4UGjk4n2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f93d277e.mp4?token=fcm4OgR1jGr_Eif2kVl6ncwemC8HibRqG8jTGb-r-uVqxELPFUDHYF9SEAHYijAESRb3RRV8CnB_j6xiXPNudupVNjqpa4KAjmVFg0tIbe5CZZj_MbPZqP0OyjRnbJvXFIp0AulMwtQjPWWZfxHL0hzzOatO0LLRtmwtKjPkk0rizvxDPeGT0mHqZ-25x0Wj5RsirbaSQ9lYY6A5B30ty44mokIFzGIFw-kn6CWd5-HN6oiK72yMzgLhDtl_eC1YZXeWFDhX7GQEwfnhiKVQVPOIax1sOKHmiCbWVobBvas0IOw3RT7BFkYlWIcMAzmZjnKIeu_4jFOVx4UGjk4n2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای که دیروز گرفته شده، خسارات گسترده‌ای را به پایانه صادرات نفت خام اسکله شمالی شرکت ملی نفت کویت در میناالاحمدی نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/673843" target="_blank">📅 19:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ac18bcd6.mp4?token=G2enAgCdsQtLsTVZM-xKCOuISitMlK5oCSv3BzhC2LqpYlBEUMYSFKqhI2cGU0EM359tMca0RfawHsfO3zYUyHpogxf0PnWWhVsrNxIxUlOBARKV-KVyWtoTLLturvB6AG1f9hHKNn5_o5rZOVfNbqe6YsYOaFFTceIfWVYvTgWgJGvwL-d__GiCx8ebAa35PJN9BVgJnqD1ZGGb54lQZtL99K-wPyK0DtqddfmaCuEM29nlvl72gAbMNsGJXhMyJ4UJ8-fZpLDa4p_BK_yqIwBh6AGKYIPd8miPxh7mXcC_TXtbxbzCnub3tHWPqhhOH8g6d475asylb3oqmKyrtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ac18bcd6.mp4?token=G2enAgCdsQtLsTVZM-xKCOuISitMlK5oCSv3BzhC2LqpYlBEUMYSFKqhI2cGU0EM359tMca0RfawHsfO3zYUyHpogxf0PnWWhVsrNxIxUlOBARKV-KVyWtoTLLturvB6AG1f9hHKNn5_o5rZOVfNbqe6YsYOaFFTceIfWVYvTgWgJGvwL-d__GiCx8ebAa35PJN9BVgJnqD1ZGGb54lQZtL99K-wPyK0DtqddfmaCuEM29nlvl72gAbMNsGJXhMyJ4UJ8-fZpLDa4p_BK_yqIwBh6AGKYIPd8miPxh7mXcC_TXtbxbzCnub3tHWPqhhOH8g6d475asylb3oqmKyrtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر رفاه: کالابرگ برای برخی دهک‌ها افزایش می‌یابد
🔹
مهلت اعتبار کالابرگ خرداد تا ۱۴ مرداد تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/673842" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673841">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913265ae74.mp4?token=mwQ78Np4NLxT6Ii0MnoHn-Y-6x0zm-p2vIwk3fkYsuV9TLNMKXqQJdxWy7blvDvoay0IUvJRTSUfvFnyrRivxfN9MCdoY32lWoKdnuGFS8RTWrsrU5Og0Its3x6gvfEocHx9wUfzRdloOnqQ2hFMqjtrcfhpjDouUfFANx1nMywl8L3PvpkhJNJULjuku9rCF6exJcg8o4RgKYDE8X-Alj46qCVvX781tdMgYy8GXWMQOyKiwW325WbKya5lpjXgQIKRaikxiVAFHDscQfpwP1f2Qds5-kxLXVvwU9ZsvjMy5M8MgPnSVFSQLWLjns9adCC6OETj4kVkB6QOzjJ17pgEufs1XY_SWfO_kS2lUCKmySTQkDfaXePaiAU_TfagvNNj11ciBbCf5LpOFdOWRIx7VXWjQ9EqCIjIdGwE0nLwBLbotFf0YGAfroOtW8JTogUrA6wDDKB4pAG_c7fgIQtZczWRtZ0elOhTLnopj6kAfzn6EF_4IoxP7dsdil_njFoMhk0inSG3usqZKtsPcza8qSw-VMqH14KR0zAl2Gh05D3lMIHcIhRdc5O-iGFd5NsS5hmZwoDlbUG6uM_NI1tC_MxxcT_KzqOqxlWUcalkcqjJzQ1EWwC9gIFsoNodtGS4jPJnCJ4Dbag1skH4G0F5dO5ZPNUkI7eWOY4oZVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913265ae74.mp4?token=mwQ78Np4NLxT6Ii0MnoHn-Y-6x0zm-p2vIwk3fkYsuV9TLNMKXqQJdxWy7blvDvoay0IUvJRTSUfvFnyrRivxfN9MCdoY32lWoKdnuGFS8RTWrsrU5Og0Its3x6gvfEocHx9wUfzRdloOnqQ2hFMqjtrcfhpjDouUfFANx1nMywl8L3PvpkhJNJULjuku9rCF6exJcg8o4RgKYDE8X-Alj46qCVvX781tdMgYy8GXWMQOyKiwW325WbKya5lpjXgQIKRaikxiVAFHDscQfpwP1f2Qds5-kxLXVvwU9ZsvjMy5M8MgPnSVFSQLWLjns9adCC6OETj4kVkB6QOzjJ17pgEufs1XY_SWfO_kS2lUCKmySTQkDfaXePaiAU_TfagvNNj11ciBbCf5LpOFdOWRIx7VXWjQ9EqCIjIdGwE0nLwBLbotFf0YGAfroOtW8JTogUrA6wDDKB4pAG_c7fgIQtZczWRtZ0elOhTLnopj6kAfzn6EF_4IoxP7dsdil_njFoMhk0inSG3usqZKtsPcza8qSw-VMqH14KR0zAl2Gh05D3lMIHcIhRdc5O-iGFd5NsS5hmZwoDlbUG6uM_NI1tC_MxxcT_KzqOqxlWUcalkcqjJzQ1EWwC9gIFsoNodtGS4jPJnCJ4Dbag1skH4G0F5dO5ZPNUkI7eWOY4oZVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای دو نقطه اصابت جدید را در پایگاه هوایی ملک فیصل در اردن نشان می‌دهد
🔹
یکی از این اصابت‌ها به محوطه استقرار هواپیماها برخورد کرده و همچنان ستون دود در محل مشاهده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/673841" target="_blank">📅 19:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673840">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ecd7985c.mp4?token=og-eLKKQ8bNzFVCCN5oJPXuTS2CFPngVBwFRbZ6T4ACxKh2sacvOKfAHSFo2RsBgGGBQVQfIJ8FWx4MHq8nRSQcqy1MQDa9ATIgdLbYokI_DB8k7ezGKlcJnYnJmIhiKeanXC9vvKKVV0AT8Admp1-pj9_Ve-4bKieU-2RUbgrYMK7NDkyFq5TDUUn5ExSJLpt-mnRP5PEofALzGm0CPEuBIjkm_jDIYQoQBehdzlOsggz5jVb9TVCWJ-6MF5mCNmPygaGZl1K9Tpp446yQpH9u6EA4BcZqihuKVb3jFMt5gxvUw-3hg_S045qnDKY-OqvxjdMK9BHDLNLW07O8ZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ecd7985c.mp4?token=og-eLKKQ8bNzFVCCN5oJPXuTS2CFPngVBwFRbZ6T4ACxKh2sacvOKfAHSFo2RsBgGGBQVQfIJ8FWx4MHq8nRSQcqy1MQDa9ATIgdLbYokI_DB8k7ezGKlcJnYnJmIhiKeanXC9vvKKVV0AT8Admp1-pj9_Ve-4bKieU-2RUbgrYMK7NDkyFq5TDUUn5ExSJLpt-mnRP5PEofALzGm0CPEuBIjkm_jDIYQoQBehdzlOsggz5jVb9TVCWJ-6MF5mCNmPygaGZl1K9Tpp446yQpH9u6EA4BcZqihuKVb3jFMt5gxvUw-3hg_S045qnDKY-OqvxjdMK9BHDLNLW07O8ZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار: اگر فردا آنجا (ایران) را ترک کنیم، موفقیت بزرگی به دست آورده‌ایم اما ما فردا آنجا را ترک نمی‌کنیم
🔹
خوک‌ هار: ایرانی‌ها در حمله به نظامیان ما اردن موفق بودند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/673840" target="_blank">📅 19:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673839">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
وزیر جنگ دولت تروریست آمریکا: به ایران فرصت داده شده است تا مذاکره کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/673839" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673838">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293924ca0e.mp4?token=v9N2L0D1YMZfYfO36G0YUjXpG29MUE3TM3wVkOE-Q53s2xDTtaGF-cKmupd9gR98-CXIzcsj_cwv0J9CrZbBs6xicRD3oAw0jO2i4er0Ii5hmd7QU5dB3RYCcAj9F1syak-uqwvUk2fv0tJ_6lO7QUwrWgnwsiVmfVLvSaqx57DZsazmmn0lgKaVdM770Is4B9dK7YJ-vXdEmnfefMeck-De7c2MroURNy6UNEW93zkwg9F-COfstJ3bAeua0kHf83apO4vQdqW0kveUIJ1OvY5NfEI8X1O4vuyjjl3ywgGgBy2sqxQ2EbvMLmT7iHqhTWUgLj6dNTAXSJQjxzjLcHYVWOu9KVcnV1DfwoRkpqi8Mhh8snAAtTMrobpZbAmO2TDvGinqppaiBtj0S3D091SUkxO5azzBwN12Ie4yIo1PpoJ0bOgE6dgjQX894BAsPlBS3Mk9_mcBi1WMXL37N5A61BWGs7frmfaEHGcTnZQjXJj_PuIdkxbznTED02jUtnAAsYJ8DE8Ds8Wr6QyfjPEz84iUKQPoRbCmryTcNu6srT87zCGFUuKDEemnNt7HCO4q_Z-xCliAawZLN98CgT0JKSY4Mdxt0uXFnaqvqg6PwGJbg55iyzfBnSA_kQvVECPEUmMywhJwvYuBEllx0sHFYHpNkgn901EDferpFUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293924ca0e.mp4?token=v9N2L0D1YMZfYfO36G0YUjXpG29MUE3TM3wVkOE-Q53s2xDTtaGF-cKmupd9gR98-CXIzcsj_cwv0J9CrZbBs6xicRD3oAw0jO2i4er0Ii5hmd7QU5dB3RYCcAj9F1syak-uqwvUk2fv0tJ_6lO7QUwrWgnwsiVmfVLvSaqx57DZsazmmn0lgKaVdM770Is4B9dK7YJ-vXdEmnfefMeck-De7c2MroURNy6UNEW93zkwg9F-COfstJ3bAeua0kHf83apO4vQdqW0kveUIJ1OvY5NfEI8X1O4vuyjjl3ywgGgBy2sqxQ2EbvMLmT7iHqhTWUgLj6dNTAXSJQjxzjLcHYVWOu9KVcnV1DfwoRkpqi8Mhh8snAAtTMrobpZbAmO2TDvGinqppaiBtj0S3D091SUkxO5azzBwN12Ie4yIo1PpoJ0bOgE6dgjQX894BAsPlBS3Mk9_mcBi1WMXL37N5A61BWGs7frmfaEHGcTnZQjXJj_PuIdkxbznTED02jUtnAAsYJ8DE8Ds8Wr6QyfjPEz84iUKQPoRbCmryTcNu6srT87zCGFUuKDEemnNt7HCO4q_Z-xCliAawZLN98CgT0JKSY4Mdxt0uXFnaqvqg6PwGJbg55iyzfBnSA_kQvVECPEUmMywhJwvYuBEllx0sHFYHpNkgn901EDferpFUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر ماهواره‎ای از خسارات واردشده به پایگاه هوایی موفق السلطی در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/673838" target="_blank">📅 19:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673837">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
موضع خوک هار درباره محاصره دریایی یمن علیه عربستان  ترامپ در واکنش به محاصره دریایی بنادر عربستان توسط انصارالله:
🔹
«هنوز اتفاق خاصی نیفتاده، اما در صورت لزوم اقدامات لازم را انجام خواهیم داد.» او با اشاره به تجربیات پیشین در برخورد با حوثی‌ها، مدعی شد که…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/673837" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673836">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/172556ab59.mp4?token=KgGBo7upYbmXBRbMhChbgZwUoUyOz_9EDnoy3Y1AYYVI7-UhgdZnVw-xCeVFvp-G70kzbq5yVpIwLKt6SOfeMuQSuPiMG-JjyEDPgb2ymABuHfFev7qBGxaOCI1__r2Mjruj4vtcOF0jtg8eLPbmg9TQ2MOyexD8KEFyVzEorRwHR5IdbXink1O_ZxrcJHEdZtd9_0RhaumBbafO43IEuT4DObHW1bt6NjFh5ktWat_UxCfIN3WW6I9kYCMUQDjXijJHmW1Dkq5e4qzSFClus7RPKGqM6qG9qm_0L_q-QG3hsd2o5y8WRlJ4R_2xMxZBU7IzYK4SmxW9svlZoCYoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/172556ab59.mp4?token=KgGBo7upYbmXBRbMhChbgZwUoUyOz_9EDnoy3Y1AYYVI7-UhgdZnVw-xCeVFvp-G70kzbq5yVpIwLKt6SOfeMuQSuPiMG-JjyEDPgb2ymABuHfFev7qBGxaOCI1__r2Mjruj4vtcOF0jtg8eLPbmg9TQ2MOyexD8KEFyVzEorRwHR5IdbXink1O_ZxrcJHEdZtd9_0RhaumBbafO43IEuT4DObHW1bt6NjFh5ktWat_UxCfIN3WW6I9kYCMUQDjXijJHmW1Dkq5e4qzSFClus7RPKGqM6qG9qm_0L_q-QG3hsd2o5y8WRlJ4R_2xMxZBU7IzYK4SmxW9svlZoCYoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی: نهادهای اطلاعاتی باید پاسخگو باشند
🔹
برداشت مرحوم شهید لاریجانی این بود که بعد از جنگ ۱۲ روزه آمریکایی‌ها به سمت جنگ نمی‌روند.
🔹
بعد از آشوب‌های اجتماعی دی ماه ایشان هم به جمع‌بندی من رسیده بود که آمریکایی‌ها هدف‌شان این است که بخواهند تهدیدات‌شان رو عملی کنند./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673836" target="_blank">📅 19:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673835">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
واکنش سگ زرد به احتمال توقف درگیری‌ها با ایران
🔹
دونالد ترامپ در پاسخ به پرسشی درباره عدم وجود نشانه‌ای برای پایان جنگ، مدعی شد که مذاکرات پشت‌پرده در جریان است و ایران تمایل دارد برای خاتمه‌دادن به تنش‌ها دیدار کند. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673835" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673834">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgWTPkxWnt1oQvZUQdp5SQmDUFNU_WOKRLcIVfgiYqCL82VhbgOzlP6S6W8mt3PDkBB52ttPZGkQaCQvb_-i1r7eJq9KjAkywwadm0qw5kpRS89LTequpo4aLy8WjtJ6ITRHaJcmO8-UzANemF2M44JlXBeiGOE-kd17d7RM4_BsTSJZAAVpE0-KOz9XT7f4lc3ZAY32Y0xMqba94cM3s_LRuG4qW0pZvTyFIAPmv-KJVMX1i2V2f9kG97loQCYp3VvnWBbUiOksFuCMHc8h-heQbT-cpt45N3UiGe15veWBU2-HfscGKT5VB4P_spNrnKS1QV8FQJZ6BO399RnvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز آسمان تهران؛ شبی که جنگنده‌های ایران به مصاف «اشیاء ناشناس» رفتند!
🔹
در ۲۸ شهریور ۱۳۵۵، گزارش‌های متعددی از مشاهده نورهای عجیب در آسمان تهران مخابره شد.
🔹
دو فروند جنگنده اف-۴ برای رهگیری اعزام شدند، اما خلبانان با اختلال‌های عجیب در تجهیزات راداری…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673834" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673833">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
واکنش سگ زرد به احتمال توقف درگیری‌ها با ایران
🔹
دونالد ترامپ در پاسخ به پرسشی درباره عدم وجود نشانه‌ای برای پایان جنگ، مدعی شد که مذاکرات پشت‌پرده در جریان است و ایران تمایل دارد برای خاتمه‌دادن به تنش‌ها دیدار کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673833" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673832">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c855cd6504.mp4?token=Y1BCouz08P8PtDjliOoaj0-5fD74ZchifsRn0MkaLKRDEBlyZgpcqp6QpJ_SD6Ah2nU1LOn18ssBZQ0hCaX9U3f5o02Qx39EUdtqG3vrw2iMqnYThU80rtUdk5TFGYP4gwRHCkQRMq7qGyz2Fab-ossrstaTcUzKa-2sKckiTdl1CvD30XDQDheiSnHCybLyj8rR0fyi5MIkHnteSP2TlCdtLUEqxjx8k3pPvgVLVcVSnpOmuV5f5CyUSI5ZBYWFmD5k8euclg_SiQUpKs49QHtpQw0g_oyWBhsbXDxRnim8mCdHpNzN8M_rx9ofNKxhYzbtMeDCxmzMVKofPOGjHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c855cd6504.mp4?token=Y1BCouz08P8PtDjliOoaj0-5fD74ZchifsRn0MkaLKRDEBlyZgpcqp6QpJ_SD6Ah2nU1LOn18ssBZQ0hCaX9U3f5o02Qx39EUdtqG3vrw2iMqnYThU80rtUdk5TFGYP4gwRHCkQRMq7qGyz2Fab-ossrstaTcUzKa-2sKckiTdl1CvD30XDQDheiSnHCybLyj8rR0fyi5MIkHnteSP2TlCdtLUEqxjx8k3pPvgVLVcVSnpOmuV5f5CyUSI5ZBYWFmD5k8euclg_SiQUpKs49QHtpQw0g_oyWBhsbXDxRnim8mCdHpNzN8M_rx9ofNKxhYzbtMeDCxmzMVKofPOGjHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی
:
در پرونده برجام، رهبر شهید با وجود اختلاف‌نظر تصمیم را به جمع‌بندی مسئولان واگذار کرد
🔹
رهبر شهید به خرد جمعی اعتقاد جدی داشت. این خرد جمعی را در نهادهای مشورتی، در شورای عالی امنیت ملی، در نشست سران قوا، در دولت و در حلقه مشاوران و مستشاران مورد اعتماد خود جست‌وجو می‌کرد./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/673832" target="_blank">📅 18:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673831">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد امتیازات ویژه برای دانش‌آموزان مناطق جنگی
مهدی کاظمی، معاون وزیر آموزش‌وپرورش دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
همه‌ ساله اتفاقاتی مانند سیل یا زلزله در برخی مناطق داشتیم که برای دانش‌آموزان آن مناطق، شرایط یا امتیازات ویژه‌ای در نظر می‌گرفتند.
🔹
از آن‌جا که شرایط جنگ به‌صورت سراسری و یکسان نیست، برای حفظ عدالت‌ آموزشی می‌توان چنین تدابیری را انجام داد تا این دانش‌آموزان متضرر نشوند.
@TV_Fori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/673831" target="_blank">📅 18:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673830">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رسانه هندی: موشک‌های ایران وارد نسل جدیدی شده‌اند
رسانه Firstpost:
🔹
موشک‌های ایران در حال ارتقا بوده و با بهره‌گیری از فناوری موسوم به MaRV در حال تبدیل شدن به سلاح‌هایی پیش‌بینی‌ناپذیرتر، دقیق‌تر و مهلک‌تر هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/673830" target="_blank">📅 18:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673829">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
هشدار ایران به بلغارستان درباره میزبانی از هواپیماهای نظامی آمریکا
سخنگوی وزارت خارجه:
🔹
هرگونه همکاری بلغارستان در میزبانی از هواپیماهای نظامی آمریکا جهت حمله به ایران، مشارکت در جنایات جنگی محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/673829" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673828">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71544cd353.mp4?token=dU65xmVGLRZLy60KFd8ap5TppCf5L-k81TvR-U6iO2HfXbZf_39hY9FtFWqsvOAPbuMw-rW5ShRp35yGTUBefVvAoLpPZ8KikuyZSYgBAYWEw016YVSqigRMOa4AZ9QcdQi0Q1MZKbptjHEhV4T5_WFuUUGthmPsQBiNwUq7CiCecOkJ7_qPUnFN4EJIncrI5435oEEIgLfP5TWmy6Z6RRRGOhBba18tSsX2_VdkdcI6xCu6cEzvSgPco1PwEAac5zRBWVH7quIuGCASSGDa1y-e1PN76WnL8ENkXlLkLTPlZ7_-V_c3G13aY034ofllAd5BRf2IWtzO7ZuOkt6-0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71544cd353.mp4?token=dU65xmVGLRZLy60KFd8ap5TppCf5L-k81TvR-U6iO2HfXbZf_39hY9FtFWqsvOAPbuMw-rW5ShRp35yGTUBefVvAoLpPZ8KikuyZSYgBAYWEw016YVSqigRMOa4AZ9QcdQi0Q1MZKbptjHEhV4T5_WFuUUGthmPsQBiNwUq7CiCecOkJ7_qPUnFN4EJIncrI5435oEEIgLfP5TWmy6Z6RRRGOhBba18tSsX2_VdkdcI6xCu6cEzvSgPco1PwEAac5zRBWVH7quIuGCASSGDa1y-e1PN76WnL8ENkXlLkLTPlZ7_-V_c3G13aY034ofllAd5BRf2IWtzO7ZuOkt6-0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب‌های رمزی در بندر کنگ؛ میراث نجاری قدیمی
🔒
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/673828" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673827">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5Cha6FbafzcyaOs2Cdnt4DVfUerVxLvBhZVWHZERqEKlkouVenCnBY7Ka0GzkASW-TSYx8zseaqqXaAMj8SwyY69UsnlbLDNnKrTjy1Yn9LaJC-TWp71dwKKt4Yd9k9n8HRDx-VTqexh2OixKZhXdjhGoNVhsuivESraOX83c56AxrdLdOY_hIAWyrH7DKMb7Z5jFSpSVgzjJ6Rs_b8-c36RshdVOX69fg82e8XkSGGwH9kEUDllKE2YJUclfNxMNw9s7kkiRK-N5WDqJIQrcnAZOOR-LIdhtx310UBIF6qDdaz6VlyU189wuV2DaUTM2OxkI_y14bgv3jjkn6Jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت ۱۴ ماه نقش‌آفرینی بانک صنعت و معدن در توسعه‌‌ی‌کشور
🔹
بانک صنعت و معدن در دوره ۱۴ ماهه منتهی به پایان اردیبهشت ۱۴۰۵،  با رشد شاخص‌های کلیدی عملکردی، مسیر حمایت از تولید، توسعه تأمین مالی، تجهیز منابع، گسترش ابزارهای اعتباری و پشتیبانی از اقتصاد دانش‌بنیان را با جدیت دنبال کرده است.
🔹
این اینفوگرافیک، مروری بر مهم‌ترین دستاوردهای این دوره و روایتی فشرده از عملکرد این بانک در مسیر نقش‌آفرینی برای توسعه کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/673827" target="_blank">📅 18:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673826">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt56oD0UfPrqhe5SQi7E94_13sHiLTi8GlfSrVjrRj0yPM0MPBrYQbPrWYbFjx7Tn7dTKjnUGPn7hNNSeXfTG8mNLgwZicLf3QJd0JMWZ0eMmRWjIJ27I2pF0oxkoFeOR8-O-oBIcal-s6WaXcIXjbTY5ZW_fS7Rcz1bmsnonwn7dE_rGbZYk5vdmwUipDMKcdj4v58R4gfgcvXVn-KcOPf1oa7t50ps7RKqvI3aJb8kkMGg_Lv7vgSNJ4PXN5bzC65NQ-W9DgYLlGVFlnU3SOJetwo-yh07FxomK0zKA9gZOKCK2W8yTkNIXA3v_7NfPfyyJS3duV6lj9EX9G_dVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش کویت: پدافند هوایی ما در حال حاضر در حال مقابله با حملات موشکی و پهپادی ایران است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/673826" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673825">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXpXMeFO0uvB65ita11ya44bLVLQiDtbavaWqAjeVp2aoemG6sbXmdjk4qX-qKcf4vDEC7F31_NJ_4lx2HypnXgftRZXtQ2QZTuCfGvkI2Xkc2RbFsUOmaq8cn4Lir6BLVMybPAXr_IoQulbZqQ7GCBAcDLoNzOrOnebGYoTKjRYG2BS1fjY5qf07lsJ4gQm2NAtVmnWS5hL9qwwfabR19e8ROtjt4afnD6cjByE-KXN2DlP5T97vYtSThIC9y2b8Irau_wL7gzbMxEAxHxPyx8a00eeEzWFEUo2fGZLNufRuL4ZuIUxV1RMDWTTW_1VGcfeG00n-AAee37_2LxJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلومبرگ از تردد نفتکش‌ها در باب‌المندب  خاویر بلاس، تحلیلگر بلومبرگ:
🔹
برخی نفتکش‌ها در نزدیکی تنگه باب‌المندب تغییر مسیر داده یا سرعت خود را کاهش داده‌اند؛ با این حال، اکثر نفتکش‌ها همچنان به تردد خود در دریای سرخ ادامه می‌دهند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/673825" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673824">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163ba97ea2.mp4?token=L33CseHNS8KIKTn7CPPw002Sh7jY5mUzkFOc5A71_yspL7ymZt-K6PXiHVnss_XN2g98KHQMLKhkSc5mUa5RRL1AxToE6DZx6RlpIRBKpvpypZRrNHEyL6_hFwKJpbG3Va4hGwjW15Nha4l966thNBA5XBiZVpjC6OO-XbK1gcKysMQl0Qg5QRXZm-UpPRl6zf6kwfRe9-En5oNc-9IUtf8Y_A0BnMfa_lWWcUS0vB2HcbPaXkkZkcKSrgiEiHzuNeUprJMmFexXZLz7REJx-lGGqkZM8UG58cApNvh0iGRnEOC00GqJvwynSetp8emDzEx84uWmPVOsRVuC0dv1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163ba97ea2.mp4?token=L33CseHNS8KIKTn7CPPw002Sh7jY5mUzkFOc5A71_yspL7ymZt-K6PXiHVnss_XN2g98KHQMLKhkSc5mUa5RRL1AxToE6DZx6RlpIRBKpvpypZRrNHEyL6_hFwKJpbG3Va4hGwjW15Nha4l966thNBA5XBiZVpjC6OO-XbK1gcKysMQl0Qg5QRXZm-UpPRl6zf6kwfRe9-En5oNc-9IUtf8Y_A0BnMfa_lWWcUS0vB2HcbPaXkkZkcKSrgiEiHzuNeUprJMmFexXZLz7REJx-lGGqkZM8UG58cApNvh0iGRnEOC00GqJvwynSetp8emDzEx84uWmPVOsRVuC0dv1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیب جادویی آب داغ، جوش‌شیرین، نمک و کمی فویل آلومینیوم برای تمیز کردن نقره
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/673824" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673823">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6oqqmyOWxcre_R4rNm2mvClJDqrIlEHE6489iEI7_bgugSHA_S6NYQswXjH1ybQtXrZAXuTg25Z3BKqs3YLaVzD875yUOL_I-fNY6hcT2hlHYTCccLiro-Wx6od8qVdDjaEeTKwwaXplEDOtiMULJYNV-Ta1Y5uT0AwLrS7aAorlqsq3gAZ2oOY67BJKs0lp6sfva63OjJ3DRCeonhRzUyuIVS8xWton3U94qQMppciXFFp_wkSFXPL2TH8HGYayIhwEl1fKlcNmvALm45XXHnRA5Wnfr_9Rm661BBtuGL9MaRzyc1QyzDQs_xJ3GbykF2bSq2PM-wLkgQ2_VjYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منبع نظامی یمنی: ۶ کشتی در ۲۴ ساعت گذشته پس از هشدار نیروهای مسلح و اعمال محاصره دریایی علیه عربستان متوقف شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/673823" target="_blank">📅 18:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673822">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9Z6k2Z4MBPMnOWIv09VbYXb11ZSQySsNT3--7cTUdsIzYG31H0VVvmLXFJrMNM1UHBWEuTHSzIvIB4Y7ii0uPyUwUzOsj9Jp65vsmIw1GaFF1WG1lQk7wDed_9sQXIV24Uy0_hCqTY8poZIddDgk9WoBkkpCSSAE3ir1GW5LG0T6awZHWSopwVzxNi3VJgcXS3hkv1b1t2DtuZFFqvmauwBb6d1eh2mwBC50tTnB_S_e7U4yO368BHYxcmZktC49EjTXUC3lBbTPvjLzoQtA8SS0Movp-4-IN-sy98Za_qFUKaiFT5ArM8739KHjA9wTf1FGNpA5rIwyw3m0qKplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیسعلی دلواری؛ مردی که جنوب ایران را به گورستان استعمارگران تبدیل کرد
🔹
وقتی ارتش بریتانیا به سواحل جنوب ایران یورش برد، رئیسعلی دلواری با تکیه بر غیرت و شجاعت، پرچم مقاومت را برافراشت.
🔹
او با جنگ‌های چریکی، ضربات سنگینی به نیروهای انگلیسی وارد کرد و در…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/673822" target="_blank">📅 18:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673821">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/673821" target="_blank">📅 17:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673820">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAvid Academy</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THfIP6__fvJvBV6GaGb5Hk6OZV1SpeKg2rhYiKLBysOI95aw19kOlH1SucgN3Gszm1A7HidpkxqDIyC9BIz3l5hJj9kYYPU5YTu-tLXFT31bsj3SJaJQlueOHnDPBoOM0uHmFDSDQhznOesv4Wp-A4FSSCtVT4_2a66IycwNwzG0Yxpju5GSkTUQjNBDn7rBA3BWGGKnuS3RYaRYl72VEmZMTrXNdteVhIqREatHTAF0lg9_cc5Aw1TWLOf6NqSl0d3UBM4-pbTPob3mYvlAEFY3fcAwS-TsvDCWosz5Ojv2L7wL5wm-wsxB-eNjf7d9YmSv3HgJ_6GyMLXGm3Qqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادگیری خبرنگاری از اساتیدِ تراز اول!
🎙️
@avid_academy
@avid_academy
۳۰ ساعت آموزش تخصصی با مدرسین هلدینگ «خبر فوری» و «اخبار مشهد»:
👤
محسن ناهید
(معاون خبر و مدیر تولید خبر فوری)
👤
سعید برند
(سردبیر اخبار مشهد)
✅
فرصت ویژه:
امکان جذب برترین‌های دوره در هلدینگ رسانه‌ای «خبر فوری»
🚀
شروع مسیر حرفه‌ای شما از اینجا کلید می‌خورد.
برای مشاوره و ثبت‌نام سریع:
📞
09981897105
@avid_support1
@avid_support1</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/673820" target="_blank">📅 17:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673819">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان: ما به نقش خود در میانجی‌گری ادامه خواهیم داد و به صلح و ثبات منطقه‌ای متعهد هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/673819" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673818">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان کل کشور: پرونده شهادت رهبر شهید و فرماندهان در داخل و خارج با جدیت پیگیری می‌شود
🔹
مجمع تشخیص مصلحت سازوکار برگزاری جلسات مجلس در شرایط اضطرار را تأیید کرد.
🔹
پرواز‌های ایلام - مشهد در آستانه اربعین مجددا برقرار شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/673818" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673817">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw2F5hg_KCejZk5eOl3G7S41LfCW_r67MkDNwMklDGZxHUbq3fAMi8_3j3CjZ_QxRua--be7k3bY5k1ZQ8DHLBqqcQwOmf0RJtZpQ3A_eXKI7C23sSRqOpIteuRHkKDXUSG5xJacgqmpw8XGAdYuevhFS-rPON5d4_QwVFJQb4JgaEpl26VtU0_7ULJVuIQTLAJlV7Y49IS3YRMfvZ-JxjqF69OtkGSqs3-K2_20lyNmaCwGAQHRKl3t8gfKcexi0BXC5qNcTXpPaep540zxAlk-WqtJ9uTy9hSmXDt6JQhu4OwiBTmlFaS8Fk9oi_AbTSDWenuKbh6VEoaOCivscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ۹۱ دلاری با بسته‎شدن باب‌المندب
🔹
پس از بازگردانده شدن دو کشتی پاکستانی حامل نفت عربستان، قیمت نفت به بالای ۹۱ در هر بشکه رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/673817" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673816">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6973d0cf51.mp4?token=I6VtBJrPyUX2bCFHr54KJVYddtrCrdgBLEWh6aaAwRLPgfQwCpPr851tqwVB3IWVHkvPnjjIHuSU51VRXOetFJCkVKDY17hKD2KU4KjUJcL1iExXirfeYq0NJ37rIYqlcCjGe0Qy9SpPKjqQMtdRrhIFMZZTli4C2SmZPLfHHPonKPIVT7gfJB8vy2wqWweZx95RMx-mwR-O3JDmfQYnh3S1k_i5BRfEts1_5oRkf80lGNwgdg2qMvMOOEdhVrNop0Y6qjrMkmpGBr3bL6O6kxWMDHsdN4X1lDKuXnrszSgJzfmZhxOGRG_DUVU9x-vmmvzRLl4JqkwrDmrBnGaiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6973d0cf51.mp4?token=I6VtBJrPyUX2bCFHr54KJVYddtrCrdgBLEWh6aaAwRLPgfQwCpPr851tqwVB3IWVHkvPnjjIHuSU51VRXOetFJCkVKDY17hKD2KU4KjUJcL1iExXirfeYq0NJ37rIYqlcCjGe0Qy9SpPKjqQMtdRrhIFMZZTli4C2SmZPLfHHPonKPIVT7gfJB8vy2wqWweZx95RMx-mwR-O3JDmfQYnh3S1k_i5BRfEts1_5oRkf80lGNwgdg2qMvMOOEdhVrNop0Y6qjrMkmpGBr3bL6O6kxWMDHsdN4X1lDKuXnrszSgJzfmZhxOGRG_DUVU9x-vmmvzRLl4JqkwrDmrBnGaiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
قیمت با تخفیف
❌
فقط 899 تومان
❌
✅
سه روز ضمانت بازگشت
✅
پرداخت درب منزل
🚀
عجله کن! لینک خرید اینجاست
👇
asrefardabale.affdn.ir/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
asrefardabale.affdn.ir</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/673816" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673813">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای العربیه: ترامپ از نخست‌وزیر عراق برای میانجیگری میان ایران و آمریکا کمک خواست
منابع آگاه به العربیه:
🔹
واشنگتن به نخست‌وزیر عراق چراغ سبز داده تا با تکیه بر روابط بغداد با تهران و واشنگتن، در تلاش‌ها برای کاهش تنش و پایان جنگ میان دو طرف نقش‌آفرینی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/673813" target="_blank">📅 17:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673810">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTgermHOrJ9FMWP2F1Hw0lElWiXS7dvzTQQJxC-Uknxqph8Gk2BwMBdbh7bgv6hUDq_soFczbxWg13pxZVTNOjy-QKzuCHdNhJiMhbfxxwGxJFB5UZ65WJVi7Axd2D6KDZXWXjtzAQzycvlI1DqXKmD6Kdub8PzUINU1yQcUfrGBC3FhakI5VHdS639mpD9nMWg6dKQr3_PJh9WC-eQVaN2aPNXJs4pGdA_WIQ37J4CwrYPGQyC2gWGLE4q5FAOJPaSesIL55uw_M4WdkmKAJrt-YAZmSZYx-S5Pdiknaze3u15K9saOepWydJnxXJtEyYP0xWB3HYeZm2Kto8fWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nI9M8Hl9fbG3oK_3PMAbv4t4S85l1zG0Rr3l7l4F_013WdgzCD3rYuQQvz_aZKlrEgcdrAzDF7_XwTMLmZ796xHWcwAHHRKYs1wFghsXHDKONhMkESjBYoadG9kF-0AbPaZ_okYB69ajG3iCCVklfrfBgxs5bObjBDoZ79aqbau_84dT0R6WoUDDWJ2JbgwaEjCAfKhXSK40X-W-wpjEC2-2QKUPQpagoe6MFVaNTCd7xqky6ppFLj7g2N-kBfy7nfc04ZKV8ncqL3ObEa4haiYA5aO-fLk7TxBU3hC4dZWlStmkaEhiZUdvp_uCTC-2PjO5SN_OpGs5BLdGrFBsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaslKmFLQ7kuXALvtsY5BpdS_G__EuJLge0FN8FVMwlqH7suNUKmshHg7oDyMOlB8ECMAz4b89CIUQBusL1_KyvWZzlrAjVbYHzRgSb6vy1qBaZSSouNyOYM59mjSnY6KBNAbrYnHttcZY_FA0XdQB12uZc1h1yJ_gUfzZW6bhmf9T1uOlqr-vleHngeejZNJEW-0D-dJ_DfxTJZGom1BGGQWUXd0453kHR9reEz5LowTvnN1vQirMPiNl3-lgIQs5glRj1KMRhxtvfdXOMkLyriphjdTlkykgk4g_RmZ3ePwt8A-fjJYkYhjjTapxc_AxcH61j6ehnwMJMAvA5MfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی ۱۵ روزه: هوای خنک‌تر از نرمال در مرکز ایران؛ شمال‌غرب گرم‌تر می‌شود
🔹
مدل‌های پیش‌بینی نشان می‌دهد طی ۱۵ روز آینده دمای هوا در مرکز فلات ایران و استان‌های مرکزی کمتر از حد نرمال خواهد بود و فقط شمال‌غرب کشور شرایطی گرم‌تر از نرمال را تجربه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673810" target="_blank">📅 17:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صادرات نفت عربستان به پایین‌ترین سطح خود رسید
رویترز:
🔹
صادرات نفت خام عربستان در ماه مه برای سومین ماه پیاپی کاهش یافته و به پایین‌ترین سطح تاریخی رسیده است؛ داده‌های JODI نیز اختلال ناشی از درگیری آمریکا و ایران در محموله‌های نفتی خلیج فارس را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/673809" target="_blank">📅 17:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صدای آژیر خطر در کویت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673808" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2fc442846.mp4?token=aDvsDjHMksgUVV9WdxGns_RKnexurldtSdO642gWw8lNdoeFqJNAqmNvvI2ffjR_VxrmNiof6r1k6BYMYVtv6QJUFaq9FdGlTfqNmivC7ZCB5ujZAe6zCAxYrV47ESFTljOfMJSChVZl8QYgnUbAfa0XKjOVt8nV0tcZrTK84HoVbltexaIhTzcEw7tit-pVAa1AtMZCDXHSAwCJ-N5hxu1EFWqcgfHHKFvc9_LOzWO85Tyz8Zgz24hz_lqdUkLtAXOtjM48R2O8OL97Mbq1UUiBXIhXIlfo-KM62JoNDm6embLF0Ad0hkJcZgm5iywmlKQgGWptbxoDs0jwDiirrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2fc442846.mp4?token=aDvsDjHMksgUVV9WdxGns_RKnexurldtSdO642gWw8lNdoeFqJNAqmNvvI2ffjR_VxrmNiof6r1k6BYMYVtv6QJUFaq9FdGlTfqNmivC7ZCB5ujZAe6zCAxYrV47ESFTljOfMJSChVZl8QYgnUbAfa0XKjOVt8nV0tcZrTK84HoVbltexaIhTzcEw7tit-pVAa1AtMZCDXHSAwCJ-N5hxu1EFWqcgfHHKFvc9_LOzWO85Tyz8Zgz24hz_lqdUkLtAXOtjM48R2O8OL97Mbq1UUiBXIhXIlfo-KM62JoNDm6embLF0Ad0hkJcZgm5iywmlKQgGWptbxoDs0jwDiirrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صداهای انفجار در بحرین و کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673807" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
پزشکیان: صداوسیما فقط بخشی از سخنان رهبری درباره عدم مذاکره را پخش می‌کند
رئیس‌جمهور:
🔹
رهبر انقلاب در جلسات خصوصی بر ضرورت پایان این وضعیت تأکید داشتند، ایران در مذاکرات با محور بازگشایی تنگه هرمز گام‌به‌گام پیش رفت و با وجود تخلف طرف مقابل، دستاوردها فراتر از انتظار بود و نباید با سخنان نادرست این دستاوردها کوچک‌نمایی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/673806" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صداهای انفجار در بحرین و کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673805" target="_blank">📅 16:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فرانسه کاردار سفارت ایران را احضار کرد
🔹
وزارت امور خارجهٔ فرانسه از احضار کاردار سفارت ایران در پاریس به این وزارتخانه خبر داد؛ این احضار درپی ادعای بازداشت کارکنان سفارت فرانسه در تهران انجام شده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673804" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkcwgFcxK7cc2PA5cZclxZTtD6-Lzu5mQTJpBw6uSjvjfNGpCgRUGt_BEhSkjUHSw1-GTWuSgd0UFhnDX2uc48QP80dMUjBxp6V2hpl5w-S3MqdqhnrElrqHM8JLg0X0iDlAMjSBqBocDeyz0JNyrmsgxV9k1SCKF2exnPQEeCMBtsnhnj5wDfam8hI-2UOqVhlqXlULX6DMG3tktwbLh1k_GSoFvw2bKE8C-TkoGvIlC0qhJy8lfaCgwRb3KFSUQNc779JoZMHvnatu94n7YUbdq59oIszpi_TepV_SUvgZOHVJbImY-cqjsOmsuQ_PC2bd8-gKGLaUe6wrys0pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه آمار مسی و رونالدو در جام جهانی
🔹
لئو با اختلاف بالاتر از کریس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/673803" target="_blank">📅 16:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f52b27070.mp4?token=Fb1hoCPBIACRT8JEX0OMFNSvfYQhXmhRFwgGsFCu4d_jMP1iAinXPxjxPoxZF5aNula54-7Y909cUhK4qJXwdsRujFPa69d1aM7hSlPqtkepoEKhtoGEIkNeIzSXGeyNdN9MybBo6Oz5E10U0sC9YVvQ55cQU86j3K3rY9ZRz7BhGylJLRh7Isxc-Blts5zsXv2joXVMZd86JHyhxKLIaPK1ralGusuzpO02ItvtfErtiQEQuyvg5E7W7M0-TPfjZ2_7dN2GTbJPoA_2bNgj6K5eGGhc8ZdQhmi5frUjajjEgu1oRDeZHaY7PPVLm7penBHw3uV-JqEjMHlpJcWvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f52b27070.mp4?token=Fb1hoCPBIACRT8JEX0OMFNSvfYQhXmhRFwgGsFCu4d_jMP1iAinXPxjxPoxZF5aNula54-7Y909cUhK4qJXwdsRujFPa69d1aM7hSlPqtkepoEKhtoGEIkNeIzSXGeyNdN9MybBo6Oz5E10U0sC9YVvQ55cQU86j3K3rY9ZRz7BhGylJLRh7Isxc-Blts5zsXv2joXVMZd86JHyhxKLIaPK1ralGusuzpO02ItvtfErtiQEQuyvg5E7W7M0-TPfjZ2_7dN2GTbJPoA_2bNgj6K5eGGhc8ZdQhmi5frUjajjEgu1oRDeZHaY7PPVLm7penBHw3uV-JqEjMHlpJcWvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه بستنی طالبی خانگی با شیر پرچرب و طالبی یخ‌زده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673802" target="_blank">📅 16:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673800">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقشه گروه‌های تروریستی/ احمدی: مرزها به‌طور کامل تحت کنترل هستند
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
گروه‌های تروریستی خیلی وقت است به‌دنبال فرصت برای ورود به کشور هستند، اما جمهوری اسلامی هیچ فرصتی در اختیار آن‌ها قرار نداده است؛ آمریکا در برنامه‌های خود روی گروه‌های تکفیری حساب باز کرده اما نیروهای ارتش و سپاه آمادگی کامل دارند و مرزها به‌طور کامل تحت کنترل هستند.
🔹
بر اساس اطلاعات موجود و گزارش‌های دریافتی از مناطق مرزی، هیچ تحرک جدیدی از سوی گروه‌های تروریستی یا تکفیری مشاهده نشده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/673800" target="_blank">📅 16:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyxvIyr4mV0lCVdZVcqrUxntK3Yf21L9TNDDDZI-PxgGOYNXqO5jeJb6hZ_7xghNflZ0RTgsn_eEXtuhcGgcMJD8F9ND1YpPrRaSsoOcQ5CMlQ62rH5VhGWc7RLdFaxS-XeOjIfYG0RYo5eAzitUU9zDfCL6LqTpny8zh2bmSVtpuuZB2eGagQnrPkKfefQr9G5ppSBQbprbQOQRvKRpaBoaVsEnL68wMG7WonvRqiCSwlBdX8ET8CGkG8QSQcRoP1p0ZFwVZLunrkj_9N07qIUAiJWob4kb7eBLgDqzwaWHwCB1pu5tFVSxBNZy409WIP0nuNkxnz4a93k850avmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور اهالی فرهنگ و رسانه در دل جنوب کشور
🔹
با حضور چهره‌هایی چون علیرضا دبیر، سعید حدادیان، یامین‌پور، خضریان، حسین پاک، خانعلی‌زاده و جمعی از فعالان فرهنگی، رسانه‌ای و اجتماعی، ویژه‌برنامه‌های در جنوب کشور برگزار شد؛ حضوری برای روایت از همراهی و همدلی با مردمی که این روزها داغدار حملات دشمن هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673799" target="_blank">📅 16:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673797">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع عربی: ۲ نفتکش حامل نفت عربستان، درپی محاصرۀ دریایی اعمال‌شده از سوی نیروهای انصارالله، مسیر خود را در دریای سرخ تغییر داده‌اند و به سمت کانال سوئز بازگشته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673797" target="_blank">📅 16:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673796">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2aGJ4vD0GLStMynUvBzlIJjcnNUNUSvbVGClwrNMF3U3ToeG2LfBgRDM6KiINx1C9mWrIvm3Ffa4S3YA7rmeDKzEjfGqrqxNYjDqDed8OnAoxaOT07dudddKuDsMsOyvbAqd7cKil3jcYXcLG1k3VMKIDr7QNtxLdwh3cQF7oIah93Lin5wi_9pZof7vFxZ2HIGItkFmILEnid1jUXHDwvWAInpXj536DMUfsgItW177KUHhf9Ub3W3KDeDYC0I_wihfUAWOQoFNo_sISyqauKrQAXJMG8u_MvPGluZjqlTYUS1kNZzR4oAvnEGQ0_GnQwRuY2zdpIhdlF9XKH0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون هویت نظامی کشته‌شده در پایگاه اربیل را اعلام کرد
🔹
وزارت جنگ آمریکا هویت نظامی کشته‌شده در پایگاه اربیل عراق را گروهبان «مایکل امانوئل سوینتون» ۳۰ ساله اعلام کرد.
🔹
پنتاگون مدعی است وی در حین کار بر روی یک پهپاد ایرانی دچار سانحه شده و جان باخته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673796" target="_blank">📅 16:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnnJktlK9KbeKfROj-m_c4AysGsZR5-CtIof7cPaBg62xz7L_D0uN3dSzYd4tb8NR0m38bVX-O9yO6A5RvAui9dnoBsGU5JcPdZKq7iHQEkLCMFq2dH6b49AOv3VMp-Un0XBdIU3FyArWziDXd8FbflkZgrnL2KqMjJNrwyn6DmJl0ywirpAAkZmYDtJXbNDAYfUahuwyjMY8w1WdFfpRotWEVRDjtXf0cWOTvlwaOh0Op1lf7Yg-O82oTG3GV7P1F9OEOgd7c_9abR38ZdsHs3B5qe-vPO6zX9x0_v5c3t6hvnz4yprL-RgPZeDiW6pEfNuc3eV4L4y_13xqa5pNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUUkcH7qb2N6HFialon7s5iRmJmdCa2iYWthp2ComJPVYnJigd7NVsaZL4_NYW4R25Z9CvOKXkSW8i8C4FUnbGJG5vnWVU4vFeG19uiXjR_eXpVO5NbX2KTChMTd9dd0FEcEzXTDX3rnKvAjPegF3Rd-ovXWz7PYNQvzNr03BhjZSIS_QNEk6pOrLJuWnjCA4u_cAosSXJBADfg16LQavuEJ2ecX_Ktt0O-aspv5LKX2mKp80PtYvLhBX_JlecoVgpet7U8AgSyAPrrghvXVPR2pZMKV2j3ijjK8mugasVGQ46uw839b9X1FQerDmWLLxZ0fCDvArExWNAjSFnK2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBEEvTRB3PbKsvJaZJ6tND8H4Tjv90qw38ey8nfA76RGdfTccWJvqBSJpc09EmgeomsR3lqSBgTS1jj8M51EOcxFeVQDd43ZdXBs3Y0H23nJQqqYBOUlALuhs2HXkbYtnHakzeOT3eyf9CFeX5w48pyquVu37xuOIRfdZmgVZonrZeCn4jskyy0lAMV_JCAskFTQYf4sSU11bxMB2htS9x6DoMP90icaqd0oL9cMfSJHossPD-3KuD3JZJBmIK02KALO0zgZUHO1L5lRfuQdmdsOD7kXlK0nndICrTewGEpr9tyXP0sb4CFtzACAkz3mlafHQdldutVw7e4XnPqj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0-TnRrbVQu0HVAK7Tff-fS-ftvZd0CniYjnYAyjcmL0yY0bMsu696KzqqSK1-OjIDvFUWTXpVNaLIffSod8RNlOx9eDTRN9vBI344kMRyZh4ezzuPyvFMRNotuRMupF9-pxev9sVvksJwhm_e5nz-JSPLxQG8HjsfyQgq-CZh7WUdBmhg1ro2oCF_a93EG0-zXmdjxfJn3D3VpcP17qFRwIWLQmYiL-7KsCxxVSBCOc78CCDxPSG2gQG6ZE0HLP2s4RdHoh4U60i4xcQOOiSlvz4m0qnlrQi4qexRy7W7gBFYug_amD_oUXUztzg4RaCiKVDtY95NntzangS_kpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SS5ftmp5VhNGn4GQK-wjkKUVGY-4B9IzZEiVVReF7_FLu4AEvjuTDiSSjjjWgzysLqb9I5aus1BirFeI8-j9y-WGbnkm2kvZVKNxqx4_3-GvNmKDm1nGIoZzKnJFIYZaTLSH1xyyDum_N6dFO8nz2dV_Lg_VpA54MwOsMZCyVZ8fhg6b8XO5yeGFikYh_P4VUgQ0doSC3O9txlktOIKCOkJXc_ZkUr_bKRuydBA4zWTu7Ku5r_AtR6avUh6ChBGPuaMaDaaA-89a-vXI490o13D33Wpl_T2aJbR8ijzhJWsAo73LVEhQOvDf7Rt1zoS-a-QCv8UyEQTii2sCnsgmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPk09UDxDuPikAS_euaPTmZIxjMjyNuuuXcN7qVzosk2CGNl0XTaZlIyP36zdb4er4bGAqcM_Sc6T-oBtYAGZdnTI2VyuYf5kzgy6KMlBHt-GlXY4Q080tbrdvse1TndgHc1OVeWcY9VPfz-rdZFVSxVQE5Tb4zzfje3UPGl5civiNEdtTX7wQ0iZZgT6OiWRz9NJNYNgm1ffyPUlV8WDZkJix0yIjAO99GB8LxXqZ-A-YEYt5X5w6ZSk-CXzqeKT7ESi4x8ju1E3dwDAhYZWMBFDxm698tVCW-FKagxfZW_psNdZBnIDrZBw0rS3dNcv8cQp-iLVVI_hnhmWvNhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuNAroiENRhsfvAb13FUFivqqelWNi1vlVccEkBAn2Z3SG5r7F7pRVyxRGUgKY_ODtL1DTB7t1BU9t94mgc0RcNlhalHMJZ-0bIQ6v-3YhXtjcn6_fi2T4oVDZXPsImns3ZaCNMQ3foAF0kicukAcygKXMNkmAIinrtmlSd1mzj7hPVelSvGcHh0xrPJA8jIAmJDGm-FjZU2eRLdQuDdTg5ODHRtjo2vRWcrDff2b37FsOrvwT9K7E39EebYRKsWZFvNZf2Uru_XBYD44KfXUVXeSIe9-mQm7x7WN1aaE329deHJfbAgE2hcIAKvaVNJTMjU2zd8JpJPCx4609ompA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNt75GC_yl8xZFG3-6vUpMt3OMQgBLHN2wIEvWmHDLh_mikFsbop5K1o3OT3PjhZgwHrWkWnaErJe5nDJbW1RO2A0ME_desPKxwUGeWG8QjGp9uYyCiQHLQhDJDhlknxNFLc7fLhpcJPaGJfWp5Q00r832BvYk8Lt9IZtQbncEhyQqLlJJ-ZR7hfWliqVJsYX3tqRfORKCsZOBKt50QcQRdfg7UaQT8Nvbg_EAmC56E2Zhul5rx-ZKBWlY1a9np96knatEgZ7GSe6tPBPBcevSMqDlERww-u5u0CR2AtpYh1UGQc9VpO9HTRd3djb7VrxDWp5g16MpmZGRsV1iyerQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جریان نقدینگی به زبون ساده یعنی چی؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673788" target="_blank">📅 16:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تفحص ۶۲ قطعه از پیکر شهدای مدرسه میناب؛ ماکان همچنان مفقود است
🔹
در ادامه عملیات تفحص در مدرسه میناب، ۶۲ قطعه از پیکر شهدا کشف شد و با وجود جست‌وجوهای متعدد، هنوز اثری از پیکر شهید ماکان نصیری به دست نیامده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673787" target="_blank">📅 16:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dce665645.mp4?token=ExgkT_vr3_cf8GjnkxEGHyAAOJgsg0vnHxIVWNyzrlyhkYigpnkFBfDY1B0yLYN_Th8t7bCc4rZfZEC09IBy304McljdLtgykmpcD86NoELoa-KaAGjLrq8oN5DM597fnURKawUAe19-9UjbS06bG-NXCFOe0QgvU2O0WHKqI0rCufbsX-QCB3tqZLeAZZ4GWiDXplknSnCxGSMajbhnvgntm0w8BIBTrY82thYIwh_qydZakKXNNdKo0g0jgp3WLkccPJNkE0mCphNJfDyFVbQqKUaxlJ5T6uCGwGS-fwdfrf8hx53gzdcALaNM2M1cEDf4AbozVoxClpvoWBPbqG8aiqtL5YkfYqwzlYcN0RU2qVVkidS9-6l6C01R2eQO4mMftwFCTXPk97EKaYe4CckGhOdQHMPj4gtO2mj4R-gKw_X1ooMZZ8irjYYMfiGh8JX0es3qvmQi9dQ45kMyRCpLtAgkdPqmhjmCr9p1gAQmDTYwjQTBzEdFgut3iFD9azW5zHyqhb5szaVSYZMiEuGi8px-1vZ87HHKUEpl9H8znEAtrPt91aFUnFNVS3C9dtLKyraU6n9bBg-Yzy42rX4TdEuKCCpml8JsHGw4ZswyFGJ-Orx90ygkd62OL-CraixQIBjAPW0WLmXwa9NyzEH1BcOiIiSwseBNG_qGESk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dce665645.mp4?token=ExgkT_vr3_cf8GjnkxEGHyAAOJgsg0vnHxIVWNyzrlyhkYigpnkFBfDY1B0yLYN_Th8t7bCc4rZfZEC09IBy304McljdLtgykmpcD86NoELoa-KaAGjLrq8oN5DM597fnURKawUAe19-9UjbS06bG-NXCFOe0QgvU2O0WHKqI0rCufbsX-QCB3tqZLeAZZ4GWiDXplknSnCxGSMajbhnvgntm0w8BIBTrY82thYIwh_qydZakKXNNdKo0g0jgp3WLkccPJNkE0mCphNJfDyFVbQqKUaxlJ5T6uCGwGS-fwdfrf8hx53gzdcALaNM2M1cEDf4AbozVoxClpvoWBPbqG8aiqtL5YkfYqwzlYcN0RU2qVVkidS9-6l6C01R2eQO4mMftwFCTXPk97EKaYe4CckGhOdQHMPj4gtO2mj4R-gKw_X1ooMZZ8irjYYMfiGh8JX0es3qvmQi9dQ45kMyRCpLtAgkdPqmhjmCr9p1gAQmDTYwjQTBzEdFgut3iFD9azW5zHyqhb5szaVSYZMiEuGi8px-1vZ87HHKUEpl9H8znEAtrPt91aFUnFNVS3C9dtLKyraU6n9bBg-Yzy42rX4TdEuKCCpml8JsHGw4ZswyFGJ-Orx90ygkd62OL-CraixQIBjAPW0WLmXwa9NyzEH1BcOiIiSwseBNG_qGESk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خط تولید جالب ساخت توپ؛ پاکستان
🇵🇰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/673786" target="_blank">📅 16:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-PeiV_qaqKV-ikx5m3NGgPaqrCs9-sfOjPVACM0qA1LilPjQd54kqooZCUZyjbVf6fLADkWL-70cBhWVPXPhjyduRa_LXHalFVr-vbywwVyVno0i2ViOg__HJ4390uSFFfo_zXhmwtaY-8-7V5MA9HpFlDP8ya_86dCRbJJEq0M88jgjxuEhv-OYRdY-ay1Ygf9o0m4f_qz9wDqhqtOfm-4Tst3XRa0vINuaB3r34PxgEMk3l55pIK05UpZkNk7oNqN1y5dFFVbpvIwMM9c7RVDkpI2AtPzeUy3ARBiXEeVLbP9w-mxg6R3FgKCdpfi5aXzAkTdMXHMJ_p02tk8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
مجمع عمومی عادی سالیانه با حضور همه سهامداران برگزار شد؛
🔰
مُهر تأیید بر صورت‌های مالی سال ۱۴۰۴ بانک مهر ایران
🔸
مجمع عمومی عادی سالیانه بانک مربوط به سال مالی ۱۴۰۴ با حضور ۱۰۰ درصد نمایندگان سهامداران برگزار شد.
🔸
سال ۱۴۰۴ نخستین سال اجرای برنامه جامع راهبردی بانک مهر ایران به‌عنوان سند چشم‌انداز افق ۱۴۰۶ بود و در این سال دستاوردها و توفیقات گوناگونی حاصل شد از جمله اینکه منابع بانک با رشد ۶۲ درصدی به ۷۰۳ همت رسید.
🔸
گزارش ارائه شده از سوی دکتر «غلامرضا فتحعلی» مدیرعامل بانک مهر ایران در مجمع عمومی حاکی از افزایش تعداد مشتریان به ۲۲ میلیون و ۷۰۰هزار نفر، پرداخت ۵ میلیون و ۳۳۷هزار فقره تسهیلات(بیشترین تعداد در شبکه بانکی کشور) به مبلغ ۵۰۶ همت، افزایش سرمایه به ۲۲ همت و حفظ کفایت سرمایه بانک در سطح مطلوب بالای ۸ درصد است.
🔸
در این جلسه گزارش حسابرس و بازرس قانونی قرائت شد و صورت‌های مالی مربوط به سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ به تصویب مجمع عمومی رسید.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673785" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b19c5fc3.mp4?token=WetTtkjfC-X0lzEQDiWUTZfAhKkkZijdqQ__-sWbS5ex1bnwCtjAmFIQ91jR8_bBZhELgqcHGtJhgrSkGGnnzP36IcPbAsvXEQ4sNdhctCYTIAyF1KPOvPMY25BdvzjpVU7dN7ozJqem_NBB5axHA1fHq6k5Ie-4-WCeWcDO0aixbq6o7l9wCFx4vnZlFhE9A8S63GKHV7H79yfONbvJH6YuI9irr-rCrB0XKEPG0G9wtGbpPw7te4_yoN8etJdLrqZtLgp8q42pXrHTFeh-uvBLP9qfAN0UaaYsumfml81BaAz-TuG_1XKWpl2cZwgZcf-qe7OtZRibr4vjkCarjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b19c5fc3.mp4?token=WetTtkjfC-X0lzEQDiWUTZfAhKkkZijdqQ__-sWbS5ex1bnwCtjAmFIQ91jR8_bBZhELgqcHGtJhgrSkGGnnzP36IcPbAsvXEQ4sNdhctCYTIAyF1KPOvPMY25BdvzjpVU7dN7ozJqem_NBB5axHA1fHq6k5Ie-4-WCeWcDO0aixbq6o7l9wCFx4vnZlFhE9A8S63GKHV7H79yfONbvJH6YuI9irr-rCrB0XKEPG0G9wtGbpPw7te4_yoN8etJdLrqZtLgp8q42pXrHTFeh-uvBLP9qfAN0UaaYsumfml81BaAz-TuG_1XKWpl2cZwgZcf-qe7OtZRibr4vjkCarjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل: جنگنده‌های آمریکایی از ترس حملات ایران، پایگاه‌های منطقه را تخلیه کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/673784" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673782">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0BTB_lUtF4STBIRsBtL0ffT6rsiA9j-PUESr7RTgZ1C_pdNNZQWiPuufH63c56mnbdPZtnJ_gSXUI6m7M1rgPUUs6nebo_zxqNSwDceQGYjVFH1d_rGLXwmFuD4z0wsx7GN4o30749LdL0L1emo7SqDRlJTMDwgJLWKKCvnwfcEVHsU3MnYEKc3QJiS5BNiOG_UAsvphKWzJRrFMy4tRDDf1VDbhnaJk90UO5Ex4XgAFttpeCV_V-jI3vO5kn5cfFxCb7kGwfJ7HcsKX6gVn-Gin9Nw96dHzSXmFRDpZtHXdvmLx7EI8DLoNYlxmvwRLQnv7OQ98FCt2NZ80VUABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور ایران و نخست‌وزیر پاکستان دیدار کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673782" target="_blank">📅 15:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673781">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtdXuXK3aaopgwJsJQWHw9EWwa93S0CX3c3iH67Llaf443AK9LcyKD3mGWwrb87Ar95VDngm55rDeoqhOPvA15oxPGBlu7i9eYJ8smf91m7nnA_epKO4xWctn9OGKDU39ovQWpML7um8-w1vmxfyXYkEHXhh9PdLN5sDUvF3yygu0w501e7brvTNd2hqcnFEOC2VERxcyK4I26ogCW0t_P1A08N7UClaX8AubI8Dliq3KcT7bZP9oyuAGlEH8RtcQqCoRK63STW4Y7_J1_Fcknem1sfsSHBP_qZEqPOg8VTvBhubWYB1VZUNeY617xA22aXI3BEEThis-m2ARpUHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهایی با بیشترین تانک‌های رزمی جهان
🔹
چین، روسیه و کره شمالی به ترتیب بیشترین تعداد تانک‌های رزمی فعال در سال ۲۰۲۶ را در اختیار دارند.
🔹
ایران با ۲,۶۷۵ تانک رزمی در جایگاه هشتم جهان قرار گرفته و یکی از بزرگ‌ترین ناوگان‌های زرهی غرب آسیا را در اختیار دارد.
🔹
با وجود گسترش پهپادها و تسلیحات دقیق، تعداد تانک‌ها همچنان یکی از شاخص‌های مهم قدرت زمینی کشورها محسوب می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/673781" target="_blank">📅 15:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673780">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozfTVNLtwHJdsW9Oq_Rcdta2qVUuO_tRqj4a6_-uYmqPDxs0rFljXGP7Jc6xecX5u2s4GPXl_s31Kt79DcEhMMnVW89Z7hAJS5h7b0JBG_FNf2vJjMdPf39Ki2qAt44UfaaxmoI3ISymkn8tlGgtT1mI434i0Eyeg73TDN39hlaT4q32_R9NFGPgx_psAcXMWpaY4tTRISOZ5y41wwGONwJO2mEfIJ9axVL30XVS4mJZoWwV7NqYpjskT9yOleO9eXS0Uxcq8AQ99e2x3gRQLMjyEVwLXT7XBLGSuVyWZ1zup370jbKKKVx_k_izYR6N50TKHDQ3CdpFDMV9ZOPCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه و فوائد آن؛ می‌دانستید فوائد قهوه فقط در کافئین خلاصه ‌نمی‌شود؟
☕️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673780" target="_blank">📅 15:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار هرمزگان(Admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2VdsOzbB1WED2iHFX9MzbS3nf8-wJBbUOLHWAyBDu7CtcQG1O7YPPQPit-nps-EbcwBKQdVHcV08JMHNoXklLBjgfz8kn8E0EhrNWMlnNSdDF9Z_k93TAZ757b06kMdqbI9NrW0hw9yStTvMOkhUj6U_yAHydg3dqyIn7s0p4piXB7kqEbULUxfxVoKcoAgu1IOiVnkTdyy2bBndQrrYnOlYKs8AKQFANd1uwcX6q_lym-IAf7mIpUEciIOgMRB-xXId6_97P_BB2bHGcKIdUqmqXK4W-_XvS4MdEi_fZHOKwQZFkW6aGRLpUx-aRy7o5JscEdQ7ZiawufDkM7-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام آب شیرین کن ها درجنگ آسیب دیدند؟
#همه_باهم_برای_ایران
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/673772" target="_blank">📅 15:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673771">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aecdbd5f84.mp4?token=SLCMVuCJo3680--Y9Sv8kdsknwaZQOd5jH2AHROCB74KHvb7apNSaJDWkTWJbuVdXXdVCSCmNj3yOq-s8A_ION2OzgwVWytfgmvSwx0Yc9yEA8MUuAIWpdV5wHj4Blhgxq4Dm2IkQnKHf60jRVOa1i7yXfbW0kU-q4d3AsMKdlVCEzH_Ces9Pe1FxC2hnaVdaiKu2B_IvPeXd7J4ZW4-oogrMVT05s8Xwo77MzQYIoj7kSqe5ywyaijCxx8Oly4EPcNHb-kpSt85wr8Tk3je85-Cm3RO9xOyWUhYshiJDeHC14cNe-3UXjgHPnO99ucowmJVSt6o4BwhWd6pTMHqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aecdbd5f84.mp4?token=SLCMVuCJo3680--Y9Sv8kdsknwaZQOd5jH2AHROCB74KHvb7apNSaJDWkTWJbuVdXXdVCSCmNj3yOq-s8A_ION2OzgwVWytfgmvSwx0Yc9yEA8MUuAIWpdV5wHj4Blhgxq4Dm2IkQnKHf60jRVOa1i7yXfbW0kU-q4d3AsMKdlVCEzH_Ces9Pe1FxC2hnaVdaiKu2B_IvPeXd7J4ZW4-oogrMVT05s8Xwo77MzQYIoj7kSqe5ywyaijCxx8Oly4EPcNHb-kpSt85wr8Tk3je85-Cm3RO9xOyWUhYshiJDeHC14cNe-3UXjgHPnO99ucowmJVSt6o4BwhWd6pTMHqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارت گسترده به پایانهٔ صادرات نفت بندر الاحمدی کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/673771" target="_blank">📅 15:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673770">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6d90750a.mp4?token=NqzOHkJcqK9cD3XzYf2rIMmi192qqFI2v1vNORfKIJQMe9QT7hIUWWZgsUTmML3jNDCLmrZpmiqoFnwb8eJbMfvTmyICi3HGqQ9xBEnX59DbJNn9ufQGJuOUoLo2dwGactkLs_PBfGVoqSg8Ku3blk_aDRWCj9rD9jD0UPdPTMqnAlKWOHRinZ0zBv3s3kWoWZByS0OSSTwf0Br__O2CpR0YgjtZjKdx8y-BwWMXUTJxot-YM4XM8XdQxSsonduc8EjVSLMwz91RwHxF9DuB_199TWTfdGXvligbm-whlBMOmqpvDi2xlbsV6rWXKmb-mWITR8Du6pYmBOA-w3QbMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6d90750a.mp4?token=NqzOHkJcqK9cD3XzYf2rIMmi192qqFI2v1vNORfKIJQMe9QT7hIUWWZgsUTmML3jNDCLmrZpmiqoFnwb8eJbMfvTmyICi3HGqQ9xBEnX59DbJNn9ufQGJuOUoLo2dwGactkLs_PBfGVoqSg8Ku3blk_aDRWCj9rD9jD0UPdPTMqnAlKWOHRinZ0zBv3s3kWoWZByS0OSSTwf0Br__O2CpR0YgjtZjKdx8y-BwWMXUTJxot-YM4XM8XdQxSsonduc8EjVSLMwz91RwHxF9DuB_199TWTfdGXvligbm-whlBMOmqpvDi2xlbsV6rWXKmb-mWITR8Du6pYmBOA-w3QbMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی دل از غم مالامال میشود اما عزم و اراده باید راسخ بماند
❤️
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673770" target="_blank">📅 15:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673769">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
یارانۀ ۳۰۰ هزار تومانی تیر به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673769" target="_blank">📅 15:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673768">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOSjmHuHGGqa5oM1ch19eOmoDvD0LhwIB-IwXPIJTlcFI3N5LuGA2R9cKdAREJ-S8bQh0oe6YpP97R2JDj102wVQNWi5ZI_ZErMbX0RbV-6OJruuobFTcnYcvWnn_9jvWGxCEzUBYeH4t2v0CIUYnhTIFgtstyIJu5cY-1cizI7iD3VBmSsn4EYpXa7Rb73urd0MfmxugMbeqoQY_atHB_L34R6pE3pcyX4JPo4ZKOLxLJScnYCu-yYQ2_yi6kU4SGyj8_YwZQUbYbTdRMt02_Fk7PjAiZpPrc7n9ckYiieZUC6rgLNnMcBZPX9dIy6aCNA51wcDccDhFVXlBUYwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور ایران و نخست‌وزیر پاکستان دیدار کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/673768" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673763">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IBTVVu0kcZmyLN0-li7UtInnIXL7xA_CM6E3LU4yULc6q3_5bEjlwKnsFXtEqAmR45yaGTXVR9fnfSuESsgQRTTzTvM9v4im4bzbsd-ERcwXUA3Yz7Q3ntG_TcZZpwJy47V8cEE2t93qTqsWalwv6O6DKbpHeBR5zl3wq-sGgcZyf0pz6np20y2AfFNJrdhyymvH2MgdYRI1K8oPR66h3aaWFuJ9lVgAd_wLq1RRPD0OYWrvjh7snZ4ATc31jPiBeDBqgTPYVT0xx06MN4BQaYil-GrtM1v8SXlr_HJBOCDj7-K_d4PMOBONURdJbaR9PkClHTR1PsPDfb5iGsV9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c8_RDvjPJ5hlf9wwS767Plf7877dqjzv9Pdkmb4OXNk5mZIBDX2OT1Ghi-xzkSvxGY9hYU6K68PZy6BYkp1xBqgX7izghQzubKAZ3zlwtXzAktTqkKNehJ1Fxsah7DHexgyhBDfnhpJgJkixegTySxh7NVe9MVW5IW1Q2hjrAhty7dMZNmIfM0w7JQkIAfkyYSGtb0m7HPMBXaUBZOG3fK-NaUYh4dt50C4Oc-N1b5vu3421Nra8hcthK0nMJU-Faw1tqd2snRTY9XQB_vRZx6zlq69hmzB9YmlLvjmkzGVx7IFOqr6nWJbz1ZVV9FS8QVJIUhnmW67bhzvgHagLZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/570c5d9e43.mp4?token=CWn6L79x-b9X192OTWMrZCofzg45FCYdM4kNUgsBbtShH8WIt2nTgCqjhvevmxE9jYuHifn562Y8L3f5UzET4TEmQOqIv73d6r7Md_qTeUpZgeN4XyIi6B4RWN5W8hkOBz1Ig6CXkaPMamLgJ6kWTrdpK2X53vA2w1Oqruqt-jxDuo9oPUkp-1gT_3OqT-R8dXSyhE275GyhBKttjJZfBfFbOLwSqxcHsxIBngKulfxBtq_iNIvWdKjDSmnRkN-wyTHvlrX5I92YmVos9DcUCf34gCGuVtLOYa3BwHmSXtkx7Pvi8UY8LZpIosc2FDkDceggglB1NqivTVkKmVS3xyUlcohK9x9qo83xlHzEycwq-prCTrNPuJs9agQZK0MlSnJPdBnOVETBOOtiVbfun_UpMrRn2NofvbGZnY8F-IqVLX0Sty0cMfRY46dNgxVGSE7oe1Ne5ATKgMf7PSnWdDEtpYntcaRH4GLO3VfRxq9611cqm_gYvbes_yFFnqmM8NDAdgbogKz9k-GO4XVWZUotKL7D_dZYfIs3_b1uXTltX846hO0ZwqfgGSU9uM1hTZMD6DNvcue9pkdMgRahlSJVkBiJPBens79L6xFPko5EL3OMgpQyYPrcge8N2xdy-v_A7bccg-vxrVOCT5j6QVAlJt4lQOsF_tyIrBUXg3I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/570c5d9e43.mp4?token=CWn6L79x-b9X192OTWMrZCofzg45FCYdM4kNUgsBbtShH8WIt2nTgCqjhvevmxE9jYuHifn562Y8L3f5UzET4TEmQOqIv73d6r7Md_qTeUpZgeN4XyIi6B4RWN5W8hkOBz1Ig6CXkaPMamLgJ6kWTrdpK2X53vA2w1Oqruqt-jxDuo9oPUkp-1gT_3OqT-R8dXSyhE275GyhBKttjJZfBfFbOLwSqxcHsxIBngKulfxBtq_iNIvWdKjDSmnRkN-wyTHvlrX5I92YmVos9DcUCf34gCGuVtLOYa3BwHmSXtkx7Pvi8UY8LZpIosc2FDkDceggglB1NqivTVkKmVS3xyUlcohK9x9qo83xlHzEycwq-prCTrNPuJs9agQZK0MlSnJPdBnOVETBOOtiVbfun_UpMrRn2NofvbGZnY8F-IqVLX0Sty0cMfRY46dNgxVGSE7oe1Ne5ATKgMf7PSnWdDEtpYntcaRH4GLO3VfRxq9611cqm_gYvbes_yFFnqmM8NDAdgbogKz9k-GO4XVWZUotKL7D_dZYfIs3_b1uXTltX846hO0ZwqfgGSU9uM1hTZMD6DNvcue9pkdMgRahlSJVkBiJPBens79L6xFPko5EL3OMgpQyYPrcge8N2xdy-v_A7bccg-vxrVOCT5j6QVAlJt4lQOsF_tyIrBUXg3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از خسارات وارده به یک پایگاه آمریکایی در اردن در پی حملات ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/673763" target="_blank">📅 14:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673762">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aba3d2697.mp4?token=UtQsJHvER0uIqoNdLwUzVdpIJTTQukgmRAd8dLxNKYv7mi0PBtImMOYMtNGgQSMgEhacldSrxCthhuuJGZrkoiPpOK48h9NSe_FQamTCiC50NZ-pAOUQgQvBXZB6oJsabHAC5KcWw8hUjvI90GoETT7GIcRMkSOYOjSb8eRY72yZ1K59C1zAFGRM0iG5JVbWa4jXia5JhWCNepZ94hZurlOIkxftHc0xe0FS4CHFZiyOq3Znlze6C3haLLvDwT2HmtJ0VDjptjcfRGtcxUwidzqJcJwz5Biz7ypsiPH0USihyKhTTKmGVSjWW-yq7Gc60oZ4Uw73h1cNaEJTNcNBVDYcJVvGeNsy3mSgDo60w9vexPVN5_a3YeeJ4MGP4tUmKXA4yGPHu6Xvfbds4BaIc9RCKR6OB0iOnh2yvZuxMiErf44fFs0va8B1S1sgi3eeWMvQSbwyFqzuVRCvpZNJ_a_GVXykC1j7CiAheNc7A0qYafJkFHyl4kSLe5tUvTqdeG72Dx1EmlWcUrjw90nyIoDBt01HO9inne8S75JJ4Ps8r9NeS8ggbX_ZWVvryzaoKA2_Smy88TIrGAtjkxd1mHNh_I5zoMtNwN0WMZ6Zi8ZtO92yh8o63Ut_XRJn53on3E7u3QEEAoHEI8dPCGt96kO1aZE5ozW6NwbcGcyG-Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aba3d2697.mp4?token=UtQsJHvER0uIqoNdLwUzVdpIJTTQukgmRAd8dLxNKYv7mi0PBtImMOYMtNGgQSMgEhacldSrxCthhuuJGZrkoiPpOK48h9NSe_FQamTCiC50NZ-pAOUQgQvBXZB6oJsabHAC5KcWw8hUjvI90GoETT7GIcRMkSOYOjSb8eRY72yZ1K59C1zAFGRM0iG5JVbWa4jXia5JhWCNepZ94hZurlOIkxftHc0xe0FS4CHFZiyOq3Znlze6C3haLLvDwT2HmtJ0VDjptjcfRGtcxUwidzqJcJwz5Biz7ypsiPH0USihyKhTTKmGVSjWW-yq7Gc60oZ4Uw73h1cNaEJTNcNBVDYcJVvGeNsy3mSgDo60w9vexPVN5_a3YeeJ4MGP4tUmKXA4yGPHu6Xvfbds4BaIc9RCKR6OB0iOnh2yvZuxMiErf44fFs0va8B1S1sgi3eeWMvQSbwyFqzuVRCvpZNJ_a_GVXykC1j7CiAheNc7A0qYafJkFHyl4kSLe5tUvTqdeG72Dx1EmlWcUrjw90nyIoDBt01HO9inne8S75JJ4Ps8r9NeS8ggbX_ZWVvryzaoKA2_Smy88TIrGAtjkxd1mHNh_I5zoMtNwN0WMZ6Zi8ZtO92yh8o63Ut_XRJn53on3E7u3QEEAoHEI8dPCGt96kO1aZE5ozW6NwbcGcyG-Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازخوانی نامه احساسی سردار ایرانی، میرزا کوچک خان جنگلی از گیلان قبل از شهادت در برنامه محفل ستاره‌ها
🔹
ابتکاری متفاوت و اثرگذار برای آشنایی نسل جدید با قهرمانان و مشاهیر ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673762" target="_blank">📅 14:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673761">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olENsoqLVHwDfxhTKeJXqvaedJ28Chce9g7NbynbPooM417Ph6k5k1b12Zdtoy6fT0wQTJUOrFjGbxWUl1TkEOI6Ef4IsicPUCHWzjmFYGp-iEBVzFXCZhsTzLRlTqJMZpsNzZn2-0pxKbOXcpkLd7R06LyqzbNR3O3tcqXYERctOOmxMXkm9oSeWQFmqbmFybo9JRQ0TtOzxAXoOICS6so0soLAlAN_jf_MF19WvWo1GBSrVT7L6ZWVHFj6_4AeB0bjAkZWx1paN5zuAC0n1OZbuq9FzviFDbweBLozvmfxgX4lP4F2CelaKEFIF3_QgJid3WQoSkBGtZgH5dew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ مدل لیموناد خنک، سالم و خوش طعم
🥤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/673761" target="_blank">📅 14:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673760">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HinoIPC79bW-z6ksst5-r40CQ-6qGL3c664jGrpbpLpQwW2w8t7_nQFx3YnTu9_0tsCYA7AWKZuazxjt4xSbuhyGC512xdGMsk1yAAwbAKt4Wcew3R_yCxfhTzMQB46axoZgC8id8aAXsmfvisiwct8sOq60QmWpK6yv1TJFagcnZ7kIG32S8sG-EO66Ow0uri7LLF5oNkXQSUJnG_So0f4_gPkr-ioqumsmkXYwUpfB4KLjY3Yro5lr0f7mC_dmLdvGw3F7yg15k_EHQjpErcvl7EcM9W3oPK_LJ3YXAXJpeo_372Cw93qb6VG8p1zpaweD-ulIkm2yL4EP-N6wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام چادر تجهیزات بالون شناسایی ارتش آمریکا در اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/673760" target="_blank">📅 14:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673759">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WHqUnkCKPm-LP0QwOq604AL1hLAfflbzZVkGcFi0s8prkRYagsHHIGJoe4RDEisebaL6UaW9pfiYZeLJuA8GK_BOaqXMXezIoIUqgWjJQlEw01x0GHlklU6JSY984KworSZHRi9YxYU_bim5dBrUMQW0LYavSk7JJXLFzoT99GBA-bKQdEUNQinTjzYc9mpIrFcHVUG7U8mCgBztNkIb-vvs_tmuEeocBXcHobwuOWZ12_nmlFntJFIcrusH3wTphbSp62oCo96WuA4H1p5u9Hm95HeoX6U24ihw3jxN1IpegeVLM1QjGGMPTBo31rv2J__3-CwfTGFQthHMU6THtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WHqUnkCKPm-LP0QwOq604AL1hLAfflbzZVkGcFi0s8prkRYagsHHIGJoe4RDEisebaL6UaW9pfiYZeLJuA8GK_BOaqXMXezIoIUqgWjJQlEw01x0GHlklU6JSY984KworSZHRi9YxYU_bim5dBrUMQW0LYavSk7JJXLFzoT99GBA-bKQdEUNQinTjzYc9mpIrFcHVUG7U8mCgBztNkIb-vvs_tmuEeocBXcHobwuOWZ12_nmlFntJFIcrusH3wTphbSp62oCo96WuA4H1p5u9Hm95HeoX6U24ihw3jxN1IpegeVLM1QjGGMPTBo31rv2J__3-CwfTGFQthHMU6THtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ارتباط ما با رهبر عزیز روزبه‌روز درحال افزایش است تا بتوانیم با رهنمودهای ایشان مشکلاتمان را حل کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/673759" target="_blank">📅 14:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673756">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUkplhbyya31yCWuiAvvluFHjttTm-0-ptyJRPY3gSgUQBW95TpemOoBmAgEIMMc8KjcQnsfZ2QYMMz-XgDCPrE1O243M5R_pN4IgMv6K6vC1WjQOmUBBCS-IhSM903fr4nVMdKkgbr4bCnmcBvw5-4G4MoNtoBDwnSIzRP96DGgBMDxoB9MCFycHUp6NvSjUknY26WosW5F2A2s7hGOlaEySO6dWS094GIB0R2zjfhDQBSVVDVoY4BfcSiC-m_-Flf2MOzXchMNeU2W7wdINCIdWa-J8cnxGqrXZ2vqcrTYnhdK9uwPcDukkWBYsQLp5dUkoROpz5_3VXGBG9cs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyUkARKt3w6R-n0GFRIyhr0dCZgHCrhbdO_9VaioS0dWv2kDuYuz0x95ItzkYzhMl9PBySPNFDiTqWdtTMIb00wEJl50bmlOdamghiuxSAGX3ltxDhS_nvFDSSwa00RuxLo_IxVV6D3_kInGbM0uxsu8EW1H2hnP-SQR2ugHAxR9nNsTIZiVfnVI_D7GzOgXljGid7crSPtLBEClVoqP1vkoVEir4gG-fmslEcxQ_kBPEpdCYiYq4if1paan5Hdz_T2_sVvsW1NUuQHBjLSPJtDwU8t1qPZ4Kum_qq95gXoU7XcPxWDrd-1afd4RCF3WizM9EM_2v0AR2yYdtr7uFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای جدید از انهدام محل اسکان نیروهای آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/673756" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673755">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای شبکه اسرائیلی: تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود
وای نت عبری:
🔹
مقامات ارشد اسرائیلی مدعی‌اند تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/673755" target="_blank">📅 14:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673754">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR2mvTwfU_HqTy9t4TKVD8LcbT2tXShYbrfWKToHEli8rO6xfl_fTOCIR7qNDm8jsEr6X5ApxRA6JEvwU_xoj1xiLGXwNUlEF49B5VIJh1B1cAEzNHr2VSm_0sW-2q7LXN1_Yw-R1fmt3e7jTFjtYfcogOX5AoxDL0VVXN8HcEnSR-PPN-9mvVZHZOsx7UqRE0C5EIrdWd4VKsWRJ8yU5IZQR-eXtm1psjLYGuKFnTcWe22E3eB0_xdSg1EHV1WnBVsfGIOL3ayEtdmoqaa37vpwuCVJtN0JAGO89E77FruLFyWk3yijqxYYOZhF0UMxGODjVWKBYvsa-9KLO4RORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودرو ۴۵ کارمزد فروش خودرو را در استان‌های درگیر جنگ حذف کرد
🔹
در روزهای سخت، همدلی زمانی معنا پیدا می‌کند که به عمل تبدیل شود.
🤝
🔹
خودرو ۴۵ در راستای مسئولیت اجتماعی و حمایت از هموطنانی که این روزها به همراهی بیشتری نیاز دارند، از
۲۷ تیرماه
به مدت
دو ماه
، کارمزد فروش خودرو را در شعب استان‌های آسیب‌دیده از جنگ حذف کرده است.
در این طرح، فروشندگان می‌توانند
بدون پرداخت هیچ‌گونه کارمزدی
، از تمامی خدمات خودرو۴۵ شامل:
🔹
کارشناسی تخصصی خودرو
🔹
انجام مراحل اداری
🔹
تسویه آنی وجه
🔹
بهره‌مند شوند تا در صورت نیاز به نقد کردن دارایی خود، این مسیر با
سرعت، امنیت و سهولت
بیشتری طی شود.
📍
کسب اطلاعات بیشتر درباره شعب مشمول طرح
🚗
ثبت درخواست فروش خودرو
🔗
khodro45.com
📞
۱۴۸۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/673754" target="_blank">📅 14:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673752">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تیزر قسمت هشتم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید حسین موسوی که به دلیل ابتلا به بیماری کرونا، روح از بدن جدا شده و به خاطر گران فروشی‌های دنیایی، در برزخ متوجه اشتباه خود می‌شود و همچنین عذاب انسان‌هایی با گناه خودکشی و رباخواری و زنان بدکاره را درک کرده و در نهایت با بردن نام خداوند، فرصت دوباره زندگی کردن به او داده می‌شود و بعد از تجربه تغییرات محسوسی از جمله رفتار با خانواده و اعتقاد به وجود ائمه در ایشان پیدا می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سیدحسین موسوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/673752" target="_blank">📅 14:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673750">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره مالی اتاق تهران همراه بنگاه‌ها در دوران بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالی، به بنگاه‌های اقتصادی کمک می‌کند با بهره‌گیری از روش‌های متنوع تأمین منابع، استفاده از ظرفیت‌های حمایتی و تصمیم‌گیری مالی هوشمندانه، تاب‌آوری خود را افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/673750" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673749">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ممدانی: جای نتانیاهو در دادگاه لاهه است
🔹
شهردار نیویورک، زهران ممدانی در مصاحبه‌ای با روزنامه نیویورک‌تایمز گفت که درباره این موضوع که آیا اختیار قانونی برای بازداشت نخست‌وزیر اسرائیل را دارد یا نه، در حال «رایزنی و گفت‌وگویی فعال» با اداره حقوقی شهر نیویورک…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673749" target="_blank">📅 14:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673748">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f2a5a7eb.mp4?token=sMYGgxHipe1caFrHnqwOqC1XTTi4Gm1fpy8XFPoJUw7Wu3Isiab1tD6nEjJusCLpl_hYaMzewNudHiHD3Ehf-4wqK4ZbxxajFRrfHIs0dhnmfyco7t-JOuqgKLr7J_n13IDfTOjo-8kq3LyHkrkIy94hq_TZXXGCCBDPSyLFGbWElY-BlYwFtYA2bt8flwS7fIzEV2C0jNPVGSaPY_4cPPmcBbjjj8zfCarQ93nBSGj0_KlOVpqlDKXUhlvbFLGTvqMCfZVizWhLA4VlMQCxVnL8C_YDH7Y-HTDVaV9tVljZdBgKl9y2NPfAA91OJxFPibiD4wNoNMxonivyqQsHuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f2a5a7eb.mp4?token=sMYGgxHipe1caFrHnqwOqC1XTTi4Gm1fpy8XFPoJUw7Wu3Isiab1tD6nEjJusCLpl_hYaMzewNudHiHD3Ehf-4wqK4ZbxxajFRrfHIs0dhnmfyco7t-JOuqgKLr7J_n13IDfTOjo-8kq3LyHkrkIy94hq_TZXXGCCBDPSyLFGbWElY-BlYwFtYA2bt8flwS7fIzEV2C0jNPVGSaPY_4cPPmcBbjjj8zfCarQ93nBSGj0_KlOVpqlDKXUhlvbFLGTvqMCfZVizWhLA4VlMQCxVnL8C_YDH7Y-HTDVaV9tVljZdBgKl9y2NPfAA91OJxFPibiD4wNoNMxonivyqQsHuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادت باشه که ما نمیجنگیم از خونه زندگیمون دفاع میکنیم، این دو تا با همدیگه فرق دارن...
🇮🇷
❤️‍🩹
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/673748" target="_blank">📅 13:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673745">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjsKPaAXcaOsL76a7-86KsyX_imCThL6mCukR1cTen9DtI8LdyZP-gS357tD4AYHa1eTcBZ5T6fQotXX9UWJV2mprxeBEZInMdEUBsPpC3UqRX_IKO8kx29gFjVHsjQ4LLakBFCCj6rwMWNwEwScJqXcRYlJuU1qPWiYE2bjdm54M-73OyKVN3sSP-YeWeyO_3WHjHaSaKb4cPmFz-0-8uRZHq7X1Gx_abYpvuvJ4ts8dEnVb9nZVQhv6br5eD5pKWwHthMHT7sSfCw4Zld4lwzhL9UF6GI8_wuRh8H556JnRtbpZurjwdWo52m3LNCJ-VPSe3hWaFSCjRnjjOi5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmUaJw_spWWsmOxbK7vowyV-A6SGoYEuwVjJnkZfHRPEjrzpNHbDn8XUvyZv-OHmIZgPRyqtoQ3zA9x6JyDsLbI_o-jeLQuEy3Mc_Isq9UR4KpzBXZId_8Bx9xPqVKBpUk-6o0kLZXxMmaBg5_Of4n1cSVqlVTFRkSd9YDg0O5MPWSj7iDcq93_AAtgotJ_t3wbFerenrgMCn9SW6ANfqnIT6gmcn7xRubwqg2UAfiBEB6UmDHHSSfHKdKqRfmg0WxSDUkc-LGzzS8FHY7b3XyE9RO6vAacTvkW09KdiRkIeQoaEtQ0HbkaaMlrypld4zNdo6iiWmo7QBtdIDwoXQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تکذیب وزارت نیرو درباره ادعای جنجالی فردی با عنوان «مشاور وزیر»
🔹
رحیم زاهدی در یک استوری مدعی شده بود که به دلیل بی‌حجابی مادرش از ورود به فروشگاه وزارت دفاع جلوگیری شده و پس از تماس با معاون وزیر دفاع، از او عذرخواهی شده است.
🔹
در واکنش به این ادعا، وزارت نیرو اعلام کرد زاهدی هیچ‌گونه سمت یا ارتباطی با این وزارتخانه و وزیر نیرو ندارد و عنوان «مشاور وزیر» را به‌صورت جعلی استفاده کرده است. این وزارتخانه از پیگیری قانونی موضوع خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/673745" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673742">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mki0w3XvBS2qU_9cJZf_h9aU3TxMCEdQ9Dl5Nt7zAwNrCUQgOJ6mewyb8ZcrDQjdMO7TKduOO32Zqail-xiJGGiDV94BAe2gPRXsURetB66ncG6wAHdx3jBziJyz2YODaV_7HzzsEOxhnWw8ho4VD3BJi5LZmzf0RLC_0-hawTY7Krx6RxR7C_dpJb5tlpfCpVN1NGrjpFxvZq24kBeDSprY7sZXCEN5thP_6ziXmVz4zcJvERY-2Tj68TIGL6YFn0IqjSnny21vCwbaJyv-c_5qXUlIdPOg2XsGs7r9PxY4nMSWK4u5ui8nrMH_o70aBO63otXGNindH2RnHOWbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس شورای اطلاع‌رسانی دولت: ما منتقم خون رهبر شهید هستیم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/673742" target="_blank">📅 13:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673741">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx_Wkqcn3Y7q_7SDCOcF_onzO5vIInFU1x6Uv9NAqpRGgE15Iid5nVlSzeiwNmknDNWC1P496CYYS2OMS1TOLVuQxyJqwqVYEeOEGhe5N3ClRUOjEYUyqZ9Dn_v4qlVOGlzm816mVyWpxiTb8P43goZLGJkCtmODyvNTzna-rKidt8llqAOLwPDASd3_m7UZh5-KI2mjHSmO7alzSBvrNBb5XZaJ1x_GngzvvHdiw7goH7lCwysiEvbQYOjDdssxWX6BuqzYwdg_q4PEBTbhL2XZhLGQPromahqBN6I9VCUjpBICbWpgn3JMhjsUnYq5hnH-t51Hd8bzpqA7_qs1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از اتمام جام جهانی در آمریکا صحنه جنگ تغییر می‌کند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/673741" target="_blank">📅 13:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673739">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRLAVWIEDKTFfQxMgj8-YjnJ6eEaPrCpkJVFaFLBwJr5gRI7feZdXuK-yT4UhUYj1QbSVSR0qptkkAkX1-if2TKKKmRzbLMthjZXw832M88NJkFdvkd7Su69vcAGRRJ9249QFtZqqlKQq0QnqCVLTDpgU7iaoc42DL5T6q2ciqGi_6FlhUbX130qYG4GK20ucD0at5dTGxzaxhsuAjruNsZoaEmYliYXVlLBD783DXopLvN1Bzh_RJsL8V1qEvb5TK85RPTIat2Oc0_EVuVTXPq89Nk8CPC800zzAL3NX4aUxRPnWFo-GJLZvLtSqjgnqA9cV2ny9IsSspeBiU7bpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایزه‌ای که مسیر زندگی یک نفر را عوض کرد!
🔹
گاهی یک قرعه‌کشی فقط به اعلام یک اسم ختم نمی‌شود؛ بلکه می‌تواند نقطه شروع فصل تازه‌ای در زندگی یک نفر باشد.
🔹
در مراسم اختتامیه یکی از بزرگ‌ترین کمپین‌های بیت‌پین، خودروی تمام‌برقی Volkswagen ID.4 با ارزش ۷ میلیارد تومان، به برنده این کمپین تحویل داده شد؛ مراسمی که با حضور ناظران و فعالان حوزه فناوری در باشگاه انقلاب برگزار شد.
🔹
این کمپین با تحویل رسمی جایزه پرونده خود را بست؛ جایزه‌ای که برای برنده آن تنها یک خودرو نبود، بلکه اتفاقی تأثیرگذار در زندگی محسوب می‌شد.
🔹
بیت‌پین که یکی از پلتفرم‌های برتر تبادل رمزارز در ایران است، پیش از این نیز کمپین‌هایی با جوایز بزرگ از جمله اهدای یک بیت‌کوین کامل برگزار کرده بود. اهدای خودروی برقی در این دوره نیز ادامه همان رویکردی است که بر جوایز واقعی و تحویل شفاف آن‌ها به برندگان تأکید دارد.
🔹
گزارش ویدیویی مراسم، فرایند قرعه‌کشی و جزئیات تحویل جایزه در لینک زیر قابل مشاهده است.
[مشاهده گزارش تصویری و مستندات ویدیویی رویداد اهدای جایزه]
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/673739" target="_blank">📅 13:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673738">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سازمان انتقال خون: الکی خون ندهید
بابک یکتاپرست، معاون اجتماعی سازمان انتقال خون در
#گفتگو
با خبرفوری:
🔹
مردم فراخوان‌های اهدای‌ خون که در فضای مجازی منتشر می‌شود را جدی نگیرند و تنها فراخوان‌های رسمی سازمان انتقال خون را دنبال کنند.
🔹
خون ماده‌ای است که تاریخ مصرف دارد. فرآورده حیاتی مانند پلاکت تنها ۳ روز و گلبول قرمز تا یک ماه قابلیت نگهداری دارد.
🔹
در بهترین شرایط افراد هر ۳ ماه یک‌بار می‌توانند خون اهدا کنند. زمانی که فراخوان می‌دهیم می‌دانیم در کدام نقطه نیاز یا شرایط بحرانی وجود دارد و فرایند اهدای خون را تنظیم می‌کنیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/673738" target="_blank">📅 13:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFm5Y8yy4nXXn1BEOcQ3t38Or5-WnAamARNXN37kZom9Zi4tg9E3x_MzieZ21Ey6l78Ye-eolj6YT-JZviH2oM56bKEWXyA1ITrCiVcO-ZRdQu0XFtz_SuHci8iJMr5_L8m7_w4KTSZ9jytePyG4g6JcTzodytRsbjCFHz1H9A6i-VZKmom98BWBFcryWZk1vKTGKTy5YD6oruS1LT76Tu-5TwJqk48LD-z_FZEel-h1GdLjyd_8BE8ZES5haS1RQLn2AcdRqeOISd8sIaX5M14qUM8s-3FWEqLBK6ScPoWrRwRZ8UT8Ag__nzEEN1muU6Z8Gu70xJq-rBx_rK71Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvOHUHRbvYFRyRbmyixKYfQ234SBgamXAQ-owK4rQqCH-KjY9JzjNvQo3Vk92aEjvUxbZu3FebuUm_EssTLZFleAc3TcVQxu9oW8-W0RGkVcMTM8qZNJzQdZmljN8evQcZRt9WBR4vwW5SvJ7PFHD3xtwOc6YZ_reiXKMC1iwENCnCSsDWnpsnNm2TQKFajFmU0FppV_7lpVRGM4QDgTurhfOyeTGoskUl7_zOEonEmEIhDoWtbGkyXBcU1mAxlacDm7fpE44drmhlb4p8VRrCvxtQNci13R_tX0pZyCNUeN7cF1Fj5aAT7x5gD5Q2VZ7cbWUSHqZ747CvM_dTPjFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جایزه ملی انرژی‌های تجدیدپذیر ایران به بانک تجارت اعطا شد
🏛
🇮🇷
🙏
بانک تجارت در دهمین کنفرانس و نمایشگاه بین‌المللی انرژی‌های تجدیدپذیر، به‌عنوان بانک برتر موفق به کسب جایزه ملی انرژی‌های تجدیدپذیر شد.
✨
محسن طرزطلب معاون وزیر نیرو و مدیرعامل ساتبا، این جایزه را به دکتر اخلاقی مدیرعامل بانک تجارت اعطا کرد.
✅
جایزه ملی انرژی‌های تجدیدپذیر با توجه به فعالیت‌های اثرگذار بانک تجارت، به‌عنوان حامی و تامین‌کننده مالی پیشرو در زمینه انرژی‌های تجدیدپذیر به این بانک اعطا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/673736" target="_blank">📅 13:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcA7Opo00WRnzMRfyEwWC9endW0B1cfUByPZXFLJb-plFzzP7uvLTG5Zof10WuDsEIe0UedLY9nCiPbQHX5p3XuTmtzcGu8RlDlVFQAi8OBJvKUjk4LZQIFbd-8CJ9bLq3-rixZouxoLWSpz4Mly4awT2lE_Wu81FmuWU8Ap5BmVLM2V0JJV6Bkv9SMXX8waZ3EeBkkfkBJIqsY8WgP610ws0bpsm6OfvOZMr_lsWYTw6k5c0_jidX4EmQjgwAqqMpxqMOkB1v2m2uEnB8qfU8IFmDpS0b1fXiTALTHsW0WdNlNIVtWRx6pbPmPqf-G8oCdLeMXVpwzb2dJZnzJf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_-Zd68BHv2jP4KJUd20pJtehniM8I8JMsmpAauNBeMx-a85v_9A-pqHYjNUXnu6156T6kngSPhh4Nm5A8g7mLd_nb8LcfpUluaLdH-rL7Fdw6b0teeG23mSCuSwM6eWf7x1k6Vg6PpIOgRx6I_6W4iGKYttVBHgNV4ONHc7M3y0OHrc0LX20hE5SYmpaMiy90_zve6j9Ku4UPplRwwpv3Y9gtZSwzJiJuhk7xRF7t82hB2fPGuM1tGddLBncmWjFiUimw6BT3MrkQ_Y_AQm9TdGxpgpQDYj7V3-2j-gR0rnJPzSLFJJIZ6vGkvaVnCyzPe2yG-1ZdRDfvNZ_hAu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryYeBoqLLjw9tLMzGd-NycMLfO7CdKPevnSMkfo7S4EmU63RT4HUSFM9dWr2WXyWT2Gk5z5qwSjSCom-dtzHj2RGOVF92WGFnMIadQBOtXg1_KXb4Ya4yyWn2NcThJog37ZFt52wHcmEVQhBKe0Qcn8DiXGqUIL4_IMHSPnVmvO2BAtSkV_hFJiInMCpo_TXck0nJDFRvTrqbXj4GaSDBqm2vc_31G0JoLtbVVJT01xmTb_5agBhXGKsmwPZPQ3xqdP9R9gUECVrZyd6Ppj2VL8jofXBRozah5Sta6Kph8h5woxkl-CmartyNT2ry_IQvVuOKM6JQqgB9zsNY3j0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP9BkNKhkCqpuMAWeuQ93SEZkLYXbao5edaMrBsMdbCYkVQ550voCejK-EIzYOrnoE_I45Bh71fld94cHdDiGY5rdlUSqApf4iqpe2NQRqtIcM3bwTAn-5zyzXgcP9I5CqGJUR_m58lKOfhyqpzBDxV9QxcZJVhcwA60SO16Hw_syIGCV7HSTAU3CGK02FB41HscP3TKFgencs23FfJKoG3UZ3NrOP5XcPVQjp7iWBx-Vo29iqSi8BsE7y32ohonoloV1M_vCaio04AbuDR4qJ3U_ZaSliBI5leKUpNHsQh6g9LLjgYmq9wm5k7J7FhkfrsRNV3ExIV5v5u3K7W7WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر قطره آب ارزشمند است
🔹
با چند عادت ساده، می‌توانیم کودکان را به قهرمانان حفظ آب تبدیل کنیم و آینده‌ای سبزتر برای ایران بسازیم. #همه_باهم_برای_ایران #صرفه_جویی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/673724" target="_blank">📅 12:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
جان‌باختن کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج
🔹
جان‌باختن دلخراش یک کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج، بار دیگر مطالبه دیرینه شهروندان برای ساماندهی این را به صدر مطالبات عمومی بازگردانده است.
🔹
این حادثه در حالی رخ داده که هفته…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/673723" target="_blank">📅 12:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBT2tsZ10RaByIR13jsuE-D1umPQwWXGt9Y52woNwHoXDWmw2tuiJmxyfMTgWpDfZ4dG5my0HK0svbXt0wRCJBOL2h3ZAHHJPuy9KE1y1DieqB9IQ4foGNySYjsADAdWY-PERgHN2n2aOf2HkYopyJvxeIhZhDZhwKbQM7kHRHaOg3RO5ylPnIxh1-HJTxj4aRkgzkJAeXA5SUrgPsTob1pbEmN5auSNO8tcPB3CUA-MrF5PwmCD5r-EFfQJaWPJ7Bu16IcAeUCYs7mOtfLCAo0xGeLJ0AXrVVB5dGzcGe5_V8w5K9x1DLU95vWjs30jzWdgHAtPxBqOa8pO1J9b0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور از ۴۵ میلیون کاربر و ثبت بیش از ۲۹.۸ میلیارد پیام در سروش‌پلاس
🔹
بر اساس گزارش عملکرد سال ۱۴۰۴ سروش‌پلاس، تعداد کاربران ثبت‌نام‌شده این پیام‌رسان در پایان سال ۱۴۰۴ از ۴۵ میلیون نفر عبور کرده و بیش از ۱۹ میلیون کاربر فعال در طول سال به‌صورت مستمر از خدمات آن استفاده کرده‌اند.
🔹
در این مدت، کاربران سروش‌پلاس بیش از ۲۹ میلیارد و ۸۴۰ میلیون پیام ردوبدل کرده‌اند و بیش از ۴۴ میلیون تماس صوتی و تصویری در این بستر برقرار شده. تعداد گروه‌ها و کانال‌های فعال نیز به ۵.۷ میلیون رسیده است.
🔹
در بخش تولید و مصرف محتوا، کاربران بیش از ۴۶.۷ میلیون استوری منتشر کرده‌اند، محتوای پستچین بیش از ۱۰.۷ میلیارد بار مشاهده شده و پست‌های منتشرشده در کانال‌های سروش‌پلاس بیش از ۱۰۹ میلیارد بازدید ثبت کرده‌اند. همچنین در طول سال گذشته، بیش از ۲.۳۴ پتابایت فایل و داده در سروش‌پلاس بارگذاری شده است.
🔹
بر اساس این گزارش، تهران، شیراز، اصفهان، مشهد، اهواز، زاهدان، تبریز، کرج، رشت و ساری بیشترین تعداد کاربران فعال سروش‌پلاس را به خود اختصاص داده‌اند.
همچنین ۸۹.۲ درصد کاربران از نسخه اندروید، ۱۰.۷ درصد از نسخه وب و ۰.۱ درصد از نسخه iOS سروش‌پلاس استفاده کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673720" target="_blank">📅 12:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران را از هم نگیریم ...
🔹
در روزهایی که آتش جنگ بر سر این سرزمین سایه انداخته و قدرت‌های بزرگ از سر منافع و هراس خود در برابر حملات آمریکا سکوت یا همراهی کرده‌اند، دردناک‌تر از هر تهدید خارجی، زخمی است که خودمان بر پیکر یکدیگر می‌زنیم.
🔹
برای چند اختلاف سیاسی، برای چند عقیده متفاوت، برای چند جمله در فضای مجازی، آن‌چنان به جان هم افتاده‌ایم که انگار فراموش کرده‌ایم همه ما روی یک خاک و با یک نام زندگی می‌کنیم؛ ایران.
🔹
دشمن اگر بتواند ساختمان پل و یا برجی را ویران کند، شاید بتوان آن را دوباره ساخت. اما اگر بتواند دل‌های یک ملت را از هم جدا کند، بازسازی آن سال‌ها زمان می‌برد.
🔹
حقیقت این است که هیچ موشکی به اندازه نفرت، یک کشور را ویران نمی‌کند و هیچ تحریمی به اندازه تفرقه، آینده یک ملت را به گروگان نمی‌گیرد. این جنگ بالاخره تمام می‌شود. دودها کنار می‌روند. اما آن روز، نه آمریکا کنار ما خواهد بود، نه هیچ قدرت دیگری.
🔹
آن روز، این من و تو هستیم که باید دوباره در همین خیابان‌ها کنار هم قدم بزنیم، همین شهرها را بسازیم، دست فرزندانمان را بگیریم و به آن‌ها یاد بدهیم وطن یعنی خانه‌ای که همه در آن سهم داریم.
🔹
ایران فقط خاک نیست؛ صدای لالایی مادری است که فرزندش را در آغوش گرفته، دستان پینه‌بسته پدری است که برای فردای خانواده‌اش جنگیده، خاطرات کودکی ماست، مزار عزیزانی است که دیگر میانمان نیستند و رؤیای کودکانی است که هنوز آینده را ندیده‌اند.
🔹
نگذاریم هیچ‌کس، هیچ قدرتی و هیچ اختلافی، ما را از هم بگیرد. ما شاید در سیاست هم‌نظر نباشیم، اما در عشق به این خاک نباید رقیب هم باشیم. باور کنید هیچ اختلافی، آن‌قدر بزرگ نیست که ایران را کوچک کند و هیچ پیروزی سیاسی، ارزش شکست یک ملت را ندارد.
🔹
اگر این خانه فرو بریزد، آوارش بر سر همه ما خواهد نشست. ایران، امروز بیش از همیشه، به قلب‌هایی نیاز دارد که برای هم بتپند، نه علیه هم.
#سرمقاله
#همه_باهم_برای_ایران
@TV_Fori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/673717" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
جان‌باختن کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج
🔹
جان‌باختن دلخراش یک کودک سه‌ساله بر اثر حمله سگ‌های بلاصاحب در سنندج، بار دیگر مطالبه دیرینه شهروندان برای ساماندهی این را به صدر مطالبات عمومی بازگردانده است.
🔹
این حادثه در حالی رخ داده که هفته گذشته نیز یک دختر ۱۲ ساله در شهرک سعدی سنندج هدف حمله سگ‌های بلاصاحب قرار گرفت و مجروح شد./ ایسنا
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/673716" target="_blank">📅 12:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673712">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyRY17fwsUVjgsUC052HdLtAbrWtXc-3HRTIFF8ZobcDR4hYIEKZbqOUhzsVJhZLm1qYhvA8zih33l2S_twa2I_sK2ELln9jNUmeMVWPRPiAgqUnwInu2KsnqObh-bjX0zUsetYSo9vug9lYcnOt3wZW0PwHmNncLN31Pne4SHWy06v4GWvPyCan9cteP58tmT8p9DCyiGabVNyokgQ-Wbfrc2FrvmVS9U8uu1RgRzu7k4P3M0_Nph22yj78cvroUUQ-anSmMzIwiBa-Q8P3sni77kz4ttrMOhOFrRr5Vg-8CBn02AI3dE8iRj04k3noNtph_4RGBw1PbPrrESCFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZ4jv_y02QILyCE164pvdnCXNT8Cx9Bu8ZEYwcbrdmfMEHtlEcQoNV7247-kqIxOm6x8fmaOOifb6Yamce1yU-vQetMCKQ4CRbGgw8YVAtjG_CyplnK4LA9DNe8Qksp6gKsK1toFQJ8uP-Gkv0_rY458QgVkXQczLYtl2gEgzVoxhA75lQrl0FioZqvOBNA5EYIrB8AZ4GhnPYGnwoUDf5vIvIfeb26blAlKYqtPCMds6pmrEr2cgbOV-uWZEUmzht7w5uEjyMuN-c3QKtTKvFaBDDtXLOjAUqHhcGRZnzE9FX-2BAsAjpqmCTj6M15iRTkEUdO8BNgoyo1gYNmoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf1wOYi088SvjDk_2Us-WEQM_kI4ZWBjlfIjmER7zPNubgdih9zE4VENjDsOPou8ovkfs2MVhIhCd-6NJnZcKY1OXLOxtALnIG-talpXlgDw7ihMQvu_-Hqu-v76yW5o5fCZ3Vk1rYMh5ca1QJ_CAzd6aUyEEr-qVZjoLVPgRWO2ZjR4eLsPdp0iKnJ9gkozayi8E3y5V2ZnkixfKH9I2fEwmc8jglcrLZqqPE3ejSXWkXhJhqaMGEGXYH2gQT5gXMTFnKlqmv47jYVCWXXvk7xPV2w-W-oxOxBzzEggssGiWxy3nTNz60Uue_e6krBymt4SHzUSRZKgdfW4cFcgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDRuvsVfgAdRZRd4U_FlbDdZ7AG8E6ULX6Ytjla4SnHHRvtHxwrNk8gIacjuEDIbRIMcymhZtkrvAZIRNZMUXtr2FzxrFUp43MSBM2KT7sScVhfVJ9pU13M-rG6uWcjr_Zfo1kFis6S4rvmQtMcGu5hxRWKM_TgE6ZascnRMtg5cghsseqzdsRwZ2uCSRH67jR6OZInvKCArV9dxxaKmZV8iwzdsNG0WceG2CUuyDNPokUnoWXiIkJ7hPcoocOjFB77UUAzl2463K4xsJ0j1MZKkgtxhJwRgaFvxjbGOXHZnuYJWsgMobSqBSGZb-SFGCPi3ft_hScyZYUPKTMyE1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا آدم‌هایی که بیشترین مهربونی رو دارن، بیشترین ضربه رو می‌خورن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/673712" target="_blank">📅 12:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673711">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfe2305ba.mp4?token=OseXxBrqTgaEdbw2ECiqe78HyYSfnx4n0JuKxYqNaJAmg6nzg9W-Dqi2ezMe0ZDARDMP4dou9oHsA4MvH5Um6aH5P1D1lbAXZHDkboio1aOICOAPQBgFT5pXCw9V5qhWo4iIWhi0Z71BCeC6KDVQOKSegVzu4FPQavL7M6gTXlyyQ8IbbwdXf4gfWp_AjitXlUbKAGHPuBl8O5Vn-bFhanLUbarF1PgfRoSgak85kXHecYeh5hGe0en2pT9eq8H-N8hriWoE39FhayPMcRVh09yB-TiGDNG10KtDKLp2Kogx405rOVSwXMkH9JnUbo4yQq-zND_B60TToqg2obtctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfe2305ba.mp4?token=OseXxBrqTgaEdbw2ECiqe78HyYSfnx4n0JuKxYqNaJAmg6nzg9W-Dqi2ezMe0ZDARDMP4dou9oHsA4MvH5Um6aH5P1D1lbAXZHDkboio1aOICOAPQBgFT5pXCw9V5qhWo4iIWhi0Z71BCeC6KDVQOKSegVzu4FPQavL7M6gTXlyyQ8IbbwdXf4gfWp_AjitXlUbKAGHPuBl8O5Vn-bFhanLUbarF1PgfRoSgak85kXHecYeh5hGe0en2pT9eq8H-N8hriWoE39FhayPMcRVh09yB-TiGDNG10KtDKLp2Kogx405rOVSwXMkH9JnUbo4yQq-zND_B60TToqg2obtctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔋
این روزها که قطعی برق بیشتر شده، داشتن یه پاوربانک از واجباته!
با پاوربانک K62 ظرفیت 10000 میلی‌آمپر خیالت از شارژ وسایل ضروری راحت باشه. از گوشی موبایل گرفته تا چراغ‌های USB، چراغ کمپینگ، هندزفری، ساعت هوشمند و سایر گجت‌های شارژی.
✨
ویژگی‌ها:
✅
ظرفیت 10000mAh
✅
دارای 3 پورت USB (دو خروجی 2 آمپر و یک خروجی 1 آمپر)
✅
مجهز به نمایشگر LED برای نمایش میزان شارژ
✅
دارای چراغ LED؛ کاربردی برای زمان قطعی برق و مواقع اضطراری
✅
سبک و قابل حمل، مناسب خانه، محل کار و سفر
💥
تخفیف ویژه
قیمت قبل: ۱,۹۹۸,۰۰۰ تومان
🔥
قیمت امروز: ۱,۳۹۸,۰۰۰ تومان
⚠️
ارسال رنگ و برند (سامسونگ یا لنوو) به‌صورت رندوم انجام می‌شود.
🛒
همین حالا سفارش بده و نذار خاموشی، ارتباطت با دنیای اطرافت رو قطع کنه.
خرید از سایت
👇
https://memarket24.ir/product/brief/34644/180124/</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/673711" target="_blank">📅 12:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673707">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNbhHOsTgfvEttEGv32kv5iWDwi1LPQzUOoctx53Z9TGlAmnrCPpmBowIDgIHLgMup2lwR67Gh7IF_GANO8oOnx52ZhV98rUES9iPnoaqsbBFHYnt7HBDszjDQLtMEdQmEKS29qMisI5NNHd9HTL4lu76cdUXEwO9RiPIGhaayOr1kJMuXvcaQ-3a8DRiM1VzsL96M8rnlzuZwqPKOUUcmCXWZ3qTihHpEAUiAs1rPd8V3kwfppFu1m2XCb5tVgsQFJw1-3c3VMHLIX5o1GNv3oI-GY3nH9ynWAIcFK25rskBOkOuHOYMxv1LZMf51_f0mW3kZUYA4j9e1cFxwo_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشته روی موشک‌های ایران: مرگ آرام در رختخواب و خواب راحت بر دشمن مردم ایران حرام است؛ تمام!!!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/673707" target="_blank">📅 11:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCBFT6k2VepWOXfRTX1kNDTWjTMEntIV4cSm70ftAni6G530Ixm9qsRa5Fh3yySG6m0vyp0FrZvxLhsedcvPvO5Pfo0kd1nm47wi_zpqM3I2hwGmcxGd6VSbBd3YqzyjyoWlfuOEK8WrL0ZgFVxlHI1uhis5PUkTMXRj_BrODyTKBnBFiGz3LkhADfz3h9zE8Okn5BhY-hOOy7dUjQf67hs42lQG3kU_lOGQfFCNaFHg7LAKdc-MkcZPhU6ScX87jlbqpjoafqhy-gg_ocNxtv_1CUcCPT9qpCaynB-9g7ycZmJ_CgrGw5SouNnV8xoUaQl8HM4DL7ITK9PBJ1XphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس نظرسنجی منتشر شده توسط فاکس‌نیوز؛ ۶۹% مردم آمریکا از عملکرد ترامپ در موضوع جنگ با ایران رضایت ندارند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/673705" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673701">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تنگه هرمز بازار آلومینیوم را منفجر کرد
🔹
جنگ ایران و اختلال در تردد کشتی‌ها از تنگه هرمز، یکی از بزرگ‌ترین شوک‌های عرضه در بازار جهانی آلومینیوم را رقم زد. شوکی که حدود ۱۰ درصد از عرضه جهانی این فلز را تحت تأثیر قرار داد و قیمت‌ها را تا مرز ۴ هزار دلار به ازای هر تن رساند.
🔹
جی‌پی مورگان اعلام کرده هرچه بازگشایی تنگه هرمز طولانی‌تر شود، کمبود عرضه در سال ۲۰۲۶ عمیق‌تر خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/673701" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نمونه اولیه «گواهینامه موتورسواری زنان» چاپ شد
معاون امور زنان و خانواده رئیس‌جمهور:
🔹
به هیچ عنوان موضوع موتورسواری زنان، حرام ذاتی نیست.
🔹
نمونه اولیه گواهینامه موتورسواری زنان چاپ شده است./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/673698" target="_blank">📅 11:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ1oYF-9cxmiG-E-WyBkwwabH7ri9iki7XXsDdTo_Zd4X2WvSTd8TRdj_RuPtRCh-dom5ilgPGm9u6fmohoETaAzCEGfFNO25vX3QH4TkIqegPYP47dNvT1jS95nq6Wv9hSn1j8K71vsr_26HaPVIY25eiFJ5S_ondKkQ-H2dGQVPqGJH_6ehk3QQTpHI2q9I0SHXMEQhXOOAvTYDkjl7sskTKdGDHenyimbEGt44MxzU4xUEHsrHP-6YvOYcn7-XqC_zjGBUIOiscDXpDwzSfg7Nmu6LMFtNhwDqEt-NROtXrpRISUZx-xbUbzB7YFMHrUPZWU0pboFDU0AHKn3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک جسد در خانه نماینده کنگره آمریکا پیدا شد |‌ ماجرا چیست؟‌
🔹
پلیس بوستون تحقیقات خود را درباره پیدا شدن جسد یک فرد در خانه‌ای متعلق به کانن هریس، همسر آیانا پرسلی، نماینده دموکرات مجلس نمایندگان آمریکا، آغاز کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3232013</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/673697" target="_blank">📅 11:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3s_Uu-gN9TACF5YlCJ64mcLK0Ulq8krvCEftbnGchhCUBamdFhAij-kn9srMgB2BqE1XH2bRJYQ0fUlvs7P-pxrpArtOlIPmXJqii1znTgphIjawjP3jhriS0OqkYMMRShYq3LeGXP1wMBvCvj53lnDPwoBKhliEvitXhClEPG-jTS_H1ZpT3S7_QwiBW_q19BR_wKbcvA8UyrC0B_T697jZkm-r4x6INezg7Eb9Q5Q4Zoh4n9FlZPbZasuHw5CR5hXrmZREA59rLmB8Qt_dh6dkKjOiIv32r5T_REpkBgx6JcsBtm4bcVR89AI5SM2-Bw7JZ7v2M_4pLDBzcmVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای اولین بار| تصویری از رهبر معظم انقلاب حضرت آیت الله سید مجتبی خامنه‌ای که مربوط به قبل از جنگ است
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/673696" target="_blank">📅 11:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0eba85d.mp4?token=FyLOV1d4VGvsi5sCaTKXGi4mhJxNV88X4xhQoLFS94N4v2OyP5oASd87_tpcXX2flFlGJxksHp6726EhS6aANHgd-Q8wkVxqdWsO10nANW3UYMZsEPcSNpkIdZJuWAywRtaAxdYmSknDZ42ZV5t7qoEPAH1OzWuMIY7WFm4JctvNHLcTVCcsTbsbR4q0dQg4Yeo90DtLJ-xRqPnkkYiWd7cjj1rz9wkUDfQhj4MnVKH_uxSFO_ULUkI0jcg7W96ScN5y08H2QTGSYG2VJAVgup2jVCgUleONAuC11th0kK8dWrA-3V2JnPlCPjt7F8FzExSV_PkUgFn6KZEFfAVhOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0eba85d.mp4?token=FyLOV1d4VGvsi5sCaTKXGi4mhJxNV88X4xhQoLFS94N4v2OyP5oASd87_tpcXX2flFlGJxksHp6726EhS6aANHgd-Q8wkVxqdWsO10nANW3UYMZsEPcSNpkIdZJuWAywRtaAxdYmSknDZ42ZV5t7qoEPAH1OzWuMIY7WFm4JctvNHLcTVCcsTbsbR4q0dQg4Yeo90DtLJ-xRqPnkkYiWd7cjj1rz9wkUDfQhj4MnVKH_uxSFO_ULUkI0jcg7W96ScN5y08H2QTGSYG2VJAVgup2jVCgUleONAuC11th0kK8dWrA-3V2JnPlCPjt7F8FzExSV_PkUgFn6KZEFfAVhOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معبد کارنی ماتا در دشنوک (راجستان، هند) یکی از شگفت‌ انگیزترین مکان‌های مقدس جهان است
🔹
این معبد محل زندگی بیش از ۲۵ هزار موش است که به باور مردم، تجسم دوباره (تناسخ) پیروان الهه کارنی ماتا هستند.
🔹
زائران و عبادت‌کنندگان با پای برهنه در میان آن‌ها قدم می‌زنند؛ این کار نمادی از احترام و طلب برکت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/673695" target="_blank">📅 11:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef36935c70.mp4?token=TTHm25EP4vxziRFGGL2vBPKvDoMIo8D935I87TjlHD8YvfiaxxCfKFcRAyBN1vNjqmJmNbdzxvLNYoOxsgzKuSRdi0aK00maHykz5_9UzsW7Ku_JQeLljpRlLLugIp31DBJ8QeGAJ1UOZ9MwV1sLeXRQpdJEi5h9HgpRgIQ2a7EUqKkcQ82XFz24eJ8UYTZMEyOLFpimF_6xxq6imxdTxj5ekwJ4dXVvRdwtdaoV69Fou2YP68E8xuFeBaNgLSCO8RjZ3fG4Vaq7JItwqj_J4ieSDjigkYEUewWPcnnGZTb29hAhf2J2LCV40LVeVhQv64M7ZAqLMZf_76PsIkJFibaxw9E1BOK_LSEq2qudFZHYvrdrqd1sGpG2DxEiAXgtcGjlIUyBrHYvvTVY0G61DIFA-VspjqJECf1CxPIi_Nqal2dp1JVeuKhZZBdM2O7uEJpzFAasDcbJB2AZ3JOBd1BsHvI5NG3Zp8yyCE0k9B6fGq22d1Yo4mIzuf_KcfHNT7jh60BdU6h07DXf7k_yc7WKz5YeqAVVFgjlPmWTLFiTXmHe19Dp8rBrYGZRFcYd97kvZC3iYUDZMXtIHNXul522JCnU5nAYOxjpmUWHmvjVXJ5XxxVSoc7LT6MQtU07WgnoQo7FfVMgw1bQHyLZQWPA5_JaqCRjn5JK8f0iswM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef36935c70.mp4?token=TTHm25EP4vxziRFGGL2vBPKvDoMIo8D935I87TjlHD8YvfiaxxCfKFcRAyBN1vNjqmJmNbdzxvLNYoOxsgzKuSRdi0aK00maHykz5_9UzsW7Ku_JQeLljpRlLLugIp31DBJ8QeGAJ1UOZ9MwV1sLeXRQpdJEi5h9HgpRgIQ2a7EUqKkcQ82XFz24eJ8UYTZMEyOLFpimF_6xxq6imxdTxj5ekwJ4dXVvRdwtdaoV69Fou2YP68E8xuFeBaNgLSCO8RjZ3fG4Vaq7JItwqj_J4ieSDjigkYEUewWPcnnGZTb29hAhf2J2LCV40LVeVhQv64M7ZAqLMZf_76PsIkJFibaxw9E1BOK_LSEq2qudFZHYvrdrqd1sGpG2DxEiAXgtcGjlIUyBrHYvvTVY0G61DIFA-VspjqJECf1CxPIi_Nqal2dp1JVeuKhZZBdM2O7uEJpzFAasDcbJB2AZ3JOBd1BsHvI5NG3Zp8yyCE0k9B6fGq22d1Yo4mIzuf_KcfHNT7jh60BdU6h07DXf7k_yc7WKz5YeqAVVFgjlPmWTLFiTXmHe19Dp8rBrYGZRFcYd97kvZC3iYUDZMXtIHNXul522JCnU5nAYOxjpmUWHmvjVXJ5XxxVSoc7LT6MQtU07WgnoQo7FfVMgw1bQHyLZQWPA5_JaqCRjn5JK8f0iswM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای یک تصمیم ناگوار برای ایران
🔹
گاهی بزرگ‌ترین تصمیم‌ها، فقط یک ساعت اختلاف دارن! داستان حذف تغییر ساعت، اون چیزی نیست که فکر می‌کنید.
🔹
پشت این تصمیم، پای هزار مگاوات برق، صدها میلیون دلار صرفه‌جویی و مطالعات چندین نهاد تخصصی در میونه. ماجرای حذف تغییر ساعت را از زاویه‌ای ببین که کمتر درباره‌اش صحبت شده.
@TV_Fori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/673692" target="_blank">📅 11:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb5d21c.mp4?token=btMAG-BBluBwpXocCtgN2QzUkU55vPbkU3XERn7Iqb8V8PQ4_zuoLjIDgbBL9U7Troa622GfpvF2ulFm91kT2t-hiOdwJioDYM4tJRTZiUAJDFs_nWiAxQ8TsU80V7auyLnu3t7qJwGsddSuANuvVIidQdULc7nw_1lDiPEB7hhLTMzfGU3afW5Qszo_9mHgdFc76cxzyPRAadEbm_zo_uGOqxd7Q6919baYuM0xnkW7Yl_F3OwYsjngMKudzLAbZ6l9lWg-6wU3dsafCUEyMnuT2_2J95kVhOuV5bUodp52rDq7jGS7YevrT_vE4SjquSeaD664prNIr6adx0hg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb5d21c.mp4?token=btMAG-BBluBwpXocCtgN2QzUkU55vPbkU3XERn7Iqb8V8PQ4_zuoLjIDgbBL9U7Troa622GfpvF2ulFm91kT2t-hiOdwJioDYM4tJRTZiUAJDFs_nWiAxQ8TsU80V7auyLnu3t7qJwGsddSuANuvVIidQdULc7nw_1lDiPEB7hhLTMzfGU3afW5Qszo_9mHgdFc76cxzyPRAadEbm_zo_uGOqxd7Q6919baYuM0xnkW7Yl_F3OwYsjngMKudzLAbZ6l9lWg-6wU3dsafCUEyMnuT2_2J95kVhOuV5bUodp52rDq7jGS7YevrT_vE4SjquSeaD664prNIr6adx0hg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتحاد مردم در پویش «قرار همدلی» برای پایداری برق نتیجه داد
اکبر حسن‌بکلو، معاون هماهنگی توزیع توانیر، اعلام کرد:
🔹
مردم به پویش «قرار همدلی» پیوستند و با کاهش مصرف، بیش از هزار مگاوات کاهش مصرف برق را در روزهای گذشته شاهد بودیم. این کاهش موجب رفع محدودیت تأمین برق در استان‌های جنوبی شد.
🔹
ادامه همراهی مردم می‌تواند به تأمین برق پایدار برای استان‌های جنوبی کمک کند.
#مدیریت_مصرف
#پویش_۲۵درجه_قرار_همدلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/673689" target="_blank">📅 10:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
مرگ ۵ نفر بر اثر تب کریمه کنگو در کشور/ بیشترین موارد ابتلا در فصل گرم
وزارت بهداشت:
🔹
بیماری تب خونریزی‌دهنده کریمه کنگو از طریق کنه «هیالوما» که در مراتع به وفور وجود دارد یا تماس با خون دام آلوده منتقل می‌شود.
🔹
به هموطنان توصیه می‌شود از ذبح غیر بهداشتی پرهیز و خرید دام و گوشت را فقط از مراکز مجاز و تحت نظارت دامپزشکی انجام دهند.
🔹
همچنین گوشت تازه حداقل ۲۴ ساعت و احشاء (مانند جگر) ۴۸ ساعت در یخچال قبل از مصرف نگهداری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/673688" target="_blank">📅 10:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6YfC36mRjICJQFwM28UOyFdot6yFgrxEubT2q0QQyNfhP4_u6VV3Irh85UVXExprxkfsGjbgSK5hkcu-KotyXzFFo3p2LajPiTksVMtQ4ReTR1BoU5gcwlL-h5dGSWIlTmQBidjAH8WnSBU4rdDyULpTW9sc4DSIYLaSWGlgoJ-wg4Oe2-FQFJu4RuuopZD4RZpz6Znzrwklug3F91yAwRrd13wwbl6YbnVrUsXkz2T2392vjLhB1zw2mROS8YAAdWYXK6gLv3wtB6eQRQBToJXwxyqenWkWiPPUuyFbLYAu5I2oy971Q8MjqMRlkwkDRe5gKP1oqfP631bQa_6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندهایی که لباس ۴۸ تیم حاضر در جام جهانی ۲۰۲۶ را تامین کردند
🔹
آدیداس(۱۴ تیم) مانند آرژانتین، آلمان، اسپانیا، ژاپن، مکزیک، نایکی(۱۲ تیم) مانند برزیل، انگلیس، فرانسه، هلند، آمریکا، کانادا و پوما(۱۱ تیم) مانند پرتغال، مراکش، سنگال، سوئیس، اروگوئه
🔹
۱۱ تیم باقی‌مانده از ۱۰ برند دیگر استفاده می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/673687" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb476e8d.mp4?token=pcWDfDBS5wzfoBng25BPAN6cfk6G8dnypkqf5vPLzZYNMgt_HvtjNcEF6YKJR7eXgHEGYlt9krm6zN_oDmE-F8z2V7yoXeCaRUha3MGzrQnLZSbOw-ngRQDpHz0y6BO84T2JRWvzArEJheEliuoCxg5fiMMQB9kpOL2j4sO6QdA3423tzSsM7By_47ELWYy39TqjNuzFPgCq3hmVXj3GsU9NuU6ONHwc8Mo-jF9N93P2RcojZWL14FMu_DMGbcXDxv6EEtcxeHG3V8OkD3jNI7TeJsIiolxm9i4Hyk-d1EbR3YwNkK6U5P8YPrayzvlzv56QUYdnMFd5k05JC_cm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb476e8d.mp4?token=pcWDfDBS5wzfoBng25BPAN6cfk6G8dnypkqf5vPLzZYNMgt_HvtjNcEF6YKJR7eXgHEGYlt9krm6zN_oDmE-F8z2V7yoXeCaRUha3MGzrQnLZSbOw-ngRQDpHz0y6BO84T2JRWvzArEJheEliuoCxg5fiMMQB9kpOL2j4sO6QdA3423tzSsM7By_47ELWYy39TqjNuzFPgCq3hmVXj3GsU9NuU6ONHwc8Mo-jF9N93P2RcojZWL14FMu_DMGbcXDxv6EEtcxeHG3V8OkD3jNI7TeJsIiolxm9i4Hyk-d1EbR3YwNkK6U5P8YPrayzvlzv56QUYdnMFd5k05JC_cm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تیم ملی اسپانیا روی پهپادی که به سمت مواضع دشمن پرتاب شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/673686" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673684">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای آکسیوس: میانجی‌ها پیشنهاد آتش‌بس را به ایران و آمریکا ارائه کردند
🔹
پایگاه خبری آکسیوس به نقل از منابع آگاه ادعا کرد که قطر، مصر، پاکستان و چند میانجی منطقه‌ای دیگر، پیشنهادی برای آتش‌بس ۱۰ روزه را به ایران و ایالات متحده ارائه کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/673684" target="_blank">📅 10:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673683">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
مرحله بیستم عملیات صاعقه ارتش؛ ادامه حملات پهپادی ارتش به پایگاه های آمریکا در منطقه
ارتش:
🔹
از بامداد امروز و در مرحله بیستم عملیات صاعقه، پهپادهای انهدامی آرش در چند مرحله محل اسکان و استقرار نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین را آماج حملات خود قرار دادند.
🔹
پایگاه شیخ عیسی از کلیدی ترین تاسیسات ناوگان پنجم نیروی دریایی آمریکا و مرکز عملیات ارتش متجاوز این کشور است که عملیات هوایی و کنترل پهپادها از این پایگاه هدایت می شوند.
🔹
ارتش جمهوری اسلامی ایران تاکید کرد، عملیات های تهاجمی  تا بازداشتن دشمن از  ادامه تجاوز به کشور با قدرت ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/673683" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673681">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngTJItB8ND-1ybbU3IZ40_fBgSEj2QdfYRPRPBcQF6T0ClTTGI0D5DlrovzBLo8E9ssVNibmgfH7O6JZR7uRowG-ujSUeaOMKQFu10OmN7boD8gHFyI2CAocQx8oQoxFEw_-bVCZJW7rxmDyKn5CaIByMvQiF_q9ziMrCJShTn-i8jQPqaATf_hA5_BgZK805l2qsmFRG_7LFRWe4MnQIpd4ziwQjfqY5xyMNB7iedsvsGxtHPymG5GnmnGgOWeP8ui3T4dCFNx-wwO_N5urgMgojKoPxLGjkluL9qzMYDZi2lVJtLvNNjaPVoT43a7dRhIeZ0QFbf16XntlLBgQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی آژانس‌های اطلاعاتی آمریکا از نبرد تهران و واشنگتن
واشنگتن‌پست:
🔹
آژانس‌های اطلاعاتی آمریکا یک بن‌بست طولانی بین تهران و واشنگتن را پیش‌بینی می‌کنند و معتقدند که بعید است دولت ایران تحت تأثیر قابل‌توجه دور جدید حملات نظامی آمریکا قرار گیرد یا موضع خود در مذاکرات را نرم کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/673681" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
وال‌استریت ژورنال:
🔹
ایران هزاران سانتریفیوژ غنی‌سازی را به اعماق کوه «کلنگ» منتقل کرده؛ اقدامی که هدف قرار دادن آن‌ها را حتی با پیشرفته‌ترین بمب‌های سنگرشکن آمریکا نیز بسیار دشوار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673679" target="_blank">📅 10:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NifxisOj3JsBE0NXVtVAHB5TV1yOjNea3-Mid5kwVwk3apde2SxmU4yxuxXo9pG0I8b-wyZK1KD8sRlOWQc-I1p1X6fPxdUzXszNug1URr_xBpVdq61ObN7oNdVcJOq4yvIn1UjeD6FfROyj2iVSwtU8xWh_Q_YkkAqBLmXKxXPRLQCoHIfIqGOk_D4iYVAnzMAyerudsHYGvgx2j9intT4QH--TOqaWh_OhT6SaDp01jBgRYGcgDyvkN5sD2HFOYDu1xlE0wf_frBEsoqBw3zTW0_nNp9JkDvjz4_rXSxYd-zKnlcfEMZHNhexVvCKi-Q7fTyqjfwnB84BLSzaWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه پاسداران: به تجاوز دشمن پاسخی فراموش نشدنی می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/673678" target="_blank">📅 10:07 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
