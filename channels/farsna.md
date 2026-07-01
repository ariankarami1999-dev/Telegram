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
<img src="https://cdn4.telesco.pe/file/txYmQHHOu6jWbRhCp_AArcEg3lx8ScC8N7OsG_63nb_iwSVY1rDFcBqgB-7WW03NRRQ2CdVdQU0R95jwLCibiDr-PrQGKvA1PbK_sxzWOWcU54SJWSoMHaYRg6fjtmk_MYHbTOQ6LEPzvdOSq36Qo8mvrasTKjnx4ts62ydqV0FlzFAAgV8BTF3nQ5dY8oRl_zdAFrya3b94iEfulHWcZJD5x264H0B2Q88Yq4MNIrnhx8yibWqVUhijvJYT1ku3JH3XLzfjmuvoD17yjiZCmfbAI5crK6FizqKa6ppGu82v82rwV4cEL0N1ydGZLtHd5nDe3Owpvy9k3WlaEN2IJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-445780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy1wrhOmJoKUjgo8aycwddigioB_Wpl0P9hlf3LcxtD6cVWgifpiK801UjD0F1n0-FjLjOOJQu1AzmlIJrVBF7XzrNo69yF2uTwKkOQzu8sQMJORnAGxlkONqYyczo0-527Vv41mflcaOp0s_9-OjBLY3-XIhC7fYytCOZfN4P6sQKdIXZ0QA9_RW_ywYRb5igdG7JL-seZKulYQE4F7usyn60THlXCk91zUMhZ28EU6KQAj3RyHDmn1SYdmLYi4roHyk1BzKeHry26uuyRYhtu2WHknnYDzjJhDId_k2EHIWejlui79Y56OvTtlZN7WEM4lDK_Y0d1zFpNuXXMitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمزی، معاون شهردار تهران: طرح ترافیک در روزهای ۱۳، ۱۴ و ۱۵ تیر لغو می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/445780" target="_blank">📅 11:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qizl4cPjqn-gU71i4L0J1m2LhSdKnm9eUi0_aAMjSIqJaXMLqkgA3EqRkbvdtLeUezNhr_JwShQqv47aAuqhZ9sZMcD0vgzQkYZvn9Rq_aSRbiLM2fn1Bz_uBkyD2Lbi8pBFC7y7TK6sogH-piCUPuEpJB8fe1IJYhCToUzlFCk72W58VU6UkjrhdJb_HbOnqiB8gcQfagtT0ogjrpViZvDdSw2iXoon3YHm-l8OCiB2mSMHRiwmyAKI5EQ4hWeBFci5J0yH_RGWqvXkioY_evHXq0LPp323IbrJYGtsP2CTT3_7Zkbf91hG2iPi6_9dbJurcQCDp3ZNY3v6Qel6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر: عاملین شهادت رهبر و شهدای مظلوم ایران به‌سزایشان خواهند رسید
🔹
رسانهٔ شورای عالی امنیت ملی در توییتی پیام دبیر این شورا را در آستانهٔ مراسم تشییع رهبر شهید انقلاب منتشر کرد: مشت گره‌کردهٔ رهبر شهید در لحظهٔ عروج، نماد ماندگار دکترین امنیت ملی ماست.
🔹
پروندهٔ انتقام خون پاک خامنه‌ای کبیر و شهدای مظلوم ایران، باز است و آمرین و عاملین این جنایات در وقت خود که دیر نخواهد بود، به‎دست «عناصر صالحه» به‌سزایشان خواهند رسید.
@Farsna</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/445779" target="_blank">📅 11:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b07raI41WDUmE__AIT7pw68iG6PM2EaO27AalRLd6m_DXjtt6CTOOww1VpDncuHV8z36y6aknlFVZGxUauR-oWfpif8hS4aqjSgx2MxAArE5Dh_QS9-wI4oiLv8nvqO_qu4BFNhC0j0rJ12f7VuBW0jcejMZ562peTFnRpu2ZIyECydEzhLK3n-ZRnBWcx2r00pdrNvqaKkUNQ1CkjdJOPfRQpabcDOu4nxtFN-7SY-eABbcX51rvyGXM3iSNtX3tbW32q0yCwQnun2L3gqD1oWW-QszfCat8XCrw2AF2UmncNSY4YmV2W4c6GB3VFmARpGWKTtBKdD4dYPrT-sRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم سپاه؛ سرنخ یک روایت در بازی کال‌آف‌دیوتی
🔹
تصاویری از یک گیمر منتشر شده که صحنه‌هایی از بازی Call of Duty: Modern Warfare 2 (ندای وظیفه: جنگاوری نوین۲) محصول سال ۲۰۲۲ را به‌تصویر می‌کشد. در این صحنه پرچمی با ترکیب رنگ و نمادی بسیار شبیه به نماد سپاه به‌چشم می‌خورد.
🔹
البته استفاده از نمادهای ایرانی و اسلامی در بازی‌های ویدیویی به‌عنوان «تیم دشمن» یا «گروهی که باید نابود شود» بارها سوژهٔ رسانه‌های مختلف شده است.
🔹
اثرگذاری «کال‌آف دیوتی» تنها به فضای بازی محدود نمانده است. در سال‌های گذشته تصاویر و زبان بصری این بازی به روایت‌های رسمی سیاسی و نظامی نیز راه پیدا کرده.
🔹
همان‌طور که کاخ سفید در مارس ۲۰۲۶ پس‌از حمله به ایران، در توییت‌هایی کلیپ‌هایی از تدوین قسمت‌هایی از بازی Call of Duty و تصاویر واقعی حمله به ناو دنا، تأسیسات صنعتی و هسته‌ای ایران، لانچرهای موشک و... ایران منتشر کرد و موج گسترده‌ای از بحث‌ها دربارهٔ استفادهٔ ابزاری از بازی‌های ویدیویی برای توجیه جنگ به راه انداخت.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/445778" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH3f5xgoMMcapPGOmYpG3ruk8HXVGz_GGvp7c-j6B1MsgironBAxQo-IMhBbFkHeoMsUy0cJaBxt6CMYWzP6YfSrTt07IpIjyOVlR1jwknsd9FiJva5FGnlfsrOECL1iKb9v4p7Zb280n0_1vA9zm1ZvgdCW1JXKVsG3fvXYvqKrEkfte1KSriZcZLr4RRans4_9wAbcF-KWEpqrvlsN3lWKd1CLvvThDChuEVYZRAZX9G17zDw8W9gJFeYNGP-fDmlEGfcReLnY4dwcYA7pUO9jvA7J3wQNnO4Pf4yw1l-LYy6JgEEuvoWJkb4fz3rB2Q1hBQnX1s-I1PRdQuv9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروی تهران در ایام‌ تشییع رهبر شبانه‌روزی می‌شود
🔹
شهرداری تهران: تمامی خدمات حمل‌ونقل عمومی در روز مراسم تشییع رهبر شهید رایگان است و مترو به‌صورت شبانه‌روزی با سرفاصلهٔ ۱۰ دقیقه فعالیت می‌کند.  عکس: محسن ونایی @Farsna - Link</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/445777" target="_blank">📅 11:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445776">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBKu6x2QqgShwUhxgLOSCsTkGGtSHBNtFET-F6uq1ssrg20di-7mXnBAMgiZTy6JII7V6gpadZlN5_JqUkKTF9hjLtCA1vtV9FgmhkUyZ33NqVBufXccYnYjEp2OrHvzEIt5_46T0cbohipLw-or6jWFBONjnB8-N0Ffj65p1BzxMX5TFThGu5katLMKdeFJyI2lNWrHXr0Mtix623Z7LwOn_NHhZ265tWO3Yp72QfPvSu35WD61GZ3Xoj_9Grs4zia3AvhUmlBnkuh67MwAwFs3Q8C_J7qNodAYgrsQnMFMzeyS_cp4ExUbLzMcb6Qz-MnVmACMdgHJhVhyvrX7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول قضایی و حلقهٔ مفقوده‌ای به‌نام مدیریت اجرایی
🔹
چرا با وجود هوشمندسازی قوه‌قضائیه، حذف ابلاغ‌های کاغذی و توسعهٔ سامانه‌های الکترونیکی، هنوز بسیاری از مردم از طولانی‌بودن رسیدگی به پرونده‌ها و سردرگمی در فرآیند دادرسی گلایه دارند؟
🔹
آیا مشکل فقط کمبود قاضی است یا بخشی از مسئله به شیوهٔ مدیریت فرایندها، بهره‌وری و نحوهٔ ادارهٔ یکی از بزرگ‌ترین دستگاه‌های خدمات عمومی کشور برمی‌گردد؟
🔹
در این گزارش تلاش کرده‌ایم از زاویه‌ای متفاوت به این پرسش پاسخ دهیم؛ اینکه شاید مرحلهٔ بعدی تحول قوه قضائیه، نه در تصویب قوانین جدید و نه صرفاً در توسعهٔ فناوری، بلکه در
تکمیل مدیریت اجرایی
آن باشد؛ مدیریتی که بتواند در کنار مرجعیت علمی و فقهی، سرعت، شفافیت و کیفیت خدمت‌رسانی به مردم را ارتقا دهد.
🔗
گزارش کامل را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/445776" target="_blank">📅 11:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445775">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKLKHhyJSKda5wIdPj5xxRznxmSVsNO6E3ztnBXzwjkReHYss3Ax-osMQiJG3cXVK7g80h3MXi4J4a2x3WQMgbC0qp_Kzk3JR_xXpyKEfK0fuZ_LEEy7BDy0x2ALeWcygj9seuovzoNhjisguDGyB2p1KViOy_KrNvq4cZowV7expuCvZYij2ITOEt4fvB4xCoVAJ17-zxY4Y7JTMdR_nrsxQRazn8bvYJxNpMJxb7nkXSCnGssSDoB-c9j4eBjgHh2VUb-jhOpcTjBorAUAMdFVH5DM81YMslhKJQZ9nVKkLOwNhRD9ELVN_Di33JxbqbiRF_b_HLIllZ8Jrax88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد رعد: شهید امام خامنه‌ای شخصیتی یگانه در تاریخ سیاسی اسلام بودند
🔹
رئیس فراکسیون «وفاداری به مقاومت» در پارلمان لبنان، تأکید کرد که سخن گفتن درباره شخصیت شهید حضرت آیت‌الله سید علی خامنه‌ای، به دلیل جایگاه برجسته‌ای که ایشان در تاریخ اسلام، به‌ویژه تاریخ سیاسی معاصر دارند، از دشوارترین وظایف است.
🔹
محمد رعد، در گفت‌وگو با پایگاه اطلاع‌رسانی دفتر مقام معظم رهبری (
Khamenei.ir
)، تصریح کرد که شخصیت شهید امام خامنه‌ای در یقین، انسجام فکری، عطوفت نسبت به مستضعفین، صلابت در پایبندی به اصول، امانتداری در حفظ وصیت امام خمینی (ره)، بنیان‌گذار جمهوری اسلامی تجلی یافته است؛ علاوه بر الگویی که ایشان برای حکمرانی مبتنی بر عدل و حق، و تحکیم مبانی جمهوری اسلامی ارائه کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/445775" target="_blank">📅 10:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p29djO0a-gXA-obYiMZTNMOT9GPPaFZTJxxSx19GCbh0REC-ev7ixdGaeYBK7sJBIiTW-1WoIG1RYX_BaxUk_hM_FF_4wZLgx7hg6F0JoY0WED9fuifBIY8pPv4C_gkBnrES7LXbRgd7NGSiTtd4i3Ajfcuk23mxRc3QPL6s3kGLYGO_bhCt-7gDPa5TqxYM8VymLAlkPO1MmYzCagCVdNH0_O3xWh-UYhGBb6yHG0tcJUeZ87CYParJ5fdD2ts-evgPLvjP9EBWq3b-5mWULI8nAe5Egyifzwsw3PVd_lFLluZezAMqu0BQdXDreAZqeKsLmOjtXFWH_xgWdWZI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ۲۵۰ کیلومتر از سواحل هرمزگان را آلوده کرد
🔹
براساس اطلاعات رسیده به فارس، ارزیابی‌های اولیه نشان می‌دهد هرمزگان بیشترین خسارت ناشی از آلودگی نفتی در پی حمله آمریکا به ایران را متحمل شده است.
🔹
در بررسی‌های اولیه، محدوده‌های آلوده در سواحل بندرعباس، جزیرهٔ قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی، تنب‌بزرگ و دیگر جزایر و نواحی ساحلی هرمزگان شناسایی و نقشه‌برداری شده است.
🔹
همچنین طول خط ساحلی آلوده در هر منطقه مشخص شده و براوردهای اولیه نشان می‌دهد بیش از ۲۵۰ کیلومتر از سواحل هرمزگان تحت‌تأثیر آلودگی‌های نفتی ناشی از جنگ قرار گرفته است. البته این آمار هنوز نهایی نیست و با تکمیل ارزیابی‌ها ممکن است تغییر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/445774" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445773">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsaC6H37MxLZHQLKBYlk5mGERRTb8eGPtLBfT58ZW1EALugTqu3ePlrYojgcvyVoqmyyv-gxQLbh7Gjpngm3v2xj6KPSDzQ8VEteK6Xn9-o2k87ykvGEbz6hPaqUf_T7wsCCzxXaP6lkfHvb2jdoQgcfU5VC9i0YYV09Wvi6TQFUEJVrDnXt1PeAyiJnWhPG_jn7rMa-t1EPremNizk_DVFz6trpx0GXBrBtrvauUfw07GyTh8VT4ZVoPIp2BoA-XyjyFybp2S-wNQbWgqV3Nw668BP34nzLPPGIBKjpOgjiPwmVAwMIEP9bwT1Pz3x3XCmATvGd6ShXX4ySwpxT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت نام خادمین امام شهید در شهرزاد/ ۴۰ هزار نفر تاکنون اعلام آمادگی کرده‌اند
باقری معاون شهردار تهران اعلام کرد: ثبت‌نام داوطلبان «خادمین امام شهید» برای مشارکت در خدمت‌رسانی و انتظام‌بخشی مراسم تشییع رهبر شهید انقلاب که به تازگی آغاز شده تاکنون با ثبت‌نام ۴۰ هزار نفر از علاقمندان همراه بوده است و همچنان ادامه دارد.
داوطلبان در بخش‌های مختلف از جمله راهنمایی و هدایت جمعیت، انتظام‌بخشی، حفظ نظم عمومی و پشتیبانی اجرایی مراسم مشارکت خواهند داشت تا خدمات‌رسانی به شرکت‌کنندگان با نظم و کیفیت بیشتری انجام شود.
علاقمندان می‌توانند از طریق اپلیکیشن «شهرزاد» با انتخاب بخش «خادمین امام شهید» از شرایط فعالیت مطلع شده و ثبت‌نام کنند.
لینک ثبت نام</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/445773" target="_blank">📅 10:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7TsKz124aeHOztb6tTTbyy9sNB7MnpVVnz4oWnxABH14rb5Pp4HWPiEkaMlhGjr1M40dyrXIEpYf75zHJ55N3ZIckOiQ0xRwbn-KnzTjG_rADZL9WzF1idDPJrwb6Bk_XNRoiBxcS-QcA6lj9jm4_oDFbFD6rWscahrjQnqr5PruybC6BrJZ2YJeLODE1YFxtqv1ym--ZJBUoLWi9UV2d0mcf9hTXZlymG_qLhyM_HHgjdmejWJizp7t4mZavA8E-CW_IqGRIZz5iSwYt9opTqPOrf0LN7mUixP5v4XMIaEML9Rmca9RSEye63ZnyHknmcJg-bJP59cWsj2WQloHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/445772" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/445771" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4dbc6fa3.mp4?token=Ph9yH-ztgF7CDHWdnn5hXgn_G3UqfXCZMOjIXRBf5TwyP0SwmrcpVR4otVlVThRvxNpSV7xtbJtL3D8fx-U8FdqiCQBOQkV7gkG4Cgo5p-g_SkkWSRIjZXvu-bE9Fl1K-8mUGBY-XLBtVkLsKH2ZyI64Bxdgjf98Ws1Dzz0upd3GfSGemqP369aIQEDd-1L-SXPz9XUeH5UzsVhVuL0HF1T69vNddgWInfZYORRRLBcKYDLFMwPPpKlpcYl16Uqt1v6wIxko4m0X-kRMwH1wbtIbrXNQgnIiBRRmVv3DT5iOfXsa5qGWXicpF0bX8Gh06CUbYbswX7OecwSuRPAaQasetJAXcPwX6i54SeqYu0zQZPZdnnZ_1iDcMwjBLHs_rG-PgZdWe1xeNU-rtYP5on2Nz9Nx3px2j5U3MwKbsc5bLlq8v3p64E_Y6C1My8nMfQR3A4sN1MRCsq5oAve2eGt10n64Gpd6pjxTLTSYxR7lszBX3vYlc-GCaXBf7hrg6vgzqbfoKN-T_RBoHI93iZiC1IvqEYSsdnFQ5FdWBWevZFr1ZOknJbsCR3Jx_xQu05jUUa4YMyX4KOsUs7wiIl-7qcMn6AZ89LWOH9vFtbfc9b-iy9pprTgA8fa28MXxfAG_FwEpJI4ICsgzSYEpxd0FvVGVbMXCSBVyvQDOsTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4dbc6fa3.mp4?token=Ph9yH-ztgF7CDHWdnn5hXgn_G3UqfXCZMOjIXRBf5TwyP0SwmrcpVR4otVlVThRvxNpSV7xtbJtL3D8fx-U8FdqiCQBOQkV7gkG4Cgo5p-g_SkkWSRIjZXvu-bE9Fl1K-8mUGBY-XLBtVkLsKH2ZyI64Bxdgjf98Ws1Dzz0upd3GfSGemqP369aIQEDd-1L-SXPz9XUeH5UzsVhVuL0HF1T69vNddgWInfZYORRRLBcKYDLFMwPPpKlpcYl16Uqt1v6wIxko4m0X-kRMwH1wbtIbrXNQgnIiBRRmVv3DT5iOfXsa5qGWXicpF0bX8Gh06CUbYbswX7OecwSuRPAaQasetJAXcPwX6i54SeqYu0zQZPZdnnZ_1iDcMwjBLHs_rG-PgZdWe1xeNU-rtYP5on2Nz9Nx3px2j5U3MwKbsc5bLlq8v3p64E_Y6C1My8nMfQR3A4sN1MRCsq5oAve2eGt10n64Gpd6pjxTLTSYxR7lszBX3vYlc-GCaXBf7hrg6vgzqbfoKN-T_RBoHI93iZiC1IvqEYSsdnFQ5FdWBWevZFr1ZOknJbsCR3Jx_xQu05jUUa4YMyX4KOsUs7wiIl-7qcMn6AZ89LWOH9vFtbfc9b-iy9pprTgA8fa28MXxfAG_FwEpJI4ICsgzSYEpxd0FvVGVbMXCSBVyvQDOsTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارشد صهیونیست: باید غزه را کاملا فتح کنیم!
🔹
وزیر دارایی رژیم صهیونیستی ضمن مخاطب قراردادن نتانیاهو، خواستار اشغال کامل غزه توسط این رژیم شد. اسموتریچ گفت: «اسرائیل آماده است در صورت تأیید نتانیاهو، فوراً ۳ شهرک یهودی‌نشین در شمال غزه بسازد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/445770" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucjOv3vsfXojBKeGtkfpvBUCK3sFDm4bql2nbuMMH16X9_nqdQghhm2_XgBAdXo7GmvEqLx_rE0yDnwB8gzV3ccrSpjroysoPRRjd3mYqnTKVLbQPPwEz0OyiJmqfr4SG_aN2LuvuJO8xFg7i74LtuwQuDQ7UwXxQfW-9d7e29vrVaDUme7xqRdvIHwa8NP1L6PCj-z5ZihkmpLNErh8m8s640sbN-da08QDDpUth22iDUC4XtSfTEot0--F7KXN1yvUKsW-IKwdrOqQ7JM_rwIZCSgM4oD_65z9MPhVkbIy0jwer1AMaiWQ8R2skatSd3gfqh_ev1eKe7SLEIwf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک پلیس در پی ترور ناجوانمردانه در سیب و سوران
🔹
مرکز اطلاع‌رسانی پلیس سیستان‌وبلوچستان: ساعتی قبل افرادی مسلح به‌سمت مأمور انتظامی اهل سنت و از قوم بلوچ که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی که ستوان‌سوم محمد پلنگی به شهادت رسید.  @Farsna…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/445769" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">استان تهران در روزهای ۱۳ و ۱۴ تیر و کل کشور در روز ۱۵ تیر تعطیل خواهد بود.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/445768" target="_blank">📅 09:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه هرمزگان: صدای انفجارهایی که از صبح تا ظهر امروز در بندرعباس شنیده می‌شود ناشی از انهدام مهمات باقی‌مانده از جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/445767" target="_blank">📅 09:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fts8RkTT4KjgFor9dxW6866-aqkYhYzNbU6DW0YmeBdVDTNSNUaKbGCLL0kktg5QFWEbCDxev9y8zoTmcBrkwofjPaa4s3zQwNzv7HOa2_PfO0CklcxSfjjm1kcJ0wv_o88YVFbsSc0cCYelmsVSFouOgBHVfw-aRGtZRLaGOvkPPSZkgDov5hoLS3R3fjnCup_J9bQf5xwdloYA_6kKv-vrjiEID3Jxny4BVzikU2IykuLpTLMbQEEZc9STbUg7mTL0UxH1CLEGtB75-nD6ErG35bOSjLgh7gcDdoJqpFbCUQAi-daCkTq55NFeYwLA8Iz8D4NsP2rg8nnjAJ4Vjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bigj7AIMAQ0m3lCm5fWBGm3U5_MA3QXGDPEeEFehNHUmGjJipj1BAZk0AYRsiAtssU2Gfy9qg9s2yK-jzkQG0CsKwml8OqS0SslGcKw5LkpPtGYRzDuZy57-rvLua1irYIL7sGpb8oaE6G54weY-Ez2nkKgwpSvnIcgi77yGj55W4r7mZ60VpYO2VsgFAnexk9SZB1Yf8nmmrj4ei9ySNxbTesLwAlJsKfpismY7Eb47vbmBLthe5doMqz3QxmqDaAWSkj9ZIcvUMEoI-Zi0i1J99DVDVw6WYKPqF4jBoMffUXb_wJpoI_wba1oXieOpyZuCUe6XOJFmkTMUOyprtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okNLuJOAcDZ9kWtLoi5JtQzCr-jbHSJf7jpoKCSd_wWuNZo8M6rLV7F7oswSMiupO1FpNM9QZmIugK1Fkf0zAQMlfQaipu2-gYzBVra1ny-Uwyzl53XjK8aMQz-yYz8ITbHNx2s9XaTo1sHLREfDOBnzPv3QqRWGw-qpHWcxsD_mhZY-NKUFVcdaJnOcYa-KzOJw_CAdLcaXZB3nwEO271tSgNrynF5LRYd8WnZWhKh0dHzKZqMqeY-xNSBPXff_Ex2gv-apCZy6429Du6RUMM4DnSna7TuNCO0NPunFUqX_FCuaGKq9yjwApcoHmLBrFyM_GnbJkmIX-xyuhaEUVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b7158ae4.mp4?token=jM0NKWIgWTdYckJYStci9lU8KE6CFaM-rJ7KS4qebcfFAYWUm84DBThNhN6SW41MfC0KVTYSgwA1Do42Yej8U22FwtO6On6nBP-oGjExAdRkof1n3xOf10Cwlx1erCQhwvA5OntAu1biGCaZmKKiZ0h_ZsfwWomLNl_gPeMdnP5tQXaY8MTq4603BqrKb-dJ-cyUT4vWfY05intHpgFTVvN6wjRNroCsoZ-3kBwq5GXuvEWeWqvyI6MRpljl1LAWh0fqXXsUV8kgVJxYblOBpTjfnOsOhMBn9Mjs006WO407QPApzWbvZzOO_nU26ChRXkC6qFFFSqP7fpHhIyknfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b7158ae4.mp4?token=jM0NKWIgWTdYckJYStci9lU8KE6CFaM-rJ7KS4qebcfFAYWUm84DBThNhN6SW41MfC0KVTYSgwA1Do42Yej8U22FwtO6On6nBP-oGjExAdRkof1n3xOf10Cwlx1erCQhwvA5OntAu1biGCaZmKKiZ0h_ZsfwWomLNl_gPeMdnP5tQXaY8MTq4603BqrKb-dJ-cyUT4vWfY05intHpgFTVvN6wjRNroCsoZ-3kBwq5GXuvEWeWqvyI6MRpljl1LAWh0fqXXsUV8kgVJxYblOBpTjfnOsOhMBn9Mjs006WO407QPApzWbvZzOO_nU26ChRXkC6qFFFSqP7fpHhIyknfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان سرخ ونزوئلا در پی زمین‌لرزه‌های اخیر
🔹
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد. بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445762" target="_blank">📅 08:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شهادت یک پلیس در پی ترور ناجوانمردانه در سیب و سوران
🔹
مرکز اطلاع‌رسانی پلیس سیستان‌وبلوچستان: ساعتی قبل افرادی مسلح به‌سمت مأمور انتظامی اهل سنت و از قوم بلوچ که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی که ستوان‌سوم محمد پلنگی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445761" target="_blank">📅 08:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n723TDr-vq1SVQQOxNmdH_G3LuurVKkE1wBr_Og1UXkoUH2ZsuSaAhF-z6cP-m8x7hfTYmr19XXhRWMfYlCulrWBJWHnv1dY9Idqr-VGuBOHgdolDwoAsrtS46qBOEqutLzG8ra3bUyWHiWCvAPrNAd6vIjVPkfy3dUudnHKLO2SJUvLAg47UK68xdecxF4B00a8qlb5XDNQ8BSl99dnUn_RN8-cpUzMjddP1_QSlf0nilv8YysVcVALK0cdhnF1GBB3q2v3TGTzU-LJvNNVgUqsFcyGoEUxFk8hu-BPA8ueigiiF56hCPBrXQ1XHlsuZCcXgywpURz73OkNuYeI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک در بهترین فرم خود
شاگردان اگیره در نیمه اول کار را تمام کردند
مکزیک ۲ - ۰ اکوادور
@Sportfars</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445760" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7ppw1rWSzlyPJSSeDIjB35ZllyI7dzrgDeYX3MSECitFJlP4w_ebEcPMyVg2l1gsUFRrg_pYKlsIUd61qDyond4sNC7cdsYulLQ6hQACTXeGjIql_QJycCyDF0glZwdlIFUorIFMhefWiikgkUGM1iUsqnEaybjuugY9zO_T6-wLAVlA43ZakRo5bGjqnyefaMtDneIDNkDGB9RBr5Eq9pvFco-kJuAR0AOL11dS4XEY7eBFrZziqrP6r_4b1Szp7m4O28kjQAuY4ftV2BJ5pVZGvkwBS_zIVOmv0aJ5uP8IczPoA7j2mBuN17XDMO_8Y_EApL1G24aXZL0L8MDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی ۸۰۰ تخت درمانی در محل وداع با رهبر شهید
🔹
کمیتۀ بهداشت‌ودرمان ستاد برگزاری وداع و تشییع رهبر شهید: با پیش‌بینی ۶۰۰ تخت بستری و ۲۰۰ تخت پشتیبان در بیمارستان‌ها و مراکز صحرایی، تمهیدات لازم برای خدمات‌رسانی به زائران پیش بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445759" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4Mj-Zf3tk0_74e3XjkkagB0VNcYqaZTw88jdxlnQINNPka7jp9r2NefAex9TvtJ8tGvwVeTstQP1JNbC_6KBalo5nDkHru__gScCIm7YcFr02Hj4x4wkn9HYLpZs2iVOsCESn-AKDKzrVAEjMeBmwHE_E_fuEylmQDZHe894iHvJ9S3ZhUmd48Wrh4ZWjNJYzW5wxLcX-F_r9NSfT8ZYuqnmXTpRkbEz32HZHBpksfMMlJf1aJlEem2wnpm2buv2KMy18tr5JcPKXuHHD0ib7aeHkQBHBJnk6q2HiuhZwVeYfqVSvJ8bT18qnn2YtKlnBnk9k1iOkg9sxTEXVJyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیمیل به حرف‌هایتان گوش می‌دهد
🔹
گوگل پس از معرفی «جی‌میل لایو» در کنفرانس توسعه‌دهندگان خود، اکنون آزمایش این قابلیت را برای برخی کاربران اندروید و آی‌او‌اس آغاز کرده است.
🔹
این ویژگی با استفاده از دستیار هوش مصنوعی «جمینای» امکان جست‌وجوی ایمیل‌ها با زبان طبیعی و دستورات صوتی را فراهم می‌کند.
🔹
کاربران می‌توانند سؤالاتی مانند «تاریخ سفر بعدی من چیست؟» یا «سفارش اخیرم کجاست؟» را مطرح کنند تا جمینای پاسخ را از میان ایمیل‌های موجود استخراج کند. این قابلیت تجربه‌ای مشابه گفت‌وگوی زنده با جمینای را به داخل جیمیل می‌آورد و قرار است بعدها به برنامه‌های دیگری مانند اسناد گوگل و درایو نیز گسترش یابد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445758" target="_blank">📅 05:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7103294b05.mp4?token=hUCm7LfU6w4PTBLm5mQlJgyPw510T9ks899uTSiBhlDaOX5-1Y8RJpUwRrGOThAtj19pPrWkF16BYmZmof3NoR8_O0nGwVPpmKhjb_muEaOCVAacaMAp9sr0zR87TNQoR5xWm6GRBx4kKMl6boQ_xlEDKtDtMl_IuI4z7hBfgCFw4KzbgAlza2KZifL2IxD1KK5IHXYlOXpyuNb5Z9ujAAb5KD4_hWWL_NWlLZkFi2_pRCEnnnRemR0W4sfBPXNjcH1fvMNCJBiWauewyQRy1E57lSCOX1g9_zmocORhr4YLjMXFhd3jdX8kVtbmJvv2xs7iMw8LASH-Vu19hQvYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7103294b05.mp4?token=hUCm7LfU6w4PTBLm5mQlJgyPw510T9ks899uTSiBhlDaOX5-1Y8RJpUwRrGOThAtj19pPrWkF16BYmZmof3NoR8_O0nGwVPpmKhjb_muEaOCVAacaMAp9sr0zR87TNQoR5xWm6GRBx4kKMl6boQ_xlEDKtDtMl_IuI4z7hBfgCFw4KzbgAlza2KZifL2IxD1KK5IHXYlOXpyuNb5Z9ujAAb5KD4_hWWL_NWlLZkFi2_pRCEnnnRemR0W4sfBPXNjcH1fvMNCJBiWauewyQRy1E57lSCOX1g9_zmocORhr4YLjMXFhd3jdX8kVtbmJvv2xs7iMw8LASH-Vu19hQvYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گستاخی نتانیاهو با تهدید ایران به جنگ سوم
🔹
نخست‌وزیر رژیم صهیونیستی شامگاه سه‌شنبه با ادعای اینکه تاکنون دو بار جنگ را به ایران تحمیل کرده، تهدید کرد که در صورت لزوم برای سومین‌بار هم تکرار خواهد شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445757" target="_blank">📅 04:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1BwPMomXPe-ZtFJeeB7FTWSX5u1VYeX_cHk71jqIcrPQiInDeRHKKi36UjTp5fREl3gst--qYF3IAFyxo_XGfb74JWTJF4P4VpiTCxW4BgWUUrQ9oYtrQG8Nqk75lQgve562WMHLJf7HWT9w-fWa-Fy9ZIAoxRr-1LcFGWJsuu41eHYadjH3Y97wudSQjmIrKtcD7EYkUFjx883mUyouK9-zcnYS7h-bzsDl9viz8ltJ_s_cYuc_oSRGddLfnvvilurlfPGp2i0QHOrx_QtMtftWVFBZQNWFXzkhJP8lKCrOGrAdSXpGocdL1mgiQuT54z-S8AKJ78Qwc-VkrghIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار مکزیک و اکوادور به‌دلیل شرایط نامساعد جوی و خطر رعدوبرق با تأخیر ۳۰ دقیقه‌ای شروع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445756" target="_blank">📅 04:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e5ab27a5c.mp4?token=Pz4tvsk-_Y-8Qdovxvz5BmMl3pB11HwNF8q0Orf3Lzk39dlATqYkAWuJH4-1_yUFf46fdGRc2LQvYRoqqWCBBVnFGxknLLlc5l9tWiBK3hCWN3HlNWlDO71h83gcTqwsg9REUAevreJKMj8ewRConTTlQvcwyMZ4k8DfLH0VK5RYoc2HXap0sEWJiS4rHx1mEd8k6ayvxs_zICCOCW-HacqoAYnI-95JW6q5F9xFCZJHXe9iorXTEjoLom_9R-hTsagsNsNEfuBWjGhp2tsJSqqE9PHkshgnWt-Xb0sTPlEfwZZK_-78pohSq6TO6ftzoave0WHn4LEh6IBpfuQELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e5ab27a5c.mp4?token=Pz4tvsk-_Y-8Qdovxvz5BmMl3pB11HwNF8q0Orf3Lzk39dlATqYkAWuJH4-1_yUFf46fdGRc2LQvYRoqqWCBBVnFGxknLLlc5l9tWiBK3hCWN3HlNWlDO71h83gcTqwsg9REUAevreJKMj8ewRConTTlQvcwyMZ4k8DfLH0VK5RYoc2HXap0sEWJiS4rHx1mEd8k6ayvxs_zICCOCW-HacqoAYnI-95JW6q5F9xFCZJHXe9iorXTEjoLom_9R-hTsagsNsNEfuBWjGhp2tsJSqqE9PHkshgnWt-Xb0sTPlEfwZZK_-78pohSq6TO6ftzoave0WHn4LEh6IBpfuQELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کم‌کم به آخرین دیدارمان نزدیک می‌شویم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445755" target="_blank">📅 04:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88c09b130.mp4?token=kRBYyZQzyBmUoEFPEWNxc9CezsB97CJOOKINtdQMD5jDxqcC154opaWG2U1hSZZ0PZkJ2GqppTVL7s_0_9wtK1Dq_apci2RpPvgFhMtqZRn29F1EpFDaVDl4eFnTuOUcUNZDk_DjgSCr3n92zLa54rTvJK2KKLWNH-v2f8sPixA5RD_K99t4Qb3ZYpjzFakDr0dEtg3WG9CwdDp13H2x0adlmQJEw7C81oW9h0CoLKnXgq9XeHNreZiMAzQeCoqInuwlBEM78CWbYYMkr4F1VC5bt9WUyIDCJKAP3oFATpD6kiVbRaixzbWLJe988Xzt_wIIFMoTY5xDrQ6XjMYasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88c09b130.mp4?token=kRBYyZQzyBmUoEFPEWNxc9CezsB97CJOOKINtdQMD5jDxqcC154opaWG2U1hSZZ0PZkJ2GqppTVL7s_0_9wtK1Dq_apci2RpPvgFhMtqZRn29F1EpFDaVDl4eFnTuOUcUNZDk_DjgSCr3n92zLa54rTvJK2KKLWNH-v2f8sPixA5RD_K99t4Qb3ZYpjzFakDr0dEtg3WG9CwdDp13H2x0adlmQJEw7C81oW9h0CoLKnXgq9XeHNreZiMAzQeCoqInuwlBEM78CWbYYMkr4F1VC5bt9WUyIDCJKAP3oFATpD6kiVbRaixzbWLJe988Xzt_wIIFMoTY5xDrQ6XjMYasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف جدید اسرائیل به آسیب‌پذیری مقابل قدرت موشکی ایران
🔹
مدیر سازمان پدافند موشکی اسرائیل گفت که این رژیم در جریان جنگ اخیر، با بمباران‌های بی‌سابقه و مداوم از سوی ایران مواجه شده است.
🔹
به‌همین دلیل وزارت جنگ اسرائیل در حال انجام آزمایش‌های جامع روی سامانۀ گنبد آهنین برای مرتفع کردن معایب آن است.
🎥
فیلم: لحظۀ اصابت موشک ایران به نزدیکی سایت هسته‌ای دیمونا در یکم فروردین‌ماه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445754" target="_blank">📅 03:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBqXi-pevSTFX_634uy-olS5bK0Z7KdLINMZGvdmIoMvs_mgUy_Aq84chPMvihuP7VBKYmSTLJGy-wL9ReOS9A2jh6bZWn_maYPj_PmKhftXJ4VVtcSB6NrpxdqqLMHuxbhHHgwQEAfmtaJpslJxgkPrBClCpPk9XkTac4WtJ79r_QssxYo9xXwblfS1O9ude2KgP5HZVfGxr_t7LphZvZ9fixOtOaaPzG_-b7HzFyp1gilgbIDxkuHMo8zFMksQgZKOz2Reh9KKl1Q-85LQrkHRoplAQ69r01M6ThN9NBLW9qmAqTl7Y03kG1sahGhTNHIc5RceOaqNRZzY0StR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای محل پارکینگ‌ها در روز تشییع رهبر شهید
🔹
با توجه به ممنوعیت تردد خودروهای شخصی در هستۀ مرکزی شهر، شهروندان و مسافران می‌توانند از ۲۴ پارکینگ منتخب استفاده کرده و ادامۀ مسیر را از طریق ناوگان عمومی طی کنند.
🔗
جزئیات هر پارکینگ را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445753" target="_blank">📅 03:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utZ6vSijbQg2n8vm4Buc8d2ZyibI6V5vset_7vTBl9XMVPvrVhO-hUiMJsXa73xvbz6LumDQiiXRECp4_rnZVMvXq2uURBmQoj_dZlkV0Scd-uix8cEZjACzrNKXZN0z5PTwQAaS78DePlEz8hIcKiRW7mfBKla519d-sjH-hqavvH4AezpAARZt5ad7L9rK4TNzUf7uy63fUHigDDPgWl1XrBqVhFZ_bivn5usYdSKI7WBQwC0XbJdk76ROVLz_e46vgciK0paOZyfCcPygSI-piHIfx7cZedqMaOkcIl9IsMIPkeWMHU2RxOmn6MyFvQqi7NQXyFTRJZJGDy_Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه و یاران سوئد را زیر پا له کردند
چه تیمی حریف خروس‌ها می‌شود؟
شاگردان دشان رویای قهرمانی در سر دارند
⚽️
جام‌جهانی ۲۰۲۶
فرانسه ۳ - ۰ سوئد
@Sportfars</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445752" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جزئیات بیمۀ شرکت‌کنندگان در مراسم وداع و تشییع رهبر شهید انقلاب
🔹
بیمۀ شرکت‌کنندگان و دست‌اندرکاران، از ساعت ۶ صبح ۱۲ تیرماه آغاز و تا یک ساعت پس از تدفین و اتمام مراسم معتبر می‌باشد.
🔹
تعهدات بخش مسئولیت ستاد برگزاری مراسم، معادل دیۀ ماه حرام به مبلغ ۲ میلیارد و ۸۰۰ میلیون تومان، و هزینه‌های پزشکی ناشی از حادثه در بخش مسئولیت ستاد، ۵۰ میلیون تومان برای هر نفر است.
🔹
میزان تعهد درمورد فوت شرکت‌کنندگان یا برگزارکنندگان در طول مراسم ۲۰۰ میلیون تومان و هزینه‌های پزشکی، تا سقف ۴۰ میلیون تومان برای هر نفر می‌باشد.
🔹
در موارد نقص یا شکستگی عضو در طول مراسم نیز صرفاً پرداخت هزینه‌های درمان صورت می‌گیرد.
🔸
تمام ارائۀ خدمات از طریق شرکت بیمۀ ایران انجام می‌شود و شرکت‌کنندگان در صورت وجود خسارت باید از بیمۀ ایران موضوع را پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445751" target="_blank">📅 01:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
به گزارش منابع خبری در غزه، ارتش رژیم صهیونیستی درحال بمباران شمال‌شرق شهر خان‌یونس در جنوب نوار غزه است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445750" target="_blank">📅 01:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ماجرای قطع مصاحبۀ قالیباف در شبکۀ خبر
🔹
مصاحبۀ محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در گفت‌وگوی ویژۀ خبری صداوسیما پیش از پایان کامل سخنان او متوقف شد.
🔹
هم‌زمان، کانال رسمی آقای قالیباف نیز با انتشار پیامی از قطع شدن این گفت‌وگو خبر داد. این موضوع واکنش‌ها و گمانه‌زنی‌های مختلفی را در شبکه‌های اجتماعی به‌دنبال داشت.
🔹
براساس اعلام صداوسیما در پاسخ به پیگیری خبرنگار فارس، بخش دوم این گفت‌وگو قرار است روز بعد (چهارشنبه شب) پخش شود. به‌گفتۀ صداوسیما این مسئله در پایان برنامه به‌صورت زیرنویس نیز نمایش داده شده بود.
🔹
این مصاحبه که به موضوع پرسش‌های مرتبط با تفاهم‌نامۀ ایران و آمریکا اختصاص داشت، به‌صورت ضبط‌شده از تلویزیون پخش شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/445749" target="_blank">📅 01:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0af691b7.mp4?token=oKEJoxYSJXsaL8wbyWnNlFJzi14ctLdMTOdiB4VC0aHtISbxubT8CReC9h2TTw1M1fo43S8B99h17khB_4v3EB9_5WMOuwISjpopaKQ0CMP-YiealowmBA2GB4RXJEKfHkwTA4bVT05aG0jr8EWxXpamU4pgHvFNhwbojdC0arUFp3on-QVnTYGAsb5Tv0P9tLD1bShsZ9iIUrYr6t8KBPU3Cip-CNLLxkYy0HoYHcjZKmmSkXY1zGWXrrA5QTW9NVGHz6cwDW4eyUo7Hb9lRPwLcjW00S1fPPFfdQGiZhZKhwH3t0f5-BGHBlOPagq9Ggeg0X4ZcakhbAiv4LKJWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0af691b7.mp4?token=oKEJoxYSJXsaL8wbyWnNlFJzi14ctLdMTOdiB4VC0aHtISbxubT8CReC9h2TTw1M1fo43S8B99h17khB_4v3EB9_5WMOuwISjpopaKQ0CMP-YiealowmBA2GB4RXJEKfHkwTA4bVT05aG0jr8EWxXpamU4pgHvFNhwbojdC0arUFp3on-QVnTYGAsb5Tv0P9tLD1bShsZ9iIUrYr6t8KBPU3Cip-CNLLxkYy0HoYHcjZKmmSkXY1zGWXrrA5QTW9NVGHz6cwDW4eyUo7Hb9lRPwLcjW00S1fPPFfdQGiZhZKhwH3t0f5-BGHBlOPagq9Ggeg0X4ZcakhbAiv4LKJWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ورودی‌های تهران در ایام وداع و تشییع باز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/445748" target="_blank">📅 01:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrzzV1wFcXUfPZjvy5d4ja7ejoyggv6r1S2DLvSoR-F8ihrt6KPuo9Bxt2W6lqWSwqg3qSrBt0ZA2XglfhgqkhhFbMPECtufChkbRZfDbr5HpZfLhlaNw_7Ct10W-wJvz95-0XNzVG8JqtYhH7FF2HNzAGa4iZ54aZN-LOHWEgPxlqHoaI0TG2jcNYL6jV_ZWluFtyw_k3lBz5xpmdQdKqVpJ5NFexFudN8-rDqxSeBPbxNClVpUi1Bzkg8tnntVvQB7f7V2uRjomRg7wANaYwNZh8vHaYRgmizgGeAc_CogdaXpQ8t_UXKsYl0V9eiNZeTfze0iU6WbXuql2somwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر امام شهیدمان تاکنون نه به خاک سپرده شده و نه به ودیعه دفن شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/445747" target="_blank">📅 00:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۶</div>
</div>
<a href="https://t.me/farsna/445746" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۵ – کتاب آه</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/445746" target="_blank">📅 00:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGunk2IshTY_Nho1F9hyRkPxriPVK-06ajEtpKNu7SX3TRWOZBQeZJ6SctOx_GJlKLhjm1w97HnGZe1n7kCDKmepL0DuEcpJOp2fPJ5fjxZOpaGtkNO0dRrMc6TbAiv8nHIK8k9Tc8wUVWbKg1sal9hl8BKp3fNmrrOPB4yBodTxcDcm5oz4JiZC2ez2TzDhoX9sm6Z0-Bs9HtvfKecBszWIyZgelZRdq6eDGSyeT-So2QL1c_0XHISLHzo75qUeRupfyYA4WNWiTOR9fi3x62cJ4F0BUOOFe4j08wYQ5CWa-BfwVEcO1Mcb2LfmSe6vIXm6kDvlLGSBvJwr6ngNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین سخن امام
🔹
پس از شهادت امام صادق(ع)، «ابوبصیر» که از یاران نزدیک و نابینای امام بود، برای عرض تسلیت به خانه امام رفت.
🔹
در آنجا با همسر امام، «حمیده خاتون» (مادر امام کاظم (ع)) دیدار کرد. حمیده خاتون با دیدن ابوبصیر به یاد روزهای آخر عمر امام افتاد و به شدت گریست.
🔹
سپس حمیده خاتون گفت: «ای ابوبصیر، اگر در ساعت احتضار و آخرین لحظات عمر امام اینجا بودی، صحنه عجیبی را می‌دیدی. امام در همان حال که جانی در بدن نداشتند، ناگهان چشم‌های خود را باز کردند و فرمودند: «همین الآن تمام خویشاوندان و نزدیکان مرا جمع کنید تا همه بر بالین من حاضر شوند.»
🔹
حمیده خاتون ادامه داد: «ما متعجب شدیم اما دستور امام را انجام دادیم و هیچ‌کس از بستگان نبود مگر اینکه او را فراخواندیم و همه دور بستر امام جمع شدند. وقتی امام نگاهی به جمع حاضر انداختند، آخرین سخن و وصیت کلیدی خود را فرمودند و سپس چشم از جهان فروبستند.
🔹
امام فرمودند: همانا شفاعت ما [در قیامت] هرگز به کسی که نماز را سبک بشمارد و به آن بی‌اهمیت باشد، نخواهد رسید.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/445745" target="_blank">📅 00:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1daa516da0.mp4?token=LXtzIfT4jN5UQt7aebN6m4M9gxGhl6paNYTDM3Nf77pOmv-WtTDBiakae6HkDD3t4uLSTZNkiQkO0E3ebBfQW8xmP63fPW7cxLq0E52jiq2fUYcTSxYZbKE5AuNth7IvC8JFTbe1HxVf_Y1EfNXHlw7Jr-7bLXMlnul2wXDyR-L9FW5w6WiaL6685KjcFng4IkcQtSTHSljsVziP0u4EqDZ9bk3_nqaghdWVca-pfSbTi308Th_mgWUYnwjxeFXpq2E_1sTZ5mVvHWZO7PEeOiAGbDqnbXfqi1fE5iLmS_Sypts-FHddIr07acis1lzT7t6bYF6WKWnkSSirWr2dn1sfpQUfvWN1zf60XUtJ9taMn7ck9I6O93FN5REEL5OlDLNBPNgbPI99ORz9KrK30hnJww4UnDOMwrN0-SGfLpdqEbd5u2jaewIds0tk2alFx_BT7IOCA2AmaOY-Y3dwwtdnqGJb_9PXXhodCXiVKpSy_ix250fSgrcS27Mwq7GkeqhUTCIvNBybt3rfbqNQoeN6oUc3DhsTLfk3X_EZXdySvo_ziwp8te7VAJyzbCzb_rfsR46FXucut58Ip7kF_zjPl-xEiWHXV8tLaeiMG_sUmL5QELVqxtELuiOruvIz7BjD754_Aegw3FqiJC_cyK_chdIN76pOiBABU5ek9O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1daa516da0.mp4?token=LXtzIfT4jN5UQt7aebN6m4M9gxGhl6paNYTDM3Nf77pOmv-WtTDBiakae6HkDD3t4uLSTZNkiQkO0E3ebBfQW8xmP63fPW7cxLq0E52jiq2fUYcTSxYZbKE5AuNth7IvC8JFTbe1HxVf_Y1EfNXHlw7Jr-7bLXMlnul2wXDyR-L9FW5w6WiaL6685KjcFng4IkcQtSTHSljsVziP0u4EqDZ9bk3_nqaghdWVca-pfSbTi308Th_mgWUYnwjxeFXpq2E_1sTZ5mVvHWZO7PEeOiAGbDqnbXfqi1fE5iLmS_Sypts-FHddIr07acis1lzT7t6bYF6WKWnkSSirWr2dn1sfpQUfvWN1zf60XUtJ9taMn7ck9I6O93FN5REEL5OlDLNBPNgbPI99ORz9KrK30hnJww4UnDOMwrN0-SGfLpdqEbd5u2jaewIds0tk2alFx_BT7IOCA2AmaOY-Y3dwwtdnqGJb_9PXXhodCXiVKpSy_ix250fSgrcS27Mwq7GkeqhUTCIvNBybt3rfbqNQoeN6oUc3DhsTLfk3X_EZXdySvo_ziwp8te7VAJyzbCzb_rfsR46FXucut58Ip7kF_zjPl-xEiWHXV8tLaeiMG_sUmL5QELVqxtELuiOruvIz7BjD754_Aegw3FqiJC_cyK_chdIN76pOiBABU5ek9O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۲۲ حماسه مردم در امتداد سواحل تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445744" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28eff41b9d.mp4?token=b69Xp4Ua_3iTHd_ZURJfDqDVBOkbKkaSUP-5qWKZSzx9ChtPCgokkelBGWfKmDoXIiCko6-R4QtjT_Jg1lSP6Plvyj3Vrc0tboJ1XjHxbZTDJUaBR0Fl_8DgMeBpPCV-Fn1UKO8Ie9gmakqc6cgg9FmsMKUPmlW6AyLy_FtaDzoZgWYg23g8AMI5TseCee-MK4S2U_S-ZAOOZs4MlH8yDLhWlBXG__Hfz6RVyWJkPuw8Oxdhn6ZRnhY4K3VejaLnqiBuiIYDojl2eHIjrBME1_Ni8jaDTAe2_xvokShCazRMswnkDpWdG8-6DkkXjEWnGWOfVOUWiqFcrD3ZZrmEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28eff41b9d.mp4?token=b69Xp4Ua_3iTHd_ZURJfDqDVBOkbKkaSUP-5qWKZSzx9ChtPCgokkelBGWfKmDoXIiCko6-R4QtjT_Jg1lSP6Plvyj3Vrc0tboJ1XjHxbZTDJUaBR0Fl_8DgMeBpPCV-Fn1UKO8Ie9gmakqc6cgg9FmsMKUPmlW6AyLy_FtaDzoZgWYg23g8AMI5TseCee-MK4S2U_S-ZAOOZs4MlH8yDLhWlBXG__Hfz6RVyWJkPuw8Oxdhn6ZRnhY4K3VejaLnqiBuiIYDojl2eHIjrBME1_Ni8jaDTAe2_xvokShCazRMswnkDpWdG8-6DkkXjEWnGWOfVOUWiqFcrD3ZZrmEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
ما اهل کوفه نیستیم، اهل ایرانیم
🔸
ما بی‌وفاها نیستیم، مرد میدانیم
اجتماع مردم بجنورد در قرار ۱۲۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445743" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c345c6f0.mp4?token=JCfzkuCFWIHJU7JDsbeVh3yzyq9BxMHRGGNq_AWsCGVt-59qUb_XgyVnkd4N9hRC_l93YpJ2FHSJnXc0xghxOkK77JftrX8Pb3ZoBJNiz54exoNR23GLhj4komDluBpUDtsDES5Glv_tPeKcBidr5t_MLE1oLJzSU-uE75N72Ny07xvnp302JCBD59ofAWappjzaNZnAWo4EPW6W4ibXkfA4R1Ure1Vkrs1zvi46Nay7LPrYt88su3EVUh2WFb_5yPWNAKhCUmO4tXN4jESdlyW4oZqGo_q4_vGAjbxJWxJv0NdBYW1WVOQFnblcApx25zJDMrqN04WINt18B7lvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c345c6f0.mp4?token=JCfzkuCFWIHJU7JDsbeVh3yzyq9BxMHRGGNq_AWsCGVt-59qUb_XgyVnkd4N9hRC_l93YpJ2FHSJnXc0xghxOkK77JftrX8Pb3ZoBJNiz54exoNR23GLhj4komDluBpUDtsDES5Glv_tPeKcBidr5t_MLE1oLJzSU-uE75N72Ny07xvnp302JCBD59ofAWappjzaNZnAWo4EPW6W4ibXkfA4R1Ure1Vkrs1zvi46Nay7LPrYt88su3EVUh2WFb_5yPWNAKhCUmO4tXN4jESdlyW4oZqGo_q4_vGAjbxJWxJv0NdBYW1WVOQFnblcApx25zJDMrqN04WINt18B7lvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج قطار از ریل در آمریکا
🔹
خروج قطار از ریل در پنسیلوانیای آمریکا، پلیس را وادار کرد تا برای ساکنان منطقه دستور پناه‌گیری در محل صادر کند.
🔹
پلیس تخمین می‌زند که دست‌کم بین ۵ تا ۱۰ واگن از ریل خارج شده‌اند.
🔹
هنوز جزئیاتی از تلفات احتمالی این حادثه اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445741" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6276572559.mp4?token=VhKMMOtF4PWxPjGPeAPriENh9b064W9h8yrzW4cemDAx-0fnOPDwCFaF77lLcA1-C__8bkfPKDY5mOi_4OhsBMehWuUnBBYxAIqUgju2OM7Z2J3j3C0nGTjunlUv8cbWdnC4hTEhU5lNq5FezT48bLFbj2VObC6aYOjBbju6Ho-OeVDY8Ea45xoBlgIOnULLrt3VdlVBmxZEaY-1PHIeMbT6H4cCsbAU5v4K5RAJ-ZB2LruB4hc-EBXbGnDIEE-Tvw42lBPLICbhT83c0OuhOdvsMEEa33VcqWf6FmeswyTBNRe5Emi81QVlcC5IrLj-JvShHtUAD0COUVlI4ArlGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6276572559.mp4?token=VhKMMOtF4PWxPjGPeAPriENh9b064W9h8yrzW4cemDAx-0fnOPDwCFaF77lLcA1-C__8bkfPKDY5mOi_4OhsBMehWuUnBBYxAIqUgju2OM7Z2J3j3C0nGTjunlUv8cbWdnC4hTEhU5lNq5FezT48bLFbj2VObC6aYOjBbju6Ho-OeVDY8Ea45xoBlgIOnULLrt3VdlVBmxZEaY-1PHIeMbT6H4cCsbAU5v4K5RAJ-ZB2LruB4hc-EBXbGnDIEE-Tvw42lBPLICbhT83c0OuhOdvsMEEa33VcqWf6FmeswyTBNRe5Emi81QVlcC5IrLj-JvShHtUAD0COUVlI4ArlGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور در برنامه پرچمدار: هیچ وسیله نقلیه‌ای حتی دوچرخه حق ورود به نزدیکی مراسم تشییع رهبر شهید انقلاب در تهران را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445740" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg_H0umDyA5gs9IfeR7S45Db77ttHx_d25tnB0CuTEr0GgTEHd_F-nKSJRCsGiivhIif2Vxsivwuu6DCJxVZgMCsq8jnW0gv3ETRghogYXIl_y0kVc42QtTMA0WSankjBk94oENNdsI_Q8gcPI_zQrHWg6jW6eseSGf1F0EJadWi2vr5V0D90L-oIr_YItRiEq9HQq8_vqfZxZL3TRwZVU-I9-2axAns81FtNc0RGIi4gtxYh2vTRw161-Cq0CFM3wOnUlRYdNXg2yHUdqLvyfM0PtsqoZqg1dhn2nMTmUKdJYnkXy4WyOfB3MqoLnmlsLV65CAaOAqyxa3HCEZzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: عراق همانند ایران، درحال آماده‌سازی برای برگزاری مراسم تشییع باشکوه حضرت آیت‌الله العظمی خامنه‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445739" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=UIgpKVMBuxk4yUcNcvJyBha9XD6GF0k-wDlrcW-IV4jsHYSOvH0-7WOiMEy9rNzIFNrN5yC4Lxa_CUd8jIulc7CH03JM5CzQL5qXUyIoqXcIitYhPgIFj2WSAoXLK1JBCAegHaKBfBEv_C-TmDyn3dCseJYLHzoGJkE0W64x3OGYJrlYJDLFtLOmCl7-9OiARIJKTTXUjwFMfnXsQP3EKpZUUM-JJXbEkWSejnxWb9OdH5zfUn1X0FO9BsVtbd7u2e6gY4Pe4MsPEOYlcN7hF-okrfOFemQqMCIAL75-cB2LDngd8EKJmew8E5PSgiymIPhcQvDSehuxnrWV1XUN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=UIgpKVMBuxk4yUcNcvJyBha9XD6GF0k-wDlrcW-IV4jsHYSOvH0-7WOiMEy9rNzIFNrN5yC4Lxa_CUd8jIulc7CH03JM5CzQL5qXUyIoqXcIitYhPgIFj2WSAoXLK1JBCAegHaKBfBEv_C-TmDyn3dCseJYLHzoGJkE0W64x3OGYJrlYJDLFtLOmCl7-9OiARIJKTTXUjwFMfnXsQP3EKpZUUM-JJXbEkWSejnxWb9OdH5zfUn1X0FO9BsVtbd7u2e6gY4Pe4MsPEOYlcN7hF-okrfOFemQqMCIAL75-cB2LDngd8EKJmew8E5PSgiymIPhcQvDSehuxnrWV1XUN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رفع تحریم‌های نفتی انجام شده است و نفت را ۲۰ درصد گران‌تر می‌فروشیم
🔹
اگر آمریکا بخواهد بجنگد ما هم خوب بلدیم بجنگیم.
🔹
اگر قرار است ما را از فروش نفت محروم کنند هیچکس از نفت منفعت نخواهند برد. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/445738" target="_blank">📅 23:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujdfq0ey1EdBWr-sMQkNohlzkUVAlK6nsEHdWKbUszymh6MpqxwpWC91vEPI-7VFf842Ym9rKwqZrUcvsd6Npc2M2zQG4INCnl3km7CIgIxGCvbxPO0Rv3qAY8yUjXfbjRxgd_7MUBmGvm2TyPNnDpwB3FglmJNgQVQ3HgV0H2a0ZuBq0EZ6cE2Nty8yr5sNpVrBSXwIFJ7vDaduFgD7k7nbXGvtjB3ydHxyN3cSzBWX4hoXtMIkoreIEI3u3kZsF9YVcuBtCl0TUDSW1n_1OBSkHn4XXQ5QdVX3NRD7Y9NR4oMUBAHmOpEOhCe4v3iCzkcfbDLNmLHoeKIkSXVu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایکینگ‌ها به‌پیش!
فیل‌ها هم حریفشان نشدند
رویای هالند و دوستان زنده است
نروژ ۲ - ۱ ساحل عاج
@Sportfars</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445737" target="_blank">📅 23:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dccf52c2bf.mp4?token=RP1hAqi7NqjuTryBYxSzYd2T7yyy0kV2HQBozSRUe4XqqeGJqtih72Yx9BvTq3_2Fht_1FW03QdgU52-8JvUctAjmNNlq_uLL7BNYWwAqPIiiOHa7BzwF7ht0WFCuqWcO0kShAW7yvJzNq_XL5X4AGvGn2vn1U740fLeMYmnmhbNLdNcgshtQdWaxYS3dYJjOJicBSbC4Jcqzvd9lrkH9GkMWRZVWTiSIAlCvCJ3Bn-_UE6ytq8_rKqzirUtPpCc2Qc8yZkDl2QViL4My3K2oEk08ic8vkLEpR_lWeW8aHBxpNUd7s5qkf_oGvefw6FGOV57akbnm5b_4PjhJeuguQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dccf52c2bf.mp4?token=RP1hAqi7NqjuTryBYxSzYd2T7yyy0kV2HQBozSRUe4XqqeGJqtih72Yx9BvTq3_2Fht_1FW03QdgU52-8JvUctAjmNNlq_uLL7BNYWwAqPIiiOHa7BzwF7ht0WFCuqWcO0kShAW7yvJzNq_XL5X4AGvGn2vn1U740fLeMYmnmhbNLdNcgshtQdWaxYS3dYJjOJicBSbC4Jcqzvd9lrkH9GkMWRZVWTiSIAlCvCJ3Bn-_UE6ytq8_rKqzirUtPpCc2Qc8yZkDl2QViL4My3K2oEk08ic8vkLEpR_lWeW8aHBxpNUd7s5qkf_oGvefw6FGOV57akbnm5b_4PjhJeuguQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رفع تحریم‌های نفتی انجام شده است و نفت را ۲۰ درصد گران‌تر می‌فروشیم
🔹
اگر آمریکا بخواهد بجنگد ما هم خوب بلدیم بجنگیم.
🔹
اگر قرار است ما را از فروش نفت محروم کنند هیچکس از نفت منفعت نخواهند برد. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445736" target="_blank">📅 22:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4d6b8dc9.mp4?token=JG8Df4hw4yjVD5nBh85V7iGB4ES9QZrL4ylDA5J7X1NC7vbFv8tWQSxZHLmJNW2V1R9bnWaWEx2mbB7Doxhu8NxJ0wzKsOfzFRb8-IqJSCP7z9JwhwxtQBM1XDyUqPDO5CrS4y_zphTOBgcq8hfjzDEz0Bvw56nusyUfyX6wmEKvW7DhKW7P8hJiIlUniQMHR7GMjsDPXtxKWsh9hYby_tS0w01wOfNMTJ_flD5qFt5XGJJjGzO81ZhELlZGqVPvg-yNUK9uiIXIcX_Zg7bg28f99CxEMRnjVb9_c30OznRHqEZsLLH4po6r8GYZi-AMwDVUTA7Gpm3-hutwkU-6iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4d6b8dc9.mp4?token=JG8Df4hw4yjVD5nBh85V7iGB4ES9QZrL4ylDA5J7X1NC7vbFv8tWQSxZHLmJNW2V1R9bnWaWEx2mbB7Doxhu8NxJ0wzKsOfzFRb8-IqJSCP7z9JwhwxtQBM1XDyUqPDO5CrS4y_zphTOBgcq8hfjzDEz0Bvw56nusyUfyX6wmEKvW7DhKW7P8hJiIlUniQMHR7GMjsDPXtxKWsh9hYby_tS0w01wOfNMTJ_flD5qFt5XGJJjGzO81ZhELlZGqVPvg-yNUK9uiIXIcX_Zg7bg28f99CxEMRnjVb9_c30OznRHqEZsLLH4po6r8GYZi-AMwDVUTA7Gpm3-hutwkU-6iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود نه کمتر  نباید تنگه هرمز را به ضد خود تبدیل کنیم. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445735" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3b7ea635.mp4?token=j_w2KoBhL3ph15Le8yz6jok6n9v4gS64-DdEGVNAbvxxzcJkr52ZGGCV4ZoS91ha8Iivk0KoPSqNw1dQmDB2KmqWVwi3J0HaMcrJEsAPYKTFvMOBcj2G9fuc5syoHW3Wpw4ARhEocEzCE-kKPIlMF6bbfYiDed1zcoN1mpahv_9Z2RkSNWIJRntTOlu2T9o6Pjbbf6Ryd-xY4AWLcH71xCEscGPOdHqmh9S0lnCWMRMx1D-_-kOjk3OGRf6-jweYq2PXsoIO5O5s3wMeD0ihW0paHuDd13_Ug8zM-t_mnPblU3w5-s3nGVbKlFvpsHSISLXvaMfJK35pKywVrhahhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3b7ea635.mp4?token=j_w2KoBhL3ph15Le8yz6jok6n9v4gS64-DdEGVNAbvxxzcJkr52ZGGCV4ZoS91ha8Iivk0KoPSqNw1dQmDB2KmqWVwi3J0HaMcrJEsAPYKTFvMOBcj2G9fuc5syoHW3Wpw4ARhEocEzCE-kKPIlMF6bbfYiDed1zcoN1mpahv_9Z2RkSNWIJRntTOlu2T9o6Pjbbf6Ryd-xY4AWLcH71xCEscGPOdHqmh9S0lnCWMRMx1D-_-kOjk3OGRf6-jweYq2PXsoIO5O5s3wMeD0ihW0paHuDd13_Ug8zM-t_mnPblU3w5-s3nGVbKlFvpsHSISLXvaMfJK35pKywVrhahhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: به‌خاطر مشکلات سیاسی با من حقوق ملت را از بین نبرید
🔹
کسانی که حرف ترامپ فاسق را قبول می‌کنند یک‌بار حرف برادر دینی خود را هم بشنوند. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445734" target="_blank">📅 22:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ebe8f2d1.mp4?token=ZN2htlMAW9MqNgwMMAgvUwiR83MLglOxSTFQYVYSn20MltsioGzV4Vnipi0eS3nONtPOd7mfEueHu-OHSvZFZJ_oqSvoEx-KyA0mBj5lwIWT16KiaIpGaHdw2qEd8xaaFxGFE3DWqIxUCaq42d9MD04pknCAD_tG5zhLZchvQXCjOCkAfAV0wzx4PdSp4nLRk_Y_OEf3CCUFBonIK6NgSF_9W31HY2poUwBYOLs66-Z05yvaIerQnOwjcYKDJoEDieRPbX7VCRYtVDA8J8TA1e9mHbllqRfrl_yG1ha_lJG0jbO2kVk9XI6hik9phxursVYzcBolQMXv79BqBb9GHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ebe8f2d1.mp4?token=ZN2htlMAW9MqNgwMMAgvUwiR83MLglOxSTFQYVYSn20MltsioGzV4Vnipi0eS3nONtPOd7mfEueHu-OHSvZFZJ_oqSvoEx-KyA0mBj5lwIWT16KiaIpGaHdw2qEd8xaaFxGFE3DWqIxUCaq42d9MD04pknCAD_tG5zhLZchvQXCjOCkAfAV0wzx4PdSp4nLRk_Y_OEf3CCUFBonIK6NgSF_9W31HY2poUwBYOLs66-Z05yvaIerQnOwjcYKDJoEDieRPbX7VCRYtVDA8J8TA1e9mHbllqRfrl_yG1ha_lJG0jbO2kVk9XI6hik9phxursVYzcBolQMXv79BqBb9GHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: عبور از تنگه بدون هزینه فقط برای ۶۰ روز است
🔹
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445733" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=Rq4KIo8-O8takW76brYWqyt-jlk4gC3rgMnL9NpqwYqgnEuqtbDMqg487ILn-ixUzasx-epjqraP7ZQYvU-KQ6PI-n4JToLSgKLeekORIBxMMNXQaICr4u0Qp0Rnvjtkr7xMzOgW1F7WZhbN-jgCtRTmuMW0fthezpnvCB8Teeoy87c66MPRCGIqd4Fj95Y9w5Uev70Ib4cVUGx77wm-cGl6ASNMPUSLji85Tg1AUnQmlWcFROpeOQvtN8l8hzJsQIkoId7snOL2PZYwOY22nEmGU12dY2lMHVtYOl5IVkGIS4fVOAME_GFUouJKppnznE4hq3rV-8FyID5PxESEzGec9Z8Bekhm36NvpzG_KxXxF_PLinI4PDEvq0hKlvLaCFjrPNs9_fnnYT4Sua8_l0oixJvnEIwjAhH6oGHOTmh5gi3L84ZCBX21KUw403uzeASYCBeYdzZxz7KTSFNhiMPiJ4O4UQyZtLOwBjq5f_lYrEUxAQ7ZjV6wwTZI6i6ASIniRZ6VKkRCgyFwAue2vCnMrDUtaxaq4oHL_jIBeLkECgm7s_NhMdX1k-SyPhWF4oIW88AU6rxM_t8yob7PMtzlIAOiQu24Nd6bJmgPhJOSitnhZsJ9tIAfOZP9y20OQ6vV-iXY1kyHnfxKY5c-iLCnIeIz5zC-48miZqg-mSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=Rq4KIo8-O8takW76brYWqyt-jlk4gC3rgMnL9NpqwYqgnEuqtbDMqg487ILn-ixUzasx-epjqraP7ZQYvU-KQ6PI-n4JToLSgKLeekORIBxMMNXQaICr4u0Qp0Rnvjtkr7xMzOgW1F7WZhbN-jgCtRTmuMW0fthezpnvCB8Teeoy87c66MPRCGIqd4Fj95Y9w5Uev70Ib4cVUGx77wm-cGl6ASNMPUSLji85Tg1AUnQmlWcFROpeOQvtN8l8hzJsQIkoId7snOL2PZYwOY22nEmGU12dY2lMHVtYOl5IVkGIS4fVOAME_GFUouJKppnznE4hq3rV-8FyID5PxESEzGec9Z8Bekhm36NvpzG_KxXxF_PLinI4PDEvq0hKlvLaCFjrPNs9_fnnYT4Sua8_l0oixJvnEIwjAhH6oGHOTmh5gi3L84ZCBX21KUw403uzeASYCBeYdzZxz7KTSFNhiMPiJ4O4UQyZtLOwBjq5f_lYrEUxAQ7ZjV6wwTZI6i6ASIniRZ6VKkRCgyFwAue2vCnMrDUtaxaq4oHL_jIBeLkECgm7s_NhMdX1k-SyPhWF4oIW88AU6rxM_t8yob7PMtzlIAOiQu24Nd6bJmgPhJOSitnhZsJ9tIAfOZP9y20OQ6vV-iXY1kyHnfxKY5c-iLCnIeIz5zC-48miZqg-mSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445732" target="_blank">📅 22:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3065cc37d7.mp4?token=simAosgfJMFFsM5694FsORX9v2t1JtiRuGl7goe9pc4AidB4J_CVvgf3IKHbzosR5Qf2n3yKeD3Vke1rXRFxCTemT1xM7ULMuFijqAsULIrmk6FULS5EdrywLeOrrqDIZeTCXolBhX6_hoMFcN9aCCw93PrEfkEJt3n1gPlyeGg_RpNuF2xE9hQsgTuX2woQ8YuQE8-m-2PFlGPVrl1N-34ClJAGfMEHihT_j4HNijAHd-HP_v9K5JcN7dxUTtKCZu41pV97WSTjst88e4BulKesjj26NiveXKeYZI33X_PLNs1FlEcE7BWmbq9Mv04L17ie4lxcpz38wZGlBMbKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3065cc37d7.mp4?token=simAosgfJMFFsM5694FsORX9v2t1JtiRuGl7goe9pc4AidB4J_CVvgf3IKHbzosR5Qf2n3yKeD3Vke1rXRFxCTemT1xM7ULMuFijqAsULIrmk6FULS5EdrywLeOrrqDIZeTCXolBhX6_hoMFcN9aCCw93PrEfkEJt3n1gPlyeGg_RpNuF2xE9hQsgTuX2woQ8YuQE8-m-2PFlGPVrl1N-34ClJAGfMEHihT_j4HNijAHd-HP_v9K5JcN7dxUTtKCZu41pV97WSTjst88e4BulKesjj26NiveXKeYZI33X_PLNs1FlEcE7BWmbq9Mv04L17ie4lxcpz38wZGlBMbKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: محاصره دریایی آمریکا به‌طور کامل پایان یافته است
🔹
این اقدام نتیجه قدرت میدان و دیپلماسی است. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445731" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c7cdd6fa.mp4?token=GVh3gZe9P7NZ6WL9B6xnzin11Nf0VFIKwmIkSogGUdNtPvn_i_mwCO5XeQaqo0rS44EWXjFJGbfrHtgoH8NfksiKTzGTWkGUQ461F0Tc2x1HZGqzUmNqbIAe9_ddxRUkDYRskqsgEwKUbJFNSTeuYCPPUZWMpRDJwe6lksPaH4LVrC8BNjconFSGjbzF7kVYEdxdDvx1SImeWlunZkXErbO1jLx00MLRv3wwEtACHn5cQI7-2XxKV7fDonZkRtK5TYCm5wzUKD9bvhxBApM0MzcMCKi8W73pJ6Xo4LjD-mG9wVzMnBHhzC_2GZhjeR8MbTCEFP_yow21CRCgWW3vugcp2kW9qT75oEc2rpN8Z8K4N5NILmpKqYe85DlXBZXtJMhpDmGYmGAhOrHSu8i3M8F7c2FX8Cz2iauQqIqqohhOkPFf5tF0vc8L3mb2P6Nkn0vlsW15TfHfFwvp06O0drFrS_3nVO39qfcbRVTw_tjY_mLb75BSIpdcs2AmDwsx0n3U-CjPWGRDQTN7PiDWBSFzjCkAZjgoTW6cdsQw8Gb1Yz4Mrmqg-mJfr1G-Tqi7lSFjEzZlOacTJuuzXodLFE8P5LQthxSnYM5ujwG5zOvSWmunXDfuXYgJSDcwiDD1m0uDpYfd7BZ1q895RPHT11vK4q0P5t_-ql5QU7O71lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c7cdd6fa.mp4?token=GVh3gZe9P7NZ6WL9B6xnzin11Nf0VFIKwmIkSogGUdNtPvn_i_mwCO5XeQaqo0rS44EWXjFJGbfrHtgoH8NfksiKTzGTWkGUQ461F0Tc2x1HZGqzUmNqbIAe9_ddxRUkDYRskqsgEwKUbJFNSTeuYCPPUZWMpRDJwe6lksPaH4LVrC8BNjconFSGjbzF7kVYEdxdDvx1SImeWlunZkXErbO1jLx00MLRv3wwEtACHn5cQI7-2XxKV7fDonZkRtK5TYCm5wzUKD9bvhxBApM0MzcMCKi8W73pJ6Xo4LjD-mG9wVzMnBHhzC_2GZhjeR8MbTCEFP_yow21CRCgWW3vugcp2kW9qT75oEc2rpN8Z8K4N5NILmpKqYe85DlXBZXtJMhpDmGYmGAhOrHSu8i3M8F7c2FX8Cz2iauQqIqqohhOkPFf5tF0vc8L3mb2P6Nkn0vlsW15TfHfFwvp06O0drFrS_3nVO39qfcbRVTw_tjY_mLb75BSIpdcs2AmDwsx0n3U-CjPWGRDQTN7PiDWBSFzjCkAZjgoTW6cdsQw8Gb1Yz4Mrmqg-mJfr1G-Tqi7lSFjEzZlOacTJuuzXodLFE8P5LQthxSnYM5ujwG5zOvSWmunXDfuXYgJSDcwiDD1m0uDpYfd7BZ1q895RPHT11vK4q0P5t_-ql5QU7O71lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
قالیباف: هرچه برای جنگ آماده‌تر باشیم مذاکره برایمان راحت‌تر است. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445730" target="_blank">📅 22:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
قالیباف: هرکجا زبان منطق برای اجرای تفاهم جلو نرود با زبان زور پیش می‌رویم. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445729" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
قالیباف: تا ۵ بند اول تحقق پیدا نکند وارد بقیه موارد نمی‌شویم.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445728" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556de6fe10.mp4?token=gyTe4JKDc2w4uboHfZou0ObxCV1JQe9vNv5TXp_wGqWhHhXs2dzB6lwcObUqfvIpyc3dN6i8ErMDOIR43eo2mrTDlU_OtuIMf3rXtvYyEUR4hr50SgzW6ISZHJS0quFNiaXjDo9hhX4mGGQnghi39UEeEcoWlG0DA0t5L6QGLoXKgiMXE7WS8Ty4QIv80mfD3qcqz6XLUJsKXKToWm-n8XcdkmuaxmzDkMY1lrbWq4pf7Ls_cU5Oy2jXifQNJi3ocmc1jjIXnCT4DYB8ibNkk6RZso2eF1o_UDM9DyA_zRALEo1dWaVBpfrEVQ2NN68NsPMHXZoLDYlYAamP3GQxjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556de6fe10.mp4?token=gyTe4JKDc2w4uboHfZou0ObxCV1JQe9vNv5TXp_wGqWhHhXs2dzB6lwcObUqfvIpyc3dN6i8ErMDOIR43eo2mrTDlU_OtuIMf3rXtvYyEUR4hr50SgzW6ISZHJS0quFNiaXjDo9hhX4mGGQnghi39UEeEcoWlG0DA0t5L6QGLoXKgiMXE7WS8Ty4QIv80mfD3qcqz6XLUJsKXKToWm-n8XcdkmuaxmzDkMY1lrbWq4pf7Ls_cU5Oy2jXifQNJi3ocmc1jjIXnCT4DYB8ibNkk6RZso2eF1o_UDM9DyA_zRALEo1dWaVBpfrEVQ2NN68NsPMHXZoLDYlYAamP3GQxjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
قالیباف: غنی‌سازی حق ماست و ما مفاد ان‌پی‌تی را رعایت می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445727" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
قالیباف: اصلا سر موضوع مقاومت و هسته‌های مقاومت با هیچ‌کسی مذاکره‌ای نداریم. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445726" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
قالیباف: ضمانت اجرای تفاهم قدرت خودمان است
🔹
قدرت آفندی و موشکی ما اصلا قابل مذاکره نیست. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445725" target="_blank">📅 22:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
قالیباف: در آمریکا روبیو موضوعات را یک‌جور دنبال می‌کند و ونس هم جور دیگر دنبال می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445724" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
قالیباف: ببینید حزب‌الله و شیخ نعیم قاسم نسبت به تفاهم‌نامه چه موضعی دارند و برخی دوستان ما در داخل چه موضعی دارند.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445723" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔹
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها و شهدا در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445722" target="_blank">📅 22:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
قالیباف: ما به‌خاطر دفاع از لبنان، رژیم صهیونیستی را زدیم
🔹
در عین اینکه این کار را انجام دادیم اجرای تفاهم‌نامه را هم از دشمن مطالبه کردیم. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445721" target="_blank">📅 22:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
قالیباف: ما با یک دوست مذاکره نمی‌کنیم
🔹
ما با یک دشمن بدقول مذاکره می‌کنیم که هر لحظه که فرصت پیداکند علیه ما اقدام خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445720" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
قالیباف: تا ۵ بند تفاهم را نهایی نکنیم اصلا به مرحله بعدی و اجرای بقیه بندهای تفاهم نخواهیم رفت. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445719" target="_blank">📅 22:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
قالیباف: اشکالی ندارد که تلویزیون حملات به لبنان را برجسته می‌کند ولی این را هم بگوید که جنگ لبنان قبلا چه شرایطی داشت و ما بیش از ۴ هزار شهید دادیم. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445718" target="_blank">📅 22:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
قالیباف:در گفت‌وگوهای سوییس مهم‌ترین موضوع بحث ما با اولویت اول، لبنان بود. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445717" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
قالیباف: رژیم صهیونیستی به‌شدت با تفاهم‌نامه مخالف است و همه تلاشش این بود که تا می‌تواند آن را به‌هم بزند
🔹
تفاهم‌نامه سند شکست آمریکا و اسرائیل است. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445716" target="_blank">📅 22:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
قالیباف: الان اصلا مذاکره نداریم
🔹
ما برای گفت‌وگو به سوییس رفتیم. گفت‌وگو برای تحقق ۵ بند تفاهم‌نامه است و تا آن‌ها اجرایی نشوند، وارد مذاکرات نخواهیم شد.
🔹
مذاکره تا پیش از اجرای تفاهم‌نامه بود و بعد از امضای تفاهم، داریم برای تحقق ۵ بند اولیه که باید…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445715" target="_blank">📅 22:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445714">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
قالیباف: گفت‌وگوها را برای تحقق ۵ شرطی که باید بلافاصله اجرا شود یا روند اجرایی‌اش شروع شود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445714" target="_blank">📅 22:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445713">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
قالیباف: ما نسبت به اجرای تفاهم‌نامه مصریم
🔹
ما هم درحال گفت‌وگو هستیم و هم اگر تفاهم را اجرا نکنند آماده جنگ هستیم و عکس‌العمل نشان می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445713" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
قالیباف: بعضا می‌خواهند مدیریت و ترتیبات ایرانی در تنگه هرمز را رعایت نکنند و طبیعتا ایران عکس‌العمل نشان می‌دهد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445712" target="_blank">📅 22:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
قالیباف: آمریکا در یادداشت تفاهم متضمن شده که در لبنان جنگ پایان یابد و لبنان بر سرزمینش حاکمیت داشته باشد و ما دنبال اجرای قطعی این موضوع هستیم. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445711" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
قالیباف: ما داریم دوران گفت‌وگو را دنبال می‌کنیم برای تحقق ماده ۱۳ یادداشت تفاهم. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445710" target="_blank">📅 22:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
قالیباف: محاصره دریایی خودش جنگی غیرقابل وصف بود که با تفاهم برداشته شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445709" target="_blank">📅 22:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
قالیباف: محاصره دریایی خودش جنگی غیرقابل وصف بود که با تفاهم برداشته شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445708" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
تصاویری از آماده‌سازی محل وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445707" target="_blank">📅 21:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b237c53a.mp4?token=mGl-uFWIXuoCGYSZGGDzmplOepO9q9H92FeCqdW0oWnLab74cWzcTveETHSJjhgQdhUoLUtoDUGWKZGvAyrlHvX9Xm6Uv6U_O0tNgA-73Km_o_IBo4b4GdVQW9u136eFvR1wxGSf2aGds9l1XWFM93eOnlNFtB1Bg0w_0VaXUkZz_m9T1SfuQVueOalfFcmlaPKJx6sHxouuGX0lRrOr-QtQ8d1OGHZjeE8ymUOwdmi8jgKXvLcglAZCeionX-tUwnIkVFFi9UXaYBXBuu_TNWqkARSfWQ7ACPjyqr42YDIQ9W0-l5YN9BuFkc0Aop8F3tlwg3GHTV0Q_yNT-TOnQ3NDHdoEPE7SOvORCwRIUAw3lg491UyVih3kRnUYXgJkJjGeNcx6cu-4WCiAE2GaiOwqdPyUZk5bVQDgU18fGU69j63BG1tL0tGHm9u244eTAU0AmEJp8opPpDBqs_k81CPMn_JS4nXvqdXPIdWKuSNPuqbPD-erq7LuB92OdOhLsFPJHYSa6pRj7Sjk_0AKqsZfkPfwVtnQ4YTvAAgYA2zy77qUISbB9wTpJu18eqU8ukNpfL-ONAftbV0oe6tm6VyEL2m5qoMno5WJnJiX56oJh3pDx2Qogm8lRU7MTFZBIO8-wo-g-df6B9-BhQFlRHmuVO26XN_SwW6suH8JGWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b237c53a.mp4?token=mGl-uFWIXuoCGYSZGGDzmplOepO9q9H92FeCqdW0oWnLab74cWzcTveETHSJjhgQdhUoLUtoDUGWKZGvAyrlHvX9Xm6Uv6U_O0tNgA-73Km_o_IBo4b4GdVQW9u136eFvR1wxGSf2aGds9l1XWFM93eOnlNFtB1Bg0w_0VaXUkZz_m9T1SfuQVueOalfFcmlaPKJx6sHxouuGX0lRrOr-QtQ8d1OGHZjeE8ymUOwdmi8jgKXvLcglAZCeionX-tUwnIkVFFi9UXaYBXBuu_TNWqkARSfWQ7ACPjyqr42YDIQ9W0-l5YN9BuFkc0Aop8F3tlwg3GHTV0Q_yNT-TOnQ3NDHdoEPE7SOvORCwRIUAw3lg491UyVih3kRnUYXgJkJjGeNcx6cu-4WCiAE2GaiOwqdPyUZk5bVQDgU18fGU69j63BG1tL0tGHm9u244eTAU0AmEJp8opPpDBqs_k81CPMn_JS4nXvqdXPIdWKuSNPuqbPD-erq7LuB92OdOhLsFPJHYSa6pRj7Sjk_0AKqsZfkPfwVtnQ4YTvAAgYA2zy77qUISbB9wTpJu18eqU8ukNpfL-ONAftbV0oe6tm6VyEL2m5qoMno5WJnJiX56oJh3pDx2Qogm8lRU7MTFZBIO8-wo-g-df6B9-BhQFlRHmuVO26XN_SwW6suH8JGWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنان مهم حاج رمضان (سرلشکر شهید ایزدی) پس از ترور شهید نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445706" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0186d74ee7.mp4?token=BkA2hVwt3qNBc4vRPh4yJhW3NKsKIVaAChyX49AFQuSkPNCM8yHWL2byzEuWmbyvutjXDMpFJJtVNEx39cgQ7oBCl01DRJTVgdnnJ08Kvz1oOcgElU_4t3bfIxFQHWmQ-Hu0_R5Fgv7wzaa6Rcw9IJ70hblXmpl8lFdjQJYvx79-sAGHjFcTR70ylwO6-UqfGIYnFLAFb1Ya1movKtmJwA3Ytd6CTbYmKPZSuahXE0EKHuiv1XQxRvAniN61ZhZQowUXHiuSPSfeBbsB87dca-pAoQGqWmhU-tTgY2MUIGnUKkaz-aUrRE9_DcVgVDzXqrwR1w8THNrqO5Yb8P4TxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0186d74ee7.mp4?token=BkA2hVwt3qNBc4vRPh4yJhW3NKsKIVaAChyX49AFQuSkPNCM8yHWL2byzEuWmbyvutjXDMpFJJtVNEx39cgQ7oBCl01DRJTVgdnnJ08Kvz1oOcgElU_4t3bfIxFQHWmQ-Hu0_R5Fgv7wzaa6Rcw9IJ70hblXmpl8lFdjQJYvx79-sAGHjFcTR70ylwO6-UqfGIYnFLAFb1Ya1movKtmJwA3Ytd6CTbYmKPZSuahXE0EKHuiv1XQxRvAniN61ZhZQowUXHiuSPSfeBbsB87dca-pAoQGqWmhU-tTgY2MUIGnUKkaz-aUrRE9_DcVgVDzXqrwR1w8THNrqO5Yb8P4TxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداد عزیزی: با پرسپولیس مذاکره کردم اما می‌خواهم به تراکتور برگردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445704" target="_blank">📅 21:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجشنواره فیلم ۱۰۰</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJflfny4SBB-fAWSmYWGpTj7C4Jsaka9cNviy8kmt9B_N2Lz4awwQAcjPlnjsG6Hhy_o5D_KIndKgfXmm1dmT4qJtBct3eTDVZLojaQOF5I5-pbwBtfmFiabFewkJU8ETnsHPY9gOIPP_j30GJ6MSu23xAKxq6e5FAjhOXN4Ab45p-xNfnklHjGNfTzcEGfuyleIT9RINAhn4qbv7YMC8QlAOeMt9eDnbs2QQkDRQKxS4tNnthJIWCHocFjOGKGJ_5RQ1oVS7rmPyYjstQfV88hItBTEKe7ajIc05KOsot01Jx7wfIPxmvlbHxL6imgwR_PLvKk0quXpATpYuuj_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
|
#جشنواره_بین‌المللی_فیلم_۱۰۰
🔻
با انتشار
فراخوانی ویژه
، از
مستندسازان
و
فیلم‌سازان
برای
تولید
مستندهای
۱۰۰
ثانیه‌ای از مراسم
وداع
و
تشییع
«
#
آقای_شهید_ایران
» دعوت کرد.
🔻
این فراخوان با هدف ثبت روایت‌های هنرمندانه از این رویداد تاریخی منتشر شده و علاقه‌مندان می‌توانند آثار خود را تا
۲۵ تیرماه
ارسال کنند.
🔻
متن کامل خبر و جزئیات فراخوان را در
سایت جشنواره ۱۰۰
بخوانید.
🔻
پانزدهمین دوره این جشنواره به دبیری
#
محدثه_پیرهادی
، شهریور ماه ۱۴۰۵ برگزار می‌شود.
🎥
|
@filmfest100</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445703" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445702">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZJAKIOAJGbCxl6hEX_Xp8d6Rc0yduYsQ3WeckaWzs8WgbDjUb71KouEYSZGlEm8cpy9bRcN3MibGvclcGB6q9EHdxjmtOei1zr7sZPJxH3N0hrNq5prSx4WkxxfbJd6axNndX5P105S_vfDjBkL4pDatqLRqN3zI8UuVmpcOg5zDn1r8G21z803L8VJMjWjpo3kalDxXVcdwul-p8v_qQ5hdC8S7Du-YcBtZ3E6W6VyTXTfe94br51t2KlGJUc2O4ge3VBqnfY3rw8ynRPr3EbtgWgSPlSbAZHlQliCZmVx_HJkNFaKYu25QALXTT2y5FTi4G_qOKOdvQ43bNikLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/445702" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/445701" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445700">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594f590c2f.mp4?token=OVBAotb9hvDGvTPalL59E4yE61oBhriKvliWtQC-hwEi_mFMjNWg4nA-oyuG2_Gqbb-Yg2hVVSJZX8XXMfkave8GTBFqSUAvTMCABvDzMqEsAYgeSHRQH5F05qaZT1X0iff3ypzuCv1nqR7HDi0vRst9PN7pen1V9ZghB9CrLrzC8yIrrq225SU_04ksmPPZkDcjjfT3h15-DwD3f-RH1yuW1lUN4ZsNaK7lncMMD3O19VxBQjueB6ufVWwt1_f2roObquoV5sA8g4ZutHncHTjYzgrRxRndRVF-iDh5WUDpp3_VIKA-ec9s_Nu3-i76HgavIMqQqKXIDKs8sPG45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594f590c2f.mp4?token=OVBAotb9hvDGvTPalL59E4yE61oBhriKvliWtQC-hwEi_mFMjNWg4nA-oyuG2_Gqbb-Yg2hVVSJZX8XXMfkave8GTBFqSUAvTMCABvDzMqEsAYgeSHRQH5F05qaZT1X0iff3ypzuCv1nqR7HDi0vRst9PN7pen1V9ZghB9CrLrzC8yIrrq225SU_04ksmPPZkDcjjfT3h15-DwD3f-RH1yuW1lUN4ZsNaK7lncMMD3O19VxBQjueB6ufVWwt1_f2roObquoV5sA8g4ZutHncHTjYzgrRxRndRVF-iDh5WUDpp3_VIKA-ec9s_Nu3-i76HgavIMqQqKXIDKs8sPG45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر ستاد تشییع رهبر شهید: بیش از ۹۰ کشور، از سران ادیان و مذاهب تا دانشمندان، برای حضور در مراسم تشییع رهبر شهید اعلام آمادگی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445700" target="_blank">📅 21:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445699">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1623a210d.mp4?token=uCgHJgIihuktRrbP0YvIMgYZJ5ri5WayuqvL84VNSYwdkVFxSA5SsNamBVgkF4Ov3NFmKVIqq0MIBg7epLXgrRQsBqjrAjcLa4r_PsfEUUSuXNSIyMVuwk1OPi5uPmAgyz83f4-CygvAadF_wFhLnq4KRAeyasmdi367OGWrAR_FBUVptHwrruo-4vNWL8qcOvXjuDwkxwWjjo1D_dsED1R62FYJSdq6CunBORunD_ecUUpYl4nm6imgTWAlWsIGBHzaZOLjd-ybZAmyTkjPdcq8xc7MS-WHX1VTjPRx3d0nHMmMWtHbZOST5s4HrztR4BeTn0I8UtUslm1A6pohRVxIC23vdhQoA0Uy56xxkxEAA2ImN2iIBW5_aPdREB1tsAi28Sl6RjcPHckc9et6B79lXlnj4mWhMwxC7Yg8gveOfsOVIMspV21dI16qzz4Az6XEVprm2Ds5GiXZ1vCROH61zMNzK73x1t1YH3M_vug-Y6UQqmjviHrCXs1r5wnVvEYozMLQAQfSH07hFKUzPJJn62nzjouN8jbPhz8rIucHwXePz-PJQZlTJZsVlLEIcowVbJnwN3Jg9bGc53U9kb6mlLC74s5k5d0An1H48HU2wnT0Kq6aF8Ay9Rt84YQaF5hhEsMzxGNJ80w5S8TH5Qy8uwnBQtdL7S-r71YDqiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1623a210d.mp4?token=uCgHJgIihuktRrbP0YvIMgYZJ5ri5WayuqvL84VNSYwdkVFxSA5SsNamBVgkF4Ov3NFmKVIqq0MIBg7epLXgrRQsBqjrAjcLa4r_PsfEUUSuXNSIyMVuwk1OPi5uPmAgyz83f4-CygvAadF_wFhLnq4KRAeyasmdi367OGWrAR_FBUVptHwrruo-4vNWL8qcOvXjuDwkxwWjjo1D_dsED1R62FYJSdq6CunBORunD_ecUUpYl4nm6imgTWAlWsIGBHzaZOLjd-ybZAmyTkjPdcq8xc7MS-WHX1VTjPRx3d0nHMmMWtHbZOST5s4HrztR4BeTn0I8UtUslm1A6pohRVxIC23vdhQoA0Uy56xxkxEAA2ImN2iIBW5_aPdREB1tsAi28Sl6RjcPHckc9et6B79lXlnj4mWhMwxC7Yg8gveOfsOVIMspV21dI16qzz4Az6XEVprm2Ds5GiXZ1vCROH61zMNzK73x1t1YH3M_vug-Y6UQqmjviHrCXs1r5wnVvEYozMLQAQfSH07hFKUzPJJn62nzjouN8jbPhz8rIucHwXePz-PJQZlTJZsVlLEIcowVbJnwN3Jg9bGc53U9kb6mlLC74s5k5d0An1H48HU2wnT0Kq6aF8Ay9Rt84YQaF5hhEsMzxGNJ80w5S8TH5Qy8uwnBQtdL7S-r71YDqiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: خودروی حمل پیکر مطهر رهبر شهید به شکل ضریح حرم امام رضا(ع) طراحی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445699" target="_blank">📅 21:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0c47cca9.mp4?token=scaaltsMYNr0prHtK1BNg7T8Cdv6__htb4DN1D1a1c47B4iaEheyXr4IwvEXwXeZyWJR9BAMl8kvniUA1r4EMHah6Hj3wma-_WC8NMOA093u-uAQB53PbPhLIzx6KJ0muvA2IAhtAIB-G-88-tM_yAf3-Pe6_rSPsb79GrcMVE_roM4gvqIVxO7ja34CswuajpDYXJfb-3iVIwnSnlztla6Kl85rrOXK5ZfEIgPZJu-shd7mKSXTc9HfYPv7YcfV3sXiqWyh7ApnGBDV68BlI5F9NlePxL5L_7KZkYH0TcKLsNV2a8RHHT_bDpJNfckrz3n2zAbc-7eakyigsPbcJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0c47cca9.mp4?token=scaaltsMYNr0prHtK1BNg7T8Cdv6__htb4DN1D1a1c47B4iaEheyXr4IwvEXwXeZyWJR9BAMl8kvniUA1r4EMHah6Hj3wma-_WC8NMOA093u-uAQB53PbPhLIzx6KJ0muvA2IAhtAIB-G-88-tM_yAf3-Pe6_rSPsb79GrcMVE_roM4gvqIVxO7ja34CswuajpDYXJfb-3iVIwnSnlztla6Kl85rrOXK5ZfEIgPZJu-shd7mKSXTc9HfYPv7YcfV3sXiqWyh7ApnGBDV68BlI5F9NlePxL5L_7KZkYH0TcKLsNV2a8RHHT_bDpJNfckrz3n2zAbc-7eakyigsPbcJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور از تنگهٔ هرمز فقط از مسیر ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445698" target="_blank">📅 21:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445697">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5992c21f0.mp4?token=FN73ukmv2gHGXmksEjU-X9s8N5ycv4TQaJ-BnrO19UO4DW756SAq6re4DJlHakh3h1l2C9sARlHtrWM1hiu57uGuM1a8Ll2cwk-RVyqVx27b1sYw7grw3oC6wRORaAu_dIPmALSw2q9_qkmJO5sOu-AK_yntSVAGpirZdNdMUb5Et471NsPQUO2IekZXtJzorNI2TuzUhbHgnZlW0QNvdQ6M7epp2gk_d7lPz3YdMAqPA6Fb_L2kCPQz5UomaqG2jPVF67Rywaqw12yA3F0BC30XPEG24UT-Ll9LgMF0ppDUr4D3o6PmcAqKGoLcmJp6Sk_c6wxISYp5HnuCz2QZMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5992c21f0.mp4?token=FN73ukmv2gHGXmksEjU-X9s8N5ycv4TQaJ-BnrO19UO4DW756SAq6re4DJlHakh3h1l2C9sARlHtrWM1hiu57uGuM1a8Ll2cwk-RVyqVx27b1sYw7grw3oC6wRORaAu_dIPmALSw2q9_qkmJO5sOu-AK_yntSVAGpirZdNdMUb5Et471NsPQUO2IekZXtJzorNI2TuzUhbHgnZlW0QNvdQ6M7epp2gk_d7lPz3YdMAqPA6Fb_L2kCPQz5UomaqG2jPVF67Rywaqw12yA3F0BC30XPEG24UT-Ll9LgMF0ppDUr4D3o6PmcAqKGoLcmJp6Sk_c6wxISYp5HnuCz2QZMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم مهیای بدرقهٔ رهبر شهید می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445697" target="_blank">📅 21:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bd6576e5.mp4?token=GX8wkg_VrC1WRpwwyHI3ff9WlY2ildiN4dz8gXBhgWWhwpunSOYM_jGsW40jtNKnr8YHS0EaUcVP2KwdU2J7ijomLsDAxKzo8mtlrzIrHUYfOqyxzbvW4zldzhEMFi3oQVaef9CM2tnQQPPeYR4-yI0Yl4tei_Ue2NYuH93ewPe9Cd_G3iKsXbBtCkB-9rtZ5FrwyTiOyZ5YE_jrh7Lflj8UNchyk8U7Y9R0cixJisY3uBTzOyKM5yCIvbWk-kIKRmHQlT1fUrCpuDZkW5gKIvKnkhINpy1xFY9PwbWyS8r13wt1NG8B8jexu5TkteERFe3hCHFGcHwjNHUMaBHnSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bd6576e5.mp4?token=GX8wkg_VrC1WRpwwyHI3ff9WlY2ildiN4dz8gXBhgWWhwpunSOYM_jGsW40jtNKnr8YHS0EaUcVP2KwdU2J7ijomLsDAxKzo8mtlrzIrHUYfOqyxzbvW4zldzhEMFi3oQVaef9CM2tnQQPPeYR4-yI0Yl4tei_Ue2NYuH93ewPe9Cd_G3iKsXbBtCkB-9rtZ5FrwyTiOyZ5YE_jrh7Lflj8UNchyk8U7Y9R0cixJisY3uBTzOyKM5yCIvbWk-kIKRmHQlT1fUrCpuDZkW5gKIvKnkhINpy1xFY9PwbWyS8r13wt1NG8B8jexu5TkteERFe3hCHFGcHwjNHUMaBHnSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمادهٔ تشییع رهبر شهید هستید؟
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445696" target="_blank">📅 21:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c5c997398.mp4?token=TAkSggKjBjrL86iTCadbGhz9jPLinAsLtkS91mfUaCJtVilY_Ys05SNY_uhFWjysNP9QEDKCbDam8THffl-GvnRvKUdqpS4NiiH-2IpoupXMoriCYnCDBLdsjuSLUzq0ucUVrKCgyTCdZpK1jCW8fcmpJdgShdYSmXDIFtkHqIpDDIKDdV-Lf2ntkSKLKererf5oGYlcflQVruTBakTONjiZcNuK_P0hRcUZd8yVSwNZoe1ZdFodrIds2rerOD5vuC0mp05gx0KGPuISGpVDVbKv3SYG60rgpiQrIfybUdUzBL4JJZ-QHITNrFGDByz-MtQzfyNt1ZX6tbDEexAEgAknXkK1ptHH9EF5nkPrnTwyF2AumCGBz3Y9c__OcjcZU91rf3txkIeY33ZJNdXyO6D9d-xO6LXWY-V5FmSG671oVxvq4ia8PwlGoYmrm25wYlRYUbhHkLW59SJTnyX7ETDBrcKmoCWtxpHb0Cm6hcJiKjgg7vfiPv9yFlEV73YgB24-tLQ_41b6LeU44IoLcvyF7IFOAT3UrajPeYVP_tzSggc6eA9bTc_KDtW7R-LXhCo4owBsRMXU77skt9lcc2HFb-wcXjxaMqw9L5meHP-8NyHLReVkk_B4OsgL2vlbZ_hfFoJjOB3vqcby8vu-PSLVU-cUp47TLFCnAs4dCBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c5c997398.mp4?token=TAkSggKjBjrL86iTCadbGhz9jPLinAsLtkS91mfUaCJtVilY_Ys05SNY_uhFWjysNP9QEDKCbDam8THffl-GvnRvKUdqpS4NiiH-2IpoupXMoriCYnCDBLdsjuSLUzq0ucUVrKCgyTCdZpK1jCW8fcmpJdgShdYSmXDIFtkHqIpDDIKDdV-Lf2ntkSKLKererf5oGYlcflQVruTBakTONjiZcNuK_P0hRcUZd8yVSwNZoe1ZdFodrIds2rerOD5vuC0mp05gx0KGPuISGpVDVbKv3SYG60rgpiQrIfybUdUzBL4JJZ-QHITNrFGDByz-MtQzfyNt1ZX6tbDEexAEgAknXkK1ptHH9EF5nkPrnTwyF2AumCGBz3Y9c__OcjcZU91rf3txkIeY33ZJNdXyO6D9d-xO6LXWY-V5FmSG671oVxvq4ia8PwlGoYmrm25wYlRYUbhHkLW59SJTnyX7ETDBrcKmoCWtxpHb0Cm6hcJiKjgg7vfiPv9yFlEV73YgB24-tLQ_41b6LeU44IoLcvyF7IFOAT3UrajPeYVP_tzSggc6eA9bTc_KDtW7R-LXhCo4owBsRMXU77skt9lcc2HFb-wcXjxaMqw9L5meHP-8NyHLReVkk_B4OsgL2vlbZ_hfFoJjOB3vqcby8vu-PSLVU-cUp47TLFCnAs4dCBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از شهید محمود باقری، فرمانده شهید یگان موشکی سپاه پاسداران در دسته‌های عزاداری عاشورای حسینی  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445695" target="_blank">📅 20:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9407c8629.mp4?token=Yd-8H0zkvmYuZYf5wJhZhuRh7D28uyPH_YQJbSc8uVHuL2I3fveqPN_7XDuc42iM3LgyvdJT0ff6ICo1z_FRulwM4CS8e9Zh9tugKkX2JE9uKgU3MSkr-fYBjaPiRvYlStZGmCsMZYgwCCbuTwNpsRE4x3xoSWuo6ss0ObE3hJjG_BKkj9yrbr3w4v49Y3bwb_-Y9_9pc6MPp_SFLPjB3sBy2jyZiGrK1uBJKYH5FAM_-1z-GQZdkasZ2T5RiupxKld5wYaKrcXAJrwgPug8Vbxvm2Y8mADrVRkcMDlf-SR2NrPrwvEhqjqgHeEcsArp9kldLr5zFxsk4Sb84npWNoS4QbvO2xBrHHmfuhyBVxMfY0WXfvFm2ChlWk1X_rQWO4enbn1g_jQdZ7O2Ef9frQ6yFry8wuksBkQbOX2kAeOWHaXBW_KhtooPRax0Hj1e9zrffYyujNJg_bKRFn8rlEMSa8G4PgqUuxG9aFXjRtNdQqW2q7UbCAo4LT0pJNLb8Xn3zio8h6w-dRWSD0ARxXB4su5dHRh3eFcBNoQa0KVFaSDAdHbZGfqrGotqn0cUj4o3-lvJtRzpJeRLueKPKks6hfNnP9Rs9TNl-MgSZ-DJG2ZVBtgRubO_cwRu07VNPJ9o4JZbNVBQ3zyZh_QqfB-v9wNvjtZLf3CldoPSn_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9407c8629.mp4?token=Yd-8H0zkvmYuZYf5wJhZhuRh7D28uyPH_YQJbSc8uVHuL2I3fveqPN_7XDuc42iM3LgyvdJT0ff6ICo1z_FRulwM4CS8e9Zh9tugKkX2JE9uKgU3MSkr-fYBjaPiRvYlStZGmCsMZYgwCCbuTwNpsRE4x3xoSWuo6ss0ObE3hJjG_BKkj9yrbr3w4v49Y3bwb_-Y9_9pc6MPp_SFLPjB3sBy2jyZiGrK1uBJKYH5FAM_-1z-GQZdkasZ2T5RiupxKld5wYaKrcXAJrwgPug8Vbxvm2Y8mADrVRkcMDlf-SR2NrPrwvEhqjqgHeEcsArp9kldLr5zFxsk4Sb84npWNoS4QbvO2xBrHHmfuhyBVxMfY0WXfvFm2ChlWk1X_rQWO4enbn1g_jQdZ7O2Ef9frQ6yFry8wuksBkQbOX2kAeOWHaXBW_KhtooPRax0Hj1e9zrffYyujNJg_bKRFn8rlEMSa8G4PgqUuxG9aFXjRtNdQqW2q7UbCAo4LT0pJNLb8Xn3zio8h6w-dRWSD0ARxXB4su5dHRh3eFcBNoQa0KVFaSDAdHbZGfqrGotqn0cUj4o3-lvJtRzpJeRLueKPKks6hfNnP9Rs9TNl-MgSZ-DJG2ZVBtgRubO_cwRu07VNPJ9o4JZbNVBQ3zyZh_QqfB-v9wNvjtZLf3CldoPSn_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دَرِ خانهٔ تهرانی‌ها به روی زائران تشییع رهبر شهید باز است
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445694" target="_blank">📅 20:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCLs-2lONAUWnsGoxAVugssuc88DIb5yDOdT4tu3TNrDZ1Zjll_k3ap6L_m2oLz2sOioMlfsK1LMnPxljJ4b6nKtbNmKm8NB7HU83F2pSSbniHNJOX41bbeATxvr32lOuk9aixWQkd3FcEzfxJQgGc-AmVfTyAnUOKQt9gXuHNmZL1961lnAQQgTkyp9-4L9izwxxzjWAqADbHZ2lUHySvlGY7-IKpyarP1KaMGlO95nvCj1DxUK3GY1Z_9r7x-EQLUgbjG2S_tMEbRIb9LElVqcf3vvVh_Wnwl3cmWtTql52heQYt2gRrU1UiinS7tHjh98EjcvS05bXxKDEkegIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حجت‌الاسلام مروی، تولیت آستان قدس به نیابت از رهبر انقلاب از حجت‌الاسلام راشد یزدی، استاد اخلاق و خطیب برجسته که در بستر بیماری به‌سر می‌برد عیادت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445693" target="_blank">📅 20:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgTbZzKCJR1p81FAvHnW2aLwgLT6BTa9qTRttgjHMNKpdnPes4MfV2F1ep0DtRIfcXyphpeqJhZaraWlz0xlxGtB0g5oYfWGXV67WSYMVKXIzTLPQLrf7iGVRbU8Syh5kad5qA8L5IikLIl-UsR0Ey_EPLddx8S6W-q6gD8jj_UwOPWTKvxmkI9oaoGVqt0PUm2Dem4HMw8kdc6VQjK1qAJZfc4OU8nsAOHzMn8JuB8HwzJW_-HF9ahBmaqJ6ygwqPYi-0XzakDe6MA8yjPTXUr61Dw4lN5nkjGky8cOA0ev8pkopuvySS0IqGDYuCIbmpnbSsHCjDEoJaLQ_6KJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه‌های مهم برای مراقبت از پا در پیاده‌روی تشییع رهبر شهید
🔹
کارشناسان توصیه می‌کنند که زائران در انتخاب کفش مناسب، تعویض روزانه جوراب، استفاده از پودر تالک برای جذب رطوبت دقت بیشتری داشته باشند.
🔹
همچنین چسباندن نوار یا چسب در محل تماس کفش و پوست می‌تواند تا بخش زیادی از بروز تاول یا زخم شدن پاها جلوگیری کند.
🔹
محل تاول‌ها تمیز و خشک نگه داشته شود و از ترکاندن آن‌ها خودداری شود.
🔹
برای درمان تاول بسته می‌توان از ضدعفونی‌کننده بتادین استفاده کرد، اما برای پوشاندن تاول‌ها نباید از چسب استفاده شود.
🔹
استفاده از کمپرس سرد برای کاهش درد، پوشاندن تاول ترکیده با باند غیرچسبنده و چرب، تعویض منظم بانداژ و پرهیز از چیدن یا کشیدن پوست روی تاول از دیگر توصیه‌های مطرح‌شده توسط کارشناسان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445692" target="_blank">📅 20:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445691">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb250fe5b.mp4?token=qPksAViGkw9_v-_q6-9ywpLrpV_PS6gURkND2kJfMCXMlm5riHHDwx9QlfbGBGr3ABG0h8kp8oFsc6iQ-Vse8eHP9Yvl2p-RKPmqShn4o_ngQRN61NcpYStbeWw2ZSie2kYiHowYMHOQ7wJ_kaBDdBoZ0n4gEqc3L55E98fqUVWac0o8Tfe3UyFHY3IYgWh1hSQzdrv9XwunKXZjDxx_74AiWtOPnysX1x5E9O1nBq_nUhKUTPo4Ku4WVwTs3WuWkAGeFOTIRvMxbbjCeHvNhdRHcEqx5N4fWHWSx8sVjUIZDgwcO2pSR92GpAJveXP3apQQ_LPQBqER8XyZF49MEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb250fe5b.mp4?token=qPksAViGkw9_v-_q6-9ywpLrpV_PS6gURkND2kJfMCXMlm5riHHDwx9QlfbGBGr3ABG0h8kp8oFsc6iQ-Vse8eHP9Yvl2p-RKPmqShn4o_ngQRN61NcpYStbeWw2ZSie2kYiHowYMHOQ7wJ_kaBDdBoZ0n4gEqc3L55E98fqUVWac0o8Tfe3UyFHY3IYgWh1hSQzdrv9XwunKXZjDxx_74AiWtOPnysX1x5E9O1nBq_nUhKUTPo4Ku4WVwTs3WuWkAGeFOTIRvMxbbjCeHvNhdRHcEqx5N4fWHWSx8sVjUIZDgwcO2pSR92GpAJveXP3apQQ_LPQBqER8XyZF49MEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمکران در تدارک بدرقۀ رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445691" target="_blank">📅 20:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445690">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3f5ced9.mp4?token=WSsilOuo3x1gKt6zU_lNNopkLAmqlN4AowbAIqMYaI1s2QKB7Gwn8AlKIqcKoQnHYxgmvGIZzQtR393LJaCcLHcFJsb7Hb9vkWN2YYvslMcv3E-0yk6ty6jyjgx98IrDY-l1OdRPDk4XywSfwlivwdAJ_8Gtauvs6eYa6378h4E_omb-YnP8YKzSyZsqnOJMwJic2BLcza7IvG07pO7ZAHPEUm3QdZQsFNvAGAMccwRmW38fHBlnXQs7lGg4onuapwAWA4gySmdImBnHZ2zgq9LWtnp_PDY-uU4tHhrBqKZurYkMvH19MbUSscW3UDAnJNR1XSJDp3XUZpkBUnLtbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3f5ced9.mp4?token=WSsilOuo3x1gKt6zU_lNNopkLAmqlN4AowbAIqMYaI1s2QKB7Gwn8AlKIqcKoQnHYxgmvGIZzQtR393LJaCcLHcFJsb7Hb9vkWN2YYvslMcv3E-0yk6ty6jyjgx98IrDY-l1OdRPDk4XywSfwlivwdAJ_8Gtauvs6eYa6378h4E_omb-YnP8YKzSyZsqnOJMwJic2BLcza7IvG07pO7ZAHPEUm3QdZQsFNvAGAMccwRmW38fHBlnXQs7lGg4onuapwAWA4gySmdImBnHZ2zgq9LWtnp_PDY-uU4tHhrBqKZurYkMvH19MbUSscW3UDAnJNR1XSJDp3XUZpkBUnLtbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: ما همیشه با برد تیم ملی خوشحال می‌شویم و با باخت آن ناراحت
🔹
البته باید عملکردها را تحلیل و نقد کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445690" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/445689" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تاکید داریم که هم باید توقف جنگ باید محقق شود هم خاتمۀ اشغال‌گری [صهیونیست‌ها در لبنان]. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445688" target="_blank">📅 20:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtV1IIL9ojQ-eh9znO-K0KgUT_BsV_anukwO9k5LD-EuZR65l6fU-mRVDKj625GwdBnP7sc8PLuDvMDIf4iEbY7WyKHIzOl1S_5XJA6rYGtBqEmSSjjuFvwu2ukQcMh4Aclpgzu75nBOdBsmaJUZnKhoqP9vOFK16Y7PkDvjEZ9QX1SsyG7PtYEiWcPyZAHd0XQ-UaN3e29ojRyAtL4ChwRN6ONVHtGP-3HyYnb2k1_OZzIzATlMTdFpJIwPeJh3A_27shXXolql44Bw3vf0b5u87aIncGMon_Y54iz3_sQv28L1EZ9l-DqKICMurxbzvLyI_TdUXN6udScAeE_bhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروغ مذاکراتی ترامپ برای کاهش قیمت نفت
🔹
ترامپ دیشب گفت، امروز با ایران مذاکره می‌کنیم و قیمت نفت وارد کانال ۶۰ دلاری شد؛ اما امروز سخنگوی وزارت امور خارجه، اسماعیل بقایی، این سخنان را تکذیب کرد و گفت: «هیچ برنامه‌ای برای دیدار با آمریکایی‌ها نداریم.»
🔹
با تکذیب ایران، روند افزایشی قیمت نفت شروع و امروز هم این روند ادامه یافت و قیمت نفت برنت به ۷۴.۶۷ دلار رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445687" target="_blank">📅 20:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔹
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔹
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/445686" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔹
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔹
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/445685" target="_blank">📅 20:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو: آمریکا و دولت لبنان با ماندن ما در منطقهٔ امنیتی جنوب لبنان موافقت کرده‌اند
🔹
اسرائیل و لبنان بر سر دو منطقه امنیتی برای راستی‌آزمایی و خلع سلاح حزب الله توافق کردند.
🔹
توافق با لبنان را به لطف ضربات مهلکی که به حزب‌الله وارد کردیم، به سرانجام رساندیم.…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445684" target="_blank">📅 19:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp0V7EesIbQAtMAX1xsdb5n-upSlsu6-yeahSH2Nar5IBUw_Q8UN5rAcE2ClnBAZX-2CqsaPvyQGMHhFPfNBsEBflLVuJY5CyDZk-Pb-VjCUervLoHh5U3JyA7vJ2a6VhqzOUKkWssskYe4nQZzLa5tWN7E15Gk_1SbymVL35OR01DIhjWKFZJTcX6SFjpJvt_z2v75g7pIrY8D7y9iskTj-zh1regbwazbidOKuAqltwaftPyWacPzUHyThIx1rbQdLT-r9j-G3RNFd3V2xsmRqPwp9OACBYU1YXtnpCzCl2FB3817oFBFMDqB3v6GqTaj7f-jag3Huu1zf6oDTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور گرجستان به مراسم تشییع رهبر شهید انقلاب می‌آید
🔹
دفتر ریاست‌جمهوری گرجستان اعلام کرد که میخائیل کاولاشویلی، رئیس‌جمهور این کشور، در مراسم تشییع پیکر رهبر شهید ایران، شرکت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445683" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445682">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75485d6e4b.mp4?token=iYw56p5p530TRHbspo-HTFn2a-D9b1UxY_Ejlg3FIZ2KtID8wXjvOHCvQRScV2kiQo3Bh1ncifogD0WJKiANver-VV6P0DsU38Y9RvID8thsgf1gLZL5Voi8B8JK2ekYXKODa6pyz1xRrarm3yGO58VQisPVi-JEzAyoLKEf42lr--SCAbZ8EKrjmXjVCoGcTPHg2iGDYmQE1KjOlu8FN7eWimAp0rWIavHTgrKitn4xh3xdOcCQTU0GFXaakmXmH1cWAr_KsqJsnXOsTp46bk1Vx0jBtGMQsV7fjhZh46DeFsCQ9RnKo3PpRcjyPSugiii8Bz_bg9ZN8KJK-2Ajbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75485d6e4b.mp4?token=iYw56p5p530TRHbspo-HTFn2a-D9b1UxY_Ejlg3FIZ2KtID8wXjvOHCvQRScV2kiQo3Bh1ncifogD0WJKiANver-VV6P0DsU38Y9RvID8thsgf1gLZL5Voi8B8JK2ekYXKODa6pyz1xRrarm3yGO58VQisPVi-JEzAyoLKEf42lr--SCAbZ8EKrjmXjVCoGcTPHg2iGDYmQE1KjOlu8FN7eWimAp0rWIavHTgrKitn4xh3xdOcCQTU0GFXaakmXmH1cWAr_KsqJsnXOsTp46bk1Vx0jBtGMQsV7fjhZh46DeFsCQ9RnKo3PpRcjyPSugiii8Bz_bg9ZN8KJK-2Ajbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رهبر شهید انقلاب در حرم امام رضا(ع) در سال ۱۳۶۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/445682" target="_blank">📅 19:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445681">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بورس ۳ روز نخست هفتهٔ آینده تعطیل شد
🔹
با تصویب شورای‌عالی بورس، روزهای شنبه، یکشنبه و دوشنبه ۱۳، ۱۴ و ۱۵ تیر، بازار سرمایه فعالیتی نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445681" target="_blank">📅 19:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445680">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACoGa3nUU-ZbKc5_Sn7YKrpmJCJhXbI1te9jIJuxaU5T0DOezCsq4F2AlVtHbgy8_FgDzQB1OUfRUUVaya8rBNUbFssXV9b9qMTglbMxJ0I64YiovKJwjLR6hnmzJhlhhdEdTqZHK8_4SqKRkB4ZZYfQFyHTSok_10enVYU29DU88XWRgE0hLl_156fI75D_SUPo_-P-5NR4hGDkNUyIpCAGNVqSAj9btLoiadYqRsGDziaiDWe2N4_Z3EgQNQksaU8vNpIU3mR02rS-urfZ4_cK0xh71wNd3oSMBvG-T1_EwuFmq5JaqUzaG6CDBlld818zZd0ugJdbU-kpVWRs2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: ایران برای وداع با رهبر شهید تمام‌قد به میدان خواهد آمد
🔹
تاریخ شیعه پر از بغضِ تشییع‌های غریبانه و مظلومانه است؛ از مدینه تا طوس.
🔹
اما تقدیر ما و آزادگان جهان، رقم زدن تشییعی به وسعت یک جهان، شکوهمند و بی‌نظیر برای امامِ شهیدمان، خامنه‌ای عزیز است.
🔹
باور دارم ایران مقتدر و امت اسلام برای این وداع تاریخی تمام‌قد به میدان خواهند آمد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445680" target="_blank">📅 19:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445679">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1nk2j3LasWJQ6dLu13w3JaWXHXd3Zo-IMhThrtnvHdY41LQ1_1paqAFdAFd7-EWqPxmYNvqp0GB9oe2XZHocWXe-Rd41luOjd5Cne3sIiYgdlmsjTX0AD8HwyPY_ARMzGF1p7Ul0KwtCwcUMePMxhn5IlGuYuiCMRYAsXXQC8H0fHtapzEax5gaPbx6yb33-0P_uUiTwixXtaZMFNmsPG7QsLuTxMoosc9ldgI9W6crxpqS-rFbfqzyZJWIg03sL6L2udR42qJjVuDGjSIy1KMMVXvNoSZajErxvVjz44Ji_xX2K1hasT5yMjLcHWMZjDJm-bfPFBrEtlBt8QlNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبی مرد سال فوتسال ایران شد
🔹
حسین طیبی فوق‌ستاره فوتسال ایران با رای کارشناسان به‌عنوان مرد سال فوتسال ایران انتخاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/445679" target="_blank">📅 19:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445678">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9risdhTR3isW7YO3evOf7SpgLC7N2M1R7RTrrnksC1W6NXMyScKswSIBvCuwjED4mCY_HBdbkUI-pg5aP-YN9fiofOrBj3r8NSZ2DTNG3cgFZcq7_CXcWQilvludTJPNp78bYLB5DYiH4M78JVyA6AX6Pq0du8udsFAcbHlS0_sjxdIsDZjlMqjuBr8Iz43_BdSSvuYYkUtnZIxfGFMoep29e3jhuBao6Xs3N4sxXN4tc1JQgPa6wjlA278G3zLRF0OiQU-PaMjWms210LAFuljbnaTFYV2nUFbHmY2LNiE2J5x8aUbxHTZ5hvCTwy3x0yzzMl17dBFg1JhR4aHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا شرایط خرید ۵ میلیارد و ۶۰۰ میلیونی چانگان را اعلام کرد
🔹
متقاضیان خرید این خودرو می‌توانند از ساعت ۱۰ چهارشنبه ۱۰ تیر تا ساعت ۱۶ چهارشنبه ۱۷ تیر نسبت به وکالتی‌کردن حساب خود به مبلغ ۵۰۰ میلیون تومان اقدام کنند؛ زمان تحویل این خودرو ۱۲۰ روزه است.
🔹
قیمت فعلی چانگان CS55 پلاس ۵ میلیارد و ۶۲۰ میلیون تومان تعیین شده درحالی‌که قیمت قبلی  حدود ۲ میلیارد و ۶۹۰ میلیون تومان بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/445678" target="_blank">📅 19:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445677">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
قلعه‌نویی پیش از ترک تیخوانا خطاب به مردم مکزیک: اینجا را ترک می‌کنیم اما قلب و وجودمان اینجاست.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/445677" target="_blank">📅 19:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445676">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/445676" target="_blank">📅 19:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445675">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازداشت تبعۀ آمریکایی در اسرائیل به اتهام جاسوسی برای ایران
🔹
رسانه‌های رژیم صهیونیستی مدعی شدند یک تبعۀ ۲۰ سالۀ آمریکاییِ ساکن قدس اشغالی به اتهام همکاری اطلاعاتی با ایران بازداشت شده است.
🔹
به ادعای پلیس اسرائیل، این فرد از ۹ ژوئن بازداشت شده و مأموریت‌هایی مانند مستندسازی و عکس‌برداری از اماکن حساس را انجام می‌داده است.
🔹
پلیس مدعی است او برای هر مأموریت، مبالغی بین ده‌ها تا صدها دلار دریافت می‌کرده و قرار است طی روزهای آینده علیه او کیفرخواست صادر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/445675" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
