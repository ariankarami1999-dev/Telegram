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
<img src="https://cdn4.telesco.pe/file/GsDeYrn3V35NNQqVK3veh1S-g8yaYYJ02j2BpV-oN5Am5x8jQkIP_huKJCNp2O9m_aSZt4WuB1D132rdJJfjxyKGNND6wi62lOiUG_d92gyQOX3EeGYxGMEQ9ihqerBN3HhYRhpZRO0ZCSQ8JaNloG1P8AEFyoolq2aQ9rpUsi8AXtLQpCJUogbmFm4NiLXqIpxdoFyzga3yU0rgqhXkT7T3BoEJWb-jFzAMPsB2uokZ6NG4q7wB1E136rVkwdRiT26A92z6chHtbv7cmQ4Hu_UFZ0JEqc0bQG9lYiY4F3PV58wQBbco7CiqU9ilIw-usqmzL8Bg_PcPCFEh9R7j-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 23:20:52</div>
<hr>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر علوم و فناوری  اسراییل، گیلا گملیئل:   وقتی که از رژیم ایران عبور کنیم، نوبت به جاه‌طلبی‌های امپراتوری عثمانی می‌رسد که به دنبال گسترش و نفوذ خود است. شکی نیست که ترکیه با آرزوهای گسترش فراتر از مرزهای خود و رهبری منطقه بر اساس دیدگاه خود، تهدید واقعی…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/18077" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk7NqxhFOiIvGmNOpm6AFNMbRaTiFd-0oBoBCdg1mIjQlwZlxM_vgQzKt3bR69YnKBjlkg9C-eQ-GE7jSyEt52n6hSO7yKtXj-jqb1WEY3K0rv4ia80AqU_TIZTzoNWHRwkj3JOtm-cGFMPFJc5246FUrS60KhfuoF7JYnuEC8eKRK_pdLaPviMOwa0lKZtJvuXxwjEw9ZbmA2p2l_Msu7gKlcWbHe-tF7bkfWFDY0i4wm8ROJZuTkLyrRvHBL86eUOg5yzcTEBQGKoBbW6yQ-Sxl4c4JyX9UilhVHXJetdi4FRkPHLZV9fxloUAraIsX1fLlK5puST5tFVU8cM76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا شاخص سهام کره جنوبی در روزهای اخیر ریخت؟
ریزش اخیر کاسپی بیشتر از اینکه نشانه ضعف اقتصاد کره باشد، نتیجه هم‌زمان فشار روی سهام نیمه‌رسانا، نگرانی از تداوم نرخ‌های بالای آمریکا و خروج سرمایه از بازار بود؛ بازاری که وابستگی زیادی به سامسونگ و SK Hynix دارد.
با وجود شدت افت، کاسپی هنوز فاصله زیادی با سناریوی «ترکیدن حباب» دارد و سؤال اصلی بازار این است: آیا چرخه رشد نیمه‌رساناها ادامه پیدا می‌کند یا قیمت‌گذاری این صنعت زودتر از انتظار به سقف رسیده است؟
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/18076" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هندی ها جوری هستند که یکی شان میخواسته از بانک پولی بگیرد به او گفته اند برو گواهی فوت خانمت بیاور و نداشته؛ رفته جنازه زنش را از قبر کشیده بیرون کول کرده برده بانک که پولش را بگیرد!  حالا شما فکر کنید بین شمال تنگه که پولی است با جنوب تنگه که صلواتی است کدام…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18075" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن، می‌گوید دولت جدید اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18074" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بحرین می‌گوید حمله ایران به ساختمان مسکونی آسیب زده است، تلفات جانی نداشته است</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/18073" target="_blank">📅 14:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=UCCouAxOILUejtV9NSK5wAFj5w-6RXkDSv_BXIlzHjexhfBBpM0wYBQ8UblhNrBTPSyb2yPxcrnpNEmoVaH4foC1lhzd7pMMzCeNQC48klF6PlTy_qt3VkefVGn5hWPe63UA_WXJF9dH1KRJd9zM2R9JavA8rx4vBw3t9GBazLwG46Y12etgdzXRO_CpHz5Ktaq2X6LbwaqGpZNEBG5RCsysNBZ0LWtPs2XsTMJ5EfIdczNahgH4g5v2oPeOp0Dm-bdCS7ZxGAFwAWfF6uzG1SfAhAub6fYpOdygEeOFySY0sjsdCyKNoPIR48Q_zrnQcIDMptiTRRKU4oXECvP5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=UCCouAxOILUejtV9NSK5wAFj5w-6RXkDSv_BXIlzHjexhfBBpM0wYBQ8UblhNrBTPSyb2yPxcrnpNEmoVaH4foC1lhzd7pMMzCeNQC48klF6PlTy_qt3VkefVGn5hWPe63UA_WXJF9dH1KRJd9zM2R9JavA8rx4vBw3t9GBazLwG46Y12etgdzXRO_CpHz5Ktaq2X6LbwaqGpZNEBG5RCsysNBZ0LWtPs2XsTMJ5EfIdczNahgH4g5v2oPeOp0Dm-bdCS7ZxGAFwAWfF6uzG1SfAhAub6fYpOdygEeOFySY0sjsdCyKNoPIR48Q_zrnQcIDMptiTRRKU4oXECvP5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی نجاسات الجزایری پس از خوردن گل تساوی تیمشان از اتریش که باعث شد تا در مرحله حذفی به اسپانیا نخورند!
بعد پروفسور جمشید خیابانی به عربی از این نکبتها درخواست بازی شرافتمندانه داشت!
حق شما همان گیوتین فرانسوی بود و بس!</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/18072" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18071" target="_blank">📅 10:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18070" target="_blank">📅 08:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=EQLxsTszCEj4Tvd5XXys6qpOnSLZWWxBcNPGK5hRUEh5Hrr_pc9j5azWsggxmnMnsoRgqSMOMRw4WfK6j7PlNEHA0Sa1y0uCfWrM1mCPAz1dY_ejWYq7PScqSiHpYBdsHI-XS-uYm-pGKndBNk2W2WxpX0KkVd7hTdN2_1g4rqiEmLlcRdj37SZRvXIcQeCXhvzhoHLmWT5W3mGZEIKjnYGvZtzqZeN3M1HYt-XmsHHi0jVaF-hpemJ6SHzXsz279KlRMuL8Ax7ndONcg_ji4TLT3AB9OjkU6H-hMRTOFsjnZVyi7u7ujFFn_936SW6SNSeQNT9vzC7Ed8mhpJndpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=EQLxsTszCEj4Tvd5XXys6qpOnSLZWWxBcNPGK5hRUEh5Hrr_pc9j5azWsggxmnMnsoRgqSMOMRw4WfK6j7PlNEHA0Sa1y0uCfWrM1mCPAz1dY_ejWYq7PScqSiHpYBdsHI-XS-uYm-pGKndBNk2W2WxpX0KkVd7hTdN2_1g4rqiEmLlcRdj37SZRvXIcQeCXhvzhoHLmWT5W3mGZEIKjnYGvZtzqZeN3M1HYt-XmsHHi0jVaF-hpemJ6SHzXsz279KlRMuL8Ax7ndONcg_ji4TLT3AB9OjkU6H-hMRTOFsjnZVyi7u7ujFFn_936SW6SNSeQNT9vzC7Ed8mhpJndpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18069" target="_blank">📅 08:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارشگر صداوسیما یک دقیقه قبل از حذف ایران از جام جهانی:
یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18068" target="_blank">📅 08:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شبکه ۳ بعد فوتبال یک روحانی  را آورده او هم آفتابه را گرفته روی همتی که چرا گفتی از دشمن گندم وارد کنیم مگر گندم تراریخته نشنیدی!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18067" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وقوع انفجارهای جدید در کویت و بحرین
هم‌زمان با انتشار گزارش‌هایی از وقوع انفجار در بحرین و کویت، وزارت کشور بحرین از فعال شدن آژیرهای هشدار و درخواست از شهروندان و ساکنان برای مراجعه به نزدیک‌ترین مکان امن خبر داد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18066" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراق عملیات گسترده ای را علیه سیاستمداران عراقی وفادار به ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18065" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18064" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ
:
هواپیما های ایالات متحده بار دیگر ایران را بمباران کردند چرا که بازهم آتش‌بس را نقض کرده بود.
احتمال دارد زمانی برسد که دیگر نتوانیم منطقی باشیم و مجبور باشیم آنچه به صورت بسیار موفق شروع کردیم به صورت نظامی به پایان برسانیم. در این صورت دیگر جمهوری اسلامی ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18063" target="_blank">📅 06:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
فرماندهی نیروی دریایی سپاه:
شلیک‌های کور آمریکا به سیریک معمای اشراف ما بر تنگه را حل نمی‌کند. اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناورها یادآوری می‌کند.
حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.
‎</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18062" target="_blank">📅 06:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا صدای انفجارهایی در بندر لنگه و قشم نیز شنیده شده</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18061" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بیانیه سنتکام:
«پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی M/V Ever Lovely، به ایران فرصتی داده شد تا توافق آتش‌بس را رعایت کند، اما وقتی نیروهای آن در ساعت ۴:۳۰ صبح به وقت شرقی امروز با پرتاب یک پهپاد یک‌طرفه به کشتی M/T Kiku حمله کردند، این فرصت از میان رفت. این نفتکش پرچم پاناما در حال عبور از نزدیکی تنگه هرمز بود و بیش از ۲ میلیون بشکه نفت خام حمل می‌کرد.
نیروهای فرماندهی مرکزی امروز در پاسخ مستقیم به تداوم تهاجم ایران علیه کشتیرانی تجاری، حملاتی را آغاز کردند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپادها و قابلیت‌های مین‌گذاری را هدف قرار دادند».</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18060" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک منبع نظامی ایرانی به صداوسیما گفت:
«صداهای انفجار شنیده شده مربوط به برخورد چندین پرتابه به برج مخابراتی در سیرک است».</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18059" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18058" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18057">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی به سمت کشتی‌های متخلف در تنگه هرمز تیرهای هشداردهنده شلیک کرد. صدای انفجارهای شنیده شده در شهرستان سیریک و جزیره قشم در استان هرمزگان به این علت بوده است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18057" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18056">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش‌های اولیه از حملات هوایی آمریکا به جنوب ایران.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18056" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18055">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مجلس خبرگان رهبری بیانیه داد:  باز کردن تنگه هرمز ممنوع است و هرکسی که به ترامپ و نتانیاهو دسترسی پیدا کند، بر او واجب است که آن‌ها را بکشد. ﻿حاکمیت ایران باید بر تنگه هرمز اعمال شده و از طریق آن عوارض دریافت شود تا خسارات وارده بر کشور بازسازی شوند. ﻿</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18055" target="_blank">📅 23:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18054">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=txAs6pLpu1dqr1Po959p6xftNhecV6Sq8wubqBuTJ0ivHu4tgYGTcLEWMcrgvgL2YeZ8BUX-cg1gnJEgSx3IbcaRY_p5iVrM4lxESBnzXgsEoeDUydon_yWTTCg30Z0Rcyyq_VqwHxEjObdHjz8WVKStuS56kPPg_Ipm9q-1aAddbiS2nRLGGo0qnZ3sAIFKUvByqlXD9hfVxeaEgN9Tlg8xFRexXqUjEkgVpkt6dlhn676LEs6gv5axIG4r2Phbz7YaW1tK--iQ7sLrCcqdjkAmQmQNJg2tPuTO6F4GfsZTdCfzgeQeTcImFa2veO86lKmx9FnO8YWuLyhcgDn_kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=txAs6pLpu1dqr1Po959p6xftNhecV6Sq8wubqBuTJ0ivHu4tgYGTcLEWMcrgvgL2YeZ8BUX-cg1gnJEgSx3IbcaRY_p5iVrM4lxESBnzXgsEoeDUydon_yWTTCg30Z0Rcyyq_VqwHxEjObdHjz8WVKStuS56kPPg_Ipm9q-1aAddbiS2nRLGGo0qnZ3sAIFKUvByqlXD9hfVxeaEgN9Tlg8xFRexXqUjEkgVpkt6dlhn676LEs6gv5axIG4r2Phbz7YaW1tK--iQ7sLrCcqdjkAmQmQNJg2tPuTO6F4GfsZTdCfzgeQeTcImFa2veO86lKmx9FnO8YWuLyhcgDn_kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داشتم به این فکر می کردم که ویدیوی التماس جواد خیابانی به الجزایر برای مساوی نکردن با اتریش را دیدم!  یعنی هر چه شما می خواهید به خودتان بقبولانید که دیگر به نوک قله فلاکت رسیده ایم و دیگر  تپه ای برای ریدن نمانده یک دفعه می بینید یک کصخلی پیدا می شود تا به…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18054" target="_blank">📅 23:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18053">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مدیرعامل شرکت خدمات انفورماتیک:   تلاش می‌کنیم اختلال بانک‌های ملی و صادرات تا پایان وقت امشب برطرف شود</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18053" target="_blank">📅 23:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18052">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت   اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.   دو بیانیه…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18052" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18051">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به نظرم در شان ابرقدرت چهارم دنیا نیست که اینطور بانک هایش فلج باشند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18051" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18050">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18050" target="_blank">📅 22:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18049">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.
عین بلایی که سر ما تریدرها آورده شد که آخر هم نفهمیدم ترید فارکس قانونی است یا نه! عمداً فضا را خاکستری کردند — نه آزاد نه ممنوع — تا هر وقت بخواهند باج بگیرند و هر وقت خواستند رها کنند و هر وقت خواستند بزنند و ببندند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18049" target="_blank">📅 21:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18048">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18048" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18047" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEcS1YShU3WPc8exvRWZtvD-RvrfvGUmDM3n9yzXH06Lwe0M_CGqxolmfH9UOsYyKsNxZJp06A0XrWsHOdPVLh9lsCf0uYPMU8huM78GFLxVqyUfiNcRxeRfps0SxZvBaSE-hyfVBLoVbRS6FkvnO_TLhN4G5SEPHZuio7j_Eo-bUluRXogsnL9u8lg7Q3DK5_7hYFjvPwuDonso_1i1ewQM8ktnJMssRypUhJrJNuUB56fpHKiNsbTQpJfetinSGOiJkoftbuXf4tx1g7LtTOfzh6DPdWNkVc89_mKd7Wsgx0FEcg0STinyQGXoebsGNpmetTo-YfIlsjwyTJ6Cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!  مصر برای اینها چه کرده؟!   دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.  آن…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18046" target="_blank">📅 18:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=PTLwFGRzh6rJtTFqZar046soK8sY6UgAMwx2rXZNB3jKCYmz8SOwzR_u8QcJgzMQfESg-NrpYbxC7ocbBaFymm-T4Qlp2aDUu9efhmdhEeNFnJGlqqKxPWeBqE_PZxml-HKlTdPwSt-xQoW3NJSO_88BO33iGXfXPER5iCVOEbaZjsG-ZYKVg-g1wX2nGn3Gx4EqEQWLYGpUbdsrkrrEw68jWS5l2WWXDoX9czgMsaidOua55QlOHQl-q_x3RexMpD1gJJBuUuDyBXJjvLdGRgyA3BU69zJ8oS1A07k23eVAiEM2TGJeg4VCkHU7C6hQTABiTkL8s5ZT2S3f6lOj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=PTLwFGRzh6rJtTFqZar046soK8sY6UgAMwx2rXZNB3jKCYmz8SOwzR_u8QcJgzMQfESg-NrpYbxC7ocbBaFymm-T4Qlp2aDUu9efhmdhEeNFnJGlqqKxPWeBqE_PZxml-HKlTdPwSt-xQoW3NJSO_88BO33iGXfXPER5iCVOEbaZjsG-ZYKVg-g1wX2nGn3Gx4EqEQWLYGpUbdsrkrrEw68jWS5l2WWXDoX9czgMsaidOua55QlOHQl-q_x3RexMpD1gJJBuUuDyBXJjvLdGRgyA3BU69zJ8oS1A07k23eVAiEM2TGJeg4VCkHU7C6hQTABiTkL8s5ZT2S3f6lOj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!
مصر برای اینها چه کرده؟!
دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.
آن وقت هواداران جمهوری اسلامی، ژنده پارچه چرکین کشور خیالی فلسطین را با خود به ورزشگاه برده بودند و این هم جوابشان!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18045" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">UKMTO:
گزارشی از یک حادثه در تنگه هرمز دریافت شده است.
کاپیتان نفتکش گزارش داده است که توسط یک پرتابه ناشناس مورد اصابت قرار گرفته است. این کشتی به پل فرماندهی خود آسیب دیده است؛ گزارش شده که همه خدمه سالم هستند. در حال حاضر هیچ خسارت زیست‌محیطی گزارش نشده است.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هر فعالیت مشکوکی را به UKMTO گزارش دهند، مقامات در حال بررسی هستند».</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18044" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رودان هم جز میتوانست جزو گزینه ها باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18043" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18042" target="_blank">📅 13:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18041" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18040" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18039" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7FV-pc3DFZ9Sq-eFzt8nfzYvQaHkB4qVm1jxaBgAzHRivj0yolVuF_W_pQC0PXJSawm6aVihpbVMTlIGpsf9QSq0UmOhveeHnwvWs0vBLVX7HjBK3RlCLLQajhJqxATeR-Z-R3HyXnN7y_PpotP-rM2-gCsaraaFvtAwoYLpPnCFzd6WsxvJhl5xsIFcT3lzFcBSg8egqCI_D7rwJ-gV5nO4FGfTyVtgDbA2QX42u7VhGSmaPemdEB_0uhK3Hd_ANk-Un8RYh6ijgEBPWRtfAAlK42NSGb6WdrV2UPgFJbhgWGteRNios8yDAjvhVyPeReST3xZOxlaXrSJgaW2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران
آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.
برخی تحلیلگران معتقدند کاهش تنش در خاورمیانه می‌تواند علاوه بر اهداف سیاسی و امنیتی، فرصتی برای افت قیمت نفت و خرید مجدد نفت در سطوح پایین‌تر جهت تقویت ذخایر راهبردی آمریکا فراهم کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18038" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjCBpVuSe-iBk8rb26SYo4VoS9EITvkiQVradPYJ5A2R7jYWUzvwKwqKc2g2-qWPhM_IPMte35R13UhRuC843VlC2OOVduY6AGpMppAxaauocOhkIOl577888KkyV_OkQLGq29wJExtDxuXvhNZuYaDr_acgUaHIFWx1Yppwo4HB6YaFTbSO5NrouK8CPbADCoE5FOJse_kIX642_bzcV2WE5vV3XHLKR_9YvMIxM4H3tMsIUeFKSd58sd0IUHziwBflVN_Pi9UbZOp5lrSSaS6QqF2rWX0FQDj0ontPviKPIKWaHvIvDK6Sob2tdhcoOBnar7B4mNXoBJ0Fl6F_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه بازی</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18037" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvbBZqyD0Jp570N3cEpGZ1cEP-u5FuwyNr-WV0ratisVKMS87v9IjunTh6OfLoc6VmX4kgEzw9iKFPSubr4tfAWBGCaShk97oTYWkqoMcoLRQx1mXmOD1RoELGopQdzcqodDlmc8pdfHVS3odgXXdxcAZ2yHRvXAKIFJHd_sLrKSpo-MG-x9lLXy9ZWTm-DpupYRIA5QfCjqBympO5cJvjNRXupX6OZ4prClsKIhOPg-pmcOAoGKrGhRMxaya-Gmr-USMmAR2z3u0KVBHS_XJ7jkUsZEHBisDbj5apXqngAZ-YciCHfqJQZcjLr3KQxv9LYvYhiC8ADwdOm4q5lDnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18036" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18035">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم؟
• میرزا •
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18035" target="_blank">📅 07:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18034" target="_blank">📅 02:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18033" target="_blank">📅 02:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس ایران: ترامپ هیچ تعهدی به اصول مذاکره یا آتش‌بس نشان نداده است</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18032" target="_blank">📅 01:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">متن اعلامیه سنتکام:
حملات ایالات متحده به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — به
عنوان پاسخی قوی به حمله دیروز به یک کشتی تجاری که در تنگه هرمز در حال عبور بود، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۲۶ ژوئن حملاتی را علیه ایران انجام دادند.
پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد حمله یک‌طرفه به کشتی M/V Ever Lovely حمله کرد، هواپیماهای آمریکایی به محل‌های ذخیره موشک و پهپادهای ایرانی و سایت‌های رادار ساحلی حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
این تجاوز بی‌دلیل علیه کشتی‌های تجاری توسط نیروهای ایرانی به وضوح آتش‌بس را نقض کرد. علاوه بر این، رفتار خطرناک ایران آزادی ناوبری را تضعیف کرد در حالی که تجارت به طور فزاینده‌ای از این گذرگاه حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM به ارائه هماهنگی و حمایت برای عبور ایمن کشتی‌های تجاری از تنگه ادامه می‌دهند. نیروهای نظامی ایالات متحده همچنان حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اطاعت و به طور کامل اجرا می‌شود.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18031" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملات تروریستی گروه های تجزیه طلب به ایستگاه های مرزی در بانه</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18030" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سنتکام   به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18029" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU65AKOgmap7KWuwU7RXWztwta8ihJxZlSX-W4V8E9mELL4qbjMas6nLhb6elr8FISceESkLeBX2UyjgNvgxLnlg1a8ML13uTmx7tcRIsXRRArGdK1URAM0u4dGD-uxabsObrtx29PcE4VEzRhX_XTL7P3lLtXY_NUFZOx8SB5UtDLdbjdq-i7wuPUPnaNdumuh-Ly_PDfxyd459Psf7D5vEZG1VH6RvQkGoicGXt5N4LnYyF58zFcADmUHeeUEuLg8iE6J1Nz_U-YqxL1QavgN7cFrqTdSvi9UXp_vi4pfPFK44wnjwcRCFYYETDLg1qNslU4z3LuzjMvTxWs9TQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مثل ما نفت را خریده.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18028" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18027" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چادرملو! صد تبریک! / مردک نزن تو سیریک!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18026" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فعال شدن پدافند قم!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18025" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پزشکیان را آوردند که جنگ نشود؛ هر 36 ساعت یک بار جنگ داریم!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18024" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به نظرم بهترین پاسخ زدن رودان باشد؛
هم آتش بس نقض نمی شود هم به هر حال پاسخ داده ایم و هم دل جمع بزرگی از مالباختگان خنک خواهدشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18023" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqV-7UA8lotBu960UfGh1q6Z5EsMmCLEIEw53C6iR1dtOBNYNT7Ugkw93L0HLo62rfgoLBpnga0DyQX6wfprSYRHsrEvlweojg2SzODV52-b3_n8VjF8rlW8OwAnQcmflFamz4Fo5e9LSIM6pGBGmbj_kiGPdIU6hFhNucuEUxUvjE9bw9jtSEj0VWwOC_MOgfhrDa6NmaCWgd4I_N0mCjFTZB8VfQW8r7UxTQJCT1GzLz3KpfzE3kfeW9SpU7UiKNNJiVq3SWdrlGNjgzQSC7Ovezq3w3kzvTRaV00TOiLI1VRI7wD0qocrh4Dmc_spDQ_DTDfqFctNnJ4MknDxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید حمله آمریکایی ها توسط یکی از همراهان باوفای Secret Box در بندرعباس!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18022" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18021" target="_blank">📅 23:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سنتکام
به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18020" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18019" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18018" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18017" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند  طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18016" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند
طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه آنها کتاب «هنر معامله» ترامپ را که در سال ۱۹۸۷ منتشر شد نیز مطالعه کردند.
این مرحله نشان می‌دهد که چگونه ارتباطات غیرمنتظره‌ای در مورد فعالیت‌های ترامپ در رسانه‌های اجتماعی در طول درگیری پدیدار شد. بنابراین، طرف ایرانی سعی کرد درک سیستماتیکی از الگوهای مذاکره او ایجاد کند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18015" target="_blank">📅 22:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آمریکا، اسرائیل و لبنان یک توافقنامه چارچوبی امضا کردند که بر اساس آن اسرائیل یک منطقه امنیتی در لبنان را حفظ خواهد کرد.
ارتش اسرائیل نیز آزادی عمل خود را در این منطقه امنیتی حفظ خواهد کرد -</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18014" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:
بنیان‌گذاران ما در اعلامیه استقلال چهار بار به خدا اشاره کردند. چهار بار.
من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18013" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds8R7p7LG2iLKKb-2pXz9T71N6Ik-UpvaJ5BKSa-szvApGltOwqsKpa3GMaKUzLVHrcf76julh0ChUHJ50hADAdvByA0e8j6hJezw1flcjVPHlOXKGcUVdK7FfC_pVk5TqGCi0ji30uKkea5I7a0M82rjWwDotTORyNRhMDSOJOr0PQNDjaupr0wp0r5una4sOLKJdtqojMM5F4jxGu7JOVElnakKitQ2RH_okJdHl4bQ6pcYTrrpe3wCEihJZu4_M0pWEfOr8v_wrUt2zVGW6B6wLvBycprWjtxjyTurBea0ZM1amfA6UBFcUOh-WpTu-PgX_SJEk3cpgEieIH3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18012" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18011" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18010" target="_blank">📅 19:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edezaygWizcwBP3J1B8zxyh4gs2bLjh7vq50by6FvN5tcmobjFtqCJZFA79SATSg_I-qXdk2MTwwS5_jncF6jJ8_X_B7wB268R1SdCjjAjqBjTtieW7QMY98n9PMN8_eVuzdrhzs7Zu5OZTokPhhDSxekuhjhCNxoTuWkdfecUhAyPxytGRHs6erk85K703gruTyI43r7u6Auf2j7scc6iUXNKMFbj4chvOvMnUhLM9v2oPg4P36-eW2-GEh-KqswQI36bUyAo3gwTrfCfiERRH50OSLyShcxXGeJ3hJTYI3aJqCUHD3RmDGcG98SZseGDltDfqT_bMxLI2o-hiF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق کنید.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18009" target="_blank">📅 18:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/18008" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18007" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسرائیل درصدد به‌رسمیت شناختن «کشتار ارامنه»  وزارت امور خارجه اسراییل پنجشنبه شب اعلام کرد که «گدعون ساعر» وزیر خارجه این رژیم روز یکشنبه آینده پیشنهاد به‌رسمیت شناختن «کشتار ارامنه» را در دولت مطرح خواهد کرد.  شبکه المیادین نوشت: بر اساس این گزارش، این اقدام…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18006" target="_blank">📅 18:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhVnIpUFnIR8_xoqcgTix5bfeyMFmRQozbt2AAm2eBqYQwlxRglP9oMn3bTmqGtdP8jWXRyjqEb3mZnXOow1Ed5O1Bq7i4GVqkM6eP-6w7v2dkAueDCpufI5ao9zSo7yUIIxNRAftmbjhD92RyiuLN2H-h-l2Wk5LyanzN13Sz1ugrVoeKVV0noF3VgM87Q10rfhjYvP65SHuzFvaRkQDBXIIzbn2vRZamWKrZLH6D-rNd1wl1ED8iEMwQQcRede_WrR7xlLBJPwDCQZNknk0PcJ8I3TtIX_U4eO_EIcldemi_rtgfbcYdZXvJ1Io6PA46bQA6n0heeYWqABG31RnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!  پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.  ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18005" target="_blank">📅 18:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApdxJO27jy4S8u6AITnUhl8Mw39LQ0_9R6mTnaXeITd8TD5agPt95Wrs8EVsiuIZ30cSoSDGCFClUnaok2IGx1rofjgcrwVkGCBVsx3NuhYfoJ-hVFujp_sgKOWzH3rxWcI13L-lLGtfRWsgFtXk0Lj7LrGU6XBSHDkdA5njyK99c_OXBrZJhyOjN7HgFK1mRVo-YhiC10OAJmrFVrYa9xlbycDRXMDz-qohOmdbrtzvDEEsmF8lnxMdk95CTzpVYFTXhcTK3GABVoldrwNz_v9PwfnDQS2SX0P8X-k_7XmjspiKKsdIPapNn-BuV6RpZ6RVHLC27P7EtCc_DVytKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاتز وزیردفاع اسرائیل ضمن تهدید فرمانده سپاه قدس، آمده عراقچی، پزشکیان و قالیباف را هم تگ کرده!
در یک لیگ دیگر است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18004" target="_blank">📅 16:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua_37_0XkwL8ieP-EIbkuXAQjwbTIpzCVWrN35pfpmbQO9mFINjSjSYAml462KjBSrKQ4XeH-1LqCobmx2l6_Oeu0m1SmKj24BQvn75IplcxvOVAg-ZPT8DQT-6UrHuIUXRVp0ce4XJbxFEWNNU5ESsnCXrhXvKOKhdQyew7fVGrBSw80ixkw0K8z6sp9AFF6cdGRKQus-H_pNDlPGq6T1rxu3VLZFe5KlxTk3N-4GfFh7nbStpZBI5AA24xOmfbWqjKhjUY0KivTZ_egCJydJVEX0ZjbYTeeZ8bQinv4VhlrP1fNZ_hnBwcwn1nujvnSMYSPuFE5yEIi4al-lgW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18003" target="_blank">📅 15:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فرمان پوتین برای ساخت نیروگاه هسته‌ای در ماه تا سال ۲۰۳۶   این نیروگاه انرژی لازم برای زیرساخت‌های سطح ماه را تأمین خواهد کرد  پس از سال ۲۰۳۶، روس‌کاسموس قصد دارد خودروهای هسته‌ای را به فضا بفرستد</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18002" target="_blank">📅 15:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18001" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18000" target="_blank">📅 15:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_394
🗓
june 26, 2026
✔️
تحلیل گزارش PCE آمریکا
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17999" target="_blank">📅 12:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n584CA3zohARNeV5QfGc_S8hQFwxmZlHuyb4ZOm-_OhaYlAmnjE8jQZPTyTrtZRwHIWow_-gFwe_lgmjtVUb-_F8bs467GU_AmmoEP1kpNhrsbvC9OHpHa0Ug66Yd-80pVLyqEa9dTg6NrS-U77xFRiAoCRWCZ91AO_y1UkYu-jwiyJVQgLjNi_N11zziX96RkbICmJoekTLkP3bKD0RKmLDBYkz84OxUsBcGIJZ7iOiCt8Z52mJqKG3Ilht3VMtdvrlXoAifiUPjCza4TMsYZHvy55lT659rx6lm_gPoLekPPSslP_R9XeEjNGUZewV3P4Q5xPbk3tEv0M94Hr6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5VCzWS-qewl1jfnkJYbpKRvLBJFef1JvH0wkbw38HS_5DzibQFyNDwTvNiNgYr4f7kV6tyTcVDw65S4yO5ADLlb4DKUKIu0-LgnqLFzaspQUUMmW8l85zo3RPuk8a9R0kROrHBu3BG0nvejpXiR4E0Z4Ss6S2wZng468JFYur-7RQroUNJ7O_VBuwSjXPTM7_GoDvG3vvfANAEVl1LMDoMKgmQjCQanrR241U9H__ZxrndWuwg3tIEkkX07oxPIwe-lnoLBF4uPbm82WS1UldvSL0kLJFhp_IWct18OIw166WkH3pQyemqZQ7sQh2ppXMElMEydnJXf9VdaGxM3TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه وزارت خارجه ضد مواضع مشترک آمریکا و کشورهای عرب خلیج فارس</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17997" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پنتاگون در حال بازنگری در استقرار خلیج فارس است و جابجایی نیروها به اسرائیل را در نظر می‌گیرد
طبق گزارش‌های رسانه‌های آمریکایی بر اساس تصاویر ماهواره‌ای، ایالات متحده در حال بازنگری در وضعیت نظامی خود در خاورمیانه است و در پی آسیب‌های گسترده به پایگاه دریایی کلیدی بحرین، جابجایی برخی از پایگاه‌های خلیج فارس به اسرائیل را در نظر دارد</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17996" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیانیه قرارگاه عملیات مرکزی خاتم‌ الانبیاء (ص) :
تحرکات و حضور جنگنده ها و هواگردهای ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17995" target="_blank">📅 10:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ حرامزاده تا کنون همه ملت ها و رهبرانشان را — از کانادا و مکزیک تا اروپایی ها و عرب ها — تحقیر کرده جز:
— چین
—ترکیه
اولی را به خاطر قدرت خودش و دومی را به دلیل مجیزگویی رهبرش
برو قوی شو اگر راحت جهان طلبی
که در نظام طبیعت ضعیف پامال است</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17994" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یونجه و سویا واسه من
تنگه و دریا مال تو</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17992" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بوی گندم مال من  هر چی كه دارم مال تو</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17991" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#نمیپذیرم</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17990" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ:   ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟  برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17989" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ
:
ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟
برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17988" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📡
ترامپ فرمان جدیدی برای ساخت کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ امضا کرد
دونالد ترامپ با امضای دو فرمان اجرایی جدید دستور داد تا تلاشها برای ساخت یک کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ سرعت بیشتری بگیرد
این اقدام با هدف تضمین پیشتازی ایالات متحده در رقابت با چین در حوزه های هوش مصنوعی علم مواد و شیمی صورت میگیرد
همچنین آژانسهای دولتی موظف شده اند تا سیستم های حساس خود را تا سال ۲۰۳۰ یا ۲۰۳۱ به رمزنگاری پساکوانتومی مجهز کنند تا در برابر حملات سایبری آینده ایمن بمانند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17987" target="_blank">📅 01:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17986" target="_blank">📅 00:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17985">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU-IBgfMa1RYLQyvkD8uTieMJgaDGAkds9cm8L79Cg8kUX2Aef83EPj6keqhSTzHnnwmcAW1Nw-ZolUs8jNQ7bkzrridgttqHOR6yLSPLLVhJ5M5HShc5YIinsiGXCIQDb-LvqaA8E9wOPw70N8-kdFmJSJN7YQVlqCJEiDMsEKsN8mnmHI8OHq2JXIm8CpMpJwxp32Yehbi622Ipf7jz9atlYFB9VxVGh56pkVstdU60jPT61d04wl_kpjTuw56p__IGJN6RjS1zamceVdQxojACQ0SBJjr5uSjLPRwyieJ6mqprPg3MDCBcLBbotc29UVREPOeVJE7xgeWigdGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پس از انتشار این گزارش، حساب بسیاری کاربران ایرانی مسدود شده است</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/17985" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.  @Milita_Camp</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17984" target="_blank">📅 19:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17982" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhZfCHnBQm7AXbGKG9_ewxJuCgEEheZudUHCCFKc8gH7T0WQD2Of8_-1lHfCEb6ZOaWx9bBdqM5wn3Ag68YeTx2aaVfXyKxMioHMpVSuB6AQhyDlnDsS66SHbNSIGh7wi2F185QGauk9OzmGy_2VMbrVPt7Ehws0G9Lxvg1O8Sn7fQPorW_kWq5ipvAmyTARczIAd2B_EF32fSJ1kaUPCRdp8WsBNt0LfnAQYyaUoqqhqJCDFjVgOP4lZpLeb1hhFMfWs4RLSxKBda_78oej4FLBAT6ULHHUk_jZQaKyWUk3e-hTxykv8wg9Cf4fXUnjbe-3ZL2sSMEAtSKg8u4XZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- نیروی دریایی سپاه پاسداران انقلاب اسلامی با یک کشتی در فاصله ۷.۵ مایل دریایی از سواحل عمان درگیر شد.   این کشتی تلاش کرد تا از تنگه هرمز از طریق مسیری غیرمجاز و بدون هماهنگی با اداره تنگه خلیج فارس عبور کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17981" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/17980" target="_blank">📅 18:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVTN09su3SGw3-tnIVaVyI7bD1QyxO99-RJd8jNoAweSeD9Pr_M0rQyR227n2UNRxevsVzO5vbK_eMFTwSeoiXKmSul8iJJAa50vOsDXNvZq-wNbU2ahuKR7nsyg7ccz4Rd2cRBhiA7yzMtOqOeny-4o65O0txpenhpCzu4EmIst-rtZFGhiADy3Zi1ORq_kstY4d9mZQt-tEgPuTKaId20vH-ndYGMGQhp3qoLU8QDudj1rZz9WB9462rgsO6ltQp-6gNvvdjhXLeQKsLgoZnYbizkgnp6wjA_P8DAHMnZAjUX4quBpidWGJaiS9xXdUF_dBa3325f7SHyGyTrlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/17979" target="_blank">📅 15:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMILITA CAMP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfMK36RRy6CUK944sXz69_XBxQKzo51YzpxKMi_y2YZraiGs9udzM9RaXgmEWFGHh24SWC2-bN7SjwBh455VZ05UlHPk4V5bWAr0UwgqxA4vbLm73NBmC7SqYT7NAbbPYXupoGmFylQmKn79qiNo4ejFSE14KMlFaM5cvH9em5k2w6xtX8sNsvhK95BhU4TebQzMQQesgynvn-ikoPWRlatzD__2EM_HneYBT3OH81D0n-NG96mWJrm2UmRo2qq_NCxwwVgkBpFyfl4LsB94qvwl1Mg8SEdG8Rcf5hlwh6Rv0VHGgiuQ9MPVluvapF6nOpeKjdvpSrl226Cj9rosYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.
@Milita_Camp</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17978" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17977" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔸
به اطلاع همه می‌رساند
تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد
، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔸
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و
با شناورهای متخلف برخورد خواهد شد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/17976" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.
پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17975" target="_blank">📅 12:46 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
