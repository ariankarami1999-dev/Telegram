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
<img src="https://cdn4.telesco.pe/file/LS3aAaFhtq0KVGUsAKWBXtM5RKCtqYzs077z4e2EHIw3oA-UhYQKODuLcm8ENz0V8pkOFf6AfjFe_Bv4Yr-Ru50z8IodLnnToCXrYCHDvlQyuzwWj71arb89cGAAUvj2vtztZ-ii3ZDv4Ak4M8iAsBLtrt42DQvmAEktxn0haRfhgZ1XB7kf_yQktJNoOEH2wyPVxy-5yUzh0vPOqd2T3Z6NRGChWZ8zqREtKxQ0PVZkK8DjvgeaAB5JFO2ubG9sPIzdLjPcbOoY2t8TeQ5TKj_NqU8aqL9-TszyCSA5WArgXoKCAJwzrunJjBLkO1rJRhtP6_GsoZFrLKMsin1gmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 13:24:39</div>
<hr>

<div class="tg-post" id="msg-455282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37c01a31.mp4?token=mw3iyQsR8oDaeezKSGOeKInXRJT8fb-22iYOh1dXXXKzl6Yf3B4G7BsFcwdN-tWFdwvuLRN3przSgLYbqnEph1wMwba7m1BRkGF4rc3lB9N5lV0YWpHQdun1BQC4KRV3Zg-iWuPMY4JthIcJmr5zpZNJuUGEOX0WNlZT3gOb-LWsGjvYUuxi7MEjKcb0s3OfM77wZXwOmxokq6KGJPz0jPwogllXImb8DaWRRoOojzlB1cO0_-iG326DPlbGPahVn9Z33RWBonZQEplgKewB5Qz__L222k2nuwzgaooTxM5F3Jt19bomkV1T_U3b1Hdp-gP9Gp_XkqMXOnO1ABm1eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37c01a31.mp4?token=mw3iyQsR8oDaeezKSGOeKInXRJT8fb-22iYOh1dXXXKzl6Yf3B4G7BsFcwdN-tWFdwvuLRN3przSgLYbqnEph1wMwba7m1BRkGF4rc3lB9N5lV0YWpHQdun1BQC4KRV3Zg-iWuPMY4JthIcJmr5zpZNJuUGEOX0WNlZT3gOb-LWsGjvYUuxi7MEjKcb0s3OfM77wZXwOmxokq6KGJPz0jPwogllXImb8DaWRRoOojzlB1cO0_-iG326DPlbGPahVn9Z33RWBonZQEplgKewB5Qz__L222k2nuwzgaooTxM5F3Jt19bomkV1T_U3b1Hdp-gP9Gp_XkqMXOnO1ABm1eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان اطلاعات نظامی اوکراین: ۲ لانچر اس-۴۰۰ روسیه را منهدم کردیم
🔹
سازمان اطلاعات نظامی اوکراین اعلام کرد که در عملیات پهپادی در منطقهٔ کریمه، ۲ لانچر اس-۴۰۰ روسیه و یک آنتن کنترل پهپادهای روسیه منهدم شدند.
🔹
به روایت مقام‌های اوکراینی، در این حملات از شهپادهای «ماگورا» (Magura) برای حمل پهپادهای عامل حمله به لانچرهای روسی استفاده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/455282" target="_blank">📅 13:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOWNvIMgWBsuzyxPxGn8NcTX5MfVqGTVUSPXHaeusPZ46yV6rpG9eYEEu08JxBHAIZYqAkJVFiY1LrjAfNzjHHGxx9-DtQ0n7VA5n4-WDLQm5c6XXbp2XYUC4xRor6Vp_3Ph0lVhZGx2CwTMAREWNq2s_lQP5SrgMGCPnAZvI60rZyiTHB3qdFaEYuOMs5xzjsjVKbx940P8XNQ5BeKJDSSTl4gIp3vhP8MvF9l05a8qitQ6EJ7avPwLJ37JKSd630oBI6DmJ4DF8AesGE4D6VRBol0GF4f3p0ts-56ykD1dmDuqse3CTJVizcSDEU4o01rTjuk56Y4tG2LNpZQesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی به لیگ ازبکستان رفت
✔️
مرتضی پورعلی‌گنجی مدافع ۳۴ ساله پرسپولیس به پاختاکور ازبکستان پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/455281" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
بدهی مجموعۀ آزادی برای کشتی دردسرساز شد
🔹
بدهی مجموعۀ آزادی به وزارت نیرو برای مصرف برق باعث شد امروز برق قطع شود و حتی شنیده شده برق مجموعۀ انقلاب نیز قطع شده است.
🔹
این اتفاق درحالی رخ داده که تیم‌های ملی کشتی جوانان و بزرگسالان خود را برای مسابقات جهانی…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/455280" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AskwXeY4yJ_r3L44NaN2VOJ_sRpJJbC8TgQ2QdVtX2Zd96ftC4868BaPI_NcipI_TkdIG9IYXtNQ8pXnHE1GSW5SWFal6ShsxforrSVDRAldK4RVfISUugcH6sKhNvm96umeRA79VEQ8A4aBGL26FZG_MsBZDpBSGO4dPunoHgyN6bDox93vNeB7252u3-fAlmbAkuWtM-95Elb3IbGwYIjvxHbXBxAFx-WxEwkt5wXqhUmxdUvTgCL_Mp5fVYBfg2RxFxZX_Haq5c0mNsN_Ik7z-9aJPnpFmWzzj2lGuyzpj34wnspiU6c8tdTLv7D_MYfmwcUNiIZOlMT0kv0z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با عبور از ۵ میلیون و ۶۰۰ هزار باز هم رکورد تاریخی زد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۴ هزار واحدی به ۵ میلیون و ۶۵۴ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/455279" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b222dc371a.mp4?token=KXkVJkeTY4ZOekIJBJIMCdCMeFD9D9zASOo67fl5s9vkyVnjbVw1ysrjvrEKd8cdbs8PrUzrK5nGG6GkgUfK5Tq0dnOxx0W4VriMKrMISWSuZfHe1p5KKMQmlsO9vUqJjOG8FAw9n0qZ87HyWwT2TTuq2G8MHJhCkcoGeN-dn-AXnlrEuGVw2OhOKYPc7TPVJ3pXwlRfoi2cCTgKr6fXh1Er63fE5ZUU1pGYMx8E1fIet7GS5E-6idnW9ed_Rh2BURaGh5-aq6pnOrEq3P60BVhG2rGvWbNRTwEabhRqwgfh_U34zcfHUDMhOhaoJk5HYaVRwDbciKNhdStunTDLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b222dc371a.mp4?token=KXkVJkeTY4ZOekIJBJIMCdCMeFD9D9zASOo67fl5s9vkyVnjbVw1ysrjvrEKd8cdbs8PrUzrK5nGG6GkgUfK5Tq0dnOxx0W4VriMKrMISWSuZfHe1p5KKMQmlsO9vUqJjOG8FAw9n0qZ87HyWwT2TTuq2G8MHJhCkcoGeN-dn-AXnlrEuGVw2OhOKYPc7TPVJ3pXwlRfoi2cCTgKr6fXh1Er63fE5ZUU1pGYMx8E1fIet7GS5E-6idnW9ed_Rh2BURaGh5-aq6pnOrEq3P60BVhG2rGvWbNRTwEabhRqwgfh_U34zcfHUDMhOhaoJk5HYaVRwDbciKNhdStunTDLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاکستان از قالیباف و عراقچی برای سفر به اسلام‌آباد دعوت کرده و این سفر در زمان مناسب انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/455278" target="_blank">📅 12:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc9a50c3c.mp4?token=GUYWbMEmH4pxJg0U5mIFJpWwJjfjZ6V0mnVbG2gH5RWINL_icfMjqAFVUu9LRHonic1mdiH-G8QygzhYk-tJwV7AIZqAQksixhYpdVloobszTqUiVQUa-BmU2OsFm9DIypZYXQO9tumLOG99KEYwOCXiC24of7xZpmgzCpAVyLSEdS8PyunjAYPwgR38uCiVMETw9lw6WaZ8FbfS7oVjb5HhJsrgEXzwqcx4fcnP_YgNrs5ES90H-Ur1zrfkIKzDHTB7nfysjVw3aFk5lXOs1U_ZYpnpb8juoG7E-OBzioxUAoNJ08foOtVfKL6KWy_vg3LrIZG0e2E9SSOjEc8CBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc9a50c3c.mp4?token=GUYWbMEmH4pxJg0U5mIFJpWwJjfjZ6V0mnVbG2gH5RWINL_icfMjqAFVUu9LRHonic1mdiH-G8QygzhYk-tJwV7AIZqAQksixhYpdVloobszTqUiVQUa-BmU2OsFm9DIypZYXQO9tumLOG99KEYwOCXiC24of7xZpmgzCpAVyLSEdS8PyunjAYPwgR38uCiVMETw9lw6WaZ8FbfS7oVjb5HhJsrgEXzwqcx4fcnP_YgNrs5ES90H-Ur1zrfkIKzDHTB7nfysjVw3aFk5lXOs1U_ZYpnpb8juoG7E-OBzioxUAoNJ08foOtVfKL6KWy_vg3LrIZG0e2E9SSOjEc8CBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/455277" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWqBebWsFy8WFBi3ck_BRqhlsYzAWyVyHbJe6Ry0R7njw2uAn3WTTs--7-u-ooBP1VlnrJthflwWADIYGOAxwOKi3vgBSJEFnoTZ8b73YjnKtt-GrEECjrPwn931BOLlEnHEYACvM5aNzOsl5ohRzIM0fh1O-MbdNUN1-pV9-tA8pBGtnpSDeZeZRK8twa709slLcLWxehduD5i0pKd3fRtniC5mrZ-16RnzByH6uzwV8NBVvPFRtsIEzM8T3n3m-xos1grfL7lQIjMRVexLH2y2ka-psQLsD8JJuQ5OR3TBPDosS2gGJ8F9PSuOyLzDU_RcFVFapTXVaB4UEmLLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تعزیرات: سهمیهٔ گران‌فروشان نان قطع می‌شود
🔹
رئیس سازمان تعزیرات حکومتی: در صورت تکرار ۷ نوع تخلف، از جمله گران‌فروشی و برخی تخلفات مرتبط با عرضهٔ نان، با قطع یا کاهش سهمیهٔ آرد و همچنین تعطیلی واحد متخلف برخورد شود.
🔹
بیش‌از ۱۵ هزار پرونده در حوزهٔ تخلفات نان در سراسر کشور وارد شده که حدود ۱۳ هزار پرونده از این تعداد مختومه شده و حدود ۲۹۰۰ پرونده نیز همچنان درحال رسیدگی است.
عکس: علیرضا مولوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/455276" target="_blank">📅 12:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e0493aa7.mp4?token=he7Jg6bxWLczFeOomrts0mmSWX9r_fjGeYo7jVTRTS-elxZnvLZN0fhv_5zXH0j5YsPAu6hGJZWgzgUNkt4mXPCmOgjesZygmobIgQ714O0HDKUpFO-9I1YNZQZTwV7C6D_xIcus_qDOdVrWy_XXttD38UQ25IcPDOzQ2vBpwG-HKQslDXasj0Rwyl4tVbi-rlvQIfxGqO29t3RJ6qvXn4NNYpOG1BAFTKapzSjH2OHzWT3lyODLzrxeilGplK7LlTc5A0NKVc1AweiFrKVf3BwRfL0GiJ5jfOJaDBgxww0ODBZGXnpcUXO7nb4gtvKsuStH13Q0vARCrUiIKzjmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e0493aa7.mp4?token=he7Jg6bxWLczFeOomrts0mmSWX9r_fjGeYo7jVTRTS-elxZnvLZN0fhv_5zXH0j5YsPAu6hGJZWgzgUNkt4mXPCmOgjesZygmobIgQ714O0HDKUpFO-9I1YNZQZTwV7C6D_xIcus_qDOdVrWy_XXttD38UQ25IcPDOzQ2vBpwG-HKQslDXasj0Rwyl4tVbi-rlvQIfxGqO29t3RJ6qvXn4NNYpOG1BAFTKapzSjH2OHzWT3lyODLzrxeilGplK7LlTc5A0NKVc1AweiFrKVf3BwRfL0GiJ5jfOJaDBgxww0ODBZGXnpcUXO7nb4gtvKsuStH13Q0vARCrUiIKzjmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/455275" target="_blank">📅 12:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e338aa971e.mp4?token=YHN6T2p5As27-HVOkrD1wP7s6phjM42jG1hOa3C9lFusZMOZZXwHJ7s3CCDzWk_TYVOhM7yBHk6PyREusweBu684xvgwVN04gX33m5T_Lm-2Cb6hhfBAkr6lM1hiDRyD6BMTHDcQ1TdW0VgxNdI725cgPeOdB1lcQlKHzGtBj8Wrb5FM4xjTulnHoKAe4Sn-90tRlXwiVhTLQvC3nKnk70_qBPqrfLZSPMB-ptqgGEwhU-PPxax6UNRcF1Ogq8v8hfwz00OXHO8FkciXiB-hrMDJph-7cWvfr06xVZbt9Zq3-C9lzV9KA5Ou4qz1wiYpJ-L-MqJWU-q4STiQOoG0Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e338aa971e.mp4?token=YHN6T2p5As27-HVOkrD1wP7s6phjM42jG1hOa3C9lFusZMOZZXwHJ7s3CCDzWk_TYVOhM7yBHk6PyREusweBu684xvgwVN04gX33m5T_Lm-2Cb6hhfBAkr6lM1hiDRyD6BMTHDcQ1TdW0VgxNdI725cgPeOdB1lcQlKHzGtBj8Wrb5FM4xjTulnHoKAe4Sn-90tRlXwiVhTLQvC3nKnk70_qBPqrfLZSPMB-ptqgGEwhU-PPxax6UNRcF1Ogq8v8hfwz00OXHO8FkciXiB-hrMDJph-7cWvfr06xVZbt9Zq3-C9lzV9KA5Ou4qz1wiYpJ-L-MqJWU-q4STiQOoG0Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدهی مجموعۀ آزادی برای کشتی دردسرساز شد
🔹
بدهی مجموعۀ آزادی به وزارت نیرو برای مصرف برق باعث شد امروز برق قطع شود و حتی شنیده شده برق مجموعۀ انقلاب نیز قطع شده است.
🔹
این اتفاق درحالی رخ داده که تیم‌های ملی کشتی جوانان و بزرگسالان خود را برای مسابقات جهانی و بازی‌های آسیایی آماده می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/455274" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_SXfxl82RwL8TJSBHlTpOOVGnhuWAO1A5zL8ZEdfJF2RNTYWbRAPHLdtFIZ5OEv8E_HJf9dQWg8mzWwshc4i4Ju0Q8s4ByTOAu-I0d4Ic08fDmBxhKfcgvA10Dzrv0oIPDJ5BI6Sd1tNea6Xi-yizf_LEQWBNtWqu96lLICAioy8a0W8TGGQzZIBekJgJ2276f42df9mv8cn8qdPhtioPKwep5NHgf50JFyqDH-sRuLpvHvD8kYZm-EMkLsxzWyYA9pEwmgeUBl-UG-3iRenibA_5TZ0DpnW6cL3AIDjewg97iGI8nMwKxzzWy_KxEKaqxojYC-XPo26l8y0FNiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ تازه سایپا به مشتریان در انتظار
🔹
مشتریان سایپا می‌گویند این خودروساز ساینا و سایر خودروهای ثبت نامی را تحویل نمی‌دهد.
🔹
برخی مخاطبان خبرگزاری فارس در پویشی اعلام کرده‌اند سایپا با وجود دریافت وجه و وعدهٔ تحویل ۹۰ روزه، پس از ۱۰ ماه هنوز خودروها را تحویل نداده است.
🔹
حالا سایپا می‌گوید روند کاهش تعهدات تا تحویل تمام خودروهای باقی‌مانده ادامه دارد.
🔸
اوایل اسفند سال گذشته، تعهدات معوق این شرکت ۵۸ هزار دستگاه اعلام شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/455273" target="_blank">📅 12:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fb6fa172.mp4?token=hhD4fM1cusaIbkXonwvBBIJ8p-Op_POiEaSc_EmTvGn3alPz9ckXjUnzqOEllF3rNk3yVJF55sGyzeXQKsTI8e3sCvmKwvP6nckKEwEoAoQTTjifjfvQIKrxX1wM_wSzqc48sYIoKzvkWnXym2jV6UB9hJQW8fFYUjm6LsnQWRip4WajvTJSvL1mn6c5SVHx7gpG-yTaD28UWLh7iYnAliIppc3jcaMKpqo_qHwZZ6M700KfYdsZuO3QeODKRFvpkUOD-FegQnHXBZNLnD2FHGMHzD0B_kA8YxV3SOzFHLnY12x7uEyvGxIA0-YUbX4-tDxkOT5H7huWmH8it_QfIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fb6fa172.mp4?token=hhD4fM1cusaIbkXonwvBBIJ8p-Op_POiEaSc_EmTvGn3alPz9ckXjUnzqOEllF3rNk3yVJF55sGyzeXQKsTI8e3sCvmKwvP6nckKEwEoAoQTTjifjfvQIKrxX1wM_wSzqc48sYIoKzvkWnXym2jV6UB9hJQW8fFYUjm6LsnQWRip4WajvTJSvL1mn6c5SVHx7gpG-yTaD28UWLh7iYnAliIppc3jcaMKpqo_qHwZZ6M700KfYdsZuO3QeODKRFvpkUOD-FegQnHXBZNLnD2FHGMHzD0B_kA8YxV3SOzFHLnY12x7uEyvGxIA0-YUbX4-tDxkOT5H7huWmH8it_QfIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تنگهٔ هرمز به‌خاطر اختلاف‌نظر ایران و عمان بسته نشده که با توافق ایران و عمان باز شود
🔹
بازشدن تنگهٔ هرمز منوط به تحقق شرایطی است که در پی تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران تحمیل شده؛ ما هنوز در جنگ هستیم و تا وقتی که محاصرهٔ…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/455272" target="_blank">📅 11:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJXU1ygsOFxUQ76WqZYgyVKLLisFjN9b22fyAu6jScv2ZYVgbNS66FYJBZRkLoXqNfXqQabxduFq2zm8gxCWcKr16l34IaV8EIMbavsIfwHoUrawacMaGL_sn3afd6FhM45ny_XZ4_kX1Tit9w9PxvB1qxFoHFAyOseq4D8a2nGnIt5nuXTHyd7K54xnYrj6dCuTmuTF5JuX98_OzXjRuLp5F8QCNtqD8TokULyhl6k5cA87fyqpJRKyVntPCEfX1Acbz4iuKMwhm6r-iLHBHgQPtHUTpRmG4dQs9WhdFIElnbC2B2g_ovGf3RoillC2f_BOZ83_rzvZfCduoVtEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خضریان: کلیات طرح اقدام راهبردی امنیت تنگهٔ هرمز در کمیسیون امنیت ملی تصویب شد
🔹
عضو کمیسیون امنیت ملی: با توجه به موقعیت راهبردی خلیج فارس و تنگهٔ هرمز و لزوم اعمال حاکمیت جمهوری اسلامی ایران به‌منظور پیشگیری از تکرار اقدامات خصمانه علیه ایران، کلیات طرح…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/455271" target="_blank">📅 11:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b1474c5f.mp4?token=BUuAn-lbIoBEozBmGZlH1_faiK0fcXY1DOhu9XsB-0QqJBt0ASKDCkMLNke4-f_cS7nUbzkW4UahnPMxK-k-h47puHR573ZDh3_IB5QoIRKC2F5fhoWYNI537O1sq2PlDeaYw1jJRYypmTg2jpz-RBljIYICmzV52ABWgu5Z1zi5qORc1WxsBCfQTOMqRBj3cXL1lrFYNYI2OOl5y_y8TlF6Jx2FSzaYDOttLI8Q2zrzN6Os72cVS4PiQzgkTpHg-XIwkmBn94Pc638goJVAl79Z6YMt61v01NDqCqgzsZvmea_ibqmNArpKOF-qe4liP07LBUFZ5_753ENrWevk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b1474c5f.mp4?token=BUuAn-lbIoBEozBmGZlH1_faiK0fcXY1DOhu9XsB-0QqJBt0ASKDCkMLNke4-f_cS7nUbzkW4UahnPMxK-k-h47puHR573ZDh3_IB5QoIRKC2F5fhoWYNI537O1sq2PlDeaYw1jJRYypmTg2jpz-RBljIYICmzV52ABWgu5Z1zi5qORc1WxsBCfQTOMqRBj3cXL1lrFYNYI2OOl5y_y8TlF6Jx2FSzaYDOttLI8Q2zrzN6Os72cVS4PiQzgkTpHg-XIwkmBn94Pc638goJVAl79Z6YMt61v01NDqCqgzsZvmea_ibqmNArpKOF-qe4liP07LBUFZ5_753ENrWevk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: تا زمانی که آمریکا موارد نقض تفاهم را جبران نکند، امکان مذاکره وجود ندارد
🔹
مذاکرات ما با عمان به‌معنی بازشدن تنگهٔ هرمز نیست و صرفاً جهت تعیین مسیری است که در صورت بازگشایی تنگهٔ هرمز از آن استفاده خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/455270" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=q1xZQ-bSfYh0NqQWi6x_tAmarg6cteFKvpSkskQ4vgR3pNzq6DVOONEcdXYEOVugFw6RkDnACOEB2iToL9w0VXa4V-C5CzOfOrFKmRllqX592iE1FLh-nr1TyatbamlCQxOAqf4XLHhMD_9X5pHtM8Ch906XodYLSNWE4RcBecqwuYiTlVZoQQN1E49-kZ7m1tJch8hEUpeSI0CJpVJgtChXr3aHlsPeQLrxfq5W6RKjOItR4Q3pSbma1nVoKb_6OijIsHlzAea5X2invTD-3btFnoHCVOAn4ugSi_H045zjZOjuMzYbRMd8hrXDxOqpKLdW3yu1h_5Ij-jMlDr3HUsWxD4Dp9_J1G1iZ8yU70Vt7-QVr4rKi8fx1nyR1nb2bNJR7wO9-oTbsH2ErU68cV_Tek8zqXmlXNOwzE928CaqKyCDtGypVGbaPSRYSFvQg-2WAwBdUd9Q3lmOJHD1bhkWHhb32YnK15W3QIZJY7ijtmeQ-NJ_SCsICtEHUZNt4ebIteh84vArGB0TlpOWzUIaeO83fbjf53Cl7QHL3FGg_u072bhhKzjrNPBxpGuDMt1XqdHCb189I7uPsYzmB6xnSQ-yxfVEWbi2UB0xCAiOy_zi7jXMF4rMW1QDzVG7BSjHq0KhYcsfcMI42we1fYkNQEpaCf_Uj3PMY2C2gfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=q1xZQ-bSfYh0NqQWi6x_tAmarg6cteFKvpSkskQ4vgR3pNzq6DVOONEcdXYEOVugFw6RkDnACOEB2iToL9w0VXa4V-C5CzOfOrFKmRllqX592iE1FLh-nr1TyatbamlCQxOAqf4XLHhMD_9X5pHtM8Ch906XodYLSNWE4RcBecqwuYiTlVZoQQN1E49-kZ7m1tJch8hEUpeSI0CJpVJgtChXr3aHlsPeQLrxfq5W6RKjOItR4Q3pSbma1nVoKb_6OijIsHlzAea5X2invTD-3btFnoHCVOAn4ugSi_H045zjZOjuMzYbRMd8hrXDxOqpKLdW3yu1h_5Ij-jMlDr3HUsWxD4Dp9_J1G1iZ8yU70Vt7-QVr4rKi8fx1nyR1nb2bNJR7wO9-oTbsH2ErU68cV_Tek8zqXmlXNOwzE928CaqKyCDtGypVGbaPSRYSFvQg-2WAwBdUd9Q3lmOJHD1bhkWHhb32YnK15W3QIZJY7ijtmeQ-NJ_SCsICtEHUZNt4ebIteh84vArGB0TlpOWzUIaeO83fbjf53Cl7QHL3FGg_u072bhhKzjrNPBxpGuDMt1XqdHCb189I7uPsYzmB6xnSQ-yxfVEWbi2UB0xCAiOy_zi7jXMF4rMW1QDzVG7BSjHq0KhYcsfcMI42we1fYkNQEpaCf_Uj3PMY2C2gfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس مسائل غرب آسیا: پس‌از ۶۰ سال تنگهٔ هرمز کاملاً ایرانی شده
🔹
حاکمیت و مدیریت ایران بر عبور و مرور در تنگه تثبیت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/455269" target="_blank">📅 11:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8806c8be.mp4?token=BC1-EUCeJRhatOLuO8fjAV1Bu8L7VmlmW_r4J-8Q1QPJsrZ8XRS8AHpmuqf9kvdqVjU6ao6yO4roQTHmmAGaiykYeSsUPJ7RD8InkEvh4NyU-crSIYJV-NlZYh66OF_PQyVfQUnZ1_pRwIr_vDAzVZxDqCEgHrx17l8iM10a7GHeXpUOKEyV7xyTKpk8Ea7J9fZ37GMD-rzqRpQKYG8P6A9-ZtqYdIiaugeoGQfXBD3RDkN18fM92TyXwGVC4AhzusVnnz9XA6MgzfvtPJ8edGxfhUvYMnL7S4gDZaMunbnaqWaFby6fJuVumwVkyWVg2C_dkARww02v0GmF83QgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8806c8be.mp4?token=BC1-EUCeJRhatOLuO8fjAV1Bu8L7VmlmW_r4J-8Q1QPJsrZ8XRS8AHpmuqf9kvdqVjU6ao6yO4roQTHmmAGaiykYeSsUPJ7RD8InkEvh4NyU-crSIYJV-NlZYh66OF_PQyVfQUnZ1_pRwIr_vDAzVZxDqCEgHrx17l8iM10a7GHeXpUOKEyV7xyTKpk8Ea7J9fZ37GMD-rzqRpQKYG8P6A9-ZtqYdIiaugeoGQfXBD3RDkN18fM92TyXwGVC4AhzusVnnz9XA6MgzfvtPJ8edGxfhUvYMnL7S4gDZaMunbnaqWaFby6fJuVumwVkyWVg2C_dkARww02v0GmF83QgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس اوراسیا: پیامدهای کنوانسیون دریای کاسپین از واگذاری بحرین هم زیان‌بارتر است
🔹
برهان حشمتی: در کنوانسیون رژیم حقوقی دریای کاسپین، فرمول ۱۵ مایل آب‌های سرزمینی و ۱۰ مایل منطقۀ انحصاری ماهیگیری پیش‌بینی شده؛ یعنی در مجموع ۲۵ مایل. این محدوده به‌هیچ‌عنوان…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/455268" target="_blank">📅 11:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ab3f7d2.mp4?token=bjRQylS-ErnGywZflXtGKu13lC3P079pCBfjNMQThyB6CVzrTcOX6h56H8Vgn3ylKyJcyesuSlMFpBRD3WOZQIjfjB9Eurn6E1OiAKIqzaQZDCg8lMN-sYmzT_Ygi6qZvbimSy0kJAwuziZvW-1p1phGqU4Kl6kkxQ_dnwlb-buzl7rq6ur1s0j5mx5Jt888jqC5C3HKW61qdXc-RGiku3XsUhV6g65iaB0Y5eSzlAkK9WX0ww2afXQ1bOHYHabPXiDRZjjyQJOCQLguIs2kzC65x6DXlnnLc-TsS4v_-AxE6zz8sV0CiTHNKu1qDZBydiW2UO3nN3HXY2SQUjsL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ab3f7d2.mp4?token=bjRQylS-ErnGywZflXtGKu13lC3P079pCBfjNMQThyB6CVzrTcOX6h56H8Vgn3ylKyJcyesuSlMFpBRD3WOZQIjfjB9Eurn6E1OiAKIqzaQZDCg8lMN-sYmzT_Ygi6qZvbimSy0kJAwuziZvW-1p1phGqU4Kl6kkxQ_dnwlb-buzl7rq6ur1s0j5mx5Jt888jqC5C3HKW61qdXc-RGiku3XsUhV6g65iaB0Y5eSzlAkK9WX0ww2afXQ1bOHYHabPXiDRZjjyQJOCQLguIs2kzC65x6DXlnnLc-TsS4v_-AxE6zz8sV0CiTHNKu1qDZBydiW2UO3nN3HXY2SQUjsL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئویی دیده‌نشده از شهید سپهبد موسوی کنار نوه‌اش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/455267" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd73ed7028.mp4?token=UXZpqLUTYDEPiEnWr-LjX3ShLmeBdFDNwPgfjnDCObkLxazC-Xpee-4eVZ8cjv6Q1xNuyNSTcn1kUN4LXdOJOzemX8GrPdrVJuLQakRuE1ojhC_-SvGHUvKcjOlioWl_a8GpNLn4TDqSpFrLh8xDF-4Od6nts74HxhUww0_pPZSrqzqJdGkG9Wb0RnillJ2-TefQ38caV3x5U_SjftW7Sh-WlD-QpCbjpTAN7sbsthXR4_DKuW_KEIdu_kGpyfIxBoltiIiXQzvP8x7vpnRQ12NXiRm8cuUfSlOC_CXrsLFYubljfF-cxllYFw6VXGHuc3W7cl2YUORjkBX4Uk-TEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd73ed7028.mp4?token=UXZpqLUTYDEPiEnWr-LjX3ShLmeBdFDNwPgfjnDCObkLxazC-Xpee-4eVZ8cjv6Q1xNuyNSTcn1kUN4LXdOJOzemX8GrPdrVJuLQakRuE1ojhC_-SvGHUvKcjOlioWl_a8GpNLn4TDqSpFrLh8xDF-4Od6nts74HxhUww0_pPZSrqzqJdGkG9Wb0RnillJ2-TefQ38caV3x5U_SjftW7Sh-WlD-QpCbjpTAN7sbsthXR4_DKuW_KEIdu_kGpyfIxBoltiIiXQzvP8x7vpnRQ12NXiRm8cuUfSlOC_CXrsLFYubljfF-cxllYFw6VXGHuc3W7cl2YUORjkBX4Uk-TEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به پیمان دفاعی مکه: کشورهای منطقه در ۳ سال گذشته فهمیده‌اند که امنیت، کالای قابل‌خریداری از دلالان دروغین نیست
🔹
هر طرحی که مبتنی بر واقعیت‌ها باشد و دشمن و تهدید را درست بشناسد، به امنیت منطقه کمک می‌کند و جلوی بی‌ثباتی دشمن…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/455266" target="_blank">📅 11:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صدور کیفرخواست ۶ نفر از کارکنان یک‌ نهاد‌ اجرایی به‌اتهام اختلاس
🔹
دادگستری سمنان: کیفرخواست ۶ نفر از کارکنان یکی از نهاد‌های اجرایی گرمسار به‌اتهام مباشرت در اختلاس میلیاردی توأم با جعل، تضییع اموال عمومی، مشارکت و معاونت در اختلاس و دریافت رشوه صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/455265" target="_blank">📅 11:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cff58db5.mp4?token=ciEPDtUlS1QCFIxeE-KJbAX3I3x0JLhH0BJZTuWMBJIBE3UIGkcDAPm45S1AIbJzjBX2IKjikG6HCD65PAMAak975Lo-f1IZQyWxluJWkt0AYPTNdY3l4VXjzoE5evPCOuKCIkDrXXMjpS99de6SDcgVL45Snz1dSJ9Se-LO5j-SrNo5p8LJpnb-ysAylcNaWLNcBrgrV6wBAfe--llQ4SPbR3AVk5F9qPK1E7F18GnohCvUNfaim02ZN3rKeiBo0QppraKU6KiA_Cwj_ZWZ6CxdRP427VEUD9uVSULfWI04NBZXg48aZKYsHkkZFYkXidcqwIK1Zsd08zu0haP9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cff58db5.mp4?token=ciEPDtUlS1QCFIxeE-KJbAX3I3x0JLhH0BJZTuWMBJIBE3UIGkcDAPm45S1AIbJzjBX2IKjikG6HCD65PAMAak975Lo-f1IZQyWxluJWkt0AYPTNdY3l4VXjzoE5evPCOuKCIkDrXXMjpS99de6SDcgVL45Snz1dSJ9Se-LO5j-SrNo5p8LJpnb-ysAylcNaWLNcBrgrV6wBAfe--llQ4SPbR3AVk5F9qPK1E7F18GnohCvUNfaim02ZN3rKeiBo0QppraKU6KiA_Cwj_ZWZ6CxdRP427VEUD9uVSULfWI04NBZXg48aZKYsHkkZFYkXidcqwIK1Zsd08zu0haP9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است
🔹
اجازه‌دادن به طرف‌های متجاوز برای اقدام علیه ایران از سوی دولت‌های منطقه، آن‌ها را کنار طرف‌های متجاوز خواهد نشاند. @Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/455264" target="_blank">📅 11:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROpp_jKuVIsxEX8junY0PCZC4sPqzdircgPdJoXw0UzLMlss0FasNaFQ5vd_YgCDupENPE0UK1_gp8Q6oeUVDlfcmtVZPS5f74Ml0-aITXtoLSFCeoORqqM2GYbjE5uVxabb9zFWS-g4hpxrQTaUsaa2255gvmoUQDNh-jH9ptcVGn2sEPXdhAsyZefmIY3OnKDTl0jfAOYvavEHgDziDiUHroXDenQGDrbd9tuqIBHddcBBiRUHECgssCcP_GYYcm3u8KHgsiSUU1okahUgi-jL5Pdu4rwPEuD-Hugh2Eo7Sz5m0f1D-gPZVnvfeQd-CE-pIYlpAnVIDrgUbJyNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس قید قربانی را زد
⚽️
مسئولان پرسپولیس در مقطعی مذاکراتی را برای جذب محمد قربانی انجام دادند اما درخواست مالی باشگاه الوحده برای صدور رضایتنامۀ او باعث شد انتقالش منتفی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/455263" target="_blank">📅 11:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae325ab684.mp4?token=IpvwLUtGdIDAyHgM7lQJ9pnQ7iazEBqIVTHbBIeAj1OJ5TCJ23MhUrFO13uBqZxlM7pQZN8TRM9ZtbgWNceEDsK79mmJb7sHJaohsMosPhX4tBiJPpRWSZZZpPWZMQvf759b0qoIrsn3gpdrcVYyWXcl9B6xxzbX2OzxRNjGfWcmH6GrDBJFbOd46L_vBS74nqYWFpUml7tIHkklmOFoh24Sg-tTxeu8WPwsPbTB2a33gngkJ6HRTFFheXqiKIB5tAIzJR6EFW7QUccY9K9H1KtHECpUsHzG4FJWFJg8MXga0VCKUpd7PDzO_lHrGskmvrAynel-1gOXB3TnVKghtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae325ab684.mp4?token=IpvwLUtGdIDAyHgM7lQJ9pnQ7iazEBqIVTHbBIeAj1OJ5TCJ23MhUrFO13uBqZxlM7pQZN8TRM9ZtbgWNceEDsK79mmJb7sHJaohsMosPhX4tBiJPpRWSZZZpPWZMQvf759b0qoIrsn3gpdrcVYyWXcl9B6xxzbX2OzxRNjGfWcmH6GrDBJFbOd46L_vBS74nqYWFpUml7tIHkklmOFoh24Sg-tTxeu8WPwsPbTB2a33gngkJ6HRTFFheXqiKIB5tAIzJR6EFW7QUccY9K9H1KtHECpUsHzG4FJWFJg8MXga0VCKUpd7PDzO_lHrGskmvrAynel-1gOXB3TnVKghtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: افزایش اعتبار کالابرگ به‌زودی اطلاع‌رسانی می‌شود
🔹
شرایط جنگی تأمین منابع افزایش اعتبار کالابرگ را با مشکل مواجه کرد، اما دولت درحال تدوین برنامه‌ها و اتخاذ تصمیمات جدید برای تأمین منابع مورد نیاز است.
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/455262" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59de1a44be.mp4?token=JO_ptWfAm0sHItOos4z_Gz4uhyUF5a8bUpwZ2FqaU2jxUeyHl4SCPhQdyIY9LgEtF32qrcwUp-qIY_ZYyVSeNC0mALQlbWfo-mfNQgc2tbQJGoFYUyPnJfsnoCpcxZG2n_DsTKIKWehS_0okD_ECkGU7vhKi706YiBmXbcxg0K144dRjulSYMPelgQsix1oTAIV60QkPZuPx0jBpFVbmohRZnerNLOwbOP5kmKr5SSni68O8d8Dty6EkH0cTeDI3paTyB08jpvjQL-5dGt-yXaocJE5uFQw_zTU0nadC8Buv9kTb2I41fRfnflSczWJ6Cj9L8uGo_DLET0KVoVnxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59de1a44be.mp4?token=JO_ptWfAm0sHItOos4z_Gz4uhyUF5a8bUpwZ2FqaU2jxUeyHl4SCPhQdyIY9LgEtF32qrcwUp-qIY_ZYyVSeNC0mALQlbWfo-mfNQgc2tbQJGoFYUyPnJfsnoCpcxZG2n_DsTKIKWehS_0okD_ECkGU7vhKi706YiBmXbcxg0K144dRjulSYMPelgQsix1oTAIV60QkPZuPx0jBpFVbmohRZnerNLOwbOP5kmKr5SSni68O8d8Dty6EkH0cTeDI3paTyB08jpvjQL-5dGt-yXaocJE5uFQw_zTU0nadC8Buv9kTb2I41fRfnflSczWJ6Cj9L8uGo_DLET0KVoVnxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه: در مکه علیه ایران ائتلاف نکردیم
🔹
هاکان فیدان، وزیر امور خارجه ترکیه در مصاحبه‌ با خبرگزاری آناتولی گفت که ائتلاف سه‌گانه مکه می‌تواند گسترش یابد و علیه هیچ کشوری از جمله ایران نیست.
🔹
او همچنین تأکید کرد که ایران «هدف» این توافق نیست. فیدان…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/455261" target="_blank">📅 10:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2LhfiYerYfzS8yG5sq2OmLG269xvbt3DvLdL57ImJDFQdApfjoHy153GmEYDOlgcd2oeX_MgeDMqVYdAwwTOPrFTADst5QeEf-NaWUpooyUFcxJp-Z0RF6CgItFEg2G29FDOYWLgtA5oDpRd0FV8wu7icjgKRPEPgCKKbJ-4hgFsbGZQUFQX3hKZVNliLh0Mkk7Y8Gqu19u2IlVmQtXC3hVwjRnzqSaCPmpk36fYqwpnCvpaTsjCxwOzQj8FkmV157bgDVm-Bp4gGFsxrGyKfDTykrhKJoL1pCjY0ncwCVYFtTorDSwdlJgPozSym9Y_CvJMATmyZRwh4N5KQ641Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بانک رفاه کارگران وارد عرصه بانکداری ارزش‌آفرین شده است
🔹️
مدیرعامل بانک رفاه کارگران گفت: زنجیره مکانیزه تهاتر مطالبات و بدهی‌های سازمان تامین اجتماعی (تکو) گامی عملی برای تأمین مالی غیرتورمی و پشتیبانی از زنجیره تولید محسوب می‌شود و در این بانک ابزارهای اثربخشی به منظور تحقق اهداف این زنجیره طراحی و عملیاتی شده است.
🔹️
دکتر اسماعیل للـه‌گانی با بیان این مطلب در همایش ملی "معرفی و تبیین بهره‌برداری از توکن تکو"، این زنجیره را نقطه عطفی در مدیریت مطالبات و بدهی‌های سازمان تامین اجتماعی برشمرد و با اشاره به ظرفیت‌های این بانک در مسیر اجرای آن گفت: بانک رفاه کارگران با عبور از بانکداری سنتی و دیجیتال، وارد عرصه «بانکداری ارزش‌آفرین» شده است. این بانک تحول خود را بر پایه ایجاد راهکارهای هوشمند و متنوع مالی، حمایت از اکوسیستم تولید و ایجاد اعتبار شفاف برای خانوارها و بنگاه‌ها دنبال می‌کند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/455260" target="_blank">📅 10:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqryfzU9O3WMkJc6NiIGImcyyoQSPozb3tBacTOFd8a54cVoZsNKLEa5B83kmn_blg9KYgYi2LS5cpxHQCQq48kHaDbBZua5h7uh6-B-PNhHOCEcut6YCW305u6nhCaF1c4fHxuUM1WzJlpxMm9WKKxNbMlQk0UHsQbm6NnkZoXKVEDzBdzN-W-ElcxyZjDLmjFAHRC0Jd4-lm0uHQA_aYDT74iYpfn6__wk_lF4qB8TvGAFoN06r_8WINRKoMMGHlYoR2MHauVL42Pl31h1gv0-A6C30i8MuBSWbj8wvjwAIDpXiO54bDPBMfcyIkviHcwLSV4dOIwrYzarjOaFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
⚠️
مهلت ثبت‌نام: تا ۲۷ مردادماه
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/455259" target="_blank">📅 10:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/455258" target="_blank">📅 10:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455257">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اتوبوس‌های منتهی به حرم رضوی ۲ روز رایگان شد
🔹
مدیرعامل اتوبوس‌رانی مشهد: خطوط منتهی به حرم امام رضا(ع) در روزهای چهارشنبه و پنجشنبه، هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، شهادت امام حسن مجتبی(ع) و شهادت امام رضا(ع)، رایگان خواهد بود.
🔹
خطوط ۸۰۱، ۸۰۲، ۸۳۱، ۸۳۲، ۸۳۳ و ۱۲ در شب چهارشنبه تا ساعت ۲ بامداد و در شب پنجشنبه به‌صورت شبانه‌روزی فعال خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/455257" target="_blank">📅 10:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌ تبریک سرلشکر خلبان عبداللهی درپی انتصاب محسن رضایی به دبیری شورای‌عالی امنیت ملی
🔹
متن پیام فرمانده قرارگاه مرکزی خاتم‌الانبیا: انتصاب شایسته جنابعالی به‌سمت دبیری شورای‌عالی امنیت ملی و نمایندۀ رهبری در این شورا را صمیمانه تبریک و تهنیت عرض می‌نماییم.…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/455256" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6396b5eab3.mp4?token=nX-leuzL4kEzGPjs0r48hmDwire0xPig6Xs8UJDnNleyjbzVlK3efX_Qk8xBxdIaRz9kNueWPh0fugPQ7BYd2TWmIl3l4cmJ2kmXoE1Fygg7Qr36MI889IFJh0TgQW-14iSlyRUs8xqkZjAJwEt6qDuLFZ46p3zUgIngL7RTYGOpuF9Gv0BirbaYU7RW9qnLVUCQDgcgMA5QECIlG4tQNE3izCqzp73EX3CeFlnDgiFL8064BdeVt7TgbfwsLV_JwH9Qt2fQJALCUwMS7bcTuhXmBL0oEsdaYtriixKpoKRjXggggk99aFuHqTv4WTCTaIeGnb5xxkazrovwpv5nKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6396b5eab3.mp4?token=nX-leuzL4kEzGPjs0r48hmDwire0xPig6Xs8UJDnNleyjbzVlK3efX_Qk8xBxdIaRz9kNueWPh0fugPQ7BYd2TWmIl3l4cmJ2kmXoE1Fygg7Qr36MI889IFJh0TgQW-14iSlyRUs8xqkZjAJwEt6qDuLFZ46p3zUgIngL7RTYGOpuF9Gv0BirbaYU7RW9qnLVUCQDgcgMA5QECIlG4tQNE3izCqzp73EX3CeFlnDgiFL8064BdeVt7TgbfwsLV_JwH9Qt2fQJALCUwMS7bcTuhXmBL0oEsdaYtriixKpoKRjXggggk99aFuHqTv4WTCTaIeGnb5xxkazrovwpv5nKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا فشار خون باعث سردرد می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/455255" target="_blank">📅 10:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ولایتی: محسن رضایی برای صیانت از امنیت و منافع ملی ایران نگاه راهبردی دارد ‌
🔹
مشاور رهبر انقلاب: در بحبوحۀ دگرگونی‌های ژرف جغرافیای سیاسی منطقه و جهان، اعتماد به نیروهای کارآزموده‌ای که در مکتب امامین انقلاب و در میدان‌های دشوار مدیریتی پرورش‌یافته‌اند، نشانۀ…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/455254" target="_blank">📅 10:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: تا ساعت ۱۴ امروز احتمال شنیدن صدای انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/455253" target="_blank">📅 10:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455252">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzY_bu9lhINJuEZnrCaNQ6rzf-YbxkqzAM30kL9oPH8777G5T4GExDqdoYGnaVJ7-3YZ01BN2MIRuM6KQG0067jY4U-OMnu3v4CL9wbRkTK36bjvjKQ0g9F3HiNHCTGVkH_vAcn2acwbS20YaE3wg6L78Uid3pHKYTkz5ok6AjyYL6noEIFjgH7IGOvL9FkcT1q8s5oJ1OG-4THlM7yGDiIiT6lAPn-LNAymAa3sWVE-6YzU8oskysBN7YeXxVwKcqvcaI_Wegf51HA53N0lFOUZl-fniM1aKgDq7_MMWXM9mysH1cUPjYv2WDjifiC_2iZWXo1uUrlzKiRUarNSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: سرلشکر رضایی به مسائل راهبردی کشور شناخت عمیق دارند
🔹
پیام مشاور رهبر انقلاب به انتصاب محسن رضایی به‌سِمت دبیر شورای‌عالی امنیت ملی: شناخت عمیق جنابعالی از مسائل راهبردی کشور، تحولات منطقه و عرصۀ بین‌الملل و همچنین تجربه ارزشمندتان در عالی‌ترین سطوح…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/455252" target="_blank">📅 10:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455251">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3641e81aea.mp4?token=kJCR6RkwaHxwM2SWEJUyHwkG1uiTs15sJ2tQL61pOK-rjWJ2e4PRMqrL4aPktCq3vB8NotMbRVxyHizv1ph3A-fPQB_j3xZqXylPeZTwN3inb5A8fq2-SBSgduPbhv8odJOtGxAWdXK5Wn641uBhNRIObirF7aPBP6x-Fd5KMOYoaAedijWpI3dJ-3VoIvaAMFX1rTiNEbo2PlgFn9c8tPpzGMgrgyfCfKx8E2uSFKnyAgQiibzzQmRcxYc62pdlvFzSDbcGCZo7KCQ_BKgZJ-093qu82Ds2wyLl-LSMIRXFsHHIk1N0MIM0BFLzvXX858YymkulNHSu403rq5gVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3641e81aea.mp4?token=kJCR6RkwaHxwM2SWEJUyHwkG1uiTs15sJ2tQL61pOK-rjWJ2e4PRMqrL4aPktCq3vB8NotMbRVxyHizv1ph3A-fPQB_j3xZqXylPeZTwN3inb5A8fq2-SBSgduPbhv8odJOtGxAWdXK5Wn641uBhNRIObirF7aPBP6x-Fd5KMOYoaAedijWpI3dJ-3VoIvaAMFX1rTiNEbo2PlgFn9c8tPpzGMgrgyfCfKx8E2uSFKnyAgQiibzzQmRcxYc62pdlvFzSDbcGCZo7KCQ_BKgZJ-093qu82Ds2wyLl-LSMIRXFsHHIk1N0MIM0BFLzvXX858YymkulNHSu403rq5gVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به پالایشگاه نفت در نیژنکامسک روسیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/455251" target="_blank">📅 10:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455250">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKgO0cVMgFgTrUSd2x0QJOMxXkOBfnLuLE2avP7HOE6TShP2oPzKDDgwnYK6akdqrVPIZSKP0Hg10Ls2Fpv3JpKsjYyC2cAiJFQ3HPrRO1DWGV-rKjv-Vgp80h42lTvwZYqlk_uI7HlEdFKGxIlcvbcHPPK6S79VAzW9tCRnDaP5cmt8NJnMkFP1qIdxRPmG81nU4wBbXFD5-dWSnrGW2yPuRbWBQ5r2REoYKug5YVz8r4WBcmXqGF2ks_FoUMSuwcgEq6o5BwXwtEzY_8n5gTG-_uwMCY4sz9mBbNTonGdeqV25ulFtknTIjOCyNxLTTSPySEQ3oYzW5JRFJ5tj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف انتصاب سرلشکر رضایی در شورای‌عالی امنیت ملی را تبریک گفت
🔹
معاون اول رئیس‌جمهور:  در شرایط حساس و پیچیدۀ کنونی که کشور بیش از هر زمان دیگری به تقویت وفاق، همبستگی و انسجام ملی نیاز دارد، تدوین سیاست‌های دفاعی-امنیتی هوشمندانه و اتکا به تجارب متراکم حکمرانی،…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/455250" target="_blank">📅 09:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455249">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در دزفول
🔹
فرمانداری دزفول: به‌دلیل امحای مهمات تا ساعت ۱۱ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/455249" target="_blank">📅 09:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455248">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c6e05ad7.mp4?token=kPuT9w09jhIBywXni_5WO1UDgRA5VFZghjAJcrdOhinTahLoNVzHUv9NRH4AwumYIZ4opN0YjblKSTVf3SiT5vQQVRXqJHlEpp6X1ijwX3AlRLMe5rHwpPj9y-GpJHd9bKf4lvM1JyU56y1iVvX_NO8XK-rROucm05N88YskoDmp7Mm4-jGzxpJ1fBoDMgn2dg1sSyTYoicn2rPskXzO8nQCXBFMzZJZhIjAcliimQqlrVnJ5bKNtx8svhlwACQrAfxSHunFnQNz5MO8c_Qep97SIWqt3JdUsSMbt_PI2DpS22KZlCIrWwsiab4StIWGTUFm1h2m5HlyXJWlfirA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c6e05ad7.mp4?token=kPuT9w09jhIBywXni_5WO1UDgRA5VFZghjAJcrdOhinTahLoNVzHUv9NRH4AwumYIZ4opN0YjblKSTVf3SiT5vQQVRXqJHlEpp6X1ijwX3AlRLMe5rHwpPj9y-GpJHd9bKf4lvM1JyU56y1iVvX_NO8XK-rROucm05N88YskoDmp7Mm4-jGzxpJ1fBoDMgn2dg1sSyTYoicn2rPskXzO8nQCXBFMzZJZhIjAcliimQqlrVnJ5bKNtx8svhlwACQrAfxSHunFnQNz5MO8c_Qep97SIWqt3JdUsSMbt_PI2DpS22KZlCIrWwsiab4StIWGTUFm1h2m5HlyXJWlfirA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه انواع سردرد و علت آن را تشخیص دهیم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/455248" target="_blank">📅 09:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455247">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0C67Y2fwoYSwMTEKn11NuTspAelwbQS_77OFsiGHs2cQWUmcK-p3WZuJHqB15972GEQsZvnSNYzQSem7Ib66fdPoyBlTKzPFWUB693PUiIdXq98XyLHJmWAz3rN6XfA-AwmcXGX3psud-ZzxkgmMW1V7RZH3h-dvwmLPVjlxXUDVUpdw58EwYq2DRBNx4fchr36z0ISyJZblJzBA7pysOSquOfqnrnvrBlg1Wr846XtQKoYioSUIGzGS9JhNqf8e72BVCT3J0ZbyF9e-9WvY6j3V6Xh9GoN65mnQb8YHMDJDeOlhsav4aPsFOO5fs18-129NoJ1-Vf2SuqY1AxUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455247" target="_blank">📅 09:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455246">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB2zOB0DFz-3SZX3VwqHGEirYoWuFCIFlCXkzwDDBtvvH7kl26-vOKbaUzxo7eJSNJsCm6RSYVgK6dGLjy1cTJcuk0QqTkN27xl4so6ePuYmHoUshRxOWQtOPoqpIrXdyKPLUstcWvdHBV40bqkqGSo8QTwOSVgv9au3Jk1di036nJXosIBEFejrNhgTF89XPTlv1GL0GMQeBVZwTglIc1z9F_bbvaC0r7LgzjY2ZP93St43ANvKNxhOLjdosnE3K64L8DuH9Je323eCF58crAmeXuAapC27FNJ7ESHPtk_W7pbB-UvjJVrRcmjj_NU-gE6KOCYNW5x1MRY6Th7ERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان تشنگی فضای سبز تهران با راه‌اندازی سه تصفیه‌خانۀ جدید
🔹
رئیس کمیسیون سلامت، محیط‌زیست و خدمات شهری شورای شهر تهران از موافقت شهردار تهران با احداث سه تصفیه‌خانۀ جدید در چیتگر، لویزان و سرخه‌حصار خبر داده است؛ پروژه‌هایی که می‌توانند بخشی از نیاز آبی فضای سبز پایتخت را از طریق استفاده از پساب تأمین کنند.
🔹
بر اساس این برنامه، با احداث و بهره‌برداری از سه تصفیه‌خانۀ جدید، بیش از ۵۰ میلیون مترمکعب پساب برای استفاده در فضای سبز تهران اختصاص خواهد یافت؛ ظرفیتی که می‌تواند وابستگی آبی فضای سبز به منابع آب شرب و منابع محدود زیرزمینی را کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455246" target="_blank">📅 07:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455245">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-T-Geykr5v5_8w9QO0hJi8jhV49_n58EdXhmB96Va27nTjm-gdMKoivcgp-ivRI-TKDfNPT7q5ChgOH3A5IhXSTMtvWyoEYO2xKSwV7GjhAyV6dE_CW2EYPT-f_U7bhlHXZjUjJnxjGgKnsAyyPT7AA2ep3jhjpsgsLIp2fzxn0q0cpkDRq4-h2Ed52OY6DLKZRk64C4uxlAaQuvEzJUZm0CXyqmEBlgG1J9dW6rSDXL2eZon5CMZ28L39twEp1TnXCNwyqM4akb8inL23lolcSkJ2x7lv7E9Xob0Ng25EgEu-OB31RJqoZcd7l1swAoOKrUahi85cy_unViLrdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکونام مافیا را سربه‌نیست کرد!
🔹
«مافیا اجازه نمی‌دهد به فوتبال برگردم» ۲۲ تیرماه ۱۴۰۵ جواد نکونام دربارۀ اینکه چرا به لیگ برتر نمی‌گردد این را گفت.
🔹
او نام از فرد خاصی نبرد اما حدسش سخت نبود که منظورش امیر قلعه‌نویی، سرمربی تیم ملی است. آنها سال ۹۳ زمانی که نکونام کاپیتان و قلعه‌نویی سرمربی استقلال بود به اختلاف خوردند. فاصله آن‌قدری زیاد شد که در میانۀ فصل نکونام از ابی پوشان جدا و به الکویت کویت ملحق شد.
🔹
البته اولین باری نبود که نکونام پای مافیا پیش کشید. او ۴ خرداد ۱۴۰۳ زمانی که سکان هدایت استقلال را برعهده داشت، در کوران کورس با پرسپولیس، عنوان کرد: «چندین و چند بار گفتم که نمی‌گذارند و نخواهند گذاشت که قهرمان شویم». استقلال در انتهای آن فصل به‌خاطر مساوی بد موقع برابر نساجی جام را از کف داد.
🔹
این سندرم البته تنها مختص به نکونام نیست. خود قلعه‌نویی زمانی که سرمربی گل‌گهر بود پس از باخت به استقلال در نیمه‌نهایی جام حذفی مقابل استقلال با عصبانیت گفت: «در این ۴۰ سال فقط ظلم بوده و ظلم بوده و ظلم». قلعه‌نویی بعدتر سرمربی تیم ملی شد و با ایران در جام جهانی ۲۰۲۶ حضور پیدا کرد.
🔹
یحیی گل محمدی، سرمربی پرسپولیس که تیمش در یک دهه اخیر اکثر جام‌های داخلی ایران را کسب کرده در کوران رقابت با استقلال مجیدی رویکرد مشابهی را پیش گرفته بود. اینکه نمی‌خواهند بگذارند قهرمان شویم. مونولوگی آشنا برای مخاطبان فوتبال.
🔹
حالا و کمتر از یک ماه بعد و ۵ روز مانده به آغاز لیگ برتر، تراکتور تصمیم گرفت محمد ربیعی، سرمربی تیمش را برکنار و جواد نکونام را به‌جای او به تبریز ببرد. تراکتوری که بی‌تردید پرستاره‌ترین تیم لیگ امسال و از مدعیان اصلی قهرمانی است و به‌عنوان نمایندۀ ایران در لیگ نخبگان نیز حضور خواهد داشت.
🔹
تیمی که حالا با حضور نکونام در فصل جدید برای سه جام خواهد جنگید. گویا مافیایی که او مدعی بود این بار جلویش را که نگرفته، برایش ماشین هم فرستاده تا به تبریز برود!
@Sportfars</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455245" target="_blank">📅 07:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9NN9y6G5ezfoJBBF9JqmtrvrTuxO73HbuqOMr_mtWkHFgigrlFl4_RfkgSQo7qxtHxEbtbODBQflibgOON41a199v96vWY8nw3VV3-dFBaYghifoHlTwRjNXb-RjXtdn_PHLVM1Uspsr8SY0UVivXSiUx3yJxY3GpnC8R6WjYnkdWyzplj9gIihl-NF5svgJFoWCn4F8QGJGjkUpVPbkARWRmE5uzb4Hahr__i5atm4SrTrVo-tEyTW2QXfCZ8Im2LeoJv3aH7llfV3kwxhgQ6ye1RKL9ODEQfA1SToPSEQj3f9NGCuKS423FrFCMKkzF6-MVa0YPW1-Ku5kccjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران هم‌چنان در وضعیت قابل‌قبول
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۹۱ قرار گرفته و در وضعیت قابل‌قبول است.
🔹
طی ۲۴ ساعت گذشته نیز، شاخص کیفیت هوا عدد ۸۴ را نشان می‌داد و در وضعیت قابل‌قبول قرار داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/455244" target="_blank">📅 07:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlU552MF13UOY8WEKb81RLgzjgFEPL_z7_DrqRl5SpFh9WUj8dTIO_zm9LufcXjTkRN7bMm_B1NNhmTgZwcM5ukB6Ofk314lQTuWYMbMV96bnX5bsW9rHqW9TVGIOKZwwimDA9u1sNQIkBwJ8weNOWqlWKiJa9UI4Q9PmRJSDXCoK5j1V_wviahLjEA81TnVq2QhkFduVDZtoSyAvnJbfiR_LSOEHbqR0W8RuVZvdXPH2knCwtzN5PDCNFXo_hhcyaohRGlgGR_9GEY1xFmJeD6YOr-589HO2k-txr7X64HrfMyLAh9MyJfzYfmXA-2IB1Fc-VXAAKDDCtRGFTic1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احیای ۹۵ واحد تولیدی آسیب‌دیده از جنگ در استان تهران
🔹
قائم‌مقام بنیاد علوی: در چارچوب مأموریت بنیاد علوی برای حمایت از تولید، اشتغال و تقویت تاب‌آوری اقتصادی، تاکنون ۹۵ واحد تولیدی و اقتصادی در شهرستان‌های بهارستان، رباط‌کریم و شهرقدس به چرخۀ تولید بازگشته‌اند.
🔹
از مجموع واحدهای احیاشده، ۶۰ واحد در شهرستان بهارستان، ۳۰ واحد در رباط‌کریم و ۵ واحد در شهرستان شهرقدس قرار دارند که پس از انجام اقدامات حمایتی و رفع موانع، فعالیت خود را از سر گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455243" target="_blank">📅 06:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455242">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حملات یمن به المخا ۷ کشته و ۳۰ مجروح برجا گذاشت
🔹
مزدوران مورد حمایت عربستان در یمن اعلام کردند حملۀ موشکی و پهپادی انصارالله به شهر المخا و بندر آن در غرب این کشور ۷ کشته و ۳۰ زخمی بر جای گذاشته است.
🔹
به گزارش شبکۀ الجزیره، شبه‌نظامیان وابسته به سعودی اعلام کردند شهر المخا و بندر آن روز یکشنبه هدف حملۀ موشکی و پهپادی نیروهای انصارالله قرار گرفته است.
🔹
پیش از این شبکۀ المسیره یمن از کشته شدن چند افسر سعودی در این حملات خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455242" target="_blank">📅 05:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455241">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خرید روزمرۀ ایرانی‌ها چقدر آنلاین شده است؟
🔹
نتایج پنج موج پیمایش مرکز تحلیل اجتماعی «متا» از بهمن ۱۴۰۳ تا اردیبهشت ۱۴۰۵ نشان می‌دهد ۳۰.۲ درصد مردم برای خرید مایحتاج روزانه، «بعضی اوقات» یا «تقریباً همیشه» سراغ فروشگاه‌های آنلاین می‌روند.
🔹
در مقابل، ۳۷.۳ درصد «اصلاً» و ۳۲.۵ درصد «به‌ندرت» از این فروشگاه‌ها استفاده می‌کنند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455241" target="_blank">📅 05:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455240">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06fd67e16.mp4?token=D8i-7wcdWm7Xh2jx1x7qkf9ix1Pf-C0aV7440RWcA0g2FgIrqPVRVtgU7lGLnkMF4AaZ2Mk6IkrbHetoYBqG1BAtGbv-ZcjEkOvvlAjF5RKgwMbjGqxRSWme6pHzVZ9HhWMwLgp7oDqXKjYJQFr93DVfPKEX4RMWLz0oDfzJpuj57Pvd2MOOh8KXCrmG7hkA9jZp-9Du92Q1KUmF9G9hTUgFx43C4OW59JRU8t5Lsq_CVMbL_u62ejRzMncfCmvSjRbRp0k6i-_six4e1kdlF00X0GqCXy5bR-pUXQ-Nj4kdEgjHLls8qS_nMKwzEYg4OsYevBZNE2q5NM9qBCmRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06fd67e16.mp4?token=D8i-7wcdWm7Xh2jx1x7qkf9ix1Pf-C0aV7440RWcA0g2FgIrqPVRVtgU7lGLnkMF4AaZ2Mk6IkrbHetoYBqG1BAtGbv-ZcjEkOvvlAjF5RKgwMbjGqxRSWme6pHzVZ9HhWMwLgp7oDqXKjYJQFr93DVfPKEX4RMWLz0oDfzJpuj57Pvd2MOOh8KXCrmG7hkA9jZp-9Du92Q1KUmF9G9hTUgFx43C4OW59JRU8t5Lsq_CVMbL_u62ejRzMncfCmvSjRbRp0k6i-_six4e1kdlF00X0GqCXy5bR-pUXQ-Nj4kdEgjHLls8qS_nMKwzEYg4OsYevBZNE2q5NM9qBCmRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا از بمبی که ظریف گفت خبری نیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455240" target="_blank">📅 04:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455239">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTmH5f3-c4pAkCmcSZKHeprASRVIIoOBTB6RWiRd6QJxwpJ2GozcYKXo_Ifne3KI_yI8VdYvh13VSnHM4BXHifbbZ67yo4XIQFf0OhfjXTcz8pcNaHVDfYDxccB5Dg2AsdodGfB5ej9jO6dy74IqADAAT07Fahl5RyGRjpJtqE_aAFJn67ZRUhaFz86_oLrtimBrl7g9LsPxBHR5PRri3KeEWFjJ_7t4VUJ6KBxw_4Y7iqfdslIGradAvKkPcfyHhRvfTnhMngN0XbPF_KiU7Y2kA6WDxiXr_Uq2W9d4vbv4fXc23-UsXTvl_iSOs2DqWCE7y7GYpWrRWtYv_wIb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ سابق ترامپ: اینکه ایران دست بالا را دارد واقعیت است
🔹
وزیر جنگ دولت اول ترامپ با بیان اینکه ایرانی‌ها اکنون دست بالا را در اختیار دارند گفت، رهبران ایران نسبت به موقعیت خود در مذاکرات و اهرم فشاری که از طریق کنترل تنگۀ هرمز در اختیار دارند، اطمینان پیدا کرده‌اند.
🔹
این نشان می‌دهد آنها معتقدند دست بالا را دارند و فکر می‌کنند در حال پیروزی هستند؛ و در واقع همینطور هم هست. این چیزی است که ما اکنون با آن مواجه هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455239" target="_blank">📅 04:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455238">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تظاهرات گسترده در سئوتا؛ معترضان خواستار استعفای دولت مادرید
شدند
هزاران نفر از ساکنان سئوتا، منطقه تحت حاکمیت اسپانیا در شمال آفریقا، با در دست داشتن پرچم‌های اسپانیا به خیابان‌ها آمدند و در اعتراض به مدیریت دولت پدرو سانچز در بحران مهاجرتی اخیر، خواستار استعفای نخست‌وزیر این کشور شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/455238" target="_blank">📅 02:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455237">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان و فلسطین اشغالی
🔹
منابع خبری از حملات مختلف رژیم صهیونیستی به مناطقی از جنوب لبنان، و هم‌چنین مناطقی از نوار غزه در فلسطین اشغالی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455237" target="_blank">📅 02:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455236">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYSGWjVowDwlA4gIfKgj-FryTjZ2y8IoD_ao4xNo9LWwEFYm8uPeV2ZbgNvhv_6Uy3RpMxVe0j1DRzO8XMZ_GKxcuBKW5SAQJAEWI-tD-Zd1SQXNS3qRorXJE4B_iz9releTF50LEGwlx5T8gcoI799f00_qZGtqG8hKo-ateH8n_KasPT-7XBtnTj6vG8K5CDCSQFwUg-VXv9gTjUx5EPOTrrhEdQFvvQWGwKkZrzZxWVungv82syHi4lbEMp8hh4O0dBkFITaZRJQ7wffkpYicZK4Tk3L5MMcbn1-XDKxSt8tfF2zGrDr0cWNtmkg3YOOIao-SkwHr0YgfknYGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: دولت با واگذاری بخشی از امور معیشتی تهران به شهرداری موافقت کرد
🔹
شهردار تهران: از دولت درخواست کردیم بخشی از امور مرتبط با معیشت مردم تهران به شهرداری واگذار شود. حدود سه هفته است با آن موافقت شده و رئیس‌جمهور نیز از این موضوع استقبال کردند.
🔹
آثار این اقدام ظرف ماه‌های آینده مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/455236" target="_blank">📅 01:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455235">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bac62a0c.mp4?token=jaD9CylhOXYTyEsXq3rwUcmLe7nlybBi49OnO78enn_fqBBTPS2qYx9fiw0Gj_NANS954uA0cN1ZVso9uOFW1Afjtj792QVemCiAN9ggOYH7xDqlxF3gD_k3lqnuSEQn1jzlO064fg-magtHD6hrAZ-u2CP0K5BEhiDXGJ6gN0W9HF5R6akwodlkl5mw3D2rpvPwufDR0ah0N6rYOE8aFuKFulKOkY8pG08fkurDyHuOQuwWacaAsYeXxxT8z6DMnuJhhpcvfuZ037NIMc7gCVR0ue-2KxDj--YqOPxiXEYpP2iTSvyFoE1ozCl0QBwWOTB5VdcTVzPF5oP_YbbdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bac62a0c.mp4?token=jaD9CylhOXYTyEsXq3rwUcmLe7nlybBi49OnO78enn_fqBBTPS2qYx9fiw0Gj_NANS954uA0cN1ZVso9uOFW1Afjtj792QVemCiAN9ggOYH7xDqlxF3gD_k3lqnuSEQn1jzlO064fg-magtHD6hrAZ-u2CP0K5BEhiDXGJ6gN0W9HF5R6akwodlkl5mw3D2rpvPwufDR0ah0N6rYOE8aFuKFulKOkY8pG08fkurDyHuOQuwWacaAsYeXxxT8z6DMnuJhhpcvfuZ037NIMc7gCVR0ue-2KxDj--YqOPxiXEYpP2iTSvyFoE1ozCl0QBwWOTB5VdcTVzPF5oP_YbbdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدوشصت‌ودومین شب خون‌خواهی قمی‌ها در میدان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/455235" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455230">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTDbnmD-OJn3GZ1Fx6tMygSldw26pjrz8c1KYkDyIvymgrzhOoDpUaKtJk5XJzeihMHXHOKjXRNN33_oWT6gLXWLqlQ_Bf7DH7pIiaRptLoEit3V_MFtAvoe_VjsMEB2413A-AQmnjrxYXAk3ZAHGj6qjSTAOHRY488XPBwZ4XmhaDQKwwOdo6tHRdQdd49OM3LAhSqqdnl0jcYSL8QFGrPpWQiE_4L8RlbyhFr_zybQRwpeUdFAe4acYU3Lto1bujWdGOQAygqQLctScLwSfKUk9mWz1TMj9Ybx7LQYogQOFHGxeGF47a4OlLksm4d6oFwW92lk_kkE69CENwsBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCeFxTKQIUWn3x7gIEgp9nhNfXKjgLqNs8tX-tnlWiTWcCTcA-VaOBjncPyH-XdMWQtb16rULXpUecO_Ym2ubfewoF6p7mtG30zBTeumakb7y95atrqYtQd_jCV0da7zQfhz7olTsYp2xXHgTVCq_QxW0MDxg4ScFDT9Bl7JAfxM0jDCbO4iT75L59XiJj81BQTZaLnOcwnNi6Bb5Dep2KN9lKPOlwlw7estNoxSQgX01GhDZhWk8TfYBojiyqhItlEwbXK3ssmO7nrtAn_uWimL2o3ySpucMTzUv0rEOePKYAsNbdwoYMQbUe8J5seNCIu-N8SjPaI3zSIscNXxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyODLoVARjUya_llVdj9YRBFLiIc3HoVGAK6LF1Rm0G-ZTQL6GzaX63db0hOzMhLG1B4ljKLD3P-SbFIh8NAcs3Hdwhwijq6kgwEGRtYvXlvOchQem1BRJbh1v1MdsA8iwiY0_glQKppv9W4pe39K0W04BDN_Z8JGzDdh0FuplYMyWTof_CbvR0S6Mnqux_PJmOZrZd6xYukNM6edx8XJvJITKLlizDftZrxPOWuvg5bOycV_ttHYFSorc5a0AjSpwUiYBiee5BvTP5Y94G2kt-W30xyXsMMhhcAXE78cesNc5C6GZ3cZt8XB75IZmficOv4mIXrxQZQEYYSAcy-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9qMHXHF-qNHNyUzX0q_ALO5r5BOUcwUpiy4CTLnXBa8b6GbYGGiPlSVwEDsUf71u2M4H8U4D0XYrhLbh03MKvzNGixGZJ7P0VLUyFZ0GhPqnxa1Az4dF_0he8vY4erbPri1zPskKfqIGxFtd5_mmcPgdmuapHsQw38KFNoAra3TankSmXIjKxjnPfXc-5i7ciDOrafxabKAI5vESKvWCQp4PmGeFlvtj22oKExn-QicKFkR4rPNQmMSo2ju1loVO37iX3qCr-BZtQ0thYd66-n0dyFtbUgwNXqfn0QGfHR3kjmXv0e-QIqcWH3QdhYsc7mBKAdZNQKODTyBa4jKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-mVsX4Kzwzv_zVdPdlQga9KxHyxv00UstRbYmc3kBzzSuMpZIgasuSTsqSn6hJaZ_GSGDpZ3DXiNi6ygNf6znE1k4EVT4pUCr79l9PO2063qxtJe6Sbk_tsKw9j3oRe4x-qpEtPjfKtGTKG_r_t2powdqt0aoVX6I-NZ9b2e1tRSejzGCUTPZaS4dH2ajqRzVVIpSc6T9lcyszPNJy-gOeyjtfu6uL8GTne1A9z6d10YlXIaz7_gqKmkUoemcjD_oL8RDOVTEvA4UeQBEKus_LAuV0QCh8QFKLaQpGDAAs0SRnO9zkSnxJ3x3uKd9-V8JgK_gZeXmLj-U2lGVoXhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۹ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455230" target="_blank">📅 01:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAfQ21tYb5h6P7VJ8CN_LcAyF6WI_oGHChRqJ5oKmcfpMm6TFZdpZjcVFGdHLBDdA6FnilKQMLrFYf5niFNqu_QEnNMVwfdrk_3ctoOpGL-dyYcUqaJbWD8sKn0no0TKeaDMmbh7aa9n-Wks5xT8zcPhw4NN87Yi5naz1LaafavvWn-e8A30fv7Sf5Nct4pTUTCuIrvXfDpx5kzTPIszInUrapKBGOUfyLqABj429jy36POHcJHRbboReDO1bvUxTsAIhPppEgae527ZKRKvwcNcu-Z_mp9D2tEiqIGnT9QhHc5NgwJYRrQqFoSBWckkJGxWiZK1cTZtLNzNRV_3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiXNzNM494DtTFeUuTeHUCa_icBJUWvVQz60AfeuHkRyYpShxnqSnBB0SEGwovQaAwCWm-q75RI4xJM8hI7JmLIZIa05_2PMzsNquvqHtngbjfJzybQsa7K6huQlchiCrXxHYUDBGHpi1SfVx_NMAjzf4OasBeM7LM0c6mPGDlNhXhrCXWgYifZP6LPPSEI8BQIDezCEawlrwTxynbG2sMsCesHy86FSFsOfrXfGijL9Fs-m17Cx49_wJwb6VNy9-R2sRCY2n8CH6bzRfLJodWaRSFxir1JlHciarevt7t6E3C_fyD7Zu0ZXzYxG6g3Ukq7--kETDprbrfU05jKllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcMJDnsaNOa-5uEM8X9XR6nyJmRyuH3AEzLND0xebMxxMVEtdxw7Bp9CqfR4XfBGwiWDVYp-Pbxe0xPIo26BiXr8pE5yzxJZGhv3DZnvhz7qISSVOUTwGEQr-tr0VGeD_L3MGeIs1xR4p30W6ZmvBIw6PMRTVQR85280rXFf30sAwOBIVL20Dun-8apLB03Dd030s9q_2Ii6-6bcq8XiBGCjCGNnKwvZ1OfkVLcOkV0mQvcYHYnZVZyqa0aNtEHr0xJwld56TSg-ywDOw946-mYX3e4WWRAbIx2Hlg3G-a7GZ_zM8Fx3eiTNqjPKfM-oj65dCSgvlF5Wbfz6QyGogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIgWo5aYfrI_gsYfxXeuFtxdW7K630Zq6CmwzSYHMDPWq2nwNKFnIRK88W1Nb4Qc47b72EO04tV5YWBrw_TMrI6OcN0PH9cX6ZUtjToBBpItm4ftRDEnk_x_TDytbKww7Vkl90B7ju1ovqphbnFbtanSR6QazBuIPcnrc8J7xX-X2OELQkPxghFUo2O2oWahOGnYMKsVluwdV3W8RkucUkkhQv_ulY7JXwbDYGOJVzLXbXnLPvXZqCvA5772AmTi5ElI_Ugt1g0elgGDSI-TPomeZLk5O2_fIDdJ7czDBEMQPZ7EWfxzzQ-H7CBXwxCIq1ePE1hNuXDIruDI1NrBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5wdRD5IoFUDAGm9OdpLhjm672IlvKGep4mOI7-bR-1g3a1XjbNKoOlZFx82dTdJDT22H-j-dMkOVlO9zpZtDU4ARNHL6L30z6gOVXcI7Tr7XRU2m52-nUIy1EW0inHA7eBmmx5vVAcuHLVpsTPIR79IP3lxn_vZI1hz4QLMKYp3AKzempBz1tbeW3mV1FCJ_o4QBnnDCJ2CMQ69zrF4T-ahShYkIP_xGbAfC67dEHIB1Sok98a0dxi8JsLM68aYJx1bBAA_4RHERQAXA3pFLL4aOh7NyciN7bw59ZVPXzEpqs29MaB1gkiFD-hywHMnqRd9v2wUl-OoX9q6X4IJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixfbt1k3LrAgRVaJ-zNlY0-_JL7NjPRIiqEKr8ADdvESAnqR0KBPm2TsdFq93UqFrcK9s3xwWH0DEPLVcxpTQfr-lJalPLt_NcHbfI5ZLMa23K2Ecop7ifHtdieb2dlwT5gi8RbWrhEOAhnxeGFfB1dbWVvBPYsIEZ-BnBAik-SsL0z2EGBiHHvqRsCEm4maKJrB7oreTeqCnOQX7f_hqLZOlJPJOLluUMCvK-f_EHNnMunE3qmiEEL5l2mR7K4W_L9nDC11hbraA8KVBpftXe1yXAYGe6bs_VWqOMowY5twdTeOVISYL4WtvBmgH8gbOCKsz6W3Cyb3BvoWpBGOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klAP2vyzEDh7hJN0LH9wM1QJOTeLLyI6dlTHg7pKaIoxNVVCDt2VzflQHok5ajVY7j9rBor5sfcK_MGUvukB_1qM0D2Pe-N9hzAH57NL85783xEfmzI2KjSVplYeJxzKnh_e1emO2y8eeKA4fPonXxNa2KnCabkGTK3BIDTBrbesyvzLTDcBb-qDmcsBWnLPdgfbc_es4KOt73cVyS5C3_E4VXVxwssmWdiwXrNJ929m0wft-HumEnAA8YZzFBlKlPlkwUXUW-BZxHco0FIENq5z2bG7CyS1UWjRpmQc7-xVfvsrx7gsV5bxYMRUCm1eDEjUeWfe8Kk81Xwt1bjNSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xwq8YOhVi9_LwAVFFBFiKGPh0ydL9HWPxqeM3TCbVZeFUvanl1yIVVbjG7h4hiI0ZkBcPxHfm6MMmkcyWQftdWoskYpNLaM2fFpPyi5UY3HYmwWdV3x0n6Vz10D8BeReSQcgsd-ksxEL8T-BAS5dgsuEtcJXA9k8e-RWxiQJRLLyfcR7PTXTdiVWxaC5HV_MjpzGVtY0yCuFD3k4VDXDqA1-W9Lf5GiI50yTXUnqRJY9MK7BPufDWpqZ3rHteFGvTTuBUU_nRPANFWaGLQRBSoMQLxMQ_5DydUWnbE2EubxyGRK_GIanSTCKU2a8LwZP6xFn-giZMAxg09AxT1v7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAGw2SbF0SuQWxnT2nE11GRKF_G2yCt-ZJFyHMIDspHIjKwcM9BAEZ3PFB3JJrs1UeVSedVVkRES0O1eipghjvlyULm7d3tqA20XibJhUeo5CiUPxl19ASPtBekhKvJGJ8_SRiZkdb1uG7_X5ETMfQx5WQnlQtEEMj3TAPaEmCHcGdLsLr0KoGgHmsUfKE-BfM-H9eGe_7kYOtWbcdyCL4MbueiktB5IkRqQwNaDFT83yJEAaD86ZfkSPejeqADfM5w31-OlM6HEKw2v5oZ1OMEBHJMbgz_A_uQlYuJbi0-cQzPDukDYdMBrQX7O78oBXrZNsYzDTLCXsdsHQETokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_lGQ0srxJtCo_BHZEiyFd6zLESU5ElXGeGvM-KmVwOPgxXet_6TClqDSz7IKmUmSBwUbI9ujfZRKKa-fR3Fr7AmpW7zGB5-mGelf9qkvYgZr-meCmymuu8QDjrqv2E8tk14zg2FpJ-nDFeKQZOwzM2XGkMOGJiy-G4gnS6xnAzPDmjHbSu1L5ZnKWnqHG5JsVFaQheSd5MQIOFuUWkyfwBJgmOYdRmTYiseA4ZH-6JA6BLGarytNO-ZgKCmbmvRWtGSEce5qmM2K_IADViT0YjgECJ72FQmrVDUs-ROdUDplr0a2wD55RhhSQR3qGQ9ab910GjDdOjktNcsU1Mv0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455220" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee78c69f85.mp4?token=JTECXvJAvZw0jXqZ60VmTecT23ftpS_lFwYHOEvPhkDOlPwQjCAr_fXUKs81ZzHURliyGB9_LaoAAD0uS9nHeriGSPTiUMUBr7lxCP3HcDh3zL0zB3JRGc2rXDydYufYMFVvJ4MhNHh71GG1mb1aDmDCb6cp2FIuDQ2wb81QcFWa6foHWWCUw8KPqgwPI1rM-ug5rYEWFPBcWeeFqUocS-s3EqlliFnYV4ZpiBUu-hhqOh-CK1TVPD68hzNGHrwGyrTJATlfhnNCC-2LYALapgD92PlNmviSjFNH5Ileu_jvZInDiWMtGRtLNUZJBbQNL7OCIBfQ3mL-VFi0fS-lOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee78c69f85.mp4?token=JTECXvJAvZw0jXqZ60VmTecT23ftpS_lFwYHOEvPhkDOlPwQjCAr_fXUKs81ZzHURliyGB9_LaoAAD0uS9nHeriGSPTiUMUBr7lxCP3HcDh3zL0zB3JRGc2rXDydYufYMFVvJ4MhNHh71GG1mb1aDmDCb6cp2FIuDQ2wb81QcFWa6foHWWCUw8KPqgwPI1rM-ug5rYEWFPBcWeeFqUocS-s3EqlliFnYV4ZpiBUu-hhqOh-CK1TVPD68hzNGHrwGyrTJATlfhnNCC-2LYALapgD92PlNmviSjFNH5Ileu_jvZInDiWMtGRtLNUZJBbQNL7OCIBfQ3mL-VFi0fS-lOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی تنگۀ هرمز خبر می‌دهند
🔹
شبکه راشا تودی گزارش داد، شعله‌های آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455219" target="_blank">📅 00:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برخی منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی تنگۀ هرمز خبر می‌دهند
🔹
شبکه راشا تودی گزارش داد، شعله‌های آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455218" target="_blank">📅 00:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY15b8jHIojkW8JirBwjQij_4LxyOARBI8IGpAkZJocnMbSdVdRB-7ypvs7XiEI99qXiPr_r5b8L_C_dW4956mqCuUk1Q1HNt6Cil11zcTsPuqIQBxQxNhTHy0wCbWkN4Q9WEQZO1K4FxfKsx7LCKctbVO9D9MelWIEJeXFo4aTX0YJQoT5BLmy2xw1vgSRbdCcKO9aZBmeWbeQkI8L37-C6jYCSGTTrS7R8dbLPTNyrtovk_ZLfcu_DfZwWgRZi4eeFeFZqlpjgXoqe4V0LUuXdLlFUdoSglCf_K3M-VAXbDM3rGhxUGOaQKCNz_UIkIYl8vqCgHeXsjnTDUY7FMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیر غیب بر قلب سیاه عربستان
🔹
داده‌های جدید از سقوط بی‌سابقۀ صادرات نفت خام عربستان سعودی در ماه اوت خبر می‌دهد.
🔹
به‌حدی که در ماه گذشته صادرات نفت عربستان که از آن به‌عنوان قلب سیاه اقتصاد ریاض یاد می‌شود، ۷۴ درصد کاهش پیدا کرده است.
🔹
این کاهش صرفاً به تغییر مسیر کشتی‌ها محدود نمی‌شود، بلکه حجم کلی بشکه‌های صادراتی به شدت افت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/455217" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpqpzKd7elFwWB0gIYU3z88DYQeIKNVctmFMINaHROpNjdITiJ4-U3H3lcXsaxN8FDz3SmfyGfvd4UmyT0nsxVZWaIL7a8cIDkrO10LHHapQcW6J11GhqZkrDF-UGXApJYOZLD2rv8T-0bMMOkiEpCSldtuzzFTggcMSoE5Yl_Pc87FIKzW-CYqjM1o-ZfI3fuLDNxU_WOUClroQSLTPFH3iACz0lWV2tUmw9sgQczHywLx-06wfrjftNK-PLcWLDp2K92vdb-UqBfBvrR3QsSx8ZE2hTN5AhoeCxrZNA47BwU8t6lDpiwP5wzRff-jeHfGpfIrv8WuPn8uJHK6Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندیشکدۀ آمریکایی: قدرت سایبری ایران در مسیر تبدیل شدن به تنگۀ دوم
🔹
کارشناس سایبری مرکز مطالعات راهبردی و بین‌الملل در گزارشی تحلیلی نوشته ظرفیت‌های سایبری ایران به نحو چشمگیری ارتقا یافته و عملیات‌های موفق اطلاعاتی علیه مقامات ارشد امنیتی آمریکا و اسرائیل، گواه آن است.
🔹
به عقیدۀ او تشکیلات سایبری ایران، در حال رسیدن به جایگاهی‌ست که می‌تواند، پایین‌تر از تنگۀ هرمز، به مثابۀ ابزاری برای فرسایش قوای آمریکا و متحدینش باشد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/455216" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f7528c54.mp4?token=Ac-M5wPFry8dBzttktBW5hz9FXR5PtvGXO4poKTRr5dmNzjCozsU_-iJ7s87UjAyg8iGHEjpVCL912v55TUHS9owtasA5oQg-QiXFl1TRy_3hLUCpEbkZ9pfW57GTbPvAHNDiEpy3IHxo_nBg3jNiHXYG_BpGOx6g-cUEJeFT-jRKT0Kk0sDNB6T5_5xL7hJn3daAVLVpHgItmXvLWoKE7aPPqjicRR7_uaL__c28fObbXJN7e0YBHt5LT96vr2vCehq5b99sRYvpd1n6jA75NvHi8ZX5QpuqzBkGJ8MbBXj5ab4r7g-cW8Oy-k2U868Dja596wFYLLB5fUmyAKyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f7528c54.mp4?token=Ac-M5wPFry8dBzttktBW5hz9FXR5PtvGXO4poKTRr5dmNzjCozsU_-iJ7s87UjAyg8iGHEjpVCL912v55TUHS9owtasA5oQg-QiXFl1TRy_3hLUCpEbkZ9pfW57GTbPvAHNDiEpy3IHxo_nBg3jNiHXYG_BpGOx6g-cUEJeFT-jRKT0Kk0sDNB6T5_5xL7hJn3daAVLVpHgItmXvLWoKE7aPPqjicRR7_uaL__c28fObbXJN7e0YBHt5LT96vr2vCehq5b99sRYvpd1n6jA75NvHi8ZX5QpuqzBkGJ8MbBXj5ab4r7g-cW8Oy-k2U868Dja596wFYLLB5fUmyAKyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطعات تعمیر پل‌های تخریب شده حملهٔ آمریکا به حرکت درآمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/455215" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad80724b3c.mp4?token=sja_-dEeWBG-VaVLEr-AqblvoEFYPVg8XxsZ-ZSSj-5h933_k3z98h3PYzX6AlNoujHfP1uMdKE8ItDSieH0RAZfdKbG0YLYv5u1GDQbwONyqCP2NpKN_NymgdOsSLPa_g_mknVrZNb1EiukeAhBncoCvc8wLJ4NJIxoHFLn_fBPLu-3ORO6FgF5aoVPSsj13tYr98WP1iIPKhAm3eXl_kLwzwPXlKLQjXbB-84F5eKjx1DdCP7r-q8PxKxErlb44yvcgaggM1VOTt3Jj20ZskPTPvr34LRzFBz2HtSz1uX9E7jxmRJWc06s7Q-q-nKak6G43E2nPClwZURebVVJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad80724b3c.mp4?token=sja_-dEeWBG-VaVLEr-AqblvoEFYPVg8XxsZ-ZSSj-5h933_k3z98h3PYzX6AlNoujHfP1uMdKE8ItDSieH0RAZfdKbG0YLYv5u1GDQbwONyqCP2NpKN_NymgdOsSLPa_g_mknVrZNb1EiukeAhBncoCvc8wLJ4NJIxoHFLn_fBPLu-3ORO6FgF5aoVPSsj13tYr98WP1iIPKhAm3eXl_kLwzwPXlKLQjXbB-84F5eKjx1DdCP7r-q8PxKxErlb44yvcgaggM1VOTt3Jj20ZskPTPvr34LRzFBz2HtSz1uX9E7jxmRJWc06s7Q-q-nKak6G43E2nPClwZURebVVJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکن جدید پرسپولیس: شنیده‌ام اجداد ما اژدهاکش بوده‌اند
@Sportfars</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455214" target="_blank">📅 23:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-MvaMkDICs8djjx3wPEZBrrUhdGrzIn1wK1BAEmsCNCdFpei4xQ9QFu3-lWuJErbChaqC6MMs_HISFxWJVw-akh62tzNjeq_HgHO48sE8fVpKYvNEbYq5Bu21XkU6s9mxnXrq-424xJyaorxjSnqcRFTYxLtapQ-hCYmmcPXpenUHSLyHmKbmuW0yiCFiWgiM0nAH5L36nZBOtnnh-g1r_bdrGWNosNEuTNAY_NQn8Rs-TbCNa9h9Rui6ruDFslH7j-SxloBGG2eLoiT_ReSNHZteq2vBigoCCpfPT-iGOqwdDHj02JDhZcfgG28_dixLKzlXBk3nS9GkQP44aarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل نجبای عراق: هیمنۀ آمریکا بر درآمدهای نفتی عراق باید برچیده شود
🔹
اکرم الکعبی، دبیرکل جنبش نجباء: درآمدهای فروش نفت عراق توسط آمریکا دریافت می‌شود و در صورت ورود به چالش با آن‌ها، ممکن است در پرداخت مبالغ بودجۀ عراق کارشکنی کنند و این از عجایب روزگار است.
🔹
سخنان وزیر خارجه دولت شرور آمریکا که گفت «سرمایه‌گذاری‌ها در عراق بخشی از امنیت ملی آمریکا محسوب می‌شود» تأکید می‌کند که پروژه خبیثانۀ آمریکا در عراق، محور اصلی‌اش سرقت و غارت منابع عراق، تحت پوشش سرمایه‌گذاری بوده.
🔹
ما هرگز در برابر سرقت و غارت منابع عراق و معیشت مردم آن به هر شکل یا عنوانی که باشد، سکوت نخواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/455213" target="_blank">📅 23:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdDG__Krt56UdQG9YQoWD94HDvtbBQFPvKXgo5o7YdWWikNnPqprk-bIINXy8GHBXdgXSYAwqfwgEEBLJ1wAc7WNKOVskirQIJHbM6ys1wtCJYLpw2jQf509dnEp8nXj5Gc20Lqe32HtxTRvctapN_0fDLK5DgdH8Chsg8qdzGDo-6XBQz28RulwuFOfSf4jitHybgXemYnTEkEhEjIYPse-he3zQWoVY8JSwWa0kuHPQgsC4o7fp94cTP5x37VZYECbKLT0fZh-8KpE0GHFOlQgis0pYKVcY9LbyZfK9c1L-ZW3zmML6JjckBpOYvWvSFhqMQQjMRc47OUMqkXjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف انتصاب سرلشکر رضایی در شورای‌عالی امنیت ملی را تبریک گفت
🔹
رئیس مجلس: سردار رشید پاسدار، جناب آقای دکتر محسن رضایی؛ سال‌ها مجاهدت شما در فرماندهی جنگ تحمیلی اول و حضور موثر در مسئولیت های مهم نظام اسلامی بی‌شک موجب واگذاری این مسئولیت ارزشمند شده است.
🔹
دنیا امروز فهمیده ایران، تسلیم‌ناپذیر است و وحدت و انسجام ملی در همه عرصه‌ها هر دشمنی را به زانو در می آورد.
🔹
از خداوند سبحان دوام توفیق جنابعالی را تحت توجهات حضرت ولی‌الله الاعظم ارواحنا فداه خواستارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455212" target="_blank">📅 23:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f70352bfd4.mp4?token=Wtcu2ByxWeTQ01R7fjVCA0cJjXYb4Wf9BigqwM0DUhbvL4hiYme-pvPfNoQDCqz65b5zHnJEVsdVXCXb-25e2BJ7PWZ9giW53EXn-c9fezdcfL6EV-1DIBbQ-evCyEr4gBlJI_AeEa2W5bxZdZzmCDKVzCHXJR7SyINa9-_uxHH-TzVb81VS4sw2Fet2JeMrhKpG6kILgssqYXPlLHdUFxMnDyfF4Cn3rGhYCZZ3MQdINcUt25nhK4T2EkUR4pawaOI3-MwtOlLGTPGgtroG_IvZ3tBdn3Q7oPDpr3DaSOWv7I8Fmi3p37YhdrFMvo3iCXYqX5w0fyxST-x705ARjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f70352bfd4.mp4?token=Wtcu2ByxWeTQ01R7fjVCA0cJjXYb4Wf9BigqwM0DUhbvL4hiYme-pvPfNoQDCqz65b5zHnJEVsdVXCXb-25e2BJ7PWZ9giW53EXn-c9fezdcfL6EV-1DIBbQ-evCyEr4gBlJI_AeEa2W5bxZdZzmCDKVzCHXJR7SyINa9-_uxHH-TzVb81VS4sw2Fet2JeMrhKpG6kILgssqYXPlLHdUFxMnDyfF4Cn3rGhYCZZ3MQdINcUt25nhK4T2EkUR4pawaOI3-MwtOlLGTPGgtroG_IvZ3tBdn3Q7oPDpr3DaSOWv7I8Fmi3p37YhdrFMvo3iCXYqX5w0fyxST-x705ARjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محفل عزاداری دههٔ آخر صفر در حرم‌ رضوی
🎙
بانوای: سید مجید بنی‌فاطمه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455211" target="_blank">📅 23:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/140506cecf.mp4?token=st10ofJixmBVMa3YCjuloTyhyMevwb_ET6gxYVfEBou9IoGjdLxR1V0yrIDqwK5VDjqUBdruUbOw9HcY8a67XUAR7jP9kc7C1ZLDZSvd3iVeNiZCWZyQ1eL3QPw_x4hQ2gWfkjdcISkACEyaKPuMkn9ybeUnIfNDrg0M8sqqk487WBuT2lyGZugps7TpRRBV-XyGk6MB_7inNjqTCeDDxr5JLnaT-D9c1YxlhLMF750qANL-0D7cknWxA1s-qafKSWYQLS0pbxzbKFdBCFcnj46uPWEKT95ok15NuiBaZN2OxPCGpTHXPcJ8NOq9YmVaCZ7yBHWJ3IXMLpYDkRr07IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/140506cecf.mp4?token=st10ofJixmBVMa3YCjuloTyhyMevwb_ET6gxYVfEBou9IoGjdLxR1V0yrIDqwK5VDjqUBdruUbOw9HcY8a67XUAR7jP9kc7C1ZLDZSvd3iVeNiZCWZyQ1eL3QPw_x4hQ2gWfkjdcISkACEyaKPuMkn9ybeUnIfNDrg0M8sqqk487WBuT2lyGZugps7TpRRBV-XyGk6MB_7inNjqTCeDDxr5JLnaT-D9c1YxlhLMF750qANL-0D7cknWxA1s-qafKSWYQLS0pbxzbKFdBCFcnj46uPWEKT95ok15NuiBaZN2OxPCGpTHXPcJ8NOq9YmVaCZ7yBHWJ3IXMLpYDkRr07IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۲ شب مقاومت؛ گناباد همچنان ایستاده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455210" target="_blank">📅 23:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662270fe68.mp4?token=ZiQ0NgBR6X9r5lQdXWnEvgksvVa1vxZ4V_i_a659WDXv34rClLyquhJ1HOdux930g8MOuhHyQBdBGBxeEqC6CbnGRRoxtH4keGcrFNEAU4YEnw4e9OOETFrfxfhQkJHTQ-706ekXhmr0eFzR1C4krSD1XKtCOpSBvVJtwcB0yjF16w4XCoVXi40oNN5CQKvrjzI7dP3NE_iya65waqI3UNgORTtAhbBocOq3uoKmdtYypCEGCtOcTWE0DTQUovYng1cdwHpBBlVgcIgJoGHpn1sCpTTc92CvCx2FwOHw2nsk7O2PlSNz2_wq9NVeii7OdxwPC-QtWrNqjUwSG_PoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662270fe68.mp4?token=ZiQ0NgBR6X9r5lQdXWnEvgksvVa1vxZ4V_i_a659WDXv34rClLyquhJ1HOdux930g8MOuhHyQBdBGBxeEqC6CbnGRRoxtH4keGcrFNEAU4YEnw4e9OOETFrfxfhQkJHTQ-706ekXhmr0eFzR1C4krSD1XKtCOpSBvVJtwcB0yjF16w4XCoVXi40oNN5CQKvrjzI7dP3NE_iya65waqI3UNgORTtAhbBocOq3uoKmdtYypCEGCtOcTWE0DTQUovYng1cdwHpBBlVgcIgJoGHpn1sCpTTc92CvCx2FwOHw2nsk7O2PlSNz2_wq9NVeii7OdxwPC-QtWrNqjUwSG_PoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ پهپادی موشکی انصارالله یمن به مواضع عربستان در المخا
🔹
نیروهای مسلح یمن: امروز انبارهای تسلیحاتی و تجمع نیروهای دشمن سعودی در منطقۀ المخا هدف حملات دقیق موشکی پهپادی قرار گرفت که موجب انهدام تجهیزات و کشته یا زخمی شدن تعدادی از نیروهای عربستان شد. @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/455209" target="_blank">📅 22:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8142d316.mp4?token=bOAMQlWAK17mjdE3ceSrvtehaF1rwDYmrMDmlombuEbqICt0tyVPuTnK0B5iqzhEklcq9Zz4fO8GuKoNj830AvZ4EROaLwoJ4cIgijKemHZu-8jyYxQNjulldK19s8g6Y8_dUPaPk_zU2jIwUvkPiRDA7i-6n5tTiyddXMlmNnDJyRAg2VVQ8jQSyNNcx84RVYhUX4XtTdwq9UmkyOm-f_XH5Iqwq7iLELkr3kmytMIwFpKj1VUsIUh4_Z32KVLHsGspadPQyEoy8Z8Wx5Rt-LErTH7tfWIAzp8fZ5Dutejc1fjbXE7wHbT8LeFAXiuPz8GIMAEN85ISgCaJmWMcMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8142d316.mp4?token=bOAMQlWAK17mjdE3ceSrvtehaF1rwDYmrMDmlombuEbqICt0tyVPuTnK0B5iqzhEklcq9Zz4fO8GuKoNj830AvZ4EROaLwoJ4cIgijKemHZu-8jyYxQNjulldK19s8g6Y8_dUPaPk_zU2jIwUvkPiRDA7i-6n5tTiyddXMlmNnDJyRAg2VVQ8jQSyNNcx84RVYhUX4XtTdwq9UmkyOm-f_XH5Iqwq7iLELkr3kmytMIwFpKj1VUsIUh4_Z32KVLHsGspadPQyEoy8Z8Wx5Rt-LErTH7tfWIAzp8fZ5Dutejc1fjbXE7wHbT8LeFAXiuPz8GIMAEN85ISgCaJmWMcMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مراغه در میدان دفاع از میهن پای کار هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455208" target="_blank">📅 22:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M08WDTCW8n0_P6LmLJvZPZ-_nl5oz1WwG7o9REA1yQTU5WGKJeWQafu9iQ5W3eWaiJfPqP6y17URjKhzdicKDgdrLxi-1q0vgNzBeEDgokQlrl1VkWh7Ac36lNIihbcCsdvTTWAC-YGuL_m7nhH1k2jzUEfidRd664J5JZU37tlF3hJ3xpRTafQDafB2EqJSa7xpaM1QmB4y5-QBDVCKYyO-VG3hSruzYm0il4qLZZfa4imPE6brN3SJJH9AfoCFfI4TKA88bVdbr-Rc8hyDa7qfshJHdTPycQyqYB_1YDOin4OKmFP_6JDOuebU4pQG_0JrSI0H-qPHP_LGwy3ONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع یمنی: مردم از محل تجمع نظامیان سعودی دور شوند
🔹
یک منبع نظامی یمن تأکید کرد شهروندان این کشور باید از محل تجمع عناصر و مزدوران وابسته به عربستان سعودی دوری کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455207" target="_blank">📅 22:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc934aeb7.mp4?token=UUe6oSpMUX_bGXpqXx0JEI23xI6pSLouEEbKrtFe-yIJsZ-xbJzdzUqpxAva3APsGSHAaOy1HbdXBI4hBxKSZjFC1fVWS7Tv3tgJXRSVtv-M9SWOmpSbmh6kIzbbHMt3cRbba8cYoSEZ-9Rw1NgMSHCEVXBC2wQzG95BGNLkDTRhUKegnqRgtjPRiHMZVuve4AA_mTWBKhsucjDGtFsb9cI8qAc4CNJdAlc-lhG0T3D0Sa5gYmCaraavPBu5DgpBAKEV5IWyAwGO3vuii0fvrNRGAUb8LasKh5nar8rxNHgXoNmaVID6P4Nu3r5fzhKBfbRtYzT_N77g6rLshiSjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc934aeb7.mp4?token=UUe6oSpMUX_bGXpqXx0JEI23xI6pSLouEEbKrtFe-yIJsZ-xbJzdzUqpxAva3APsGSHAaOy1HbdXBI4hBxKSZjFC1fVWS7Tv3tgJXRSVtv-M9SWOmpSbmh6kIzbbHMt3cRbba8cYoSEZ-9Rw1NgMSHCEVXBC2wQzG95BGNLkDTRhUKegnqRgtjPRiHMZVuve4AA_mTWBKhsucjDGtFsb9cI8qAc4CNJdAlc-lhG0T3D0Sa5gYmCaraavPBu5DgpBAKEV5IWyAwGO3vuii0fvrNRGAUb8LasKh5nar8rxNHgXoNmaVID6P4Nu3r5fzhKBfbRtYzT_N77g6rLshiSjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۲ شب ایستادگی؛ حماسهٔ مردم همچنان ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455206" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a012b9df14.mp4?token=CKiV4euGnljzJnfkp_Q_8b72wrI1veA9Enx4sv1ubDlmVzPifnuoBuU72MrqasTMJSy7ds1xXckpZFqtQ5qxhqxYyzHjfDTYCiZa4BxvxgkmsMfzVKzI_X1ns1i-Bc5KRGEHPjHfhH7CMc6N2n5jnGL874FiE2EgSMuQ5Xd5TmAPbadWEjL0ObWRXSylxDD55T0ViH-sGdUpnznhAX0CLk9nmq5Wa-RUY8aSVPZ0j9b1yf9y4i2wdmvieVFzXkrrQ1wIndQGPaWElxZwOQBrbs4rVlTs0q9I-jgDx6Aa3xNM3YoN83nTWW4Oj2_20A_WYS5nrOXKJR8BkRSifVvNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a012b9df14.mp4?token=CKiV4euGnljzJnfkp_Q_8b72wrI1veA9Enx4sv1ubDlmVzPifnuoBuU72MrqasTMJSy7ds1xXckpZFqtQ5qxhqxYyzHjfDTYCiZa4BxvxgkmsMfzVKzI_X1ns1i-Bc5KRGEHPjHfhH7CMc6N2n5jnGL874FiE2EgSMuQ5Xd5TmAPbadWEjL0ObWRXSylxDD55T0ViH-sGdUpnznhAX0CLk9nmq5Wa-RUY8aSVPZ0j9b1yf9y4i2wdmvieVFzXkrrQ1wIndQGPaWElxZwOQBrbs4rVlTs0q9I-jgDx6Aa3xNM3YoN83nTWW4Oj2_20A_WYS5nrOXKJR8BkRSifVvNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حادثۀ امنیتی در نزدیکی باشگاه گلف ترامپ
🔹
فرماندهی دفاع هوافضای آمریکای شمالی اعلام کرد جنگنده‌های اف-۱۶، ۲ فروند هواپیمای غیرنظامی را که وارد فضای هوایی ممنوعه موقت در نزدیکی باشگاه گلف "بدمنستر" متعلق به ترامپ در ایالت نیوجرسی شده بودند، رهگیری کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/455205" target="_blank">📅 22:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8JnFBSHt6rdEQ5lTpMoxAlGZc26WmCHbzhcj0NZUUbay465u9KYSv3bmrrMRhXvRxjiXiGRh55FFKV2rOpaivjal_wYTGs4cbksmqwZj7npeFyIBBTQX7cc-8d8cnyQaNXuNg80xlXKfK3FfWBL5_BqtgXCah0DuPOMyRbXP0oVHFn0A9-DS5m02p82pvtemTaC-nncKmK3D5-kUauUeMGc_MhLjrEUByY0jfyutbRChCrUUo_B2wFh4DyCb3bDiVrOUiBxiwvcoHkpN-fhtVIbpGsNNoaeo2fecBRqgAReTpEwFFaNwwpRRsUhWFZfdlEirVvPc4E8wbCMeIkiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEwr09bSZR_s4hkJoESvy2XD8eyByKw5rMeVXo8wjK0opuoBWVKqi031qJOrqjCVEzTmooImoOx-W4Ai2TFuafKbkIHZaz8mEK6FyK78CMZZMDo3qxCHI8rgyR4jMPqVNv1tw7wV1hrfByXySVmnp6LdXY4J6xudomQOGDzOvSmStycc4Oo75HI2Un1SLKm7qxLQXLyvrTE6yP1Tm4oz4umftWs9Iv_tERt5xSavw_xkAQ5h-5TzLAQVb2BOtxtsPa8Z-Rm6p1lkyFW64fqFtM3WdA8r_owfs98ilGeyQwRtMdAxnXPv9CieaTOz3V-s_GOpMyQIArLS5EXE_cZdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXUsOiKOh2T-W3WZ7U6x270tJKKYBwPo0cmW-xGrCaaf3pn8S8Gt3Y5EXIeBHXKpI-iXxktZRDBthWRZFolSMFwy3FXKmHZbDyPF-pOYHnJGkZYqVEpaj7nVYUXlsdJTZPP6UhGZL2qVazWY-_a-9Ny7eiCKyelb7K08_Rlz80l2VjahRaBGgprHdyL7biFEz7pQXMTZdFIAeA6Dm-XRxle3TMYApPakbpAkkiHV8KsMz0AfX97Pq6xsXEo1FvDXE-8oNzbcQbmVBIUnV2zCukIiCGXDpPA4f2BGWLzIrEzN7sxt9EkY-Of5mo4EJx4qq-4mkoNt8PWOw4_zHZLeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDSDkUHPy7ALus39RQJ14_USK07kWwt7UFpehyNtINYLJsn6M9OfY1ACHKXrflGh2Bcnz2WRQYIN9VxjZr13GxVRebsGZFbiOOfTdsRbTPOvP3HalZkOuQaBrQ1DLCQCH94F-QbCK7lViLpJQ1ioR7QZdKpwnyMFbQdslkTyuvmBuMQaEgFDKDYW6ELmbEu-XzO0rNzLCxktFFqetdgpWgnGRXfWs-wpz-CGfRSrCjPE6BX57bAojYXSOd9Gs-Ew2vshsmGBlsAv5iNDwkGiFMzseH5ADxiSjTCqr2VPuk_NZGYTrGjBx0gzqca3tXSPZR1ycXZBVbqxu2ASX5fKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSO5XmAyzOYb9YhO5pgGqyGFSPiPviTGnweCEdD3tQZArldhJC918YiNa_1vVRXqoa2GsisOi2ANXpHscl4ZC6qvA22SMBxAguUS4zfVzZeFNeMNjl63JWQopN_eHZqhDWDvhlwJ_zMUjj-g6kjkH14osqrEtToDV1GKdKfXWvb9wmekkyn8yo29firA48aqJBXI6NV2D4WUMVKz98TaTX_gnaYftGH4GSnFID6-KRDJ8X4RkT1rCxT2HSSRZbo8mmHIUImstTkvrFrOzIX0RE4RhMrZJyz2Tsv6inCPpNF-kTLdbkCSpYb6xf2nbpvPMsH6qcSyz_aZNoActcb2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbrJxIwIKIzTdrhmmk_-sfkW2pSV820BWFyUaOPfAIlrCbfPfFF_hOEPKRCrbUKHXDxdDd__epFZmbQsRRujqH22-Kuwa3Hru6zNjmgwYefvh2jykFcCKico_BC81YvW_t9sZhVw65mxtNTYDQdlWgY5nQCN0js3LioXK8h3ZVh1xpcykrjZLEtccDUxcwfBGmVD1MVDROfSL--vgC9eEGclZoTn2oaIxb45dQCqYfsEoiZX1U9LEkaHppF-xtd7Qpc7a9Q_kdQJl9UYGo8thqp0oyQ7B153lrTrm3WSiEf1OM4iQx_84FLZn_PVkFxITc6DDIoxgQ-N32oR03Nd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikUCUMY07a5g601Q0IGncSBU-QNzlkWiHilx8i2RCdGFkoPP3lj514lfZznVf2U2z3NkM_JWrECI7gxhfhiZGC-ZJ8cXKQEanwZn0fI8gnC7T-k2t01nXcMkA5dj0YNsfNJmtw3HYoXAhlDsUlVxTZrRWHZnOuGRgNVeIOZqF3SLRZdXxUYRCtigj1PzPNLBkiJf35uGpt3ovOvhZFAdqKNiVvOZYi4m7MzqyiOEeFJgP9KGpbXkJCO0bYNiW5c1VeVnM3YprqkN5CqKa-LVZhjmRCgzpPQ_Q5wZrPeo1VUhdrdsZyHTynfPu36yVC0RvwtmdXh_UoghrwdPaIxc6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سالگرد درگذشت استاد فرشچیان
🔹
مراسم بزرگداشت سالگرد درگذشت محمود فرشچیان باحضور وزیر ارشاد و سخنگوی دولت امروز در مجموعه تاریخی سعدآباد برگزار شد.
عکس:
‌ محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455198" target="_blank">📅 22:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455196">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkGfQTBbK_xhEDn_1npL_iv8FBf1mRxgsjPF2ZLqEZTJVFZsqieZDS23kGizWux_TQTUzaX1E0VS228lZqxVeAlPBw5FW5an22knoqn9-URUKdlgwe1M4_W_kvmdfx3ewsCMkL2moZuXwVOsvfi4sF3hvETCGAUsax7Tv6EzLPGDtnEd9kImtYd9kEoZA3mB9I9GfsrRFKfdJ-LpIANi7xkGGO66a035VOZ4kTvr3xEc98dGorAsoAoaEzzc3xZAgeyweGh4AfEMz2G8J9gePEicCor9pdIzCAEZg18_QqGgz4g9g8xsiLMfsRUQlVeFvUxmJhMJdMAia6_IqvtGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات جدید از ضربات ایران به یکی از مهم‌ترین مراکز ارتش آمریکا
🔹
بررسی های اطلاعاتی نشان می‌دهد که در جریان عملیات «وعده صادق ۴» و هم‌زمان با پاسخ نظامی ایران در ۲۸ فوریه ۲۰۲۶، پایگاه هوایی الظفره در امارات طی چند موج حمله پهپادی هدف قرار گرفت.
🔹
این پایگاه که تنها ۳۰ کیلومتر با ابوظبی فاصله دارد، یکی از مهم‌ترین مراکز استقرار نیروها و تجهیزات آمریکا در خلیج فارس و محل هماهنگی بخش مهمی از عملیات‌های هوایی ائتلاف غربی به شمار می‌رود و میزبان جنگنده‌ها، پهپادهای راهبردی و سامانه‌های پیشرفته فرماندهی و پدافندی است.
🔹
نیروی هوافضای سپاه با اجرای تاکتیک «ازدحام پهپادی» و به‌کارگیری پهپادهای انتحاری از جمله شاهد-۱۳۶، موفق شد از لایه‌های متراکم پدافندی پایگاه عبور کند.
🔹
بررسی تصاویر ماهواره‌ای نشان می دهد که در اثر این حملات، منطقه استقرار پهپادهای شناسایی و تهاجمی ارتش آمریکا، آشیانه‌های هواپیماهای هشدار زودهنگام، یک رینگ پدافندی کرتال (Crotal) و مرکز فرماندهی و ارتباطات ارتش آمریکا مورد اصابت قرار گرفته و منجر به تخریب و نابودی آن‌ها شده است.
🔹
اطلاعات به دست آمده نشان می‌دهد که پیامدهای این حمله فراتر از خسارت‌های فیزیکی بوده است؛ از کاهش توان شناسایی و فرماندهی ائتلاف تحت رهبری آمریکا گرفته تا ایجاد شکاف در پدافند هوایی الظفره و زیر سؤال رفتن امنیت یکی از مهم‌ترین پایگاه‌های نظامی آمریکا در منطقه.
🔹
این عملیات یکی از مهم‌ترین نمونه‌های به‌کارگیری تاکتیک‌های نوین پهپادی در جنگ ۴۰ روزه بوده و می‌تواند بر معادلات بازدارندگی و امنیتی خلیج فارس تأثیرگذار باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455196" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455188">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39826177dd.mp4?token=D956e4SLKi_xxsDBu3FH-NN_tvzkIs2mEO4MmcqP1V_QvfEp2RUPYLy1l1gEZOfE5egBlF3Zd1pkG0KQ04EufIuuBKCQ-bW_CK-J4xiYfomLjO-NmTxgE-2TOSVT9tz79LW0FnTAZ6vaD19-m8a6WOJxDbU1icnucKSBM7uD2ULeBUOJZ-BYFUwmgPPXULpXRNhyGfN7T-1yxRuwhdxm03K2rjqo2XjcY2jiMlcBeQdxtOYrLQBK6T-iM3UIdjbnZp80sArU18MplhnmauheVgZNfBj-lz1PSqUi7R48S4zncA0LT6bfNUVA3FcdHVlSSxiDPMUDAKAJdj8BQaWlRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39826177dd.mp4?token=D956e4SLKi_xxsDBu3FH-NN_tvzkIs2mEO4MmcqP1V_QvfEp2RUPYLy1l1gEZOfE5egBlF3Zd1pkG0KQ04EufIuuBKCQ-bW_CK-J4xiYfomLjO-NmTxgE-2TOSVT9tz79LW0FnTAZ6vaD19-m8a6WOJxDbU1icnucKSBM7uD2ULeBUOJZ-BYFUwmgPPXULpXRNhyGfN7T-1yxRuwhdxm03K2rjqo2XjcY2jiMlcBeQdxtOYrLQBK6T-iM3UIdjbnZp80sArU18MplhnmauheVgZNfBj-lz1PSqUi7R48S4zncA0LT6bfNUVA3FcdHVlSSxiDPMUDAKAJdj8BQaWlRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقل‌قول جعلی منتسب به سردار وحیدی چگونه از هند به سخنرانی نتانیاهو رسید؟
🔹
هفتۀ گذشته نتانیاهو، نخست‌وزیر رژیم صهیونیستی گفت «امروز شنیدیم احمد وحیدی، فرمانده سپاه پاسداران به صراحت قصد ایران برای توسعۀ سلاح هسته‌ای را اعلام کرده است.
🔹
این درحالی است که این نقل‌وقول جعلی در هیچ سخنرانی یا گزارش رسانه‌های رسمی مطرح نشده است.
🔹
روزنامه اسرائیلی «یدیعوت آحارونوت» نیز ضمن اشاره به اشتباه فاحش نتانیاهو، در گزارشی بررسی کرده که این نقل‌وقول ساختگی از یک حساب هندی در پلتفرم ایکس آغاز شده و در حدود ۱۵ ساعت، از چندین رسانه عبور کرده و در نهایت به سخنرانی نتانیاهو و سپس به فاکس‌نیوز و مقام‌های آمریکایی رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455188" target="_blank">📅 21:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455187">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxUmcoNaSR_XZ9Ck0bB8XN2A5zJlnbiQd_4TNr_uS7Lk3-Uckmpal2IayPbyW9RPgcaO6ngoNuc-5iZIJjfAFOqUM7Z0CBEams3RlCEvnmhywDDrwc3NZQRE6F496dXGg7GL0m3sML5HTNfDrwEaZ9E8efnA6nUAjk8W-T06BuCo1qAbY16yDNRZi4oRfFUfbsbykx1QFC0RTpWWbUg9fxNICtt7UARsfss8E4m8wWNeESQpewA-Blly7zalQXR3-GEeaTQ9bDX0YTzNZzZf1vvY3fBSVOxw0x7FPVyhFBL8PgFFQg4P1DwqmBUtiWKekcBJ-i-a1OWcjLFsxLCW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyL1vQ0pozGXEVXdEWFLbOMdVsriNfqTTodmssaFGj4vTRd_U8h-L83cRvz0XV7ybODdF-VF9Tm-KL_85Q2p1wtDyyrF942WXEDXheX81gVv5zJwE5duUw-44aes7P_pAMOJy8FRLlXhXW29IXkglJUm-uXs96amPD4SnazEjUnbxFZs8L6l68_k3s0vgCbSvK98ToyvKsbbt2fe6xKUSqadKq4aZRndAUaAys3GjT3-Dtq_6QoNH1n4l0ZbyEYS2_PzSDHyW-Z-3wcTro5Z8PNFMRbM-b5qwOCTeU1tgCPcPSeLE2paiRwWueLntr3RfU2rWcBXXnah-abz3w0U4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcwkJb5MBnZ8pTeHF9yrFGXeNnaI1T6hLWd4q1fxVpIXXOmEDNdnZew7298-zwiqXphLjnXmfAtnGNhRxRVq-gjaz6-mknha7d3XvU2vEwIhrnKOdzQ2yXasGsgkPj_WAdIMsSYrE7yI-br--4-qDtV8kQZ-GDksKVk2Q0QUTb9IJVaOqxKVHnRAbkiSYqyykwjeUPM4bFVhsZmwWkWes1BmarCovN0xYESioL0JQ9sefOQwXDJlqUPPO9b7FH4JgPKSurpjVz5z5hcyda4QdRu5AztDzpnNeABnB3hB5bfcLOvH-r2TTRxjy6MUNmnGUZkkqdDFUbm3J_sfPLwIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Apyin8gwV6Mj3aSh3_q61-cY9suu5-pkASuQDlL07QQilsn39NC0XeQws_y7j710ZUNAc5NXGuUUWXtRzE-p90KhHUaeCqoayXAMYPMu8uLLgDRmR3G0iy7JQGU6G34w5Ek2Y97WEUX6hs5H_B6nYc1ypUaR7JHcogIzqYp8qTNOw9g03lAHJxuAUlHSJBCrRFU7EvXt1KLMObK3oPen_YsHnag2olXVqC9TRb4Dbi3R50VaA_pFZ5wVw5Z8QblP2ybigND30oDCs04YVjMYaTtIbfCE1abKkxfYgt1FEWlcwmwMEcHqgAPrCF_W-eiJ50TwVPdSWEjSJgi7BFhGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTUY_UY9255kvQvB8jcHjPq1xxfW5xo6TqS1l3i-rly8goEJD6BMvHgJdPK5dWhHfH1dW7QAPXHeDKVwuh9fJo1t92_pyzGmSO_Y7WqJ0MZRTbx6rNZRlnb_D8FFl9T3lgUSe1N_6DMT7ifFe-jXon4KY9mTApPzWsINb8WWR9y1oMO0tHtSJ3AmaeNiKjnBtMcjsARfnr-haLa73-JvOYAubetzrKbE42zFDbwvG2DbNWrUgh8-U6pPvznRwEyfVXwi2qq-LbAQ4PcatTIbqx262e9yIlS229LwKserW60m8CLQj76kv8HwfkM9OXNmjziCncASFcyTSQyFx-YD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDSL-kFAi_Ysa0uJxNxlEyrQgtoqbJc6vT6Ja9JV1KCVBNPBo86aBXnmAtsKs47iHKvoGO6FS7tOaBDyrGMd_P2dLPuYI3pGNlr-f6gR3e4M7nNjTp0zWOJdyCHPGXKFBpg0dIM1RO9pULnk4i6Pq55y28SleJwZLNbGTKytvaINIuXFQcDaEwX0sq692GfKOvWrJJ-_ZsuQD-2uevkzgGZUnRDozNxcG3ZMFer2ari1P99OQDmSnQ7qm0WVsXwbgg_NP4QAWzO105--JHwkiHKt5RQhh15tdQ35KpLI310SgJ03dYxwgDcApXaUxTODn2hqsRbSaL0rSQlzkAyN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-hY_0Rs3c2eWQROXMK31gTNyCw749OZlTNqUDliBY4UgvhsQLuQJLXwwtxORrJvE4hgHUUuGJXExn3JDyg4L3eM23hhdGp_gn31RlqMn5iNsqSNw4ehoLVPx1aTl3540oTiZdWPaV-D-9SKVhdMV-iMUeDdMQEeKh3d1RIdftENY5nmO62HSC0rlvmN2VfgCtiHZq8RLVsSCMGAag4JRZr6KWKkByaCoYXHsklf_pfd6kwk-66PPJjKNZYyrLT6bRcEGFe_YBZKma_CVPLeHaY79IwPAuJU3qykH9lTFhYgW3f0vE3UGMXJf3KC2wTfDdS2V9wfi1oDRenoUnCB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTIegI7A0bPDDg6-31sMtTzA_J8QrxMIAcWEmUNL74sUTGaVTknsjj9rx_FzROvVki0TsO3djqXq8Fje41T7ACoK_HIGZyx6yNbcXySrsr-sLrXjRINugaHvq8SxSH-hobs8GxYGHZbI61Gsw0CVHS29NtFFjcIXF6SbqMfbpQsX7Thhn8zZiNB9GMxioe06Wzb6nLzuS2KZ3_mGNLrPfs8uGsNs6z7tEvo09BqXggvpzWFdnzsqXvTsHpKHmcaVmkQ9DQkZ1_ka9P4uGU-J5B_TBAjGvHRw05fY9yglj2QniDyAYpnt6-iX4TVAOQQofEU11t7Ml-P0bPo-DKLbCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر جدید از انهدام مواضع نیروهای آمریکایی در غرب آسیا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455187" target="_blank">📅 21:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455186">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ce2e9abd.mp4?token=S_Ca4LNs3IhI-RJqqjQ-Jl23KnMEuG3aknZqWSvK6ptZf2T3r1OYsClukhDtYM6tSy0wKqHF68OPscZdYktIaFv-F7Xh-ybu2RNjaUn8uZTKwZJ_PkAgyrZOST4PFV17Q-etuT2ZXE5gAOCEgCgqTi2koNbJxhWn2L1fdHq7CbYRhM7NUG4kn1ox6y8syDLkaIhNvooU6KBtTkR5aWzUH_gKVLy6cdg9FbNaGtebN3guetmTIinUhP_p0M_u-JgB6QUMELlxRQC-8-9DzX0RHqA9a7HE1tIQceHOFhdgImX1IeDRKqmsvgiB-rZhSSWnx2_f0aCa6gkf3FhB644uGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ce2e9abd.mp4?token=S_Ca4LNs3IhI-RJqqjQ-Jl23KnMEuG3aknZqWSvK6ptZf2T3r1OYsClukhDtYM6tSy0wKqHF68OPscZdYktIaFv-F7Xh-ybu2RNjaUn8uZTKwZJ_PkAgyrZOST4PFV17Q-etuT2ZXE5gAOCEgCgqTi2koNbJxhWn2L1fdHq7CbYRhM7NUG4kn1ox6y8syDLkaIhNvooU6KBtTkR5aWzUH_gKVLy6cdg9FbNaGtebN3guetmTIinUhP_p0M_u-JgB6QUMELlxRQC-8-9DzX0RHqA9a7HE1tIQceHOFhdgImX1IeDRKqmsvgiB-rZhSSWnx2_f0aCa6gkf3FhB644uGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبری از ۶۰ ناو جنگی آمریکا نیست!
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455186" target="_blank">📅 21:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
حضرت آیت‌الله سیدمجتبی خامنه‌ای در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند  متن حکم رهبر معظم انقلاب اسلامی به این شرح است: بسم الله الرحمن الرحیم برادر گرامی جناب آقای دکتر محسن رضایی
🔹
با توجه به تجارب ارزشمندتان بدین‌وسیله…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/455183" target="_blank">📅 21:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انتصاب ذوالقدر به‌عنوان مشاور سیاسی رهبر معظم انقلاب
🔹
رهبر انقلاب اسلامی در حکمی آقای ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔹
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
🔹
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455182" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aba5bc2af.mp4?token=UU57yjVTPn-bYlRkNKnVBC_bU3dbU2cU8mvznysIUYh-d0cyY2RuDG4lLr_PFyo19mo-GeS0dUZ7qX4zaWY6hlx8G8XnbiJEzSALdWYhjCE3Ru3OgnpyKovFLThz9pQLQ9ZAs3etdO0Yi0Gd3qtCUNtFVqT8FrgDZtecxkVfa7f2mrEMWpqIAEZHmwBqC7q215ideaV5leRSkyvrFK3EHGDBKtTWr8YXQ8rbNjH1K1Yu0ow2gvuUgijUqH3nHaFD1PlzPqFY3iezwDQ31kHGqqw8uPVhjVBRc3I27IOcYSqgUVobixd2JgDcb7GjDi39r5AFBF6l99Wj-XeelO94kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aba5bc2af.mp4?token=UU57yjVTPn-bYlRkNKnVBC_bU3dbU2cU8mvznysIUYh-d0cyY2RuDG4lLr_PFyo19mo-GeS0dUZ7qX4zaWY6hlx8G8XnbiJEzSALdWYhjCE3Ru3OgnpyKovFLThz9pQLQ9ZAs3etdO0Yi0Gd3qtCUNtFVqT8FrgDZtecxkVfa7f2mrEMWpqIAEZHmwBqC7q215ideaV5leRSkyvrFK3EHGDBKtTWr8YXQ8rbNjH1K1Yu0ow2gvuUgijUqH3nHaFD1PlzPqFY3iezwDQ31kHGqqw8uPVhjVBRc3I27IOcYSqgUVobixd2JgDcb7GjDi39r5AFBF6l99Wj-XeelO94kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان: کلیات طرح اقدام راهبردی امنیت تنگهٔ هرمز در کمیسیون امنیت ملی تصویب شد
🔹
عضو کمیسیون امنیت ملی: با توجه به موقعیت راهبردی خلیج فارس و تنگهٔ هرمز و لزوم اعمال حاکمیت جمهوری اسلامی ایران به‌منظور پیشگیری از تکرار اقدامات خصمانه علیه ایران، کلیات طرح…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455181" target="_blank">📅 21:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c44ea7008.mp4?token=tHwNMbCErM-ovttPr6y6vcdT20L5ktf8rSTs3LDI1KH-crN37V6NYoP4_AaLumXR9z4znj4JmA1hdxxgcV-I28iBkFxEKAe9neZdFbrJZw7gi0Yeb1QDlh7yKd9lOJpk136PB8gXcmfMLXmy_n1_P7MaH0ot-BSbtXVeSVF-Bvcf6HplmM9kBLoysXYS1vgusWLgkBgSHbn3YDowSe1CnmDzZjYxfs37fGm1i8dmEKTBAf2leCRTEVLg4Q6aj_cDhaKzmZ4PAFOS4dAUpB6F3Ep9Of-TnkHfmmSM9oPJ8QY9d5sbmYUVQv1M0SoircVMqxpX4MysKIUl2TB6fLEc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c44ea7008.mp4?token=tHwNMbCErM-ovttPr6y6vcdT20L5ktf8rSTs3LDI1KH-crN37V6NYoP4_AaLumXR9z4znj4JmA1hdxxgcV-I28iBkFxEKAe9neZdFbrJZw7gi0Yeb1QDlh7yKd9lOJpk136PB8gXcmfMLXmy_n1_P7MaH0ot-BSbtXVeSVF-Bvcf6HplmM9kBLoysXYS1vgusWLgkBgSHbn3YDowSe1CnmDzZjYxfs37fGm1i8dmEKTBAf2leCRTEVLg4Q6aj_cDhaKzmZ4PAFOS4dAUpB6F3Ep9Of-TnkHfmmSM9oPJ8QY9d5sbmYUVQv1M0SoircVMqxpX4MysKIUl2TB6fLEc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش اعتبار کالابرگ؛ از وعده تا اجرا
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455180" target="_blank">📅 21:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax56nqeqd7RTTSMI3YAcCS3CV43xay7uHYWGeFNB0D4yZnYWtdP3jtbeYsVlJEqgIpxc3_Oe9uEe0cKgkfo7nafh_m0YSp4Rl4x80YaF6W67rfYbAWLxYFIlhYnB_ftS-eNoi5h_OjTq_WMU-aOoa9Sykt5MsFaOh4_OxcfcoOzT9BsrNfIShr3TFF-RTUPKgiuci3e7pOdlr9TtkJkeoc1ubeGOHljZ6qq9s1o_pyW3KwuoKib6YNDnlh6_il3F-3UMSOhBRxBOIltdULV4TkzR6tigzgRYdmnsqk69UKLHtA7vNxiJCTsiPgSMP_cEc0lmDXQzURa09GDIyYpDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب نقل‌وانتقالاتی تراکتور عمل نکرد
⚽️
بعد از معرفی جواد نکونام به‌عنوان سرمربی تراکتور، شایعاتی پیرامون علاقۀ تی‌تی‌ها به جذب منیر الحدادی و توافق اولیه با این ستارۀ فصل گذشتۀ استقلال مطرح شده است.
⚽️
بااین‌حال پیگیری‌های خبرنگار فارس نشان می‌دهد این ستارۀ…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455179" target="_blank">📅 21:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372042832b.mp4?token=K9IT8ekcVGRU39b7DwuZaN8elnVLzaNEC89dFyCNU13Ot_IQ_SOpyFJy-OtnW_Phi--n3DVLn0XdXk4VZzibVyyP7qc4RmQfu_lU1Yn6bSN2WlJgzivYdkAGSkPG_arY8JKUNpyinYroUFnzdBc28veFZWYo_sTliC5y2hQg-DvXeUP0ul5l4UWQO5I0SzU0HwqxBazD2FxFRkYBxr4A6xCCg46Y5s4w_NYvHkhM1c5jBKv1D25aXcQL5pDgRrxhk01XftGL8Q4Bv0uQWi62e9wwIy8KWaqiICcU7OvTLAiVikOFfJX4SKRNAcs6_OJwdO61j7svmnEGySirLOn9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372042832b.mp4?token=K9IT8ekcVGRU39b7DwuZaN8elnVLzaNEC89dFyCNU13Ot_IQ_SOpyFJy-OtnW_Phi--n3DVLn0XdXk4VZzibVyyP7qc4RmQfu_lU1Yn6bSN2WlJgzivYdkAGSkPG_arY8JKUNpyinYroUFnzdBc28veFZWYo_sTliC5y2hQg-DvXeUP0ul5l4UWQO5I0SzU0HwqxBazD2FxFRkYBxr4A6xCCg46Y5s4w_NYvHkhM1c5jBKv1D25aXcQL5pDgRrxhk01XftGL8Q4Bv0uQWi62e9wwIy8KWaqiICcU7OvTLAiVikOFfJX4SKRNAcs6_OJwdO61j7svmnEGySirLOn9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ روشن به ادعاهای بی‌اساس آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455178" target="_blank">📅 20:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDxR0nVL1kKG25JnXU1j0GAqmwJPB4ux3uApsz9dfutCtIvugTpjpMF8hLri12bMJ8pWkQIsvfg-8OBcMtf4IhtTaIgVnw77ma0phl_bKh5OeErAQK_cC2oec-dxgyYpvNWKtWwfBOFYNa77HL4hNefMVpa_xy-laVJDAWApNVjF3mXv_vvpA8RfV1BcMNgZsT4fddzfn7Nn90KDtnlMfFeNfPJ1Y1kA8klx6O9X1txzW0A9r2zKtfOZCyDxT3UXpMENZXCKBImkPTqBQHo7v6f7i8DA_4zUOq-BSuIQsBmhmQ8NJ_MfLtIXLENJoIbbOfLqclnuELwHuWqQBv9OUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ‌فرش خیابان‌های تاریخی برچیده می‌شود
🔹
طرح سنگ‌فرش کردن معابر در بافت مرکزی تهران، با هدف تبدیل این محدوده‌ها به پیاده‌راه و کاهش تردد خودروها، یکی از پروژه‌های بحث‌برانگیز مدیریت شهری در سال‌های اخیر بوده است.
🔹
حالا آقامیری، رئیس کمیتۀ عمران شورای شهر…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455177" target="_blank">📅 20:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aISWlH01VcyjnLXIwGALCGPAFcfL6PJYMoCPeOZ8IkxysgknS-tfr2wr5D5KPwABx9HeMRtQQ5_kOCHy1tJ-999Zk27krIXmgaLZzd8nDhcD3bfwL3WXqJnCD2tRTZeIziOzxZkvVYnRRQ3LSW0j4BxKHCI5lv39JiNkrp_XOBctjF3UOE1sMmoHRRuUEml4HFnaOPP8ez7f3WN2qh4JU7G1UEFmammrrmGQJf8WOYRJPWkrcue2ctvleoU1b47bsLzzddUW8wtL1oXIE2tifVVQh9u8UlAz5tZfHShdO69NpxzlgI2Z9jyutNQyxqVzMN-Hnl1UJk1lQRns-HVpag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: دولت لبنان در برابر نقشه الحاق سکوت نکند
🔹
حزب‌الله در بیانیه‌ای اعلام کرد که ورود رژیم صهیونیستی به مذاکرات مستقیم با هیات حاکمه لبنان چیزی جز تلاشی آشکار برای وقت‌کشی و تحمیل واقعیت‌های جدید در میدان نیست.
🔹
هیئت حاکمۀ لبنان مسئول وضعیت کنونی است و باید با بازنگری در سیاست خود، مسیر امتیازدهی و مذاکرات مستقیم با دشمن را متوقف کند.
🔹
همچنین ضروری است در تمامی سطوح، از دولت گرفته تا شورای عالی دفاع، اقدام فوری صورت گیرد و جلسه‌ای اضطراری برای مقابله با این موضوع خطرناک و ارائه شکایت فوری به شورای امنیت سازمان ملل متحد تشکیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455176" target="_blank">📅 20:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTrlSlPjMRYVwgricftIw2sZxIZT0lRTgcbkXIUkilv-WJpAsLriPGYRPt8mDt8G2Cu25r4eXPkJ971vu3iqaTmfihB3uuRJdIVnRu5n6T8_4IDyzBX3V-hTCF7pfWeQqAsccLHqteNKI3P1-ZVELnFiTeT5zq2EAQ3FHG1edalb84puRYXgodgrR2uMFvc8cwaN5tHrKG87r5a--aGVDxzv8WYNccY-xZVB9s2XoApzsXZf0V4t9ltQSokRTTMlpiG_N4xoksZaqxlaMVTg0LNKaHlqLY8FxSADxpgGOZVKOqdPXzRqi6qT0raHPOkrb7sSUlTrrjtraB19h8p7vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضرت آیت‌الله سیدمجتبی خامنه‌ای در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند
متن حکم رهبر معظم انقلاب اسلامی به این شرح است:
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محسن رضایی
🔹
با توجه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را که از پیشگامان دوره‌ی پرافتخار هشت سال دفاع مقدس هستید، به‌عنوان نماینده خود در شورای عالی امنیت ملی منصوب می‌کنم. امیدوارم در انجام این مسئولیت مهم، کمال موفقیت را کسب نمایید.
🔹
ضمناً از تلاش شبانه‌روزی برادر عزیز جناب آقای دکتر محمدباقر ذوالقدر تشکر می‌شود.
🔹
إن‌شاء‌الله تحت توجهات سرورمان حضرت بقیة‌الله‌الاعظم عجل الله تعالی فرجه الشریف همواره سربازی مجاهد برای ملت سرافراز ایران باشید.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/455174" target="_blank">📅 20:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c72983f7.mp4?token=ZPX_W6UftlNYjOHstk2tt7T55Z06rV2U3EW1MeysZpTvkiWJGE7gm6Sk5MFvYDWjj76GlJz08cFHa9uGzUAhTBZUg4l891ZMxIU0ImQ33a8aeacGuz7OL80nAV2dFCuAR9B6_u1YwLwTG1nKd7-gtL2tgVPMGqgflL1W03zMUUULsErRvRODtNTzXLBGh7EPuGtKksZZXaj1kIgAp1CeSs6QvXrLNccn8OScwSWIJMARfc0VGm1eIt7a-QbLMyN1VO4as-3ka6fE0SYFAweUzqskPF5aDql76KLfj5QHCl1FpBpl55nV81kZSmsGLY3P2iDGGwu4udWcNNuqq6200JJYEbDUKeWkeA_8B6-36JfOgg8skNsYm7eU7KIwEEFEZmXEKzkQXGjajFi_t3z69nHMHQViZ4ViLJGJizKXZhMXgtkCVbGeS4ktIxtHTA7o9SAkhFwqbSD7cyipbL9bkULqZ8bFIjsypWPq3kemvQzn36IZV0jOvcZmiUSDace2oqZ9LPpmvKKSkani4O70LKg9zb4Ze_otStNZ80fCmlU8w8fP9cquJLMjSPui3dvYEY-uBuoal8K3fB5ca8gh-e7U1ewHU7O9G2wmTQUGpoe8GuM285HQ05y9BN0e0QOencvbTC6IpGM_fPjeGHefnxqdEyt0G9TCh8DATh7z5is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c72983f7.mp4?token=ZPX_W6UftlNYjOHstk2tt7T55Z06rV2U3EW1MeysZpTvkiWJGE7gm6Sk5MFvYDWjj76GlJz08cFHa9uGzUAhTBZUg4l891ZMxIU0ImQ33a8aeacGuz7OL80nAV2dFCuAR9B6_u1YwLwTG1nKd7-gtL2tgVPMGqgflL1W03zMUUULsErRvRODtNTzXLBGh7EPuGtKksZZXaj1kIgAp1CeSs6QvXrLNccn8OScwSWIJMARfc0VGm1eIt7a-QbLMyN1VO4as-3ka6fE0SYFAweUzqskPF5aDql76KLfj5QHCl1FpBpl55nV81kZSmsGLY3P2iDGGwu4udWcNNuqq6200JJYEbDUKeWkeA_8B6-36JfOgg8skNsYm7eU7KIwEEFEZmXEKzkQXGjajFi_t3z69nHMHQViZ4ViLJGJizKXZhMXgtkCVbGeS4ktIxtHTA7o9SAkhFwqbSD7cyipbL9bkULqZ8bFIjsypWPq3kemvQzn36IZV0jOvcZmiUSDace2oqZ9LPpmvKKSkani4O70LKg9zb4Ze_otStNZ80fCmlU8w8fP9cquJLMjSPui3dvYEY-uBuoal8K3fB5ca8gh-e7U1ewHU7O9G2wmTQUGpoe8GuM285HQ05y9BN0e0QOencvbTC6IpGM_fPjeGHefnxqdEyt0G9TCh8DATh7z5is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدافعان حرم و درخشش جهان‌نگری انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455173" target="_blank">📅 20:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCqVMFdIVOkMzJvG69p70-Mb5DmzSKW_l21ittynQYDDSLXDS8YFglf4J-3AGKK9aAVDrGDrGz-wBzQDspcNCi3_FMjkhPOU39WpWxX3HzB6f9y1eE2Xfv9jxlYINZYUGuAXHdjJGIJpd7eH_S1FyAqVnH_VEh2yBINMr_-4QKea7hz0RNItJHaPXdiDKcdJW_CTUUmpyzi7QnHdIJGe55sUhNEtd-7lFd8Jg-dCVK9gV5R91kjvQdMhZK7Qfn3xlvoxc0-3NL1IdDsBfD0oUcDRSn-RmCD35T_PZrb9C28pMvO1TRm8GY_NpPKUmoL1LivSIcxv0BdMNxFVoHZuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب نقل‌وانتقالاتی تراکتور عمل نکرد
⚽️
بعد از معرفی جواد نکونام به‌عنوان سرمربی تراکتور، شایعاتی پیرامون علاقۀ تی‌تی‌ها به جذب منیر الحدادی و توافق اولیه با این ستارۀ فصل گذشتۀ استقلال مطرح شده است.
⚽️
بااین‌حال پیگیری‌های خبرنگار فارس نشان می‌دهد این ستارۀ مراکشی ازآنجایی‌که به دلیل شرایط ویژه منطقه از استقلال جدا شده، برنامه‌ای برای بازگشت به ایران ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455172" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd0280352.mp4?token=XZJVOJQwvPFcorNpHIDtaDP-X7AGmzUW9nJ_2oHpNAKSHAljsuIKOviJtmm9RiDsAtWIVsJOCUtEfHBOVndGP95ipf1IlLm02qUuB7eaM3S27NB2y8R3bg1375c8u7Akhu6IxDSdWPc7ezjUUJ5E6aJ_tFjAozXIfOtjBDvCQBKzEnYivh0jYmLvb941xr8BYbp4UiS2mZ3_wXElcxpHtm-ZxPytV60lahu2_YwYSTpqJQEbG3gS9_62Hu5eUOcwna_ELMEAeDRj6sXOgLeI9DxiSBwJ8w_9JMZZBZbzWOOkNcGwCX91xwz1zQ2PwoGdaChQJByRuuovc677dD6LLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd0280352.mp4?token=XZJVOJQwvPFcorNpHIDtaDP-X7AGmzUW9nJ_2oHpNAKSHAljsuIKOviJtmm9RiDsAtWIVsJOCUtEfHBOVndGP95ipf1IlLm02qUuB7eaM3S27NB2y8R3bg1375c8u7Akhu6IxDSdWPc7ezjUUJ5E6aJ_tFjAozXIfOtjBDvCQBKzEnYivh0jYmLvb941xr8BYbp4UiS2mZ3_wXElcxpHtm-ZxPytV60lahu2_YwYSTpqJQEbG3gS9_62Hu5eUOcwna_ELMEAeDRj6sXOgLeI9DxiSBwJ8w_9JMZZBZbzWOOkNcGwCX91xwz1zQ2PwoGdaChQJByRuuovc677dD6LLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامۀ سمت خدا: بازسازی کشور احتیاج به حضور پررنگ مردم دارد
🔹
از حالا باید برای این حضور مردم طرح‌ریزی انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455171" target="_blank">📅 20:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPx5B4fpR4Z3ZPxo6fxsmE3dNuTVvsg-jnecfeDcvx4EHHMzrR4_WevnlogWO7AAJR56K7ZsCxXdKacK_CL6oBgxoe9jA-WKTeRGCx_Knehm53kTypFZ-z_i4CYOXw-He0cPSrJW0tQnkCL3fGhpu3OJZDOV1nrizlPLCZvE2d25JujD_uErMD7snvyWBHTVO15fVXvbBtSR_fIUbBvUSsqCMbsMtzqcb-0NjT5kHciacUyADwP4G4t4HDLXgvidBoUym_7qLQr73YW3ufB0hXtRTFg9OEEqf48lQyEhtStuM_ZYcoW4l2vHZdRm1rksUjxoqm6VJ1b60bzarQKM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کنگرۀ آمریکا: به‌خاطر جنگ با ایران، نه‌فقط بنزین بلکه همه‌چیز گران می‌شود
🔹
الکساندریا کورتز: من فکر می‌کنم که مردم عادی آمریکا شکاف بسیار بزرگی که میان حرف‌ها و عملکرد دونالد ترامپ می‌بینند.
🔹
آن‌چه ما دیده‌ایم سیاست‌های ترامپ، منجر به افزایش قیمت‌ها می‌شود؛ نه فقط در پمپ بنزین‌ها بلکه در هر چیزی که شما می‌خرید.
🔹
ترامپ بدون هیچ دلیل و منطقی و بدون مجوز کنگره جنگی بزرگ به راه انداخته که خطرات بسیار بالا و پیامدهای فاجعه‌باری دارد.
🔹
هر روز که این وضعیت ادامه پیدا کند خطرات و دامنۀ این جنایت برای کشور و تمام جهان بیشتر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455170" target="_blank">📅 20:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441a65f11d.mp4?token=hmCBUgBZvTdQpgUWMdvN7Eduaj_oGfwoDDHXeD1vnOAa0wXM8LRd0clvRyFDCIuTSCJrxZNuyhGl1FtccW65z-tSeiOVSN57UrSU81uONtANPgo3vggdMTBwCBbo6eawIC2kFk9OOXh3l-P5aGpSAY0A0PSCiy6Ts_-5kha7Ylb5oeJ4kQkVTLrkBFyFFSrlOckRG70YWmbNPerrH5R9F6SoLjWE-Vi3caGo1ECefLgVQH3WLA6Hr2GMZazuLpqfQF48ixVSM2kh6TdNbt41cXXH4lsN_2-VWzlgwm8Iz3EueADVUkLg3quUoBfpKolx8Dk1CwNbPlw4FbqwpT8g9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441a65f11d.mp4?token=hmCBUgBZvTdQpgUWMdvN7Eduaj_oGfwoDDHXeD1vnOAa0wXM8LRd0clvRyFDCIuTSCJrxZNuyhGl1FtccW65z-tSeiOVSN57UrSU81uONtANPgo3vggdMTBwCBbo6eawIC2kFk9OOXh3l-P5aGpSAY0A0PSCiy6Ts_-5kha7Ylb5oeJ4kQkVTLrkBFyFFSrlOckRG70YWmbNPerrH5R9F6SoLjWE-Vi3caGo1ECefLgVQH3WLA6Hr2GMZazuLpqfQF48ixVSM2kh6TdNbt41cXXH4lsN_2-VWzlgwm8Iz3EueADVUkLg3quUoBfpKolx8Dk1CwNbPlw4FbqwpT8g9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: افغانستان و پاکستان نگذاشتند تروریست‌ها و تجزیه‌طلبان از خاکشان وارد ایران شوند.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455169" target="_blank">📅 20:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieal6VSOIkv0Xf4suFSt0RdI-apXoufXJCtLwL_m2V6AyhC66Lw7uOeYNR73EgapPIGoJPdHDbDfamk4tcAyEYgX3AtUs4rYtVmhypODX4xKiBweVOpzJLXQgfW1GUS-30RoQwlBXlnkJwHjGAOo3N_S5DS5xKwUsDGH0qWrphfti8yJDSQmagersZqou3kyCJFc0-MAjWX1F9WHZLLQ1dVk1S3a4wpF7nQRqrC1qX9cR5rbaFJ0RdQkZD6zrMc0pBmMfMVrwtUwtLn8voLN98ZODhGFH16cUlI6ihLqAk68mCG9_1Imw0PaeSeXS81Wa9_Qg1AsVg2MbYI8CizBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0zBaTAYA1tQnMSXlndWhSQADAd93iNAJjKuKWbk6gAARtM0EeNxG-1NLkgNiiTja2JhYViyAYB97uDET8qzMloG6rh5nUZj3CV4Ffc2nkwKrxtDHFOdJWR9rcXZWIOiBDNnUtCzHrIpL4fZocBVjliUE-CyhhaMqHSUwbda2VCK7GNxAsxZaqa4WAcx7CWPpO8_exLs_A2qMl6vmghhQZVDrVMAvEJ1-LeQtFlxU8YQ54eDzkcFsM8Fi5se8B0CS0acfXMQyfEUMWYr03v-gYNgzk1qr4KPtSYpVb6CgkKS8MCFTAiVeyMcBTxMGZTdpnn1Xy0Fb1Go9xE4xsr1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llIo18UuFUw22m8cXq6pyyylHgFArR4vM-Z9HlKDumFd71I10-hb4stf7yIWy5uEr2goK3-MLAV_e04x05brOsWoeqjf3b1B8Vh87PAZ4gVjaq6rMp4COey56VxQfRF1MX0VKmam6GXtiJ8CuBA08nBooZ7oARViF0e14055OaXOB8QUiE-o-lC709NU3bXtnix3MHjTXo7mtHUh1q74_B-0aKXyts3doSj86lx7r_2YL33oKYFSwH4HTh4oDyIWMjJaQQbS6X8pQJpFI2KL0ZWhtRR2VdR0uBiGfwZ_qER2WEsqAyXaJuYZC0UffM8_qZtvc3MKpJgpK9MWpqpwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEdvI4Gta703M_PTa6bIrqjV1UT6Pe1SpKzIVy9Bb8Y9pfukeY-5qJZjC7mtTTwggJ_tBPqkaIeGzes2REGivcJuVoQvmbEb6OTMaRj9L5vSDV5oHateS-6RsmwGaEEpqFLZrW2uHqvnWniV0iFKnx-yBQlZakUu9C8-DSAoKE9lxravQ8I-QTiNg2OBuMaB7mgevp-ucLZG7Oqy6RUPgdhNaDrCszsN53y3nO-g0mNEtGzRQPjeBVqD9SRCfO7yb0NjfZ32ARHwsLQUNgI06-zHmA9wJTeOBmJOr1-eK3fl_wiZgO-lHQxZEMxkp8hYy6P-5gFv2wZ-hpXCT6lTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqZhK4z9JS8KGXBhbshCBsbCQ1f1p_0kYDMFUKHtGVHcqxiiP1wombWkDOeWKl0fxwnu2DiCY4rQVmXvmZtIMPZux9W_IZ_E2fuzvSxZbGGJUwiwL9Ru0V5WeK8ewPEuxaNUwfwvChQVSxsIzl0QJ6MsTAbfv3eKjpmJNEXgks3mEPt--XUmE3zTPOb4ajzBOh9Mft6nLkkGalw9zYegJfa4DBObe_axBRsgj5nAmN3-l6epIH2L3NpdJBI01sLARPgy1Dk6J2bq5NnFlDLQpeaOED6r4kEHcCnPjI2O4o0ublvVGsljac66btLZT3oZl6zRoYF-zPcYRbx8dLoQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnRoH6z25V5Egb3RVm0FqVoGOcc9t4kHhI8IiWRO_6sDaIF5Gl2uqe9bnx_4Hq21AL77l-6ajSjNj2KD3z-7N_MtrN_YujQXBpZcYBvrwpmqChLay5N9f-v-JZQ3-aS3l36cxsVvcDpyk54rw59953pQCyMTFXh2ONe6cER8TMQkiai8lBLpzrFKP5tAN4oPK1myX992IAcp7HNqPhgZsWyGNRwqBAKIBrczxnTu1KAS2FOsGpwK-gcP5c3Ti9vRtb6W1BgqtOMvIlKw0Ju4WlaQBZUvRjfsH2cE1FuNkJkVo_FTviM3Caap7AsGpNZOuNWXiNvZ5ebvxRoq2YpPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید حجت‌الاسلام موسوی‌مقدم، نماینده ولی‌فقیه در بنیاد شهید، از خبرگزاری فارس
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455163" target="_blank">📅 19:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a5d6e71f.mp4?token=sOPC5Bg04ZDuh_MQxQmIpa4--G0mcpj7y34Rq4UcQpM0EM1ikj6bwtvP2jj6BWOxpX3gW7OgfP4lIegHzqvAR0Lpgez-4y9Ratp2_ohF3cbNh2c6rl55hKg4UIwxsNTtDmTzjyIXZQPP6Z2l1PkJbdhlZtALAepaomJHFRb05PaN6dLEa8fShNoC_g19_3SQuR6BDxPv4nqcqa8QunZHeEieX12TEK53-bKb7JVHLfwl-x597ip61IcLTNllPymHgLNEdnjMaOv1H3AE3kIYeHGTJ2VUUpGFzjKPiNSNvP7nNF5Fpgx5wvkS0y2kB-Nnwx4D6XLq_Y-D59kr3FuCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a5d6e71f.mp4?token=sOPC5Bg04ZDuh_MQxQmIpa4--G0mcpj7y34Rq4UcQpM0EM1ikj6bwtvP2jj6BWOxpX3gW7OgfP4lIegHzqvAR0Lpgez-4y9Ratp2_ohF3cbNh2c6rl55hKg4UIwxsNTtDmTzjyIXZQPP6Z2l1PkJbdhlZtALAepaomJHFRb05PaN6dLEa8fShNoC_g19_3SQuR6BDxPv4nqcqa8QunZHeEieX12TEK53-bKb7JVHLfwl-x597ip61IcLTNllPymHgLNEdnjMaOv1H3AE3kIYeHGTJ2VUUpGFzjKPiNSNvP7nNF5Fpgx5wvkS0y2kB-Nnwx4D6XLq_Y-D59kr3FuCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باوجود پیچیدگی دیپلماسی پس‌از جنگ، ارتباط مطلوبی با کشورهای منطقه داریم  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455162" target="_blank">📅 19:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c87c18ff.mp4?token=pEDc2Wo649RMEgd7LS7UdW_JNvgJnnSqthFGsVhjAxU2eFQcFTFOrQt5aAHf6Zr1vbElvXhaxu-3G37Rz4oVsvMgMZfL9JAq0mHvVlHsb95nlYV9405wIVgm6Pt8GkX5fceQfjG2aTBWSge_7XmLZCIsUR63u3_pBGwLZlpSBCfKvovR8lTV1I_at0fgMsI7TajHYwCljKehPlF9Mz735rIETGLR6YmCrjxykUF3QiJqfTcTZHXJ2YF6g9JXQ8jLafInrcZ0NYfs1hNnIYOXrwu36-7WaTxYlpEb0z2bQZXPw5FYBG_C6yM6ih5R1dYqBNA1aqMeXq6Ia0o3svJakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c87c18ff.mp4?token=pEDc2Wo649RMEgd7LS7UdW_JNvgJnnSqthFGsVhjAxU2eFQcFTFOrQt5aAHf6Zr1vbElvXhaxu-3G37Rz4oVsvMgMZfL9JAq0mHvVlHsb95nlYV9405wIVgm6Pt8GkX5fceQfjG2aTBWSge_7XmLZCIsUR63u3_pBGwLZlpSBCfKvovR8lTV1I_at0fgMsI7TajHYwCljKehPlF9Mz735rIETGLR6YmCrjxykUF3QiJqfTcTZHXJ2YF6g9JXQ8jLafInrcZ0NYfs1hNnIYOXrwu36-7WaTxYlpEb0z2bQZXPw5FYBG_C6yM6ih5R1dYqBNA1aqMeXq6Ia0o3svJakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باوجود پیچیدگی دیپلماسی پس‌از جنگ، ارتباط مطلوبی با کشورهای منطقه داریم
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455160" target="_blank">📅 19:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0mvIz1JW9O0QuXUX3BJSDu58sjU0ccFmGa2lA-dZFbkmOpaU4AWvlYr64pYK6_i27nygHTaX2SIksFD9_nVM1ZM5TN3XOWvu2IDEorQuTsOXh_ZQ1FWsJG7Tp0heCpbnVbHvleTsfKPul0VOI38uJ1fVhT0VJMm0ckPXjKPWpIDwoq-lITmiFahU6Ej3Z6V3VcoFWYoRkZ-iUGUelYYBpl1eyZbuTuM2S827QNFtZmVsVI7Dv7ue_LG93o0-vS2J4Cn12k6hPnsIa7g1Ai8wHEUlo1ZFVCnF0FSS-yS5mJtWjizYGQwxOUAf7AY8HljZ73ZhTeMDllVYwtu_1GdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌برقی، سهم مردم ونزوئلا از پیروزی بزرگ ترامپ
🔹
قطعی‌های مکرر برق، پایتخت ونزوئلا را برای نخستین بار در هفت سال گذشته در تاریکی فرو برده و مردم دست به تجمع و اعتراض زده‌اند.
🔹
ترامپ یک ماه پیش باز هم مقابل دوربین گفت که ما خیلی از ونزوئلا پول درمی‌آوریم و این «حق ماست که این را داشته باشیم».
🔹
حالا فایننشال تایمز می‌گوید که واشنگتن از فروش نفت این کشور چیزی حدود ۱۳ میلیارد دلار درآمد کسب کرده است اما باوجود وعده‌های دولت مورد حمایت آمریکا در این کشور و واشنگتن، صدای نارضایتی مردم بلند شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455159" target="_blank">📅 19:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC47ZJlgX-jXobWGLdKAjbgOI85x_8pqjpS47Ke9eZPjzYmeQJyfU3svFvb-IS4Y5m3bUsQ-V90kwdTewUDXmQ-TsxmRHEwfcs0GtuZmxejXR0rrSBR_90AvXwQlSxjli3aQfjlZcjlv825rOsv9oDVW5ZFOdwyNHaG6grRcbWMylOW3eNGDXXydM02YDxh7-4H2Gag9KPd-ZF9JD4Nia1nTBJlRdcXRyZ8u0myv3uZssFMLol7NL8THxC_muljKHyIVXMWhIaRrAdKWkUsjKewntWCZeSgnvwUbpDAsslfxFcSQRX6aSSlP8ESFK_x9wo0arQOhYJ3hRgh0t4W2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاچهٔ ارومیه جان گرفت
🔹
شرکت آب منطقه‌ای آذربایجان‌شرقی: حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است. …</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455158" target="_blank">📅 19:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85c2b1087.mp4?token=gN5BpD2yjRVX4khkeycqBz_7HWwn90v0lHg7ZcmpaXP6Ija1Ox4gwG3z9zMhGF35UVIYcBHNXhAPv_hp0xi_hkndFa6MIl6Fcotny1hngry0n9NRvJeYyje5PIbLrojl1U6b6TCyibMg2ZOKch12aoiaRYD8AbPBkk_50P79FGFWSSQg6voAd5wxBWYfQ3tBRbYaIdh6ecaQGD-8z0bGfi4UtfRkDVvj8998amI2Avd_wTUmt98nNr_SEc1WG0LMwp3AMlo1hhwyqjfSmjO55nGSXPFgHN6B8RXK6NY9OjuoAKrb_2GWyVfAej66iHKf2DNMiOSItjYr1U1a6lmgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85c2b1087.mp4?token=gN5BpD2yjRVX4khkeycqBz_7HWwn90v0lHg7ZcmpaXP6Ija1Ox4gwG3z9zMhGF35UVIYcBHNXhAPv_hp0xi_hkndFa6MIl6Fcotny1hngry0n9NRvJeYyje5PIbLrojl1U6b6TCyibMg2ZOKch12aoiaRYD8AbPBkk_50P79FGFWSSQg6voAd5wxBWYfQ3tBRbYaIdh6ecaQGD-8z0bGfi4UtfRkDVvj8998amI2Avd_wTUmt98nNr_SEc1WG0LMwp3AMlo1hhwyqjfSmjO55nGSXPFgHN6B8RXK6NY9OjuoAKrb_2GWyVfAej66iHKf2DNMiOSItjYr1U1a6lmgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری آمریکایی به یک اسرائیلی: دیگر نمی‌شود از شما دفاع کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455157" target="_blank">📅 19:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbbd8f7d2.mp4?token=DjJJUrR1-92LauQw8gHpVzJDrcKI7SM9IHPN_ULNC6NHv9hJM-HMV6FhyKJrhbMIoXAZJAQq7Sbv2W7f0cMTr5mWR2FBDAPJSZCbNOL2-NCbO6jtF8aMTx_A0BCHb8UZymR9rEYu3UD3qpuNn-xRYfgk6p3KDZ1GzCb_dTlfq7LjeiUc_jvChPY4uL4AiJ0WrPSbgZIH39AgR5r8p4sl0tCQ9dLuBP1pBC6s7SRt3g-rvSnZC5nvJU-PCeDJF2-nlLnvIrJsDF5odV-6IpfZ-CbEkPTsBJbszdxm2c6gOBylu1lelGPc5lhLAP-h5XlgkQSnKd3V3KFXx40oIluauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbbd8f7d2.mp4?token=DjJJUrR1-92LauQw8gHpVzJDrcKI7SM9IHPN_ULNC6NHv9hJM-HMV6FhyKJrhbMIoXAZJAQq7Sbv2W7f0cMTr5mWR2FBDAPJSZCbNOL2-NCbO6jtF8aMTx_A0BCHb8UZymR9rEYu3UD3qpuNn-xRYfgk6p3KDZ1GzCb_dTlfq7LjeiUc_jvChPY4uL4AiJ0WrPSbgZIH39AgR5r8p4sl0tCQ9dLuBP1pBC6s7SRt3g-rvSnZC5nvJU-PCeDJF2-nlLnvIrJsDF5odV-6IpfZ-CbEkPTsBJbszdxm2c6gOBylu1lelGPc5lhLAP-h5XlgkQSnKd3V3KFXx40oIluauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع سعودی: انصارالله یمن با ۳۰ موشک مواضعی در بندر المخا را هدف قرارداد.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/455156" target="_blank">📅 18:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c2022554.mp4?token=Zwbq_fh2v6PWF9KFB9OzcgZfNglFbsh9_B0toyt4fwADF1zOdLMjdaF2f6xmxonRgdk9C-htI4CsNP2HqVVKnEoRFu82n4b92LbBaQztBwXTaT0mfsy5DE2TV7Nut6ZGZUGOiwWd1ZDwZrf8dUSFCMiXiB30GP3K3weDSc9DWvQHzGVlGXG0cdQoz_3DvwzQs2yeW2Lj7cjcuiWpHi42tEBX8rTrkAMnrpFwzAJ7A-Dsk2ueSSMMMWFIZ8mOU-FZPlVIPZ6W0FQbq90Wh5krvKl6YcisRTRQWFMZWXY19dyrrSfa67blExwOLJstMr3jrtA5qVmGYSKNikC_CMcoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c2022554.mp4?token=Zwbq_fh2v6PWF9KFB9OzcgZfNglFbsh9_B0toyt4fwADF1zOdLMjdaF2f6xmxonRgdk9C-htI4CsNP2HqVVKnEoRFu82n4b92LbBaQztBwXTaT0mfsy5DE2TV7Nut6ZGZUGOiwWd1ZDwZrf8dUSFCMiXiB30GP3K3weDSc9DWvQHzGVlGXG0cdQoz_3DvwzQs2yeW2Lj7cjcuiWpHi42tEBX8rTrkAMnrpFwzAJ7A-Dsk2ueSSMMMWFIZ8mOU-FZPlVIPZ6W0FQbq90Wh5krvKl6YcisRTRQWFMZWXY19dyrrSfa67blExwOLJstMr3jrtA5qVmGYSKNikC_CMcoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان یکه‌تازی آمریکا در صنعت هوش مصنوعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455155" target="_blank">📅 18:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌ سخنگوی فراجا: در پروندۀ قتل رجب‌زاده تاکنون ۵ نفر دستگیر شده‌اند
🔹
سردار منتظرالمهدی: در پروندهٔ حمیدرضا رجب‌زاده تاکنون ۴ مرد و یک زن دستگیر شده‌اند که یکی از آن‌ها عنصر اصلی دخیل در قتل بوده است.
🔸
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455154" target="_blank">📅 18:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
منابع سعودی: انصارالله یمن با ۳۰ موشک مواضعی در بندر المخا را هدف قرارداد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455153" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ca6e5f69.mp4?token=YSJg0vaW-agmDKxIkHihIZDoPuUwF0wn1dcZEX6J5bssm7hxJk81rEcagtbAA4PHOAeV4DG2CCKzYP_fvumiT0x-N5wEJmgKW8W4I4XBxgfPGJTkNkpnZYuQj3C2F-za6pRfHRlUPP3BA0q5Ff6q6faJ6vtVNEaaGiK7_fgvDp_b0pLXMMdYt2exF-qZ9CHMGJH3W6CYiUlNQwwM4MpHnikLAzsyt2ckkNhlt1h_Pjd7NGgIhReCTHiM6VwWf4S_gJOO1KHnZ93PzF9TPsLbBIZKbzWXtDjh88Ow7r-n8t_I0xO7vBEQ7KZQu4m2p6BTqtJe_xIonSpgtr-4h4QDIocHcIrKGMPbXutWGdCY5bG_I6zxbmSW3j8BUEe4LC-1EtiWdsJW5-xNc3U4Fd6RnY27IwWSuptBGWqEjjsrrii8ZD8x9wQrAdz1PJJ3PFO5X17EVdK8geA1AYqCxGrUT3FeChzuVMyUIu6Ztm-23IPCgf6DyI9Mewqk1BSUmtJBCxrWH8Y4pLQE4D2QC3WNg0CG0wpHgkgImIRVAfRGNrwU3fZRVGgqQhQXvOgKlMzAKIXtLznxODhR0yrxt-An7XsaPdTwReNxI-tDS6m4VU-g8zqHghyMYzUwvLOTE9y4wE1Kx7rYc6FszIG65oPE4o9cJAGqq_dg9KyjbXdW2cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ca6e5f69.mp4?token=YSJg0vaW-agmDKxIkHihIZDoPuUwF0wn1dcZEX6J5bssm7hxJk81rEcagtbAA4PHOAeV4DG2CCKzYP_fvumiT0x-N5wEJmgKW8W4I4XBxgfPGJTkNkpnZYuQj3C2F-za6pRfHRlUPP3BA0q5Ff6q6faJ6vtVNEaaGiK7_fgvDp_b0pLXMMdYt2exF-qZ9CHMGJH3W6CYiUlNQwwM4MpHnikLAzsyt2ckkNhlt1h_Pjd7NGgIhReCTHiM6VwWf4S_gJOO1KHnZ93PzF9TPsLbBIZKbzWXtDjh88Ow7r-n8t_I0xO7vBEQ7KZQu4m2p6BTqtJe_xIonSpgtr-4h4QDIocHcIrKGMPbXutWGdCY5bG_I6zxbmSW3j8BUEe4LC-1EtiWdsJW5-xNc3U4Fd6RnY27IwWSuptBGWqEjjsrrii8ZD8x9wQrAdz1PJJ3PFO5X17EVdK8geA1AYqCxGrUT3FeChzuVMyUIu6Ztm-23IPCgf6DyI9Mewqk1BSUmtJBCxrWH8Y4pLQE4D2QC3WNg0CG0wpHgkgImIRVAfRGNrwU3fZRVGgqQhQXvOgKlMzAKIXtLznxODhR0yrxt-An7XsaPdTwReNxI-tDS6m4VU-g8zqHghyMYzUwvLOTE9y4wE1Kx7rYc6FszIG65oPE4o9cJAGqq_dg9KyjbXdW2cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شکوه طبیعت در زیست‌بوم زاگرس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455152" target="_blank">📅 18:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWA8jVm6nz2tJ6zIriQQs-lSIbp0ZBJeA7IszYpHrB9Mdn5fvvOiH8QcbT90YLVOSMD7y40AQDBED-ovYrh7Pp1YLgSp0NMdDaLnLexavmY3WflxeCxM_JJWBGsL_1vJ1vWERaj-76fXTEcqcoIJxy0vh0LORPzvuRnU87KBbz9_51fKRaL_qGQ3UrjnuNfJwuQrMAXc2xYIRXzshZJSUOnI9Ir9Sxi_tkLUle6EdlJf-EI3E-c3SNERNPELuS21cHka35ebwJu8YROyq48wfVDXnRaEo4PWj3N4QAiCZvdniQYmxuNj8DPkyDsgoUtYbUW-2NWX2MiOsGSKTL9kXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات متن اولیۀ طرح راهبردی مدیریت تنگه هرمز
🔹
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.  براساس این طرح:
🔸
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455151" target="_blank">📅 18:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455150">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxecfvbeiFF7GoqLfdoHqv102unNwBQUTTqiBep9lDzyxZEoT9jVXKTNxtIcMX_HNZxAHBENPMtd0AbNKUHHeYhwEcLx2DhFjsEGdRDvHA629yylDWl4-IDvAjdUUxrLo7812tIsO1eM3kNe9ZnxNiC2ICGqRfLDEsfKzU4_1F2YsbXEn4AJBTy0Gjh2zsgc0bdh8hj408UmF46mz0z11QR-zfL33_iypRGgNOuPUvVc8ac-5_YxSUjqDVNQKHEvCVf6HaqTXnshTJIBwtyFzBw7GljSXiHnenMCctYIOBOhU6iQr69MGV2Ay69bsQn42oDzs1noM4Nut1hALkL3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخصیص بیش از ۵۰۰ هزار تن ورق فولاد مبارکه به پروژه‌های انتقال آب، نفت و گاز
نخستین محموله ورق فولاد مبارکه در سال ۱۴۰۵ به کارخانه‌های لوله‌سازی پروژه‌های انتقال آب تحویل شد.
پیش‌بینی می‌شود امسال بیش از ۵۰۰ هزار تن ورق فولاد مبارکه به پروژه‌های انتقال آب، نفت و گاز اختصاص یابد.
این ورق‌ها پس از عرضه‌های متوالی فولاد مبارکه در بورس کالا و انجام تعهدات این شرکت در زمینه کف عرضه، بر اساس مدل فروش توافق‌شده به پروژه‌های مذکور تخصیص می‌یابد.
اجرای این طرح علاوه بر تأمین ورق موردنیاز پروژه‌های استراتژیک کشور، به تأمین نقدینگی فولاد مبارکه برای بازسازی بخش‌های آسیب‌دیده این شرکت نیز کمک خواهد کرد.
@farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455150" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455149">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKwswDugGQpw_VjwaVOejRw4XFU2gHDaR2xL2GXmw2smKmqUwECtcK-HVI_FZEwdU-JaEHDkuVMrUZjNpHpVSfSPd1OT18BnR7KmVN_2jYUb1dfkS0WGs5AM4yeoT17lpSjuDEGAYQd_7y-HV1u39ChwWODwTr6aiyGl5sNTEPUc0Wnb4I5mYY5PndEVNlpc1KXfjfNLFttO65pSwG-LjULxSk8obUwTrdmNVS4OOdXDcHhGM_v8Is7yCGee1uXSBNi7HlqBroAkM4qfGTF88sp5ge-kvomMHBAKFUixEzQH_hkaVKW9qxaq_GlFnqMuEsp8XyUT5lbY65U99ABauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شرکت گروه پتروشیمی تابان فردا (سهامی عام) با نماد "تابان" در فهرست نرخ‌های تابلو اصلی بازار دوم بورس تهران درج شد.
🔸
به گزارش مدیریت ارتباطات بورس تهران و به نقل از مدیریت پذیرش، با توجه به موافقت هیئت ‌پذیرش بورس تهران در جلسه مورخ 1404/09/12 با پذیرش سهام شرکت گروه پتروشیمی تابان فردا (سهامی عام) در بورس تهران، از تاریخ 05/06/ 1405، این شرکت به‌ عنوان ششصد و سی و هفتمین شرکت پذیرفته ‌شده در ﺑﺨﺶ "محصولات شیمیایی"، طبقه "تولید مواد شیمیایی پایه به جز کود" با کد "4411" و نماد "تابان" در فهرست نرخ‌های تابلو اصلی بازار دوم بورس تهران درج شد.
🔸
سرمایه‌گذاران محترم و علاقه‌مندان می‌توانند به منظور کسب اطلاعات بیشتر در مورد شرکت یادشده به سامانه اطلاع‌رسانی ناشران (کدال) و سايت بورس مراجعه کنند.</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/455149" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/455148" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455147">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ffc69a97.mp4?token=cajEFLJGP_5zH2QNZh81bdVK39qHQ27g402Z9jXoq4BtX246Q1WOvHkZCvhOD0oo_5Qcza3JrA-OnOee3lkakR4e0LDIoBtvIcgzgvjEtFp_co-GklG0wPdruJEzffECYVHzSRfmeMybxf3MuN3PgW-5MfSiw-3_J2k8VyFN5EjZjRG9K4zOtrafiJKwWPtjUpIoZBtmCBhGgvUEVAQG42MYAmL2KIiNtGCArYxsfsbqV8Gik32JHe0G1qTc3BHmjFY2k7TKMXKCEAW5kyDjWjN4hJeOerAOv-OyHT333Z_5Ju236zgGtbAVRsqAjArD6KslYP3TVf46USvUT2yI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ffc69a97.mp4?token=cajEFLJGP_5zH2QNZh81bdVK39qHQ27g402Z9jXoq4BtX246Q1WOvHkZCvhOD0oo_5Qcza3JrA-OnOee3lkakR4e0LDIoBtvIcgzgvjEtFp_co-GklG0wPdruJEzffECYVHzSRfmeMybxf3MuN3PgW-5MfSiw-3_J2k8VyFN5EjZjRG9K4zOtrafiJKwWPtjUpIoZBtmCBhGgvUEVAQG42MYAmL2KIiNtGCArYxsfsbqV8Gik32JHe0G1qTc3BHmjFY2k7TKMXKCEAW5kyDjWjN4hJeOerAOv-OyHT333Z_5Ju236zgGtbAVRsqAjArD6KslYP3TVf46USvUT2yI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت مشکوک یک هواپیما در نزدیکی پایگاه آمریکا در جیبوتی
🔹
یک هواپیمای ناشناس و سانحه‌دیده درحال سقوط به‌سمت پایگاه هوایی چابلی در جیبوتی است.
🔹
ساعتی پیش سفارت آمریکا در جیبوتی با ردیابی این هواپیمای سانحه‌دیده از مردم خواست تا اطلاع ثانوی از تردد در اطراف…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455147" target="_blank">📅 17:58 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
