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
<img src="https://cdn4.telesco.pe/file/s51JG8acMDCVFVweWWqwjmmFFAw5iurd_refp3UKstrFfqmoVC6ylhgMPwzRPuDUieVOqsQFB2vKvHTcGg-zqmEUWvSRrNwoDnvSpiecVKMIEUGWQ0j8YQW8XIEu4BTjRVl0F-HFA6R58sQhsix6me39t4c5TLibqRyaNJjJeKqRpBIZjFpg3Z-io7WOSP2mot2Azzd24TCUH9HxspjD1LA_u1LXZoZRirXv3YkgQJnO-eVfrDylYjRpgsRsGLhRUnDC91jm2bHVwlDlA3M9O1BPdXuYzDhFi1whllbDCDXHVgsSOrcPIYFJ3MVAkPncjqkjjsmUNDXt5BcuJ6uLbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-458642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملۀ رژیم صهیونیستی به یک خودرو در شمال کرانه باختری
🔹
شبکه ۱۲ عبری گزارش داد که یک خودرو حامل سه سرنشین هدف حمله پهپادی در استان جنین واقع در شمال کرانه باختری قرار گرفته است.
🔹
به ادعای این شبکه یکی از سرنشینان، فرمانده نظامی یکی از گروه‌های مقاومت در کرانه باختری است.
@Farsna</div>
<div class="tg-footer">👁️ 251 · <a href="https://t.me/farsna/458642" target="_blank">📅 17:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4775207fb6.mp4?token=lIdFk4FxcQt-GpWj_enBOeFxFCjJ-Vc3riTmtKlczkY0nyEXsxJ14CaVzsUOJDU-0zc79zvHWW8dJwOlY5v-DsRcdiae6h3Y0MlPVMKIXl88z5i5qZYF5JTNPlZGAOLy3cKOsj0dr7z7J6cBgiRS0nh6zQt1CHlz1A3x6HGu6cM5hGrruOHE2gQL2HmKM0xENBAfIDXVoGqjtJkB5SzuxfxplvjII63G2iT1zQXkv6EFq2wvxyR2GQQEYPJsPZh5n1Csr7B89V4CZYhETWFtDNPXQk-GABH5H08ofDriPIvO2FwKhXYpY6XCUuayAd8T8IRlTDp00k97ojgdsPJ8LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4775207fb6.mp4?token=lIdFk4FxcQt-GpWj_enBOeFxFCjJ-Vc3riTmtKlczkY0nyEXsxJ14CaVzsUOJDU-0zc79zvHWW8dJwOlY5v-DsRcdiae6h3Y0MlPVMKIXl88z5i5qZYF5JTNPlZGAOLy3cKOsj0dr7z7J6cBgiRS0nh6zQt1CHlz1A3x6HGu6cM5hGrruOHE2gQL2HmKM0xENBAfIDXVoGqjtJkB5SzuxfxplvjII63G2iT1zQXkv6EFq2wvxyR2GQQEYPJsPZh5n1Csr7B89V4CZYhETWFtDNPXQk-GABH5H08ofDriPIvO2FwKhXYpY6XCUuayAd8T8IRlTDp00k97ojgdsPJ8LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی، کارشناس مسائل منطقه: افرادی که صحبت از صلح شرافتمندانه می‌کنند بدانند که در شرایط کنونی صلح به معنای تسلیم است
🔹
هدف آمریکا تسلیم جمهوری اسلامی ایران است و هم‌زمان با پیشنهاد مذاکره، تهدیدات و فشارهای خود را بالا می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farsna/458641" target="_blank">📅 16:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458640">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTFLnPiTmRH6rNvzAaq2OwJHXJ-RHZ7Ps9NdT1fW15dMLgk6ZVMmbvfd8JBiy5ZSx-E8iTUmRoYXiEsf6-M2friNBvBhN6mWvpOOixi2yii3xPSPjl3PTjyWVtcSCJ2qwzduZb9GMh_7C9RUZYMFgAbexu2v-f3rrO2IsOsnH1gk8qqgHCriJ-v_SHb_ty-nJ5RJow82HcFaISkl1j9e_jSIHqcnL1g_FIkdVUO_yD_69ltz-xPb5k7iJx0a0vwGRvfnZgJRG01yYdf_cCeWG2f0nMmmUxJJYYXlQ4KuCx0JnH8a6J7a-CL52G0URwG5vERWZ0YdzuVN7LYgTuCAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چراغ سبز دولت به ارزانی سیب زمینی
🔹
معاون توسعه بازرگانی وزارت جهاد اعلام کرد: صادرات سیب‌زمینی تا پایان سال ممنوع است.
🔹
قیمت سیب زمینی به کیلویی ۱۰۰ هزار تومان رسیده بود یعنی نسبت به قیمت یک‌ماه اخیر ۳ برابر شده بود، فاصلهٔ بین تولید مناطق گرم و سرد عاملی برای رشد قیمت شد.
🔹
دستورالعمل صادرات و واردات به عنوان اهرمی برای کنترل عرضه و تقاضا و قیمت در دست دولت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/458640" target="_blank">📅 16:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts8tGEVMxOZ9jScG4QH9SOYEUsZH-T_hEIKCi-ORTpE2OreRiOlkfU-wb-6cqDEJ7wSqhf_GcfjuU7j9tjp-dHPS3SJJgA_c9AJEXnuDvON78KOiR0jSKVfd3CtX2FJIgc7xaUi30BCF2dYN1d1z9apVNCwYxLmJ7kzR10q_fsUAVsEu2ZDZJLpzEiz9eY_llYpZ9C3bcYXA-nX0RWC3l2EsacnUtUwBkLIz_sjGqOvag4hfKbeZjpyYEqIj9qd7uUsexRxLNOcVprTQObpn0TTXqP-ic1POR9Pyp0T47nIoauRM6JE5XDv1vNoynU7svEigPZWRzvns7DlhtKpWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریورماه است و هنوز خبری از واکسن آنفلوآنزا نیست
🔹
از آنجا که زمان طلایی برای تزریق و اثربخشی این واکسن از اواسط شهریورماه تا نیمه اول مهرماه است، داروخانه‌ها از یکی دو ماه قبل اقدام به ثبت سفارش و خرید این واکسن می‌کنند؛ اما امسال با گذشت ۶ روز از شهریور، هنوز خبری از توزیع واکسن نیست.
🔹
سخنگوی انجمن داروسازان، درخصوص وضعیت تأمین واکسن آنفلوآنزا در سال 1405 گفت: سالانه به‌طور متوسط حدود ۳ میلیون دوز واکسن آنفلوآنزا وارد کشور می‌شود اما متأسفانه امسال هنوز اطلاعات دقیقی از میزان واردات، منشأ تأمین و زمان دقیق توزیع در اختیار نیست.
🔹
او در ادامه بیان کرد: هفته گذشته واردکنندگان وعده توزیع واکسن در نیمه نخست شهریور را داده بودند، اما تا این لحظه واکسن وارد شبکه پخش نشده و متأسفانه شفافیت لازم درباره میزان واردات و محل تأمین واکسن‌ها وجود ندارد.
🔹
همچنین سخنگوی انجمن داروسازان با تأکید بر این‌که اکنون در زمان طلایی واکسیناسیون قرار داریم، گفت: تزریق واکسن باید در همین بازه زمانی انجام شود و تأخیر در آن، اثربخشی پیشگیرانه را کاهش می‌دهد.
🔹
در این‌میان، سازمان غذا و دارو باید پاسخگوی وضعیت موجود باشد؛ زیرا سلامت گروه‌های پرخطر شامل سالمندان، زنان باردار و بیماران صعب‌العلاج به تأمین به‌موقع این واکسن‌ها وابسته است و نباید اجازه داد این فرصت حیاتی از دست برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/458639" target="_blank">📅 16:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458638">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9HIIDu0JSG6KscS8jIet8LDP84ZY90YHO3ScMULHeanLKVivWIg-_ahgaDO6It-ukXnvtJTrlumVE4jHBfqPkvCXk1HuA6BK1z9BUQRUhi0-R5U9zU-2XGt6XiINYjN1CnRULNLD0YcsUr5r4VnfCo_YsOFQzzADRQVQh89KwkAp9lVxk9s9XJ8im-O1vHYvc6w0enQpUsAISpOrSbZldrMW89BXBZ4Mt9AxEEYjlQ5gY7e_d76kBqVIUH0b2e1PMBb3xrPXJPOyYvYQtVDamF-0cvv5pXHpgPlShuest2FmDCh-tV6quddqw54LL_gf_4r5UzrCTy9wZ53BBsGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خوش اخلاقی با مردم
🔸
حضرت آیت‌الله العظمی شهید خامنه‌ای: این‌که پیامبر هیبت الهی و طبیعی داشت و در حضور او مردم دست و پای خودشان را گم میکردند، اما او با مردم ملاطفت و خوش‌اخلاقی میکرد. وقتی در جمعی نشسته بود، شناخته نمیشد که او پیامبر و فرمانده و بزرگ این جمعیت است.
@Farsna</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/458638" target="_blank">📅 16:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458637">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8xhZfiodJx7_OWdSSOeZcXCUVbF_6et3fIxW5pWOcOKdoWY52rJdSfpf-yCc15q9AfjUmv3umnqKnKEdaISlNWOh5RPDk6MrU0t8XQHBwuBrSYncs0b_aj9-IRAZPcunNvXYlUlPOh1n5nCxowU60NzAdW0MtROUxGjVMnteHGDjRHNq9d45YXKcF61FRBF62JPNbZyafTBhy5qwO90HkHDh7Xbu7EPvkNEpoz0GOQL0DSA-FbPnSEnBSXEuu99mhIwPedr6V0shA5KL3nuAU0SvLV3ovDrPDPEy_Ellx-MFFxPLWrbqz7s1R_DZ7NH1jZdTHUk3oRM6dfxKoB1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار جدید رژیم صهیونیستی در حومهٔ «مرکبا» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/458637" target="_blank">📅 16:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458636">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajM6U5q9dgn58Tp5za0ruzIpwz3rVOlLXNipf2hv5k9JL0m0hX4Cs5UTRHNysbozHYAOMbbi-VIgaljtAnPNm6_s38Tpd1ptrqCYCCHZSsIJe9Zk-uDzr-YIIB860HEGVEEPOt5ls-UQfkDCZu7-389RsZ46-2At1L6Nbj9acV5e5c1KurIDlLhdh76rxWDv-PQAzwXCS4ZlctIdFIDA9vpNfTFrYTnLnF933HzVOox63ETkrEwL5GxeERP6uBvMRWZTh3b9aAlGsZ1XgrdqSzKnl0QAucR1sfLO9ZBved8DfMSlIt0QFSwNecF8DEKMUq-vr0A2emsbxzRswQX2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ چین در خط‌تولید موشک‌های پاتریوت آمریکا
🔹
وابستگی آمریکا به مواد معدنی به چین آن‌قدر عمیق است که اگر پکن بخواهد بازی دربیاورد، «حتی خطوط تولید موشک‌های پاتریوت هم نمی‌توانند تامین تنگستن مورد نیازشان را تضمین کنند.»؛ این را یک مدیر سرمایه‌گذاری در بخش صندوق پوشش ریسک کالاهای فیزیکی با اشاره نمودار اس‌اندپی گلوبال می‌گوید.
🔹
نموداری که نشان می‌دهد که چین سهم بالایی در تولید مواد معدنی خاکی در جهان دارد.
🔹
اوایل مرداد ماه وزارت بازرگانی چین ۱۴ نهاد اروپایی را در فهرست کنترل صادرات خود قرار داد که یکی از آن‌ها غول دفاعی آلمان «رین متال ای‌جی» بود و اعلام کرد که صادرکنندگان چینی حق ندارند اقلام دوکاربردی مانند تنگستن، گالیوم، ژرمانیوم و مولیبدن به این نهادها بفروشند.
🔹
پکن ۱۷ مهر سال گذشته پس از اعمال تعرفهٔ ۱۰۰ درصدی ترامپ بر کالاهای وارداتی از این‌کشور، محدودیت‌های صادرات عناصر خاکی کمیاب را بیشتر کرد.
🔹
حالا جدیدترین آمار فاکس‌نیوز می‌گوید که دو سوم موشک‌های پاتریوت آمریکا در جنگ با ایران تمام شده و تنها ۸۰۰ موشک باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/458636" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458635">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIzPS-DApLfIEsjjbsibAknCs26IcCH4pFoHzfdaNbwrV-XYwLQB6LfpayjKTGyTioGhxt1AFjom-vHwQDk52ipg4VVOrsGHP5EXV7INiOk0ZC2eLmb4fGxkGQxzM0fJyN1xIwPwMspkmsYesnGpPRNbLAK5o7O_n-gxDHBVomNjzR_vlEJxxfpzlROWp_mGQogBpyob2IFXw1_YRX4yiCIZ2BKWkecLdDUANnjZeJU-fsDHyvVnHz8yaZWqcZ10etMm_uffUBSF3xXTkgebhS0f30T4SVMHgRDlY_747AVJ0qIyFsJIoUaRnWIGg0xsTa-nS-wWl0-6IJOkUq_KbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: آمریکا به همان اندازه که دشمن شیعه هست دشمن اهل تسنن نیز هست
🔹
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی: اگر امروز همهٔ امت اسلام در کنار هم بودند رژیم پلید صهیونی به همین راحتی ۶۰ هزار نفر از برادران و خواهران بی‌گناه اهل سنت را در غزه به شهادت نمی رساند.
🔹
وحدت از عمق اعتقادات مکتب نبوی برخاسته و همه مسلمانان باید برای نجات مکتب اسلام به این موضوع اهمیت دهند چراکه امری ضروری، شرعی، سیاسی و اجتماعی است.
🔹
آمریکا به همان اندازه که دشمن شیعه هست، دشمن اهل تسنن نیز هست؛ چراکه اعمال آن‌ها در افغانستان، غزه، لبنان و ایران و جنایت‌هایشان نشانگر این موضوع بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/458635" target="_blank">📅 15:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgcS1dl8YYzoaadC_qkb6HuUDloDW6EWb5RyfEjbz6WzTCRzbpuXH2gg6bQX18FxtfO8ihyX7NUdYlwtYHk2Iq18wUknA-0t8gpe-V8bvacZStJgjy2IWi_Zhctq_dkt3OsaIHFmZgau3lmEXRVIzIK_D6kXAT1sQKMn5B-WYbBw5aoGQdynFYuuGJGoEw7F7zTkcJ6NK5k8IbT34Um0fsEejakq5EP_w_dlhCFNv467TRGyCBsqvc9w-WCCFNJoouqtMPO54dIWRxKpiNb444gslWzCTSCcp9JBYivzYV507Quam-td8mXFQ5W7YZU2LXZk6kPTwSAymBJqzvh6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود ۳ پله‌ای والیبال زنان ایران در جهان
🔹
برد ایران مقابل اندونزی در مسابقات والیبال قهرمانی زنان آسیا، برای ایران ۵.۹۱ امتیاز در رتبه‌بندی جهانی داشت.
🔹
بدین ترتیب تیم ملی والیبال زنان با مجموع ۱۱۵.۷۲ امتیاز از رتبه ۴۰ به جایگاه ۳۷ صعود کرد تا برای اولین‌بار در تاریخ در چنین جایگاهی قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/458634" target="_blank">📅 15:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2149e889f3.mp4?token=IuC_-KuwzmpkiggroZduaKk3ZCUAz-3TsS_qd-Msr7yHx0GZ17icdwyIj8lfa6f7dWcc0KnlQKT6r1uGBgT0mjWCtvflOOhrs5ERKyXhZfkRerbun_-WsodZmpfMvWPLKc6r0tNZA9nzrSwvn6PIfWXko6FBRzliGRqQLsAS_mL4MmF2WLrrey1GTTwH-ricJXsRSPFy5g6IYgWJSoorIjUbuLJt-W8sLqTbaYN7cwYgDde1l3sUQZ6vihSZrArDPDtFRo6Hf1lh2Ai5YHMd8ywsMrbrQS4ivkxHDA0qyO1AoIgLnJIwgKHBG8DSnxpUvTmrhDATE6l3xFlcXQTXTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2149e889f3.mp4?token=IuC_-KuwzmpkiggroZduaKk3ZCUAz-3TsS_qd-Msr7yHx0GZ17icdwyIj8lfa6f7dWcc0KnlQKT6r1uGBgT0mjWCtvflOOhrs5ERKyXhZfkRerbun_-WsodZmpfMvWPLKc6r0tNZA9nzrSwvn6PIfWXko6FBRzliGRqQLsAS_mL4MmF2WLrrey1GTTwH-ricJXsRSPFy5g6IYgWJSoorIjUbuLJt-W8sLqTbaYN7cwYgDde1l3sUQZ6vihSZrArDPDtFRo6Hf1lh2Ai5YHMd8ywsMrbrQS4ivkxHDA0qyO1AoIgLnJIwgKHBG8DSnxpUvTmrhDATE6l3xFlcXQTXTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان مرشایمر: آمریکا هیچ برگ برنده نظامی علیه ایران ندارد
🔹
مشاور پیشین وزارت خارجهٔ آمریکا: سیاست تحریمی جدید آمریکا علیه جمهوری اسلامی ایران و کشورهای همکاری‌کننده با آن، بی‌فایده است.
🔹
من حتی یک مورد هم در تاریخ معاصر نمی‌شناسم که محاصرهأ اقتصادی از نوعی که ما (دولت آمریکا) مطرح می‌کنیم، واقعاً باعث تسلیم آن کشور شده باشد.
🔹
من فکر نمی‌کنم که شما بتوانید ایرانی‌ها را به زانو درآورید. اما اگر بقای آنها را تهدید کنید، آن‌ها آن‌جا نمی‌نشینند، ناپدید نمی‌شوند یا تسلیم نمی‌شوند. آن‌ها تلافی خواهند کرد.
🔹
ما دیگر هیچ کارت نظامی برای بازی نداریم. این ایرانی‌ها هستند که کارت نظامی دارند. به نظر من، موازنه اجبار نظامی تقریباً به طور قطعی به نفع آن‌ها تغییر کرده است. این یک وضعیت واقعاً قابل توجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/458633" target="_blank">📅 15:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458626">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zlb57UKRIXvod0QpBkgrHyODYHvXeaT7TtGlvBg770O79DbGMikbHRjFSTfYvvswZQqIZmXTZF5PWLYS0tUifDNlXkmfTIgHmTNiO87HyuWvZ2B_acnxyLy6ER20VdSgsF1AC6Tg3_vk8Qp3r7JQj3Jsf_0oaeWIonSYfGnmJxkkt9U11dxwedB6dkLlozIfnU395HdEDSlzruClEItpu5EW2LtNMqFdNtWwj_sskjIFEgIYyaIEY5Bu_4PTjbayOhlBCipfr7vSsTynAus7-l4eZTkS6O20SB4CAIHh_hfYrP-ledamMUQwPWmLqUKByp6EXfgFdZ62mH4oELAMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyTPjLdVXoSfH2tID0wZIu0Xg5tfA7Rb-3accREQV6V0QJtPzu3eKdaZIl_6Q8cLvCAhkzRCExIJf2hpIf9tfDMuE4JXByEaReNVW-na0mXQQaVI2QI8klcxoVs0_lZDczn9XhcD9kX3SIvlBdGxTKwBYU97_RfyXRXU-uNcRYT1OlI2FC3hc1tWMNIkcKgN_9LY75OIvKAcbOYjX4zFuvrfdDL7Ne9lBuyz_GqtMGyS1EEqn7ajo7i-4gYLRfyqy25wh6cFH9How_pId0AePThEa5V2I49W3VwKXDeKlIXHGY2EtdfIAD5NvLEKSvt2rFJanL1n99VV68kFVS1tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrBRo-faHILyYS3SC4nyhIqYxFkxGOPs7_LrUTXr0VtJoeOhOY7uYSc4wFPXh6NeBv0nJrG2CMOriXFpodBnyTWXjYbJeuid2b1AmZdiudnW-l2Om4pN_B60X0SpNeI0VmXCv3JWtQWhTrsoedSXldLDAGtyaRNJ9-_qe22l2kTU7-6FUJecK6HDXXJnhHzveid1NsEyWrLIHyDBUnA4yD2PGr46Q5MMjBJdHRcHV7k0352b05pxjefpe9ia5E7rztjdS34ELQN_VbenFOMf7o-6VQqTcCKDPQfPyYI1e5DnmNFdMquGMWSQJGDxVo7SkebCdZ_ehOwmjgLzkQiXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqlLp4AjAXEEk2QPGT7vf0pYtRs7UR3c2lv8W2CCOuwsd-GeZIf7BVNwpJjIE9his8debPrIJ_4VVdxe5yIO5t8nzAdEE2X7ZN0L6qVklzrUlK6CAcw_MgK9EyT5qzXP7YpJvAArGnZ4bcEy_KnhOovU6DyPReEzTVvqaRLDRg40dSQXA1cdjZuo_hVRwhgpaTZediUu7_qWPKMKEI9kKDiuGiZ9kcnL-iGWowq2UVST3b3Rl1G2HbZNOd_G02NnB2BWagmwxvCe8YyMS2f4orB6xIWW3ysTJhYb6FkG5J6GiEbl0QETwLMQXitZoci4IxiBrQgLYpNoSC-yaKNJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBj2D1ku0BZIT_knmy4bzwTNidZZEY7_4ixjS7UHWJGxn9nXrwMVwsL_wG4Jl48zYUIjEVyIcev4DTF6cUgzHDcqjCu_ZpKYLB7zOsDgDAILz8c6OZTnUgalASWzZvq23QR-fGWIUATwOsJqOW8YM6XnaelH1mIgFhJBxrZku6TcLEdLEDWFEFYN4Qa4t3fpWFpQN_q2FaNcdO8xMjrLMXFJ_j_sYcphBzyg389D-54HZ3jNDDi3qp9jhpIRUp6PDX55ToCemghuZCCBkG-d9sDJvbTmM_uWcEAdEyF57u70fiLqEMEvTUDLNmHlL50PLRbnS7C7mNYAbCCnbP7EiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eePXxdqDPz67xKU7eMZn0BQMmcpXcerJbcfYiURyKSRjCTH0nevD6HeyCPcr7v-rwJ3pOSBSWKnQwvd_zG29GLCzsrEZckeYB_jby54HCty4ni5wjJ8WqMqeH8E9cX71diiptMHC6Cvb4FKb5qD4BaEz1dqbQo1hEWeRpA7v8icjx-RfErSwJoOiGkGhrUS9hd5A-P_Qb8D827BYfnXlSEruC7I40i8VbJQaloQYgMR4laAGq4-FfQ5CDt0hrM6reYMtx_c9KrK99wmZTFoRBZauvwt4DA5scOf06WBwS2cgew53eIlrjKO881KVceQnvlhyeXEjSHu4j5YlNpt_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FT9YcdxfeyoqyceXJQGD1zAwXRYvKbYYJ4u5TV-JG4648Rv-NgRJsBc68gBC6gcZIyYBlrYnBVDa8-orrt7THICZBfiYZuzkNo0j_h56wXJrvvKfyadSQEiW59cx9WGUmZObRtBD1deLQ5AMahC69sO2QqeQcmwAf0yiGIxev7A9SpoCrDBmx-eCo4WLZhic-QlKmGxwC-LlFa5dPm97kbljcRttLYMFQSA9jFrTydsOEchEFXkRuoJLV-ecY67uQkFOjkLtA-4Ut0dkLeyCi5kqOaMCwByhk2h_ubelSVMhY2ffL5BydCRQicjjY8Qj2js2IcLz4AQzKWdVzaJoSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کلیبر، بهشت گمشدهٔ آذربایجان در قاب سرخ زغال‌اخته
🔸
نهمین‌جشنوارهٔ زغال‌اخته در کلیبر آذربایجان‌شرقی برگزار شد.
عکاس:
مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/458626" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458625">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u91y6LNe1gFNTl93CeJ-_V74ELkeBgKIGKYFFdasBwR88WGSj0HGMsXWhS8WjSyBtTscJpBsT0vJQIRbCWd3Y3HuoE8_AemSvGwhESj9y-vHMaA2pMRgOuml-Hg_u-jxqRGGOCKQMYCi8xd20e_a1MqWv9FRC2ZOIAUSrykeHpB9og9JDDFa60QQ4_Vx4gpSv_A3-nh8dB6I8QBYs5_ZJxzd49noEShJ2007kRO6tVzNRgi-0D25HlNlb13Tj0S35dx43lqjvpA7cpy_miF-VZGOaXQsxkE2bJpxNbpruxki6nCpsPwsmN_3TRvUmdu-juyr2CsVEqp49GjPLOY62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال به دنبال تعویق بازی لیگ برتری
🔹
باشگاه استقلال به دلیل حضور در لیگ نخبگان آسیا، به دنبال تعویق دیدار خود مقابل پیکان است تا با توجه به فشردگی رقابت‌ها، با آمادگی کامل به مصاف السد قطر برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/458625" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458624">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7WPIKGkEu2qnYDnmbuFS3wNwsXirKS3Ns8cAhFY8TFpkXWDPikWU0Qe0eTms8yqYKlufUqlSo585SEf0dQQTjlYpdRXMycEx7L4Zk-OouFqOZaLUXJcvA34sSUB6qDSR1Tzt6WGLQdzWY-4whDwPmDWLEIX-nl_w4YX_aOp5AZY5aWk9lGnVxSFEQa6yHdUVX6Uv1tPc3qUctONNGAfwMyuVxddUJNDOS5yxWb1lgj1y_mHw6LqWHsrCLkkoVvhWhc-sHTklgiT-YtAU6o-qu0mVwIZ1FXIcemtB0iKwVkmvnJls4vUS3eLdaNPKMiWf12D-TePIzQhARt_Kh8mng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مدل هوش مصنوعی برای کارهای پژوهشی است
🔹
شرکت چینی تنسنت از نسخهٔ پیش‌نمایش مدل هوش مصنوعی متن‌باز جدیدی با نام «های۴» رونمایی کرد که برای کارهایی مانند مهندسی نرم‌افزار، پژوهش دانشگاهی و تحلیل مالی طراحی شده است. این مدل در پلتفرم «هاگینگ فیس» منتشر شده است.
🔹
«های۴» از معماری «ترکیب متخصصان» استفاده می‌کند و در مجموع ۷۷۰ میلیارد پارامتر دارد؛ با این حال، تنسنت می‌گوید برای هر درخواست متنی تنها حدود ۴۹ میلیارد پارامتر فعال می‌شود.
🔹
تنسنت با عرضه «های۴» تلاش می‌کند علاوه بر کاربردهای عمومی هوش مصنوعی، بخش‌هایی مانند تولید کد، پژوهش و تحلیل‌های تخصصی را نیز هدف قرار دهد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/458624" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696ebd6be8.mp4?token=Bf_cA9PkVFTlx6Pbdh5x-6oev0yLWO7vhrEAfYYo5MtGdJaBSvdnFIx5GaMZ7k0HHVxjlSO6coWKr5tAxStm2wHFqvgTcZ4c7fsd_bsfdH2j18dVJusqHCfaKPuKSKVRwn5umHTyJ9gy15Ad6SEYczNWJ3Ix6UkoMefAY-6FqL4w9Nk4EXIaFNIZkBVM6enKEoxy6mb2GhCoSX-86bKEe8n0Whi8MQlZwPQkduiiNpcgOMQ6lo6pHABiJqbFeArHF88HpwLT1cnPIhU4W9kZi2A7BsKpPvgQwGlLYUbHlpobde9OIzjb8GfkuhNReHN7yDgbdXxiK8rPePWRmM8rFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696ebd6be8.mp4?token=Bf_cA9PkVFTlx6Pbdh5x-6oev0yLWO7vhrEAfYYo5MtGdJaBSvdnFIx5GaMZ7k0HHVxjlSO6coWKr5tAxStm2wHFqvgTcZ4c7fsd_bsfdH2j18dVJusqHCfaKPuKSKVRwn5umHTyJ9gy15Ad6SEYczNWJ3Ix6UkoMefAY-6FqL4w9Nk4EXIaFNIZkBVM6enKEoxy6mb2GhCoSX-86bKEe8n0Whi8MQlZwPQkduiiNpcgOMQ6lo6pHABiJqbFeArHF88HpwLT1cnPIhU4W9kZi2A7BsKpPvgQwGlLYUbHlpobde9OIzjb8GfkuhNReHN7yDgbdXxiK8rPePWRmM8rFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: درحال کار روی موتورهای جدید هستیم که خودروها بنزین کمتری مصرف کنند
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/458623" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458622">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e65eecda.mp4?token=SnN2J2Ru0uw7Ajg7vtznuwNk1kG0EmcXYPf7b8Dw6flGhwWBtgMnsFY6EvKDrNWYa-pYQZ0xVz_sVVFD0YuYVk_ZoH-AoXmxvzK9xacBlocNKOnp2_dFmNqXQmbunAQTrxfH-te3Wo3mJAl1HP_8-Ga3--jP6K2xqJu-TweW3ze9e8OlnU5O0GpU4PqH0Dk2FxuV7g8Vm1GCQROliJP637agZH6tgFJzxw4G9AX3hN8AKplLp6yVHxrDSeFAz9XvjZ-mXzCoS6CC5B5t_R0KXabTNXnPDo_NUB-gaoucccRlRin9LuYEbgReyD2Ns4JALDW_Hog0Kab6_8YUiqXdNkqwCBxXUCp6kh4Ceto_3wvu7fQqlGVFWnwh0OictHuKfckrjdVYqVtCaz0aNsyz2WZpXaU6LEqCyb98jMDafD6EQ5loMu9nHyu-Ya7aapkMsrZKypxY-cfeUe5BTfF82KhugLz951z6uCRwurdC7KwIYYWaY13IrNPtn3badDt3jQT_FyM2y3ymwlF5b82qF2Y4AHxooJEqQRk_pZOXZqyiSH1JhwMlhYeC6zJqxgjou1ccosQTBCeSQnvckxxzKDZ45pF08s5RRUvZ-v2mokH9B2fG-rj8hY3g4lqXHtROdZWpD4CPAkiQjruVPWhWrSolB0ByC-Isij64sf8lGVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e65eecda.mp4?token=SnN2J2Ru0uw7Ajg7vtznuwNk1kG0EmcXYPf7b8Dw6flGhwWBtgMnsFY6EvKDrNWYa-pYQZ0xVz_sVVFD0YuYVk_ZoH-AoXmxvzK9xacBlocNKOnp2_dFmNqXQmbunAQTrxfH-te3Wo3mJAl1HP_8-Ga3--jP6K2xqJu-TweW3ze9e8OlnU5O0GpU4PqH0Dk2FxuV7g8Vm1GCQROliJP637agZH6tgFJzxw4G9AX3hN8AKplLp6yVHxrDSeFAz9XvjZ-mXzCoS6CC5B5t_R0KXabTNXnPDo_NUB-gaoucccRlRin9LuYEbgReyD2Ns4JALDW_Hog0Kab6_8YUiqXdNkqwCBxXUCp6kh4Ceto_3wvu7fQqlGVFWnwh0OictHuKfckrjdVYqVtCaz0aNsyz2WZpXaU6LEqCyb98jMDafD6EQ5loMu9nHyu-Ya7aapkMsrZKypxY-cfeUe5BTfF82KhugLz951z6uCRwurdC7KwIYYWaY13IrNPtn3badDt3jQT_FyM2y3ymwlF5b82qF2Y4AHxooJEqQRk_pZOXZqyiSH1JhwMlhYeC6zJqxgjou1ccosQTBCeSQnvckxxzKDZ45pF08s5RRUvZ-v2mokH9B2fG-rj8hY3g4lqXHtROdZWpD4CPAkiQjruVPWhWrSolB0ByC-Isij64sf8lGVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدال‌آوران هوش مصنوعی: این دانش را برای پیشرفت ایران به کار می‌گیریم
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/458622" target="_blank">📅 14:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458621">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2ZFNjpSZ7EejCR1fWgcxintgEeU_jrlx2ZDOBjk6rcwN8M02fuAUppp53ZvcbDWk5_NB6b6cMGk4XIrHZiMwaHQ-rYJTVE2LXzMR26eypevIyizs06p3muw7omJiWW85UNyoUts68-F_BaGZ_eIi1aj65cSzI5Ho6cS_c2G0YHGuk_MoXAcw46aOW5q7R7rGHI0tj1x56r6xZIgWa4tfB-WNkjT68LOaTTyCVThDs2RGOIpnITbJpyPZTPmd-LPZlPu1TT6dn28X5cZPFK1wDeyNMWMAC_h4BRknhfacYOUomelBD5NVExSFcGwbaYbYKrpPl0tRfhO-Fio0eKhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: بدون امنیت، هیچ زیرساختی ارزش ندارد
🔹
جبل‌علی، یکی از بزرگ‌ترین هاب‌های کانتینری جهان، در نیمهٔ نخست ۲۰۲۶ با سقوط نزدیک به ۶۰٪ حجم و افت از رتبه ۱۰ به ۳۲ جهان رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/458621" target="_blank">📅 14:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458620">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d333bbdbf.mp4?token=fPJ3xQqPFmOvtwpYFlD9K2QMd0GZEUjjY1VptzdIkdppitcu8aUWWgOKUwKGC7R8neR0rc2PuOqvtnPN8qnqqNLDN2ZBQmNEKq-DiyNgJFqNzOQyFnNzSlitpw_QYIsUENLM3FkOQ2PfBN9Bu5hWEKlpuActtuDIlEfqXb8RljQagXowKJtEK0dSshwfPiaHjmDwG4kRQmBnngLeGykc8VN9W7Im1D4pzVNc9vmVfy1SftBEpgoVtEFxbUot8H8lIUnOZoZMQdzmJEk28Pa2YyoJ7MiA-cGpC0JEPZcV8t6rbLTCdJg6PXtVrSPLvnM_Vv3u0l6piWurmqoaK5fYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d333bbdbf.mp4?token=fPJ3xQqPFmOvtwpYFlD9K2QMd0GZEUjjY1VptzdIkdppitcu8aUWWgOKUwKGC7R8neR0rc2PuOqvtnPN8qnqqNLDN2ZBQmNEKq-DiyNgJFqNzOQyFnNzSlitpw_QYIsUENLM3FkOQ2PfBN9Bu5hWEKlpuActtuDIlEfqXb8RljQagXowKJtEK0dSshwfPiaHjmDwG4kRQmBnngLeGykc8VN9W7Im1D4pzVNc9vmVfy1SftBEpgoVtEFxbUot8H8lIUnOZoZMQdzmJEk28Pa2YyoJ7MiA-cGpC0JEPZcV8t6rbLTCdJg6PXtVrSPLvnM_Vv3u0l6piWurmqoaK5fYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحدت، میراثی که هنوز زنده است
🔹
میهمانان چهلمین اجلاس بین‌المللی وحدت اسلامی با حضور در حرم امام‌خمینی (ره) با آرمان‌های امام راحل تجدید پیمان کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/458620" target="_blank">📅 13:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458619">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3092b745.mp4?token=kJM__qQxRApOgjWDdQZDVxY69hruwWbNnZrXvmx0FlyzN7yV_OY3N9fGIboOA8pIIt1yqWIjKX_91pua72vgrxcthHtAOc86UsbbyABscRAiPHyH912FfcWm4qmF1fMotmGvD_Oe2gpoo11yfbA3HdUHMozGn3aehtr8cH9HsY7wBLy4tbHx3QFYzBiXAmbKtKqgHFyQq4SdCv7OOZ964WrXABXZGIEAq5fjF0Bg3DwbKGxnH_u2UY-s3SIKf1LBJOSCzqoMmDBPPuvMfkveuusQvX6arcowcm_cRC1sEq0ltQTspNcuVs1YqATfS0DkZs_LxeNmySKNtYdzO58_ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3092b745.mp4?token=kJM__qQxRApOgjWDdQZDVxY69hruwWbNnZrXvmx0FlyzN7yV_OY3N9fGIboOA8pIIt1yqWIjKX_91pua72vgrxcthHtAOc86UsbbyABscRAiPHyH912FfcWm4qmF1fMotmGvD_Oe2gpoo11yfbA3HdUHMozGn3aehtr8cH9HsY7wBLy4tbHx3QFYzBiXAmbKtKqgHFyQq4SdCv7OOZ964WrXABXZGIEAq5fjF0Bg3DwbKGxnH_u2UY-s3SIKf1LBJOSCzqoMmDBPPuvMfkveuusQvX6arcowcm_cRC1sEq0ltQTspNcuVs1YqATfS0DkZs_LxeNmySKNtYdzO58_ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ ۵ میلیارد دلاری ایران به شبکهٔ جاسوسی آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/458619" target="_blank">📅 13:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458617">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EC84yKFpHu_XCxs8sMVtxhI89LPWqO9ANYJK9jKjZa8MyNpQlGQ9kMdHTZlveVGg9YUTGEGyWAsrKExxjvwbq0ii695qvUt7MNkbUB8Fx9HMPk9cbkMWYY6kH5VS81MN_8vDNFaDBM01efU7mXnuDyq0tbtbwWdP5Y7LaXO6ZZ6lO8IRGCXeRVMSmtBYJGWw2CGkgIeeKEiWYn2hsk8I_TE-ZQS5UZ_bD5ARrN_DDU-YT7sRtqTL6pAwPTl_Y5sn7EfKtND80kbv5wVfAFa4jN4h8uZ4NI5AdnKDG85KZ8i_tw3elWsdqYdFgBLQFctTVYX2ozJ-fBysBZWdottuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXCwZLMG8yPyG9TzF-9q95Fsi_7bJ18gBdq0pLpxU0tEPCdXs6hHZV0kN3sOisHDtjlTs_7OfvqcuRyPVpxkZHn_qk2-aPoyh_fwVvBhToN01J_FZ1A6peL3ZgnOC_AVMFjwI2XxzFRK11KmNJMdu5abgqYNdX5S1l-pkuHGTqyKxVI7zjP3PnYR0_aum8gQinwhM6hisTzmzf47bfl-wVVlQEj_E7OckXs1lcDbBY1TBTeD-fSlQ6eEI3EDmc2so2LBpxsfQFxIo2456UVzrx2xCER90HMkfaoNClYyAd2TPWxF3sLyqjOdD3znUbE3FN-6wIBTrH-tuoLNspozHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
بیانیهٔ وزارت امورخارجه دربارهٔ تروریسم اقتصادی آمریکا علیه ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/458617" target="_blank">📅 13:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458616">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خطیب جمعهٔ تهران: ترویج بی‌حیایی و هرزگی، راه میانبر جریان شیطانی برای تضعیف خانواده است
🔹
حجت‌الاسلام حاج‌علی‌اکبری: جریان ضلالت با برنامه‌ریزی دقیق به این نتیجه رسیده است که راه میانبر برای بی‌خانواده کردن نسل بشر، آسیب زدن به فضیلت‌ها و بر باد دادن بنیان‌های اخلاقی، ترویج هرزگی و بی‌حیایی است.
🔹
در اجرای این پروژه، غرب به عنوان یک مزرعه نمونه انتخاب شد و برای بررسی این مسئله می‌توان به آثار ویل دورانت، از جمله کتاب‌های «تاریخ تمدن» و «لذات فلسفه»، مراجعه کرد.
🔹
در ایران که از دیرباز مهد دین، هویت، حیا و عفت بوده است، خاندان پهلوی در دورهٔ حاکمیت خود پرچمدار اجرای سیاست‌های ضدحجاب و ضدعفت شدند.
🔹
جنگ علیه حجاب با اقدامات رضاشاه آغاز شد و در دورهٔ محمدرضا پهلوی نیز این مسیر با ترویج فرهنگ مورد نظر رژیم ادامه پیدا کرد.
🔹
این روند را باید در امتداد همان پروژهٔ فرهنگی دانست که هدف آن تضعیف حیا، عفت و بنیان خانواده بود.
🔹
این‌که بخواهند بار دیگر آن فرهنگ منحط را به کشور بازگردانند، آرزویی است که ملت ایران اجازهٔ تحقق آن را نخواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/458616" target="_blank">📅 13:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458615">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l49DaeE5kVH2qtnqqngvyYFkLCuSXAgvILgWFxkrkxzIOuze2Ak_prgjVat05Y83xMqTkkfItqF0ZNF5izRyq3V1otfJ72OtMRM0rKl9ltHaPrhvjKkkTQ9Tqq0Q56vcdh2Q2qxWvR6B5rCAswXtmaSmDyMoK4F8MDtMOaHJmwRUl6Ph7KStF6sWOZhrXeroLuNlZ6flcdG20X0BuDqJT53q6nB9fXaoOHPVNCkdxw5LRYalFn2heXcBFu3fllHMZMCWM6HXewLctE9BDsNEGV7kFIPW_h8XL9JpwDe8iG54OGeRgXrONFyXigXb0KP0-1eGbRb7NsMlaotOz-tpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون وزیر خارجه به ادعای مالکیت ترامپ بر تنگهٔ هرمز: شایع‌ترین علامت اسکیزوفرنی، توهم و هذیان است.
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/458615" target="_blank">📅 13:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458614">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شناسایی و بازداشت ۳۰ لیدر اصلی، مرتبطان و تخریب‌گران اموال مردم در استان مرکزی
🔹
وزارت اطلاعات: این ۳۰ مزدور دشمن آمریکایی - صهیونی به وقت کودتای دی‌ماه ۱۴۰۴ در شهرستان‌های محلات و نیمه‌ورد اقدام به تخریب گسترده و آتش زدن منازل مردم، فروشگاه‌های بزرگ سطح شهر، بانک‌ها، خودروهای امدادی و شخصی مردم، اماکن دولتی، چندین مسجد(از جمله مسجد جامع علیا و مسجد مهدیه بازار محلات)، حمله به ناوگان ریلی و تهدید جان مسافران، غارت اموال مغازه‌های مردم کرده بودند.
🔹
سربازان گمنام امام زمان (عج) در اداره کل اطلاعات استان مرکزی از این مزدوران شماری سلاح سرد مثل قمه، تبر و چاقو و مقادیر قابل توجهی مشروبات الکلی و مواد مخدر هم کشف و ضبط کرده‌اند.
🔸
پیشتر در بهمن ‌۱۴۰۴ هم ۷۰ نفر از عوامل میدانی کودتای دی‌ماه در استان مرکزی بازداشت شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/458614" target="_blank">📅 13:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458613">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWzzxiscPHhgWCQhZ4tOcOIIAERaHzesxMEgoAMbHwDysa8Bn1dZX0E6VmhzUFC_eqcs_7tk-aThKKBhrYQCsi4wAnC3EG2nONpeJprF21TCi7c3-UtV-P_d2hwtRDzlHoipMC0wTEtjXtbfuy_VVPx1JoFTbWXDqvFqN68Nzb1Yjbq9cInDcJRlJb7uZTGJyQhY-v0otxg4ZWG3iJWaBNDwgP2Wln24Ses48f852GsyYYQfU5gWTnMdmE6FMDZ2jlRoXEIusnT4FcbwTL_d7ewS7XjGHJgCWcKiL_HvI2EZ44kIa2WwJ6jFjZiOCS7UHLoG9lelq4KpbQNvvew7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ کشته در انفجار در شهر حسکه سوریه
🔹
یک منبع در دولت شورشیان حاکم بر سوریه اعلام کرد که درپی انفجار یک بمب در نزدیکی کاخ دادگستری شهر حسکه در شمال شرقی سوریه، ۲ نفر کشته شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/458613" target="_blank">📅 13:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458612">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85005e3e6a.mp4?token=haNODXkadd1OTaCGeOK1FUAiKK7n6JGaOqHLXxjJj7U5EtfjyuTce0QbmHBLdF-BJ0rRLIISxANVt0XeOVA4trIG3v2ueNZK4LHEAikTSP5fnDK5EngZ-X_yT_clSUAYJzF2T8-6qkG1ZXgrV9O9V3zyPTyMzXfdWPv-R0QP3ubgsyM3RSZYZisdSabxLfCdkKbvEUIMuZzqXhMmqEyRHBcBiQNBJlm5ldyI3SLnIoTl_RX_ovwr0d8kCiWGMfBqKBL4bfM94a3qmg8bfasoXlHkipr2GrQcLwLC8arPGhsGtShUnWfuDON5cjkwfiS3IlT9c9K5R-pbGrW8LxluZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85005e3e6a.mp4?token=haNODXkadd1OTaCGeOK1FUAiKK7n6JGaOqHLXxjJj7U5EtfjyuTce0QbmHBLdF-BJ0rRLIISxANVt0XeOVA4trIG3v2ueNZK4LHEAikTSP5fnDK5EngZ-X_yT_clSUAYJzF2T8-6qkG1ZXgrV9O9V3zyPTyMzXfdWPv-R0QP3ubgsyM3RSZYZisdSabxLfCdkKbvEUIMuZzqXhMmqEyRHBcBiQNBJlm5ldyI3SLnIoTl_RX_ovwr0d8kCiWGMfBqKBL4bfM94a3qmg8bfasoXlHkipr2GrQcLwLC8arPGhsGtShUnWfuDON5cjkwfiS3IlT9c9K5R-pbGrW8LxluZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیوید تیلور همچنان مشتاق رقابت با یزدانی
🔹
دیوید تیلور رقیب قدیمی حسن یزدانی گفت که همیشه مشتاق است با این کشتی‌گیر ایران رقابت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/458612" target="_blank">📅 12:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458611">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSUM5uswMEuExW_q3FTR5da6Jr5VLb-WojzWiMquCmsqJ1bvK0AYeeNoEPAFWDOThCduvM2pnbE9cIN37g_UYUY7vxfgKexbcvkWcSaJn_q4CP_RusMdCq85IVmujFTAG1c5SgMxwC2vqeT_ViYpJz5gSA-6jZmpbDwZpVNHeXcDH41XTIGkBwBn6lNdWOgTV7EV31T-GoosASLtZC6-6JFoVqYygIf8HhByL1LjyxI8sGFo7F86tRnWqdIg7Un0iH36Sgt4xuw1HJrvipFz4sJ4U3xniAXyTOldjTpnZhk2xtvIg2wf83yvnXtWUKl0ydj-sSbap9x50evTYc08vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت
🔹
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود.
🔸
قالیباف در واکنش به گزافه‌گویی فرمانده سازمان تروریستی سنتکام این توییت خود را بازنشر کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/458611" target="_blank">📅 12:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458610">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22b60f9ed.mp4?token=i3YXZOTOB8eRMqEP2gHzvVgqjj38Ju-qVPcV7DHfcq89KdDJgd_f4uPAUosLfOEZHSehJyLHo5C9m7NfWk2nshRAzBCUs2Br9RG3n1f7cC6eQ--M29MYMUEgJgcbuDz6zwJSxZOQJ_rIhlDirirY9PAIlmGQWPj8tHZZRIvktXnnxhTKP2U5wgYSYs28w9sZ6eXwX2v1QKDaV0VAIcxV9yuIheQcfxr6CjrTTc07YKez5ay6nWc-0SnY5ALFRcGjV4Xw5Y29BcPcYqjYJ2yLB1UJjgDTG5-6eB_Occq1y59vOYlQNmVknkVyDsutQD9C2E2r0koPgIW05ZddEB8dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22b60f9ed.mp4?token=i3YXZOTOB8eRMqEP2gHzvVgqjj38Ju-qVPcV7DHfcq89KdDJgd_f4uPAUosLfOEZHSehJyLHo5C9m7NfWk2nshRAzBCUs2Br9RG3n1f7cC6eQ--M29MYMUEgJgcbuDz6zwJSxZOQJ_rIhlDirirY9PAIlmGQWPj8tHZZRIvktXnnxhTKP2U5wgYSYs28w9sZ6eXwX2v1QKDaV0VAIcxV9yuIheQcfxr6CjrTTc07YKez5ay6nWc-0SnY5ALFRcGjV4Xw5Y29BcPcYqjYJ2yLB1UJjgDTG5-6eB_Occq1y59vOYlQNmVknkVyDsutQD9C2E2r0koPgIW05ZddEB8dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علت فاجعهٔ مرگبار نپال فاش شد؛ سیلی که دلیلش زلزله بود
🔹
بر اساس جدیدترین شبیه‌سازی‌های انجام‌شده توسط کارشناسان و مقامات نپالی، حادثه‌ای هولناک در روز ۴ شهریور در منطقهٔ هیمالیا رخ داده است.
🔹
بخش عظیمی از یک یخچال طبیعی فرو ریخته و حجم عظیمی از یخ، سنگ…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/458610" target="_blank">📅 12:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458609">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df21508150.mp4?token=qHsyAmmBzfD0NFwO5Aij4YUdGXN8odBPMQOeEFA3QQOxKYZNDwmSJmagYa75S9-W07KC4CUCQ9hkHJPu2ykVbolMlUiAp35FAdbyrnqpkstw6-Uz_Qy7wz5OOJUyd-fUOyyObbRjEWw6FnnsJnLqsf_1OlKmOQEQUAedr6gZP5YaeaItbk4cnSq_pmKivgNHeZtr74L3G9rsTSIKjw1Igy7U-TOGyIUkKmkYEbEoKJdy3rKWW5B6QirmVjkFTxW0oMhNUE3CA3aBHsI4Rp0GsXbONln1ku4le5FsdfqQLji1iCyN1AznR2pK3XiTXUmnfAjy5VP2ns9dv1FH0hyuXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df21508150.mp4?token=qHsyAmmBzfD0NFwO5Aij4YUdGXN8odBPMQOeEFA3QQOxKYZNDwmSJmagYa75S9-W07KC4CUCQ9hkHJPu2ykVbolMlUiAp35FAdbyrnqpkstw6-Uz_Qy7wz5OOJUyd-fUOyyObbRjEWw6FnnsJnLqsf_1OlKmOQEQUAedr6gZP5YaeaItbk4cnSq_pmKivgNHeZtr74L3G9rsTSIKjw1Igy7U-TOGyIUkKmkYEbEoKJdy3rKWW5B6QirmVjkFTxW0oMhNUE3CA3aBHsI4Rp0GsXbONln1ku4le5FsdfqQLji1iCyN1AznR2pK3XiTXUmnfAjy5VP2ns9dv1FH0hyuXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: مسئولان واقعیت‌ها را به مردم بگویند
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/458609" target="_blank">📅 12:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458608">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975b99dfa9.mp4?token=h68KW0--Pw8Y_Zl59CzN6lG-xCYgP1Q6wVdkXecoOWybFMUnwgSPM_g_jkQlR5S9zcJWXzoc6Ta-seWnnyjtJuDvHse2REJQty92rUbGt8f9yeYQUKD4KfPO1dsD9WLcYR-KG3mgjY4nfVo0O_N0qxC7gmFRSdmURwCy9lsEQqFMONx3lavGv6csdAoB4MTeb8-1EFwzKRuWHht8sd7YcPNE-rsvIq7q4VORCJXLtpRBQ0t5-RuKvP8UyA7-_l9k6vXYCwk2EXY-Df05ijuToxK-3hQgL2-rahNYQ7LINRJuJ3oKAzcqGjT9myzfhtvQUKE3_yn5GoYmnYEgsyKl9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975b99dfa9.mp4?token=h68KW0--Pw8Y_Zl59CzN6lG-xCYgP1Q6wVdkXecoOWybFMUnwgSPM_g_jkQlR5S9zcJWXzoc6Ta-seWnnyjtJuDvHse2REJQty92rUbGt8f9yeYQUKD4KfPO1dsD9WLcYR-KG3mgjY4nfVo0O_N0qxC7gmFRSdmURwCy9lsEQqFMONx3lavGv6csdAoB4MTeb8-1EFwzKRuWHht8sd7YcPNE-rsvIq7q4VORCJXLtpRBQ0t5-RuKvP8UyA7-_l9k6vXYCwk2EXY-Df05ijuToxK-3hQgL2-rahNYQ7LINRJuJ3oKAzcqGjT9myzfhtvQUKE3_yn5GoYmnYEgsyKl9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر اکتشافات شرکت ملی نفت: هم‌اکنون یک چاه در منطقهٔ «دهنو» استان فارس در حال حفاری است و امیدواریم در این منطقه نیز به کشف جدیدی دست پیدا کنیم
🔹
پیش‌بینی می‌کنیم حدود ۵ میلیارد بشکه نفت و ۸ تریلیون فوت مکعب گاز را با استفاده از دکل‌های موجود بتوانیم کشف کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/458608" target="_blank">📅 12:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458607">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f168a6e4f.mp4?token=Eu4CXsrn0YZiVOiHcaUp0sMU2fyMWcW3p152kxok7JPWFxRR2p0TTYoNyJICbzt4d87lo159kACdM4DtDTcopkYa4IvaWKo7YRBdXw_XPQPFTdlxCskr_e1LQ02I6pFzxiV3eOkWgoi6Xd8dvZ3Xy1eiu2p1Zw9qmbTm6CdgkwWXYwr_OCbAl9lHm2qLELmDRkna-U7ReoWmHiAQcBPlysjV0HT5R-OdtP-43LPkhmMMzHKa0Jd29bCwEyuX_zTwfTYdfsWCkRB7uR_nO-uLvSToqXLLvIPIAdc_XNeeGESNHL45mErKv1-hHGbjJS0y_nWebdMtlfHfQpz9_vC7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f168a6e4f.mp4?token=Eu4CXsrn0YZiVOiHcaUp0sMU2fyMWcW3p152kxok7JPWFxRR2p0TTYoNyJICbzt4d87lo159kACdM4DtDTcopkYa4IvaWKo7YRBdXw_XPQPFTdlxCskr_e1LQ02I6pFzxiV3eOkWgoi6Xd8dvZ3Xy1eiu2p1Zw9qmbTm6CdgkwWXYwr_OCbAl9lHm2qLELmDRkna-U7ReoWmHiAQcBPlysjV0HT5R-OdtP-43LPkhmMMzHKa0Jd29bCwEyuX_zTwfTYdfsWCkRB7uR_nO-uLvSToqXLLvIPIAdc_XNeeGESNHL45mErKv1-hHGbjJS0y_nWebdMtlfHfQpz9_vC7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: تفاوت نگاه انقلابی و غیرانقلابی به تفاوت در دستگاه محاسباتی برمی‌گردد
🎥
دشمن تلاش می‌کند محاسبات مسئولان را تغییر دهد. مسئولان باید در پذیرش دیدگاه‌های کارشناسی، ملاحظات امنیتی و سابقه افراد را هم در نظر بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/458607" target="_blank">📅 12:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458606">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-Oc0IDl9eZVx0Jal_hbeLxFc62DUgtAIfzzKTJCc0sMBwKV4CopzaoAaIRtRRCihUxyIJHOEyR2ui1YBpENCI_ScG5DkUTPZ7SArR70dJevIO2Q7GrOtwaa0C6sRwL0-XlQYY7CzzpiHHbHM_VKgokUiGUZijw4DVjH_-eeIrp4yh3UW9n0QXtogC7WZXXUcS9E4JfdKO5X78vygP0egqlCgtuayV2XADmFDrvmf-kTCXrFpRIGrJY6RGwalVB7UkDA5oxCb_rQSDxd72q-YcDVjcX04U49d-hqfzOn9-eK4X7xmvhRvrX0GG0cOTedcRRVK4QwZrIVcgrWs-Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیرخارجهٔ روسیه: آمریکا و اسرائیل مقصر وضعیت فعلی تنگهٔ هرمز هستند
🔹
لاوروف: تا قبل از جنگ تجاوزکارانه آمریکا و رژیم صهیونیستی علیه ایران، تنگهٔ هرمز باز و بدون مشکل بود.
🔹
تا قبل از این جنگ، صحبتی دربارهٔ اعمال عوارض بر کشتی‌های عبوری از تنگهٔ هرمز مطرح نبود.
🔹
البته ما هم نمی‌خواهیم برای عبور از تنگهٔ هرمز هزینه‌ای وضع شود، اما این موضوع جای بحث بیشتری دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/458606" target="_blank">📅 11:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458605">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0801b66378.mp4?token=QadzpOioV58jc4DwMPblQWwTknC4upbVR0hsiKX4mwe1NHmOncP7rAHlfaDJ9aflbCpK5M_n1tzniQuMjMtKylUQ9xIOQhYIY3xTn9ZSGOuNbW2YMsvo4DSXJBJYPNdgJu20GFTmhwVsHMyI16fcM3J38EJO6qoLTuXyTPbDy23hf2IW2Adn8-f7jefx1zcD3aMAY9J2fk4kVuHmo93nts6vsjM8xG5n1uxxUNmcyE4QSEAzhAJ6krP2DNNFfIhPIpUuk6eIDpy0OOe9GttZAUVRsbQz4X6o3YxSn7E_2P-jXfJXwfux1woRTw9iz9w4g8JGogdBdVRC1iLvgvpXjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0801b66378.mp4?token=QadzpOioV58jc4DwMPblQWwTknC4upbVR0hsiKX4mwe1NHmOncP7rAHlfaDJ9aflbCpK5M_n1tzniQuMjMtKylUQ9xIOQhYIY3xTn9ZSGOuNbW2YMsvo4DSXJBJYPNdgJu20GFTmhwVsHMyI16fcM3J38EJO6qoLTuXyTPbDy23hf2IW2Adn8-f7jefx1zcD3aMAY9J2fk4kVuHmo93nts6vsjM8xG5n1uxxUNmcyE4QSEAzhAJ6krP2DNNFfIhPIpUuk6eIDpy0OOe9GttZAUVRsbQz4X6o3YxSn7E_2P-jXfJXwfux1woRTw9iz9w4g8JGogdBdVRC1iLvgvpXjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کوثری، نمایندهٔ مجلس: سپاه از سال ۶۶ برای بسته شدن تنگهٔ هرمر برنامه داشت
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/458605" target="_blank">📅 11:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458604">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THOeq5drr4QiYZL365ZKUKPOXCta-kfj4ACUiR1EkA-ZfF6NOPzYbu1oCxdfClhJE92wIN7KyK4RrPseYmjz8NIOkjRaN9q4CeZhZl9431sH2Fa0ilwr2GH9eZ_36UU1n3PvkMdL0vZuETgw8qSWonjclK4KhiuVygeQ-ivjnrwcuZQldwxAZ43o-uEEZFwU5pHbHQppURi_R3dvTrYZorJlXUBTP8xrnkmH1v28lJZMnVv68k1en2Wvg7gjQ-wyt4gYjdVlIpVmzV4kj1dVowtqYvK8Scl9a--rOBx40hFe-zrgtuU_62JypSoXNrxnlN4Qq68R-zBDKPOsBHLs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید چین بر لزوم دیپلماسی برای حل بحران آمریکا و ایران
🔹
وزارت امورخارجۀ چین بار دیگر خواستار توسل به دیپلماسی و اجتناب از اقدامات تنش‌زا بین آمریکا و ایران شد.
🔹
سخنگوی این وزارت‌خانه روز جمعه طی نشست خبری گفت: «گفتگو و مذاکره تنها راه خروج از بحران آمریکا و ایران است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/458604" target="_blank">📅 11:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458603">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16075b86e8.mp4?token=luM9siB8HsiGmCqlJwgHEIMvatOIaNtAxxfnujXO4BOJLQ7KoFvzWOvt6LVVJeFymHBq43q6FdTCf-2_fW9fLd_tJeXKVy-Tt1m0NyrSYBxsUIU_x2L7LYPM-985WoNP4eGAXH4ICtugazJaybgN-Zba3Q9EY1Q_8gLoURhup0UaBV19rKWz_8dhXhoEr7agpoc3w2V29CyZryxTfte4WCwIC8hxdQCPsKyugz_VzlGiq0Cs0cCiq68uz8tiRM5bmsc35Hdhuk7yWjVBFPlmBAVEzRAy9W1EYVBuuAU3Hts6PB6sPVmlT8PvAwZooTXca_lej42yQfBsHgA5DOXPwz5ZhHUhL5v7YW5DUgAzhcv4UuZcl-gvuBLTabVShXELMyedTq--V_jUtJNLQ8OLbvlAUleKL1v6Ft8GnoV7uNtAZiZ_wvpxoRpxWRv3r-h4OIW3vpn6wwk2V_7TTcCOwGt-bYv98mTToGJvj3ByBnvwz3tA3JHusO9zU39EIboVgfY4W_JDhJUAn70CArsD5hWwOYYC0NoVjoWVTAQlF1S2XqcHaeaTye_RjX-5ZgjWvqoIsizjkd9pv63TSuf5xbqg6k_6I1iVYdOpUXVoSU33GHxMM4LRepjuwPtZwGdM-xv87JbpeD61qibe8DRw8fjYcaD5HAKeOUSc1Af0fbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16075b86e8.mp4?token=luM9siB8HsiGmCqlJwgHEIMvatOIaNtAxxfnujXO4BOJLQ7KoFvzWOvt6LVVJeFymHBq43q6FdTCf-2_fW9fLd_tJeXKVy-Tt1m0NyrSYBxsUIU_x2L7LYPM-985WoNP4eGAXH4ICtugazJaybgN-Zba3Q9EY1Q_8gLoURhup0UaBV19rKWz_8dhXhoEr7agpoc3w2V29CyZryxTfte4WCwIC8hxdQCPsKyugz_VzlGiq0Cs0cCiq68uz8tiRM5bmsc35Hdhuk7yWjVBFPlmBAVEzRAy9W1EYVBuuAU3Hts6PB6sPVmlT8PvAwZooTXca_lej42yQfBsHgA5DOXPwz5ZhHUhL5v7YW5DUgAzhcv4UuZcl-gvuBLTabVShXELMyedTq--V_jUtJNLQ8OLbvlAUleKL1v6Ft8GnoV7uNtAZiZ_wvpxoRpxWRv3r-h4OIW3vpn6wwk2V_7TTcCOwGt-bYv98mTToGJvj3ByBnvwz3tA3JHusO9zU39EIboVgfY4W_JDhJUAn70CArsD5hWwOYYC0NoVjoWVTAQlF1S2XqcHaeaTye_RjX-5ZgjWvqoIsizjkd9pv63TSuf5xbqg6k_6I1iVYdOpUXVoSU33GHxMM4LRepjuwPtZwGdM-xv87JbpeD61qibe8DRw8fjYcaD5HAKeOUSc1Af0fbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقادهای تند شاه از بی‌عرضگی پدرش در ماجرای تسلیم ایران به متفقین
وقتی که حتی محمدرضا پهلوی هم نمی‌تواند ناکارآمدی و بی‌کفایتی رضاخان را تحمل کند و هویدا نیز پیامدهای شوم فرار وی و اشغال ایران را شرح می‌دهد!
@Fars_plus</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/458603" target="_blank">📅 10:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1171c62e65.mp4?token=mjhAJFeKR37TUZECwYfwz3nvTE4fLqMqjygOrSbkEqVFsgUKZ1AMu-B9RyD5oXXyT5-ywZygAumGL2n_GweKF7EEcUP2om360SAG6p7KchMuFpR_byKGboO9T6OAwp6UDSQRp9KNlHxplcbaU1DvyjqTZnV1K0Sodx2UK3GQWtiQ8t04uySDIVfzbqtWfoVw5ubRlE1fYJwbLWorO0AR4QRWWGG1vIv1U8rsLAQ1XA72KJrQYbqp1H9eiwQIabPs5UguNaod9o0vJaBarrtSC-3LpVeUKDaoGpeQf0xnxFsoEWSbLYuNGFKqG1RVh0TvSUmuLhSuN23g7BmMKkiw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1171c62e65.mp4?token=mjhAJFeKR37TUZECwYfwz3nvTE4fLqMqjygOrSbkEqVFsgUKZ1AMu-B9RyD5oXXyT5-ywZygAumGL2n_GweKF7EEcUP2om360SAG6p7KchMuFpR_byKGboO9T6OAwp6UDSQRp9KNlHxplcbaU1DvyjqTZnV1K0Sodx2UK3GQWtiQ8t04uySDIVfzbqtWfoVw5ubRlE1fYJwbLWorO0AR4QRWWGG1vIv1U8rsLAQ1XA72KJrQYbqp1H9eiwQIabPs5UguNaod9o0vJaBarrtSC-3LpVeUKDaoGpeQf0xnxFsoEWSbLYuNGFKqG1RVh0TvSUmuLhSuN23g7BmMKkiw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل ویرانگر نپال به ۴۶۹ نفر افزایش یافت؛ ۱۵۰۰ نفر مفقود
🔹
پلیس نپال از افزایش شمار قربانیان سیل ویرانگر در دامنه‌های هیمالیا در مرز این کشور با چین به ۴۶۹ نفر خبر داد و اعلام کرد جستجو در میان گل و لای و آوار ناشی از سیل و رانش زمین برای پیدا کردن…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/458601" target="_blank">📅 10:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3KENMKDICR0WOCD95sGHMRKU0G22e_1JHhGobjNoARx1YIOFaG1P040a4XC-mwRbAH1Ususzx0yrcLcC8T3FozfQ1ApEaly130KqnZjQ7EdIP0hGte2jFH4H3Bs3nPljLQPgfIT0ZMwvk8SBO9twemltlEoDtae4JFjXvSceTB5xZUpy0lNIiVRD2jcRD08xv6hj1gcUtkIA9YwCZwwqWaPDyHTqGE5X5tOrjEWwCGj1aw8kSSZ9eJHv2othVn-4tzpu5VACTJY1EY4OYlrukVEsw-8XZCoBtsiS9rM68uu69N4J8sYMcsJl1caKRY2BI0B6yBuYtf7KCdvE-LMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر جدید صادرات نفت ایران باز شد
🔹
موسسه تحقیقاتی و تحلیلی در بخش نفت‌وگاز، اچ‌اف‌ار می‌گوید، «هیس، سنتکام متوجه نیست که آمار نفتی‌ای که دارد اعلام می‌کند، شامل نفت ایران هم می‌شود.»
🔹
ساعاتی پیش سنتکام اعلام کرد که ۷۵۰ میلیون بشکه نفت برای عبور از تنگه هرمز اسکورت کرده که هیچ بشکه نفتی از ایران در میان آن نبوده است؛ چند ساعت بعد، شرکت کمک‌کننده به رهیابی محموله‌های نفتی ایران به آمریکا، تنکرترکرز محاسبه کرد که این رقم یعنی روزانه ۶.۵ میلیون بشکه نفت.
🔹
اما اکانت ردیابی‌های دریایی منچ اوسینت می‌گوید که پایش‌های ماهواره‌ای نشان می‌دهد که یک نفتکش مرتبط با ایران در حال ترک منطقه انتقال کشتی‌به‌کشتی است و این اولین بار نیست که نفتکش‌های نفت یا LPG ایرانی در این منطقه یا در یکی از بنادر امارات یا عمان دیده می‌شوند اما تنکرترکرز ترجیح می‌دهد «به دلایلی این موضوع را نادیده بگیرد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/458600" target="_blank">📅 10:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70deccbfb.mp4?token=LjR27Day_0qadqkXqZOL_SLsK8GuS_w4t_gWUSULY076Ws1TP1IUMlHBA5vMkHogV2gfhnhbZzGsDAk2I1oGt2GBaSyght02HedxGtJA0nFiECZQdWcyKlfLRnLuZZTUN-x8N_lo2aGVERKRWy4TOW8qVWErGlD8kugPUuxOhGyasNTbv_-KWZRDrJcWs6B2Ke9sgzODX5lXHlue7FMpM71X-pkiqCuBH1ATBQs6ujT3WsF5ajE3bFVME9-gvhxkeDjU2ezwrXtyFkhefEqmtGPjzotLPKMJ52TXG-ENfRyi-F9gy5Xtzn9NNLc13hW2D0YJsfC9OZ7uZyO7xc6-tq5QWjNJPPbk5_oQxLnWB28Gp6RXfkKktXwY94G_96qxLnrIB5uAZLEz6CzYez-M4d_F4xlF0KnmmCuwk6JvLPifBFltw2o91Uz0g-gONucm9RGtc32kyicHcQG1PANkeQ4Ca0bfOET3j6XXyzeMB5-w2AEDvprqW7CoKk_3jCtjJOG_innYnegmQjQZPMVFjsl1xnuXqjTJcTwMFjBDxKwN2y2m2LbtZHNx0Qpvload4oeoGYA3ONzMs-yos-Ci_l6sUakoOAsId6IOEhXkfLW-7Ms7k8XMA0bevoTCmXr8rSNBloI5Bw030EM_jXQiPOpbgrimsQqewMbTBH0hY1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70deccbfb.mp4?token=LjR27Day_0qadqkXqZOL_SLsK8GuS_w4t_gWUSULY076Ws1TP1IUMlHBA5vMkHogV2gfhnhbZzGsDAk2I1oGt2GBaSyght02HedxGtJA0nFiECZQdWcyKlfLRnLuZZTUN-x8N_lo2aGVERKRWy4TOW8qVWErGlD8kugPUuxOhGyasNTbv_-KWZRDrJcWs6B2Ke9sgzODX5lXHlue7FMpM71X-pkiqCuBH1ATBQs6ujT3WsF5ajE3bFVME9-gvhxkeDjU2ezwrXtyFkhefEqmtGPjzotLPKMJ52TXG-ENfRyi-F9gy5Xtzn9NNLc13hW2D0YJsfC9OZ7uZyO7xc6-tq5QWjNJPPbk5_oQxLnWB28Gp6RXfkKktXwY94G_96qxLnrIB5uAZLEz6CzYez-M4d_F4xlF0KnmmCuwk6JvLPifBFltw2o91Uz0g-gONucm9RGtc32kyicHcQG1PANkeQ4Ca0bfOET3j6XXyzeMB5-w2AEDvprqW7CoKk_3jCtjJOG_innYnegmQjQZPMVFjsl1xnuXqjTJcTwMFjBDxKwN2y2m2LbtZHNx0Qpvload4oeoGYA3ONzMs-yos-Ci_l6sUakoOAsId6IOEhXkfLW-7Ms7k8XMA0bevoTCmXr8rSNBloI5Bw030EM_jXQiPOpbgrimsQqewMbTBH0hY1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت پدر و مادر ۲ شهید از روز تلخ مدرسهٔ شجرهٔ طیبهٔ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/458599" target="_blank">📅 10:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458598">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpjIK_H-51RkFuHII2nHjVyqPT30oT8OqG5q_bPsZCp61goXFyr4_ZSjiGD537sz70ErnefiTWTTzfRPYf-jSMmbDs2wK2s5B-on_G4rXJF-3rHJlJllmV7j6Lp425CR_yHSdvNv0mrnk7LEvRN3EuB7a5c7IAESJiYDH96P4bAxUjsaJ5YUBbT3f8uXpGYM04dVe40CeGFnbr1rO1a3Kr7D6qxRn5a-5xUj_gI7ZR6nJXcOjrJfxIfQTF3RfO3871JEfG3jy5c2OpeO0tOvFZyQCRy40YoVZWrDC5Eg9GNEz_fTQwh6s3uoVUgnit5H3dZguRP1VyXKBKeTykCwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرالد پنجم پادشاه نروژ درگذشت
🔹
منابع خبری از فوت هرالد پادشاه نروژ در سن ۸۹ سالگی خبر می‌دهند.
🔹
روز گذشته کاخ سلطنتی نروژ اعلام کرده بود که وضعیت سلامت هرالد پنجم که به دلیل بیماری خونی در بیمارستان بستری است، رو به وخامت گذاشته و او در وضعیت «بسیار وخیمی» قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/458598" target="_blank">📅 10:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7447ddb869.mp4?token=mlz2HrP0KFRBhYR1BQhueRVDT0ppGL4z85-X8uBS4rb4nK6c-vqGoPNsZJNdSWIoQHiC8toKvAUfo_D-40gPEgG0KL12eIAKIwCMMtSNGAdug4vUFBndgWzLrKsuHJETzZof6xrOS1dGq0T2hbDC6Dt_NOqh9cDTYUVsgPdRZ4zuUsH4AoKGdC6gpHlIssaAq5QhaMZfoBS9HOLaAkcT97wSP80n5gV56YZZTA-aAa7T3kQB7sgYZl3Q1kAo0u_q3dWqsF9mpuDfUTN5cq52N6dTfBk-13l4pNgBZDqJtQtCGR-dp5qEwXpqtYFvEnGYrrzckW7RGxU5_Tb5AwQc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7447ddb869.mp4?token=mlz2HrP0KFRBhYR1BQhueRVDT0ppGL4z85-X8uBS4rb4nK6c-vqGoPNsZJNdSWIoQHiC8toKvAUfo_D-40gPEgG0KL12eIAKIwCMMtSNGAdug4vUFBndgWzLrKsuHJETzZof6xrOS1dGq0T2hbDC6Dt_NOqh9cDTYUVsgPdRZ4zuUsH4AoKGdC6gpHlIssaAq5QhaMZfoBS9HOLaAkcT97wSP80n5gV56YZZTA-aAa7T3kQB7sgYZl3Q1kAo0u_q3dWqsF9mpuDfUTN5cq52N6dTfBk-13l4pNgBZDqJtQtCGR-dp5qEwXpqtYFvEnGYrrzckW7RGxU5_Tb5AwQc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیلاب در نپال به ۱۵۷ نفر رسید  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/458597" target="_blank">📅 10:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458596">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfiKj2V9aE1LSjTbU3ljkRBl5O9QDsPGuQEa6d5IeSv-a42_K8bhH2DnXZNoLWY8CWWf16nR3LuYedwdm_i4c6kaz6SQCqz2UFht2iaPnOHmIVdkqGRUyquWtf39tCIYKrl3vai9qfnWd5hedj7OCl2XciLLYRS8NCpKi3AXUcRaPgYW6zYZiPsqFK7YeG7Lf63pMnuoESmzqHqqQSPmzJ8VwGuqla0VBdc-uQcsUTxk7x7rWypVwvawN7Zdxlgzar_GpDKbJVYW43YTmxPUEkLsrv2e9dbzIcspmJghyguqA2F2WcpkTfn6_nP0i7HJg6BpXV8uS43FLP9sZwWlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: آمریکا باید یک واقعیت ساده را درک کند؛ فشار نتیجه نمی‌دهد
🔹
با نخست‌وزیر و وزیر امورخارجهٔ قطر، گفت‌وگوهای سازنده و مبتکرانه‌ای در تهران داشتیم.
🔹
بازگرداندن دیپلماسی به مسیر خود ناممکن نیست. این امر به درک یک واقعیت ساده از سوی آمریکا بستگی دارد: فشار نتیجه نمی‌دهد. آمریکا باید اعتماد ایجاد کند، با احترام سخن بگوید، حقوق ما را تصدیق کند و به تعهدات خود پایبند باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/458596" target="_blank">📅 10:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458595">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf3da1cac.mp4?token=RjXHkeS9x31C0ieDrdabMWTdxxhVwwdQ8mPhTEzWDa_aNbcofs_SdJq9jK83P5Bqydo98o7E7hVP7Rw1Sbk9Djj6DYNtn9L5zcjmmk1CUxeduy9jALAkb8nRWGPpKJAva8ag5oU01C07cAj-adCj4LEKKrbn-Wp3K8Bp2ZK6FeKZA5nCc2hN4cusdk8KwhUWf5gOzEsZl1X69_HfMhoO8suReF5U2G39wO918QzIp8niCaWzcYDPZ3pmnfrd_kULTGlm4eW-Rbdm7DzqytPAgo68XZykQU9rjs8wsF8enhSC_JDo1OqUoole_JRK7xFLUHs9yRza_0xvCa--dPk1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf3da1cac.mp4?token=RjXHkeS9x31C0ieDrdabMWTdxxhVwwdQ8mPhTEzWDa_aNbcofs_SdJq9jK83P5Bqydo98o7E7hVP7Rw1Sbk9Djj6DYNtn9L5zcjmmk1CUxeduy9jALAkb8nRWGPpKJAva8ag5oU01C07cAj-adCj4LEKKrbn-Wp3K8Bp2ZK6FeKZA5nCc2hN4cusdk8KwhUWf5gOzEsZl1X69_HfMhoO8suReF5U2G39wO918QzIp8niCaWzcYDPZ3pmnfrd_kULTGlm4eW-Rbdm7DzqytPAgo68XZykQU9rjs8wsF8enhSC_JDo1OqUoole_JRK7xFLUHs9yRza_0xvCa--dPk1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار جدید در پالایشگاه یاروسلاول
🔸
نیروهای اوکراینی با اجرای یک حملهٔ پهپادی در مقیاس وسیع، موفق شدند پالایشگاه نفت «اسلاونفت-یانوس» در استان یاروسلاول روسیه را هدف قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458595" target="_blank">📅 10:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458594">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e1f26f10.mp4?token=A_G52vjIU-UAemcuq4OcmGiEv-cp2OqY6h-aBHan56d5Wcy7ovulYkUMk7nBZgQWfTiUtJhARYweC35vGDJRmUV5rHoL26w7RlsY-tUtcKNWE-GruxioxpRDLfNtF6NAobSVm9J3nZUA4jhtIxGaNrbNQJo5UMri9Mfv3P9kuumbs5U3HFFYxOjlLEMmnjHPNk7sRD0-iAkDMcCx8DR-dVduTzXduLqhvafr9tFcnu0LdChaLVFgpnTetrMyff92bRN3c9sXk-AIFXPnqC6Vj17q2NS1qHGIum7gSLmO_b6DF9Kt8s-aYf5FDeGDhn0o2mAqWZ1htuDloPKqH4q2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e1f26f10.mp4?token=A_G52vjIU-UAemcuq4OcmGiEv-cp2OqY6h-aBHan56d5Wcy7ovulYkUMk7nBZgQWfTiUtJhARYweC35vGDJRmUV5rHoL26w7RlsY-tUtcKNWE-GruxioxpRDLfNtF6NAobSVm9J3nZUA4jhtIxGaNrbNQJo5UMri9Mfv3P9kuumbs5U3HFFYxOjlLEMmnjHPNk7sRD0-iAkDMcCx8DR-dVduTzXduLqhvafr9tFcnu0LdChaLVFgpnTetrMyff92bRN3c9sXk-AIFXPnqC6Vj17q2NS1qHGIum7gSLmO_b6DF9Kt8s-aYf5FDeGDhn0o2mAqWZ1htuDloPKqH4q2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمؤمنین(ع) در آستانهٔ میلاد پیامبر(ص) گل‌آرایی شد
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/458594" target="_blank">📅 09:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458593">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به مناطق جنوبی لبنان
🔹
خبرگزاری ملی لبنان از حملهٔ توپخانه‌ای رژیم صهیونیستی به شهرک‌های «حولا» و «وادی السلوقی» در جنوب لبنان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/458593" target="_blank">📅 09:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458592">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr1zR58UrRO3sVdYUm7MNz_LPqOipPaYe-nT0Ax5Ue6ZqeTTg-xWWMRZQmfEfl7qt-yT23w1wKGkkf5sO01mpoBhlGSLpMEbyM1C92Drh-ezX354eROdUYF-_3rBXRZDL8h8ArTS2oE9bxUdYDSipFYTfMJhSRwNxlUNGFxmbInzMUB2eVE8HVbJhVCRkpvbEnQ0W47TRPdXBlLPm2PiT0fNvDg7lUIMA1bd9DKZGvJZyqZNeXyutWeDmrn3dDcAw7IoKML22cCxPKziiBh76DBtSA9hcH-4XA-EeMZX867LwzUo7VJtjdgfmhW_Gj7YkfRrIV09NHfTh-U-R3ygLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پیش از آشوب، روایت کشته‌سازی را کلید زد
🔹
رئیس جمهور آمریکا با طرح این ادعا که حکومت منتظر معترضان با تک تیرانداز و مسلسل است، پیش از آن‌که اساساً چنین رخدادی اتفاق افتاده باشد، درحال ترسیم چارچوبی رسانه‌ای است که در آن، هرگونه اتفاق درجریان یک آشوب احتمالی، از پیش به جمهوری اسلامی منتسب شود.
🔹
موضوعی که در اغتشاشات دیماه سال گذشته به شدت با خبرسازی و آمارسازی نجومی دنبال شد و حالا همان سناریو پیش از اجرا توسط ترامپ کلید خورده است؛ موضوعی که پروژهٔ آمریکا برای ایجاد آشوب در آینده به خوبی برملا کرده و لو می‌دهد.
🔹
ترامپ پیش‌تر در جریان جنگ تحمیلی رمضان بارها از ارسال گسترده سلاح به گروه‌های مسلح تجزیه طلب برای انتقال به هسته‌های آشوبگر سخن گفته بود.
🔹
موضوعی که نشان می‌دهد در کنار فشار سیاسی و رسانه‌ای، ایجاد ظرفیت میدانی برای تشدید ناامنی نیز بخشی از محاسبات طرف آمریکایی بوده است.
🔹
از سوی دیگر، طی ماه‌های اخیر برخی گروه‌های مسلح مخالف جمهوری اسلامی که مورد حمایت آمریکا و رژیم صهیونیستی قرار دارند، آشکارا از ضرورت «قیام مسلحانه» و حرکت اعتراضات به سمت خشونت سخن گفته‌اند.
🔹
تجربه بحران‌های منطقه‌ای نیز نشان داده است که در جنگ‌های ترکیبی، روایت رسانه‌ای گاهی حتی پیش از وقوع حادثه ساخته می‌شود.
🔹
بنابراین مسئله فقط احتمال وقوع آشوب نیست؛ مسئله مهم‌تر، آماده‌سازی افکار عمومی برای نحوه تفسیر پیامدهای آن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/458592" target="_blank">📅 09:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458591">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770e915a1a.mp4?token=CPncIX88zjRHr2mkV4l9N3wjSrxvDlIQ971nveJSAdglb5_N4MAlRqkJzCy_6iJd5pT8oLqxoWczeDVvFCjV3uBwHe671IZYvqo6kawcJKU4oaVQb28-EpxF1xVZ50lTHvB8f1I1kw5Mi-WkS4g1DzLLysg1alPHcNS3Pu4GWQsBrM8atb9TIkKqqca28WQ5T6FEQhdnsMK1T-Q-A69O-2eYTwX4H25fcVQ2trhTikvTdpPDzIfrNqPUrVGdiQ642tqDaXzL1KsZ4IufcN-MjH3x99WYnQHz6S-GihU1PGfVT_ZZqyKwRP5At9hN4vVjagYKaXXkzh-2QGgPtSzDt0dTKALwaaWzBQ2K4wUdIOVBBQR2d_qNP_R4Q_v5LgJu4SkQuVBVUe1AVq-IgCmYCW-9-l5uYdy1p7jx1V5e83o1YYckALbK2gIVSmzwGsahX6djLNrO78gOXFJbCBMsaEJZA1Wvu75Stlx0hYCO9p6MQPztyokwscQGkH_EZuj0mKMh3ZtAwdQg6dESdnQofFwozI-QCmx5gKOk6L3CKlvSLAJEeSLyAyCXbP0Ah3_crbesF7PBKAiIVeUghoJcCPip7s379ARelum3luo7eC6GdZi-w7G6dco8bY8aUSiH5GU9-bA2fzrurhv3mKz62mEdHCxCwBJc8Y8xqq_bnWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770e915a1a.mp4?token=CPncIX88zjRHr2mkV4l9N3wjSrxvDlIQ971nveJSAdglb5_N4MAlRqkJzCy_6iJd5pT8oLqxoWczeDVvFCjV3uBwHe671IZYvqo6kawcJKU4oaVQb28-EpxF1xVZ50lTHvB8f1I1kw5Mi-WkS4g1DzLLysg1alPHcNS3Pu4GWQsBrM8atb9TIkKqqca28WQ5T6FEQhdnsMK1T-Q-A69O-2eYTwX4H25fcVQ2trhTikvTdpPDzIfrNqPUrVGdiQ642tqDaXzL1KsZ4IufcN-MjH3x99WYnQHz6S-GihU1PGfVT_ZZqyKwRP5At9hN4vVjagYKaXXkzh-2QGgPtSzDt0dTKALwaaWzBQ2K4wUdIOVBBQR2d_qNP_R4Q_v5LgJu4SkQuVBVUe1AVq-IgCmYCW-9-l5uYdy1p7jx1V5e83o1YYckALbK2gIVSmzwGsahX6djLNrO78gOXFJbCBMsaEJZA1Wvu75Stlx0hYCO9p6MQPztyokwscQGkH_EZuj0mKMh3ZtAwdQg6dESdnQofFwozI-QCmx5gKOk6L3CKlvSLAJEeSLyAyCXbP0Ah3_crbesF7PBKAiIVeUghoJcCPip7s379ARelum3luo7eC6GdZi-w7G6dco8bY8aUSiH5GU9-bA2fzrurhv3mKz62mEdHCxCwBJc8Y8xqq_bnWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه ساحل عاج: وحدت مسلمانان معادلات قدرت در جهان را تغییر می‌دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/458591" target="_blank">📅 09:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458590">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807e5d4f72.mp4?token=FvODHoBUxltmVO-AzQJYPiDGob69lKxq0pujg_XlakMofTm9qC-d-7oZmZlj2WznHPVglr5hvo-ruH4RjF-GjH83PrCsOuzyu2gPvaUU9-2TI8cmeALC3B37Ph0DCuBt_ku6gpl0ThnHBiPPK29QEJ9hgDAbsSI9GYp3qXGgEN_BHmknlPgnIUTWyuSYzLJa-4O-Gop1nPhX3YIKsKCkJ98liTa2meaz_hIgaSS6eXZci6hXyXtgdASsSyULD9thvYpZSpTOl1Ap4fLbYAie_7hseVU0ccMA_BX4Goq9wu3PVeRB7sPhvDsChFrTCkJB-FoaLv-i8dNfoaoxuVUAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807e5d4f72.mp4?token=FvODHoBUxltmVO-AzQJYPiDGob69lKxq0pujg_XlakMofTm9qC-d-7oZmZlj2WznHPVglr5hvo-ruH4RjF-GjH83PrCsOuzyu2gPvaUU9-2TI8cmeALC3B37Ph0DCuBt_ku6gpl0ThnHBiPPK29QEJ9hgDAbsSI9GYp3qXGgEN_BHmknlPgnIUTWyuSYzLJa-4O-Gop1nPhX3YIKsKCkJ98liTa2meaz_hIgaSS6eXZci6hXyXtgdASsSyULD9thvYpZSpTOl1Ap4fLbYAie_7hseVU0ccMA_BX4Goq9wu3PVeRB7sPhvDsChFrTCkJB-FoaLv-i8dNfoaoxuVUAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌خوردن «شاه روباه» در حیات‌وحش بهاباد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/458590" target="_blank">📅 09:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458589">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مسیر شمال به جنوب کندوان بسته می‌شود
🔹
پلیس راه مازندران: ساعت ۹ صبح، مسیر مرزن‌آباد به سمت جنوب به‌طور موقت بسته می‌شود.
🔹
همچنین از حدود ساعت ۱۲ ظهر، تردد به سمت شمال یک‌طرفه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/458589" target="_blank">📅 09:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458588">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZEVYj5ZAEUEPOjLyqx4ycItiHEOoeY6qK6pqsVkQ1ygWZ54ctWh7WAW2juA5H9Ou2u1ZTnsv-KAM4UrKCoux7TCcTikCTvw0b8yfELjeBjpPfcfaoJ6SG-rhatH3A2pR4XInBYrXT9sijYE8vrMRcD7m42_kA7gJA8LaI7jTgtBU5yhZxgfdSEWhJbxlLebOpiGJO2uY2fzCcLlJ5ZIUmiZl_HrlBWztXPJu0wbYf70eMRc1jpp6V9Iw2JWRyDe8gMc872TkPih3lz1b5o_Afmy4CqFVkETiiEVbVW7DhZERxF21V6FId5A-FW49cMIjpcs6OySCYATTqRmplNI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدرالحسینی: دشمن به‌دنبال غافلگیری نظامی ایران است
🔹
سیدرضا صدرالحسینی، کارشناس مسائل بین‌الملل: این سؤال وجود دارد که آیا مسیر نظامی به‌طور کامل برای آمریکایی‌ها بسته شده و آن‌ها راهبرد نظامی خود را تعطیل کرده‌اند؟ اعتقاد من این است که چنین اتفاقی نیفتاده است.
🔹
جنگ ترکیبی که از ابتدای درگیری به شکل‌های مختلف علیه ملت ایران دنبال می‌شد و رهبر شهیدمان نیز پیش‌تر نسبت به ابعاد آن هشدار داده بودند، در شرایط جدید افزایش خواهد یافت.
🔹
آمریکایی‌ها به دنبال آن هستند که مجموعه‌ای از اقدامات را به‌صورت هم‌زمان دنبال کنند؛ یعنی در کنار افزایش تحریم‌ها و فشار اقتصادی، جنگ اطلاعاتی، امنیتی و رسانه‌ای را نیز تشدید کنند.
🔹
در کنار این اقدامات، احتمال زمینه‌سازی برای غافلگیر کردن ملت ایران و نیروهای مسلح و انجام مجدد عملیات نظامی نیز در محاسبات دشمن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/458588" target="_blank">📅 08:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458587">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070bfe7e97.mp4?token=tsXATxe7kqjxwcSwlt_0K3D52BMmuhRF4TBs8E1k4ewfhDeS3hs_1j0W_swxAHn-N-L4C6N2zyUlkUJNqiWy0AiLkhamIwp_sZIyS2bil5G1T4toLZF77H7wNS_oCuKm0JBAX-BxeyKe7rJJKN6o-0g3XuRjgy2CSiGcPRwCzUe7nfYYOGO55j17LhJILzswNoCKLgnuspUVCMVMWQiLQxxlNrQuGPVdz5o_XwPOlVMh41ED3ogyR7hLvBle6-K_9CXqbWCOau-yLvkQ1kBodA12tdbqjQl29H6oelBdb6C3gHVF2mutcX_Z9rUwRPpuGVBIrwlLryu18gZxiY8JdCl1_zkeGLDUcyA8HxqjuvIBz4pNPgkzh7kssgpnKAt-16D9BDJOBocm1fJOfaQcGroryQpR4caA_cj1w-62Lhp07_wxN33h1mSy1F70JYNLXSwC0YXnqxVhbvmtc26wSvMllPDAedru8t-NvTOtWZ3Lv53DgJnhrVfFvxigEukR0yeHc5lGQtkvqxRxVH0OtEf7N2GhmDQyZq_3VUi3Q9v-KbupurhxpEVyUTCFQSpWIp0ROg02FcXT5v_j6mSy7420RXH2DUpOYZTuXhhrmL0IFNAm3XL0AAdRbJMA0m59av7adVh7o4MU1iCvyhJrAnfHPf-rT6rEDAfZcHe7Kfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070bfe7e97.mp4?token=tsXATxe7kqjxwcSwlt_0K3D52BMmuhRF4TBs8E1k4ewfhDeS3hs_1j0W_swxAHn-N-L4C6N2zyUlkUJNqiWy0AiLkhamIwp_sZIyS2bil5G1T4toLZF77H7wNS_oCuKm0JBAX-BxeyKe7rJJKN6o-0g3XuRjgy2CSiGcPRwCzUe7nfYYOGO55j17LhJILzswNoCKLgnuspUVCMVMWQiLQxxlNrQuGPVdz5o_XwPOlVMh41ED3ogyR7hLvBle6-K_9CXqbWCOau-yLvkQ1kBodA12tdbqjQl29H6oelBdb6C3gHVF2mutcX_Z9rUwRPpuGVBIrwlLryu18gZxiY8JdCl1_zkeGLDUcyA8HxqjuvIBz4pNPgkzh7kssgpnKAt-16D9BDJOBocm1fJOfaQcGroryQpR4caA_cj1w-62Lhp07_wxN33h1mSy1F70JYNLXSwC0YXnqxVhbvmtc26wSvMllPDAedru8t-NvTOtWZ3Lv53DgJnhrVfFvxigEukR0yeHc5lGQtkvqxRxVH0OtEf7N2GhmDQyZq_3VUi3Q9v-KbupurhxpEVyUTCFQSpWIp0ROg02FcXT5v_j6mSy7420RXH2DUpOYZTuXhhrmL0IFNAm3XL0AAdRbJMA0m59av7adVh7o4MU1iCvyhJrAnfHPf-rT6rEDAfZcHe7Kfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای یک آهنگر هرمزگانی که با ام یک پهپاد لوکاس زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/458587" target="_blank">📅 08:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458586">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322a6b6211.mp4?token=jq1Qw0xYdlbg8mvAuocApYaDHozVWw1m7jl3r_fxE7w4Itnk9b3CkWh5ga_50oOOiUXWQKz27bV6JqvX3lvY92_lQsk8_jUsSWRnt5WRJPMnqMtp5yDtDsM2zK3KnXYD_sofmCJRorQR_12jHqWT-GbwbevLLsmokHjYMaSklP_VLj5TuLi-ZUL7WCulFiXsv29E2xLVRQU7lsKu6hDG4Vj-FLSo_kCqqSNy_iCsVqPf20rakn9pKE_a7d_w51Y2kxxkuBS_x9d8cOrSrBQpkwEIa9WJFZckHelyPC-LfA9W7BA6_QHpaSpUmZQFq3YXJcZi3wZ9I2dUQaRDTIEP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322a6b6211.mp4?token=jq1Qw0xYdlbg8mvAuocApYaDHozVWw1m7jl3r_fxE7w4Itnk9b3CkWh5ga_50oOOiUXWQKz27bV6JqvX3lvY92_lQsk8_jUsSWRnt5WRJPMnqMtp5yDtDsM2zK3KnXYD_sofmCJRorQR_12jHqWT-GbwbevLLsmokHjYMaSklP_VLj5TuLi-ZUL7WCulFiXsv29E2xLVRQU7lsKu6hDG4Vj-FLSo_kCqqSNy_iCsVqPf20rakn9pKE_a7d_w51Y2kxxkuBS_x9d8cOrSrBQpkwEIa9WJFZckHelyPC-LfA9W7BA6_QHpaSpUmZQFq3YXJcZi3wZ9I2dUQaRDTIEP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: دمای تهران در روزهای آینده کاهش می‌یابد
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/458586" target="_blank">📅 08:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458585">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f19D5zckBqOlABAhHG2jbZlaxRahfTieGodklXpLrHjfMu0LmfUfZPhVUN0qo49Qv3fEpK1dvxXQTxkPzybuS2wem-2JpD8qSP8oYKZn1tgmZMa0-cA0yQSxZ0rAzpmIc71nspn41k3Bucpkb8Q7uRy5s39v43XLpTQGqDf9uALQLhGIdn4Mp_jnfJKlpGHbWFIkTDOT4oz3mYiV6CVHP89LZY8doIZErwQEb7v_XXfo_rIBKBYhACpOXegQUGfFjPOugUUkpdniA7crdXtYG5I0yIaau4rZV5CXdb-ky5EMiVnrXBdwBXhDNH_qTIWBE8DnRIoxj4vP_AX6bvFzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جریمهٔ دیرکرد بیمهٔ شخص ثالث بخشیده می‌شود
🔹
معاونت اجتماعی و پیشگیری از وقوع جرم دادگستری استان تهران اعلام کرده است که رانندگان تا ۱۳ شهریور فرصت دارند از بخشودگی ۱۰۰ درصدی جریمهٔ دیرکرد بیمه شخص ثالث استفاده کنند.
🔹
این فرصت محدود می‌تواند برای رانندگانی که بیمه‌نامه شخص ثالث آن‌ها به هر دلیل دچار وقفه شده است، امکان مناسبی برای رفع جریمه دیرکرد و بازگرداندن پوشش بیمه‌ای خودرو فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/458585" target="_blank">📅 08:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458584">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIIm3lYcaFpFnx295k4UJld2nfVpERisrGTPjrb5FcJQtU6VJSlB7QLLxwgExxU0433bVeDJSnwIbl5Gkn-qrL0F6NBSGeR5LGK10kBc51yssgv6udQTf3fNB9r48WE306p1DlKnImpquNqnrB6kMoROPVGYU-8QYsLaJsqpguC-V4D3gdtwu8D7e6Q-dzd0tdaBtmmXkKofM3Z_Vd3CjlTm5TKnU1cWOI97qirC4GOYVhcRIricdELzL_y-oA3sxfoOQOI1pg4PG3sQVe3iGu5KAcWnTTDrZLLwA6dpptzrxDWodP_wqDwW--vjSHVss1E8FNUpBu3JvX_7WzqIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی برای اولین بار دست به تیغ جراحی شد
🔹
برای اولین‌بار در جهان، یک بیمار ۴۸ ساله بریتانیایی به نام «ریس هیبرت» تحت جراحی تومور مغزی قرار گرفت که در آن هوش مصنوعی به‌صورت زنده تصاویر جراحی را تحلیل می‌کرد و به جراحان در شناسایی رگ‌ها و اعصاب حساس مرتبط با بینایی کمک می‌کرد.
🔹
این فناوری که در دانشگاه کالج لندن توسعه یافته، به پزشکان اجازه داد هنگام برداشتن تومور از بخش‌های پرخطر فاصله بگیرند؛ زیرا در این ناحیه حتی یک خطای یک‌میلی‌متری می‌تواند به نابینایی، سکته مغزی یا مرگ منجر شود.
🔹
تومور هیبرت در صورت درمان نشدن می‌توانست او را نابینا کند، اما عمل با موفقیت انجام شد و او پس از بیدار شدن از جراحی گفت که دیدش به‌طور چشمگیری بهتر شده است. این فناوری در آینده می‌تواند حرکت ابزارهای جراحی و تماس آن‌ها با بافت را نیز به‌صورت لحظه‌ای ردیابی و به جراحان بازخورد ارائه کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458584" target="_blank">📅 05:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458583">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عاقبت تلخ کشتی متخلف کویتی در هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس تأیید کرد نفتکش «السلام ۲» متعلق به کویت، شامگاه پریشب در ساعت ۲۱:۵۰ به وقت جهانی مورد اصابت قرار گرفته است.
🔹
پیش از این، عصر همان روز نفتکش یونانی «مترو ونیزی» هدف حمله قرار گرفته بود.
🔸
توالی این حوادث طی روزهای اخیر، نگرانی‌ها دربارۀ افزایش خطرات امنیتی برای تردد نفتکش‌ها و حمل‌ونقل دریایی در منطقه را تشدید کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458583" target="_blank">📅 04:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458582">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOv69Lt1jRin_kS0h88Qjd4tLno3uAwce5-6KdgOKYZUd4Xj4aDgzjTjhSvTVgxP2D1K9X2hFde4ArdS5wguPMw_O7Ve4p93zMy_Li8U41A2-I40kxtqkEGFI4PbsdWPBm7ws-yKzaSmOeTyI5iGfU2EtAWwFvCADQ46LI1bDDJYcTzBRQswqp2M42TV7PaCDVcDwrT0v_hvADXchLiXD1MgdFis7VaYPqRgy1WGUu3A0wcmkXzt0bBASKvgcm4pEJXpgnPDQeSKBZ1K_SZcK6Ke8IVtFK6NCnaebIGfYS3Cpe31YHYjh_RKKmTFTK6UJRQxyHrZpLk3XiMlWOUgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت گذر نفت از تنگۀ هرمز در یک هفتۀ گذشته
🔹
درحالی‌که منابع آمریکایی مدعی عبور ۱۰ میلیون بشکۀ نفت از تنگۀ هرمز هستند، داده‌های تانکرترکرز عبور ۴.۱ میلیون بشکه را تایید کردند. رقمی که معادل ۲۰ درصد شرایط عادی تردد از تنگۀ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458582" target="_blank">📅 03:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458581">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5ZuwfbHAmWhGOm5JCmgHX8Uqfxw1UpYanFndBXSQzBA--p2GjLo2pc2g9udC0XmtKRii2jH0VTSn2i6FvTwaXldqAiVkxipNoVTzWoMWTMUuLmhqZBnxdLtenaWMJe34duaMhKgHjiBKhPQeKpOM-baEtSBnUYp1P6naPmiRbGSGMncG-hlx85C_4L-Oj1GXXJLUfUclct_gN9k3VlPTvGU044r-IkS7xZpNaO1ycrRvzIrHJEAyUzE5nZGfEA7lbw16RKiQRinbr_vaAU-l0XMy1tpQp_j3RDxU71kprreopfRYA9sXncCdTb1AF6DH6UYZkcs4-U4NjFFjrmH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی ضعف نظامی آمریکا به مشام پوتین رسید
🔹
گزارش‌های اطلاعاتی جدید آمریکا نشان می‌دهد کرملین تحت ریاست ولادیمیر پوتین بر این باور است که جنگ شش‌ماهۀ آمریکا با ایران باعث تضعیف ایالات متحده شده است.
🔹
واشنگتن‌پست می‌گوید مقام‌های آمریکایی نگرانند روسیه بخواهد این وضعیت را فرصتی برای تشدید اقدامات خود علیه آمریکا و متحدانش در اروپا ببیند.
🔹
این ارزیابی محرمانه اندکی پیش از سفر غیرعلنی رئیس سازمان اطلاعات مرکزی آمریکا به مسکو مطرح شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458581" target="_blank">📅 03:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458580">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ونزوئلا خروج از اوپک را بررسی می‌کند
🔹
بلومبرگ گزارش داد که ونزوئلا به‌طور جدی در حال بررسی خروج از اوپک، سازمان کشورهای صادرکننده نفت، است؛ سازمانی که بیش از ۶۰ سال پیش در تأسیس آن نقش داشت.
🔹
موضوع خروج ونزوئلا در جریان گفت‌وگوها با مقام‌های آمریکایی مطرح شده، هرچند هنوز تصمیم نهایی در این‌باره گرفته نشده است.
🔹
خروج ونزوئلا می‌تواند پرسش‌های بیشتری دربارۀ انسجام اوپک و توانایی این سازمان برای تأثیرگذاری بر قیمت جهانی نفت ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/458580" target="_blank">📅 02:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هشدار یمن به شرکت‌های بیمۀ دریایی: فریب عربستان را نخورید
🔹
وزارت خارجۀ یمن: شرکت‌های بیمۀ دریایی به اطمینان بخشی‌های عربستان سعودی دلخوش نکنند. این اطمینان‌بخشی‌ها خطرهای موجود در ناوبری دریایی را از بین نخواهد برد.
🔸
همچنین سخنگوی دولت یمن اعلام کرد نیروهای مسلح این کشور با جلوگیری از عبور ۴۸ کشتی از دریای سرخ و دریای عرب، و هدف قرار دادن هشت کشتی نفتی دیگر موفق شده‌اند محاصرۀ دریایی کاملی علیه عربستان اعمال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458579" target="_blank">📅 02:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6COADb-q-Vm3rpdoHxgrMY0z7-0FewMjP9yf_I3cXBBl1tAm-L8LW2bxRc9BWP6x8HINUfBqpLLf21LWwBCyM2nvoG3kBpBDaYYuMX3IKVndW7rU799PCSF_jCknkeAfiBc6CW4LYHGMhQMIejeDkYrwtNJMF3TvZWpvr7z49hgE6t5spZe55WA4cYnkK1Ih1vrnOsJDl6sbttd_bwJQ_N0XDOtpC26H1JexAA2JSiJK7csIgHG7oh3_Jlv7Pd5I9uYOfv4urJ9ghXKj9gNxnvMCg8wADy1bzkL1Q2u2yduZetQdRsfPl_o5XNKgunTRPHOXEIJ63Q2NWkjzWXgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه اسرائیل برای مهندسی هوش مصنوعی
🔹
روزنامه گاردین گزارش داد رژیم اسرائیل اقدام به راه‌اندازی یک اندیشکده جعلی کرده تا بر پاسخ‌های و حتی داده‌های آموزشی چت‌بات‌های هوش مصنوعی اثر بگذارد.
🔹
این وب‌سایت که «مؤسسه هانوفر برای سیاست عمومی» نام دارد، طی تنها ۹ روز ۱۲۴ گزارش با بیش از ۵۶۰ هزار کلمه منتشر کرده  است.
🔹
گزارش تحقیقی گاردین نشان می‌دهد که این وب‌سایت تلاش کرده است روایت‌های مورد نظر اسرائیل درباره جنگ غزه و مناقشه اسرائیل و فلسطین را در اختیار چت‌بات‌های هوش مصنوعی قرار دهد.
🔹
گاردین می‌گوید موسسه هانوفر ظاهراً در هیچ حوزه قضایی به‌عنوان یک شخصیت حقوقی ثبت نشده، آدرس فیزیکی مشخصی ندارد، کارکنان آن معرفی نشده‌اند و هیچ‌یک از گزارش‌هایش نیز نام نویسنده ندارد.
🔹
حتی در بخش شرایط استفاده از سایت آمده است که این شرایط تابع قوانین «کشوری است که مؤسسه در آن تأسیس شده»، اما نام آن کشور مشخص نشده است.
🔹
گاردین می‌نویسد این سایت بخشی از یک کارزار بسیار گسترده‌تر است که
ده‌ها میلیون دلار از سوی اسرائیل
برای آن هزینه شده است.
🔹
هدف این کارزار، به گفته گاردین، این است که محتوایی تولید و در اینترنت منتشر شود که احتمال دیده‌شدن و استناد به آن توسط چت‌بات‌های هوش مصنوعی افزایش یابد و در نهایت، این چت‌بات‌ها هنگام پاسخ به پرسش‌های کاربران، استدلال‌ها و روایت‌های مورد نظر اسرائیل را ارائه کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458578" target="_blank">📅 01:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48134c9b6.mp4?token=sVien0PHwvK5wR3tS1Eqo7vitIubYF_jh0UT-OoFC5zl-_cjgxg036Ykqhifj7Thc8v9z48k030KdG-WdwvTSrwz6eXj0KH7xIfj4X90lg0Z7tmlUEobNyH4SzmilHe1UudcX4o2ud7EivfqtvhERHSpIHiLvwZc0zQ3kmMoeeawHNdcHQ3fho5-ymNYMcAVD0cNvgTIG_6mbqIYSNFo8DOr1wVOp8lcMpJmGOyI_4bjg7cxUO-X-bmkv3EZFSuoAgXooroAPMfVNuDvJgoCarLVVlTpUZuewEPV8Al1y1qUM-XKO0IEFHbB-QF88VXm4SF-A-I88HvSM_0HR4GQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48134c9b6.mp4?token=sVien0PHwvK5wR3tS1Eqo7vitIubYF_jh0UT-OoFC5zl-_cjgxg036Ykqhifj7Thc8v9z48k030KdG-WdwvTSrwz6eXj0KH7xIfj4X90lg0Z7tmlUEobNyH4SzmilHe1UudcX4o2ud7EivfqtvhERHSpIHiLvwZc0zQ3kmMoeeawHNdcHQ3fho5-ymNYMcAVD0cNvgTIG_6mbqIYSNFo8DOr1wVOp8lcMpJmGOyI_4bjg7cxUO-X-bmkv3EZFSuoAgXooroAPMfVNuDvJgoCarLVVlTpUZuewEPV8Al1y1qUM-XKO0IEFHbB-QF88VXm4SF-A-I88HvSM_0HR4GQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید حاج قاسم سلیمانی و رهبر شهید انقلاب از سیلی خداوند به صدام و مستکبران دنیا در اوج غرور
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/458577" target="_blank">📅 01:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458576">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNstVbJOA0LqMU1VsiEo9WxXWEpw-t5drDUaLVgXy-HwT9A8kU2gh3g77l31zylLBbQTox2tjsq1KTLXBG-OdYZwAvRPAxPrkguNGVnGtldyNQQxb2uW0Ca5ia5TUKIzXY1DM6OuWkr1-GnHoX6d3TlBkjIeMYpjV0npRmwrGhzfvJJ6ry-s0IRtwn8jiKzoVbzVRkE6Q01M8sSTuqQ-GdaOW7Oa7OnsUJoqkN25UOtiHoZUtLT-bkR0qhEOwf916u1firHZMtVQ9oC7aCTQEaTlA7rDvevbl9MZaghv9WZwujxYziwVmp1BnYILe7nxdfmkFgZDqgqABjc7LwKPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزی: هیچ شناوری بدون اذن نیروهای مسلح از تنگۀ هرمز عبور نمی‌کند
🔹
رئیس کمیسیون امنیت ملی مجلس: رفت‌وآمدها در تنگۀ هرمز با نظارت و کنترل جدی نیروهای مسلح انجام می‌شود.
🔹
درحال‌حاضر هیچ شناوری از تنگۀ هرمز، چه در ورود و چه در خروج بدون اذن و اجازۀ نیروهای مسلح به‌ویژه نیروی دریایی سپاه پاسداران نمی‌تواند عبور کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/458576" target="_blank">📅 00:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حملۀ اسرائیل به حومۀ دمشق
🔹
برخی منابع از حملۀ رژیم صهیونیستی به مناطقی در غرب حومۀ دمشق گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/458575" target="_blank">📅 00:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkBC5ACiAjh8rf27uzQzKFeMBuSK7QNISQHhsBJq6ot15ddTBv_eH805iRXpDJ9rsemEQVlV7Znef7448ezBKqqwhubrqhjrYrOSrFkrEWPoG2oASlL95Cu6VpCwnat69fbKYY76nXXXfDVd-z0dtYOpIVEKp4uSYZkiMUys35rZZBeMz24Q1_I1Q6vT1WMvgMHVoHrmfGVKy1pnYjHc_QQ0P9jAUHG-dqyg2e0zN9h7-7Wi9In2KO9NFApiC_mgDC2y4EW8IGkORnY_hyFWSxto9ULtE_9Av8lptmz5NrFCwBy5U3L2wloereS0pV-gYJtMxNuACbEl3AyTm5i_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا علی کریمی علیه رضا پهلوی و سلطنت‌طلبان شمشیر کشید؟
🔹
ماجرای درگیری علی کریمی و رضا پهلوی در شرایطی علنی شده که بخشی از حامیان جریان سلطنت‌طلب، پس از ماه‌ها امید بستن به تغییر شرایط سیاسی ایران، اکنون با واقعیتی متفاوت از آنچه در فضای مجازی برای خود ساخته بودند، مواجه شده‌اند.
🔹
امید چوپانکاره، عضو شورای مرکزی جبهه شریان، می‌گوید که این افراد متوجه شدند که آنچه برای آینده ایران تصور کرده بودند، در نهایت چیزی جز «رویا و خیال‌بافی» نبوده است و مردم ایران تحت تأثیر چنین پروژه‌هایی قرار نگرفته‌اند.
🔹
حسینی استاد دانشگاه هم معتقد است که تصور برخی جریان‌ها این بود که حمله نظامی، می‌تواند جمهوری اسلامی را در موقعیتی قرار دهد که امکان ادامه حیات سیاسی نداشته باشد و در چنین شرایطی، رضا پهلوی خلأ قدرت را پر می کند.
🔹
بخشی، استاد دانشگاه هم می‌گوید که تحولات اخیر برای این افراد روشن کرده که جمهوری اسلامی از پشتوانه‌های اجتماعی و اعتقادی برخوردار است و همین مسئله آنان را با واقعیتی متفاوت از تصویری که در فضای رسانه‌ای ساخته بودند، مواجه کرده است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/458574" target="_blank">📅 23:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌ سرلشکر رضایی: ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.
🔹
ما با جدیت کامل اوضاع را رصد می‌کنیم و زیر نظر داریم. اسرائیل مجبور خواهد شد از مناطق اشغال‌شده در لبنان عقب‌نشینی کند. @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/458573" target="_blank">📅 23:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما نتانیاهو را روانهٔ جهنم می‌کنیم
🔹
سرلشکر رضایی در مصاحبه با المنار: ایران بنیامین نتانیاهو را به جهنم خواهد فرستاد. ما ثابت خواهیم کرد اشتباهات بزرگ نتانیاهو باعث شده پایان موجودیت رژیم صهیونیستی نزدیک شود. @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/458572" target="_blank">📅 22:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNd0KimZsotjlJVx-Zn3fMrDG0B9of0FN5sP7p4_6E9WITb3fMdK-kNOKYlKLanvS326GRYmlMBgIJPJNMtcwiJ9QLhs6gwNlpyegFURmNOVqlultK4XUopFjSYHfcJ0f-hwRsz9aDMhi5MzYnIzpQc782Z5mfjomfHgeB_ozQrhMvJZ7_EzdQnOEDcR_FcZQ1IvMb9nbDHKtDlmB0mSHdPlLg6_wzYvm4tTJbNnQz0MmiQdkART5P94Ot1P0uaFsT9Tc7728An5nqlYkrutirlBjGLgnNmRUiaAoZ7NcxP1yPepL3nFQNphF05_Hxvp4sgdWwF8zUK2k1_RyvwRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما نتانیاهو را روانهٔ جهنم می‌کنیم
🔹
سرلشکر رضایی در مصاحبه با المنار: ایران بنیامین نتانیاهو را به جهنم خواهد فرستاد. ما ثابت خواهیم کرد اشتباهات بزرگ نتانیاهو باعث شده پایان موجودیت رژیم صهیونیستی نزدیک شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/458571" target="_blank">📅 22:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXrZqj_IU0X0exI2z56DnaN0PZ-RotTu_vMIcUIFjKAgUr3qrOBAFotSK_OWUWxKS_6mZFCyuf5HH_k7ZxnaMMre-hWSr8hk_wevSXz5FpXw3Dbu6LdRi56dchK3NSXJYX-0Xn4jvHCeHmhNFSaSMUuqTlWsszaGoKof_a-_KzyQqt3oIa4v13D9x4sIuD13SSNaL2FJYsNAMp2lM6GWrBfZd-_eYlFBEgeZULNjSE1dfUizV08br2yjWHhJrFCTdE7lKIbrxeDPtSCW5Bv-_JABiQLA9aTOuAWUIVUnqJG8Jp17X-yUp-std2gDUiQW_eaLsFFU94gYCzyWyVYSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت‌ژورنال: ترامپ تمایلی به بازگشت به تفاهم‌نامه با ایران ندارد
🔹
روزنامه وال‌استریت‌ژورنال گزارش داده مقامات ارشد آمریکایی به میانجی‌گران بین‌المللی اعلام کرده‌اند که دولت دونالد ترامپ هیچ علاقه‌ای به بازگشت به مفاد توافقنامه اولیه‌ای که ژوئن گذشته با ایران امضا کرده بود، ندارد.
🔹
به نوشته این روزنامه این موضع‌گیری، تلاش‌های گسترده این هفته برای ازسرگیری روند دیپلماتیک را با پیچیدگی جدی مواجه ساخته است.
🔹
به گفته منابع آگاه، ترامپ اکنون بر سیاست فشار حداکثری اقتصادی بر تهران متمرکز شده و حاضر است منتظر بماند تا ببیند آیا این راهبرد نتیجه‌بخش خواهد بود یا خیر.
🔸
منابع مطلع گفته‌اند ترامپ به‌ویژه دیگر تمایلی به احیای تفاهم‌نامه ژوئن ندارد؛ توافقی که در داخل آمریکا به‌شدت مورد انتقاد قرار گرفته و آن را در برابر ایران «نرم» تلقی کرده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/458570" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt3ij96AMdURvMftV6khhjcouuryk0jtz0iqxQO7xFr2l9Bux997Y4CAIKyx4MZMNISWy90_-4YoOOX4Tl4xHCK5qgCZRRXb2y1nmLZnaDYMsjp6dMohYtFllMj6pRh8PhoyquQ0-k4-El9QpW9kV4L2UOiGA2OFT08wXAiGNl_2mYjUKoNL-dG22dPIGutkjC8kRzmxZTB-62Ryg35ZLdofwXvW5MrwSS3l1O36dzBISievN4dZIc0BfWaEGb5xHOC8jQ1f27kbnIfco9c6SNFTWznlTesdvF9Q-OLrMr9qD3tuq9GmKVOegYLqdyIlU3TEQ-tKTTE1hM8QyZIz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فولاد شادگان تا مدرسه نابینایان شیراز؛ روایت ۱۴ گام بلند «امید امروز» در گوشه‌وکنار ایران
🔸
۴ شهریور ۱۴۰۵ را در تقویم امیدهای ملی ثبت کنید؛ روزی که خبرهای خوش از ۹ استان کشور، یکصدا فریاد زدند که چرخ تولید، آبادانی و عدالت، حتی در سخت‌ترین روزهای تحریم،…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458569" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۷.pdf</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/farsna/458568" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۶.pdf</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458568" target="_blank">📅 22:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7c1b068c.mp4?token=FYX8y9EXEd4WQjdK29dZTBzCZ2aiTfcx9L1N82-xQcUdC0x4BuSD4s12YuCZvAzfPTA0ajWSsxIt5u7wZ_4rGC8VmAokvLwEpjrqmAC1d7Re7iB1UC1T-aVoFqH5jEhv0X9A35noHHViGiOZUAAphWauV6BKi2WTj5EaCPoawJDbQo6YBoF7CAEpRgh3yMR1Mbxjf4zQ1olR-fb5ECD4WYOZkicjTkgigF3AQIJlZYlOzhZ8yOJjlJggOyDBT4r3cGL5eetSv7MhNmT49crukIHKc00lTWKDOHMYk9aP5DgpyWvyG3IFzOIfx5cz-HRD0InEHXh0h34mdr4BhH2O82zJe19HmVR389K5s4wqVCrSWNPKIZtCgungHhk9JGOcjTY4kBG1CGrdkvoY0G3Rz27gvHtrZqXK_sP1zRXFnoerQvUEBWEPDx4tUjF5MoSotzZWhSY-BtA6OkhCaIItex5qShNa3U_gUa3C-a2fwjdtx-Gvd59VG0cB3XjT6MwRdDrWGTV44PIPBTxkTtvsvM9XfZm3W8P_W7u6TbHCiZF_AuDIur9RY60BFkJP2k88-adaqqFJANqyuI8bp5t0fgZIoK6wSjY8trlZPEvu2BOsVmZg5lK9bp8nNL_DikUJa_N6Eb8YvOnigQo1-TDbZMVyRVUF92vLV0h0nhMhChc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7c1b068c.mp4?token=FYX8y9EXEd4WQjdK29dZTBzCZ2aiTfcx9L1N82-xQcUdC0x4BuSD4s12YuCZvAzfPTA0ajWSsxIt5u7wZ_4rGC8VmAokvLwEpjrqmAC1d7Re7iB1UC1T-aVoFqH5jEhv0X9A35noHHViGiOZUAAphWauV6BKi2WTj5EaCPoawJDbQo6YBoF7CAEpRgh3yMR1Mbxjf4zQ1olR-fb5ECD4WYOZkicjTkgigF3AQIJlZYlOzhZ8yOJjlJggOyDBT4r3cGL5eetSv7MhNmT49crukIHKc00lTWKDOHMYk9aP5DgpyWvyG3IFzOIfx5cz-HRD0InEHXh0h34mdr4BhH2O82zJe19HmVR389K5s4wqVCrSWNPKIZtCgungHhk9JGOcjTY4kBG1CGrdkvoY0G3Rz27gvHtrZqXK_sP1zRXFnoerQvUEBWEPDx4tUjF5MoSotzZWhSY-BtA6OkhCaIItex5qShNa3U_gUa3C-a2fwjdtx-Gvd59VG0cB3XjT6MwRdDrWGTV44PIPBTxkTtvsvM9XfZm3W8P_W7u6TbHCiZF_AuDIur9RY60BFkJP2k88-adaqqFJANqyuI8bp5t0fgZIoK6wSjY8trlZPEvu2BOsVmZg5lK9bp8nNL_DikUJa_N6Eb8YvOnigQo1-TDbZMVyRVUF92vLV0h0nhMhChc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶۸ بار حمله به یک پایگاه؛ چرا العدید مهم بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458567" target="_blank">📅 22:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کلاهبردار ۱۰ هزار میلیارد تومانی در ارومیه دستگیر شد
🔹
فرمانده انتظامی آذربایجان‌غربی: در پی گزارشات متعدد مبنی بر کلاهبرداری از شهروندان به شيوهٔ خريد کالا و صدور چک‌های بلامحل، موضوع در دستور کار مأموران قرار گرفت و متهم فراری را شناسایی و دستگیر کردند.
🔹
متهم در مراحل بازجویی به ۹۰ کلاهبرداری سریالی از شهروندان در استان‌های مختلف به‌ارزش ۱۰۰ هزار میلیارد ریال اعتراف کرد و تحویل مراجع قضایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/458566" target="_blank">📅 21:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f09d5bca.mp4?token=ZuAUxjg6NrhHHpgonztdyexdr7fd9DFkTDvgAQIUGaB87EJ7YuY7KtO75WcBB81vn4b7oHXa1nABjrbbh4z0Ehf-CfqHQecHnVzF6S6me-rySKoTwVz9K7eriT1wDRCrrThhnZV1IIbA2VI1cfhO0qw54vWL_invfmgyJxKNZ5y5xQxjhHWFSLHwxqSgxlRgvRI8Jg_N-QclaCITPQBVQZFgOxK6k0HM7PFAEdUEy-CthgBx2pDptBmWG9ODNamvs8h0eV4Vk7dfxHNSGMWM1kKV6bH7FDtKGzolZ2ZH-zcQbwZsRQSAQZpUx0qHpCPQ6PQbxiGEH5abgGYRz3b8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f09d5bca.mp4?token=ZuAUxjg6NrhHHpgonztdyexdr7fd9DFkTDvgAQIUGaB87EJ7YuY7KtO75WcBB81vn4b7oHXa1nABjrbbh4z0Ehf-CfqHQecHnVzF6S6me-rySKoTwVz9K7eriT1wDRCrrThhnZV1IIbA2VI1cfhO0qw54vWL_invfmgyJxKNZ5y5xQxjhHWFSLHwxqSgxlRgvRI8Jg_N-QclaCITPQBVQZFgOxK6k0HM7PFAEdUEy-CthgBx2pDptBmWG9ODNamvs8h0eV4Vk7dfxHNSGMWM1kKV6bH7FDtKGzolZ2ZH-zcQbwZsRQSAQZpUx0qHpCPQ6PQbxiGEH5abgGYRz3b8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعی، کارشناس مسائل منطقه: اگر آمریکا بر تنگهٔ هرمز مسلط است، چرا هر روز مجبور به تکرار این ادعاست؟!   @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/458565" target="_blank">📅 21:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4308563c0e.mp4?token=nXyVHa-g0EvgNnk4Vy7S3mKG8TjogU3JloRU1vwuIBJZ4aizAvVi2--JPA4x3UoLtcQ39dYK8R40r9kkbnFrOK1jMdBE8_WpbRXH1dyc0dJi2dPmU16YIzh1MhJ_0Dg627DJrXTjj8WA1iBVSKSS1cbP9ou5v6W2lGWKSW7-XBm23rAVKIdzSb1duFd4c9S9P82jPc2mGAspjMWESvPY-VPi5m241oQcdb4JjYQYYNo6OH5z472-VAuP1-nHxNjj2lFR7Yv5Dloi2CA6tVS-OHy_QkKbQ8v9bSDDpKYBBC3oA7qZVK6YCTwvvURQRLauo45w90SDNjyBT7t7xG58mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4308563c0e.mp4?token=nXyVHa-g0EvgNnk4Vy7S3mKG8TjogU3JloRU1vwuIBJZ4aizAvVi2--JPA4x3UoLtcQ39dYK8R40r9kkbnFrOK1jMdBE8_WpbRXH1dyc0dJi2dPmU16YIzh1MhJ_0Dg627DJrXTjj8WA1iBVSKSS1cbP9ou5v6W2lGWKSW7-XBm23rAVKIdzSb1duFd4c9S9P82jPc2mGAspjMWESvPY-VPi5m241oQcdb4JjYQYYNo6OH5z472-VAuP1-nHxNjj2lFR7Yv5Dloi2CA6tVS-OHy_QkKbQ8v9bSDDpKYBBC3oA7qZVK6YCTwvvURQRLauo45w90SDNjyBT7t7xG58mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعی، کارشناس مسائل منطقه: اگر آمریکا بر تنگهٔ هرمز مسلط است، چرا هر روز مجبور به تکرار این ادعاست؟!
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458564" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f572f47b.mp4?token=UGWepb3qnq01ucwGeyek0V-v-9MrCqA6ZJA981-M_ClI4dsGqA1HXuCApxSX-ER2KphN9d4rPryVZIRarb0VJte0nMYaz0dRl-1UjQw0BrcGItgLhMk5L8os_lDfzRIIl6Of-ng5Jh4n_VQpVT6rUj4LG56vR-4FTdAs37pyCKE1vTiXyPTgg15yetVxYSNURLgWeHtAfzi90gZwnqlEkEf7G-h5rcTt3aIWslXHi8-UfS8tHwVgBNRZRK5gfY7itw_1zqCU0kG_ac0o0WMiHvJSE2churnf4opYfY8WPD4_hARnK8voKrnPJAl0D-Hb1cQIiXnY-2XANIA1eCFhzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f572f47b.mp4?token=UGWepb3qnq01ucwGeyek0V-v-9MrCqA6ZJA981-M_ClI4dsGqA1HXuCApxSX-ER2KphN9d4rPryVZIRarb0VJte0nMYaz0dRl-1UjQw0BrcGItgLhMk5L8os_lDfzRIIl6Of-ng5Jh4n_VQpVT6rUj4LG56vR-4FTdAs37pyCKE1vTiXyPTgg15yetVxYSNURLgWeHtAfzi90gZwnqlEkEf7G-h5rcTt3aIWslXHi8-UfS8tHwVgBNRZRK5gfY7itw_1zqCU0kG_ac0o0WMiHvJSE2churnf4opYfY8WPD4_hARnK8voKrnPJAl0D-Hb1cQIiXnY-2XANIA1eCFhzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید لاریجانی از عطری که شهید لاریجانی به رهبر انقلاب هدیه کرد  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458563" target="_blank">📅 21:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f61098eb.mp4?token=IZd2IODvkhOeD13sgO83md7ukWx9BZxnvxPQsuaDkkjmaCvuaTSA1Iw2Sxm_bT2QsOfN29_2AmDNa57JpFLaqwq_tKteinuxGOK6m45rKoTwEtfxILFVHsIXH9TnrTVS1p93RnRZ-H4Bw6IzDW5FivW9y7h1JOuMxnqrY1NFAH9xQjXwPRfg1Djopb5nxD6SzZ6jWuSfJBUhTdNh_2lYcbvq7a6lhgZN9FAjIVSK_iip7TclPMGVRdrsfH3YprAkAAAoIpmQ5a9tev8ndGlobNcjJ7aM-QYWnlhPoMYONhqA-xgGsXpOCGab041nQjATrC9_9wrq_Oil5tXNYK8oeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f61098eb.mp4?token=IZd2IODvkhOeD13sgO83md7ukWx9BZxnvxPQsuaDkkjmaCvuaTSA1Iw2Sxm_bT2QsOfN29_2AmDNa57JpFLaqwq_tKteinuxGOK6m45rKoTwEtfxILFVHsIXH9TnrTVS1p93RnRZ-H4Bw6IzDW5FivW9y7h1JOuMxnqrY1NFAH9xQjXwPRfg1Djopb5nxD6SzZ6jWuSfJBUhTdNh_2lYcbvq7a6lhgZN9FAjIVSK_iip7TclPMGVRdrsfH3YprAkAAAoIpmQ5a9tev8ndGlobNcjJ7aM-QYWnlhPoMYONhqA-xgGsXpOCGab041nQjATrC9_9wrq_Oil5tXNYK8oeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدار  اعضای دفتر حفظ و نشر آثار رهبر شهید با خانوادهٔ شهید لاریجانی
🔹
حدادعادل، وزیر آموزش‌وپرورش و اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب به دیدار خانوادهٔ شهید لاریجانی رفتند و به ایشان ادای احترام کردند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458562" target="_blank">📅 21:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec9b5f41d.mp4?token=lukR5hIDSCLqfyMyADpuJEfk1QDBB37Bs9CRRsl6vJihzlqZ5QDxm-dXyXbJqrkvkQQNPLhJ4yXjsIuuOmuiEalc2qkINCO1-ByhqZtPKBRVx07cTcZWyPAc-f3MeRC2b4q4godWkdR1oiabv8W-nAOmXDOe1avI46tx6teiMMs0fOsxctLZM7H7d7TPILr57BFMztlbXe79sXNxz-GLJkuxvKv7426iveNZnBGcpB-UyGzM_NZhyDzbudLq-aWW56UnHT6sbgTz73s70vZip4SZwq9-CeAJkOk6dr6lTQGRZFUDSJIrc_5WadVgFs4bPh-IdTbZQb_HElnEMXhG3g3bsIb8DGz5HnCzZUzW6UkMBYAwVp7OBTPOq2ombMSq6BsfnJsUGYnmOOMQvR4cqgBvTRmsfwjpd6pdvD-By2tqqqQx8jn1t1PJTa4IPt_uyufv0FHAbZvDIn7c9AEAtlk3hYx6ln_j17sMV9Fn7TKaWdNM5QFWozBJIeNCI92gbsdDxMLwCd4bI39zYjjVKi1IokaZMntNSq9GHuUZFdsypcH6Wfx73SNB6pHJLCiPrjgEDd9eRxroDejW4CZCW_QLPPNbpsnYF68kUGErAvSD9sXDdxflwHivu0Hk5zsDhQIo656HIDLTpKIaabQFUEPj-Y0jrYssPJwsOjBZcMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec9b5f41d.mp4?token=lukR5hIDSCLqfyMyADpuJEfk1QDBB37Bs9CRRsl6vJihzlqZ5QDxm-dXyXbJqrkvkQQNPLhJ4yXjsIuuOmuiEalc2qkINCO1-ByhqZtPKBRVx07cTcZWyPAc-f3MeRC2b4q4godWkdR1oiabv8W-nAOmXDOe1avI46tx6teiMMs0fOsxctLZM7H7d7TPILr57BFMztlbXe79sXNxz-GLJkuxvKv7426iveNZnBGcpB-UyGzM_NZhyDzbudLq-aWW56UnHT6sbgTz73s70vZip4SZwq9-CeAJkOk6dr6lTQGRZFUDSJIrc_5WadVgFs4bPh-IdTbZQb_HElnEMXhG3g3bsIb8DGz5HnCzZUzW6UkMBYAwVp7OBTPOq2ombMSq6BsfnJsUGYnmOOMQvR4cqgBvTRmsfwjpd6pdvD-By2tqqqQx8jn1t1PJTa4IPt_uyufv0FHAbZvDIn7c9AEAtlk3hYx6ln_j17sMV9Fn7TKaWdNM5QFWozBJIeNCI92gbsdDxMLwCd4bI39zYjjVKi1IokaZMntNSq9GHuUZFdsypcH6Wfx73SNB6pHJLCiPrjgEDd9eRxroDejW4CZCW_QLPPNbpsnYF68kUGErAvSD9sXDdxflwHivu0Hk5zsDhQIo656HIDLTpKIaabQFUEPj-Y0jrYssPJwsOjBZcMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدار  اعضای دفتر حفظ و نشر آثار رهبر شهید با خانوادهٔ شهید لاریجانی
🔹
حدادعادل، وزیر آموزش‌وپرورش و اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب به دیدار خانوادهٔ شهید لاریجانی رفتند و به ایشان ادای احترام کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458561" target="_blank">📅 21:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرماندار چابهار: فردا از ساعت ۷ تا ۱۱ عملیات انهدام مهمات عمل‌نکرده در محدودهٔ شهر چابهار انجام می‌شود و صدای انفجارهای احتمالی جای نگرانی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458560" target="_blank">📅 21:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458551">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_RvL4F2m2qMGPXasXWMj4XkqNWNGHUHWRAjA0-Uga1PPQ6VYrFh9blh3xfpByrfJEOP3brIQn6ozdv9HMgH1RnXjS75PfmjlBKRl6RA9n4YwFfSdvmZPJQgX8pJCz_yuNw0OJqIcc78V8UqNUIDSZdOMRg2Gd3R3pK9UgOYKroTbGFd2mxwTAIft8SZr6YoQq5OfUEkCd_oHW1fauoL6AWXTNAGYDt_PEvwxRgm64l_e4lRHIYobN1glTDsqar6tppaIfbvLgt79t2JSEAmlIuwrAWaSKwwgjRe4Uf_FP9S86eMcbLHzM9FfpzCERuEX7fpNJv88xHdCs3vL-n8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeO9r49iyHiGd461V73Z3LcUPwUHfI38_Lu60Py_COIxzqSDlvXDfDOpMYSY2LbssBjPeMvNSjIzsxV1kuhdPFkwmAWg1bgYwtIPhzLRJ4oj8N-qHd6CYoXyEjeMUHn_9d1Is3PvS_-6P0eD1YRLAD1rhr3xD2Qck4WZRotQfOYuyEURHGaXz_-NPKS2NqWBb13TGTrrIZ4V9RdJ7BQXPukAT172uPgbYiwrNoqeghUY4N2MC1tJo7y7ovE0brUJ8gocbodLGe-kbHVKkOR4I248UpakpGWSz7xqJqNlJ08EQ45BOiebl8vfOIsg2N1yR3uWRqOkbA-Y9eF2Nm2duA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9dRE415nhQR2xfFTJ2Zc3P9daEht3Na0V4loAHUepXne3-6BOU1NFm7wI1kdougZ28mYH2ZkkrHt-ItpUjrHRTrBWCYRwfcHqTpV5BivJjoBm5og3OVi6qtTCr-26BRKCUKUmpHm89FJyXSM6174-y2wTwpb-4-YpbyavgfDgU0ZdLdAue-4qdyZgptBWLNMfkP5ZM4l32dABqRQ1dRmmKKfCOI-Uaidey5FhcGYIoZCGESmSx7GmGssC6gKSFQ87jbO7x_Xyp07B9rimaILyYF9_zN86ooP_kM23RwTKfW3m4qDl7lAUvTIUWnj2Xdq0vPPrXABC19O1ZmaTWLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIPhQAdngoESv4tqs4lrS4zf8fBEhUSFQnL2KKyz52pKbuaZSeo1OtFBcc02OhAtUYX_sq6CUfTny5uGoqT2xh_6noZpN8-MjDduBu9XgTveJN1G7wcSPelkkg5ixwGCUi1BrSFnNlHGU4DWBD66oj2TtjPQdMAEgoy8ox1aubWSEx_PdumB4JVaypauX8ItUUCpiWHp3tgOlCAg-xadNnU2wuYzCQ6oF_7JeXn8Mqm97JhobSMetI7HdPfG1FQVP78AFrdQVLnhVNto4dh8Rdh5NfGWVKmZyPbKgTPmMiAZ6NTB9rmkfTGbbqznbe9xTEw0coNdF6w-6_9_5ifBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7NX65DQegkwBMhRpZ0hoA4HlsjnEdLHTewTE36ojmF8jprRxOn-xXgV5sKmY0MkmDvgIe6wvNg7T6Hz64F3x4iQcN7MmrjdLQUSz-O9_SVRKxx83tHwry6FxPcqOQp7V15MJH0MEudaGrMafX09_UtoudWpTNDpbV11mJz2j9YDZ11Un2jD9jy9W573D75NdH2HgVbYRy9pMquGBT26jstdD-LJ8hkAoqmN12Sj5JSRQ-0H2o7n5XPSx8eQAzA5CELKfKXkbcd5MWcGUYt8sJRZ5rx8CmujQIvZ6GMjtmehfvrx-MA8Pm370h9mOvAp2w2gOlCA_btB9B41uwQdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVXLAesdgzbanr6ZUuQ4LbmAFBqD7xDUAKS_rNoUCTArxh0P1H-ZxKo0mHuYluEJ5XvM_fEvVsHr9m05axgE7ndqKCMrICXklgKqa90M9Mj5r7MV-U3bKUnNJTfJXOTQEgGN715W9KZMPTUOqeoPk0tw2bdpbvK12f2MpFnb6gs8q5MKz0KZxfdPzrsEMhmw6OyLlf8kfyZaIKiKKuNFaW8yieTTvSbZZySgtUjXCOz0P4cqnR7mO69UU5-O5sSx0OP0-uJi1pluNZoN6LYM3ukZR774nQU9TDODXxdP-WV4f2xTmjhtaetthxRb0Rk81aYHxx5ll9Km_qzmANfuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V70qmBehjayEBKMSmVmWS6umAmPTI_CmgIoQiDhtvEVpJoU4YFCQV6P7KbzwNpZi-6a7DNX630Ukas9UGDPt7r7PV0phgnwvOLhiLot_3lQBYOZ6fyp1Lj7QVb6Krv91gVB6HrIzoybCszBJc1q-rGJ9zlGmnRIQGqjBHXxZepQKBOHNUmWXpTSToc-oSauTcv7piBC6FS5w_KtQEAfkjKv6kfHeKwxBXGVs_185dE_GnzlCAgDqZi05llUXlOm_b25LHqcKXl-nAmwP1oLMOYizyUp0KZfiJKU-KIgVsRKwZpWxQPQ2-GaIO0QZK_vlTXT1txF1EgWDlOI1jWCRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxCG3Bvz4iImpob_jh6tkZE3Av4IngUB8uS8D6PCOPS5UtY-FAMnQyBAUPoWjlNJvWZXBfq75Kw5gy9rGYEPDE9jAQe9CQYc6pYa5VPYP1mG4NDFhrof4DGfBG3RCdAxpaVK58UnZkheZWDsgGaMr_jN5_qcZdOFLJWALszOIxJzd6y6KjDLBDEdI2QGhbuKuMOTM90OZZMnEE2f6Z63Xc9KZnLmCatBTAlJ7NK8HyoYq58DQLS7TatZ354RuXSWGzn9o6jGMlqcu3JwV2r79kQnUs_9PSFJNtTgFr6RrBz6Jn4Bdk-YB0PRYG-ZZOA197KCT-3vMBvVhP8VQrDkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEPhqOzhoAtosAnoqIl5VlPsWWcDWCWmKDGwWi-6hF7Y3FccVMrKMMXi6QVGpGB5Tie6tl5r77G-V6DOUfLzIHAHfKfzz5Evd0GgylBMuYccUxe-m7p68ucvu1pv8YsXuTPGOYDEIvEEc8DRBsI04AgWfHnuBZvtbogD6sCN-ZJSS8lA3_F7J8ymWi_-OJENLLeqZ_R4wQkhIK6dZMr4dmUajAfzA_WEhjcK9Vh9bT9gw8IFJNUtNFw3dg4EbKSzCXSUpFu_K6bB2T1Z7cxsgwwBl2R6UsDB7lCO_977TyZNnJeI6k2WMDfZ5DSPyNhz2f3oUAwEJxhxsLlfAj4H6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قرعه‌کشی لیگ قهرمانان
⚽️
تیم‌های
سید یک
حریفانشان را شناختند
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458551" target="_blank">📅 20:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458550">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzJaIaJJ0gJr4C5MX0HgSF6n_JXZfZ7U9uRfGszp3mPD04j3k9AQksRcwHw3hmPjbIULvVkaxNIaVo1VadviZeOhHRESF8fwX8I4sdh8wNH2eCW6Rw-FPQwmHsX_ERoUVcabX9Ec_zBtLSCv1JIoHmO9g0NU8qe7C2VmuczQxZfEbLFy2nqlwhac9laC-uqr0ReHVJ5OjF4Jj1mDrmO3cCiNxlQgHyk4OrQjzpd4jrwwWerTrPrJe6voAR59lcbj4xMLmk9hQ4utpOLDHaKMJWZg4EX4wJ3ab6hO8pTq0e_gDJKsIMphIqxd60RH9AvNu85T2XJls3lwPE_v3437vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف به بسنت: نمایش مضحکت «روز پیروزی» نبود، «روز دلقک» بود!
🔹
وزیر خزانه‌داری آمریکا که ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز به سؤال خبرنگار درباره توخالی‌بودن این ادعا…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458550" target="_blank">📅 20:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458549">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شهادت یک مرزبان در حملهٔ تروریستی در مسیر میرجاوه-زاهدان
🔹
مرزبانی سیستان‌وبلوچستان: در یک حملهٔ تروریستی کور، استواردوم «علی حیدری» از دلاورمردان مرزبانی استان بر اثر اصابت گلوله به شهادت رسید و همچنین یکی دیگر از همرزمان او مجروح شد که بلافاصله توسط عوامل امدادی به مراکز درمانی منتقل و تحت مداوا قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/458549" target="_blank">📅 20:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWCspbw4c6CnS-PgJynBeKlRRjmQDo8K3Z1Xhrru5A3ETKYcQ36EO-BZpihgjfde1xI6qJfkesdo8GeJYCNfSzQ9K1EZUx_gH3pg0NZ40Av99AqjXgMhRFUcF_U7eIqXDOeXssleo4scH9R9oO1s_ZqT8CTjOqzzNMkHvq2E89At7S596tl4TSFpdXuGHutlVFFIgjr80JZilgDoFrX3itnSMLWl2dPWShH2ifjaX6p5B-xtWwhH2_IXhqJxzwwMw4sjRd2HDuNflkgV8l9yaDo6xNE1L0GlCDhR3A3rcnOCIL4uuYro23SkCwO5lNW0qdbUkw2LPaibOv1W8hq6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجهٔ قطر در دیدار با پزشکیان: امیر قطر شما را مثل برادر می‌داند. موضوع خلبان‌های ایرانی را هم با صداقت پیگیری خواهیم کرد
🔹
محمد عبدالرحمن آل‌ثانی در دیدار با رئیس‌جمهور ایران با بیان اینکه «دکتر پزشکیان نزد امیر قطر از جایگاهی ویژه برخوردار است» گفت:…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458547" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Al1zDtP7ZC2IoEqDmhB0InHBviykKT9j2PWQJpW0XrzmFwnZN8UIH1tt6S0TPWAqcWZ711OVIxUO_hyl3QGPjvCtZE5s_4VDHddELXCPkj5P-zrtxZtYGCUNiQ4xNfpctnXHEdOvnaOx1Q12FFiKzpDCL1pKr_T_fNruHOMeeqn6gjnGxy2DF0p33i3_T9xO81OiqIyboCKTdYtIEA-Ny81SB0Y5nAdFOQmbUO5oy6cufNKUO2sBttSFoOY2AEqZX9Dp27bY98OKse-8Xqbh51vaIArobwh3CMjGwJB0G-PkxTePvZNffvjKjnjaTgK54Qv42xnyff0lidBniEDA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار وزیر خارجهٔ قطر: نقشهٔ رژیم صهیونیستی جلوگیری از برقراری روابط صمیمانه میان مسلمانان است
🔹
مسئولان آمریکایی باید صداهایی را که برای جلوگیری از بازگشت آرامش به منطقه تلاش می‌کنند را نادیده بگیرند. منافع عده‌ای در ادامهٔ جنگ است، اما ایران معتقد…</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/458546" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv4dDJGclvJB7clxSLBKMnU9lXmda7Et5ELw0WUOxlSxG7LdOsM8D7tVcOgu5l0sr4csxAJ5KUglBWW6m-MISDG0_ZvFw2eMDpzRTuzdq0ZLHPhxr03iqxu1Ag1IETYd97_sltwGIykEYTRcCxyj8Zv-f5-ru7G0UKLu4Na3lh67EroCwglcFPstDuPfIBI65GuekmUXx0knqeu4MIFfcXqOSM9q1C5kfkoEj2iAV0eY3wP-hB7sL74KqyBnVKQ2eRH6sIpPHVLR-IiwS6xFW1pqN-exoYk7SSpwkPisaWvjtGDcM5wfCSpLWNq7fU4LoYiDL37-Cq-nc4_iqxp7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجهٔ قطر در تهران با پزشکیان دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/458545" target="_blank">📅 19:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyQ-C9GLhzivHQaNRV8B1Ra6JUdymJPAU1VQPp7lokF0Zb3QK-H_viiS6HAnZzQ3i48q5r1UDt3P4J_Hqv1G2B82iDOFg-pdsXOLsQknGQ2QjvcCM8boWRJVbAbZIYf8FN1fnuq60tmDGc82_CmIKT6uxhqR8vRuyFK-jay9D5s6TdXXR6FAywDND88LgRviu_iaB3KWjs82Uzcoo7pO6XS3bnUjOgHBtLUPQZrUSe9XqemH9Wo9_v3J1RJD10sp96AOMlI0aLA8kJ_-FXnVrT3UfCOv-1KoYDvmJQjyraUw7h_octpaZ2QmS5VntSeP45TygC4HKOcYmsAJUQ0ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_GmeD3PRVrdRFpiesL3t2mR4N-z-01XTlFffaoL6zqZpbfEMb8vYRajD9-ZWnt_ZOXLIhEZMdTdCcumYwbiJGAcH4Upy8jGxht-LCpmD8vn32Oo0h_N6rZvNPvkHFCSl9eOIcERGCP1DXYsDIax-EEq1n-qGtHfxbrdOnVq6yFX1GnlJIfwJzgJw7wu4xn3sD4LHzGMZDA3nQG2LhvrYkKQeFgp9qFV0sH6YC3pFNgGzzZDm-8jTUWucuf5CL4JcKhBJjpneWhQf5g9DWzvCRoFx7i0hhQDtA5ffJ2Ba7isLrVOS2_SWxIZS7xsprq4EFsVPl7K37Vg2h8dgY3sNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAnNLXrVQ5uQzlP16JPuR6MdllLTjIbEK4I67v-I3BNVxLUiPBlb51NI_Of1o98KtVu7akRCdAmldRMCRbS0OoLDRZf02rJJ4FvFC3wvFWOJhlS2c3K5DSScoHL4bFhFaOfyU5cqDCReNn4NR7AN1S7pkhBP_Ym_DSmSpVVRS_2oTSp9-KIswKlBov0DRE0RGNWy74btqZxlR8DXZGCCB36-iI9_IJz2XaLeu77KuDLAnjZb_WUEEwmLDp357sW2MTTOpS-sIc1rrFwDES-g8ztWsgwimsg8QTCbH285UVxw0up8lDNC_0dkiCV19rJLdhzuJ9_j1sYewpGkGKtu6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
همزمان با روز پزشک و طی بازدید از بیمارستان سپهر سلامت انجام شد
✅
قدردانی مدیرعامل بانک صادرات ایران از کادر درمان/ افشین خانی: ارائه خدمات درمانی مناسب به شهروندان، نماد تحقق رسالت اجتماعی است
🔹
مدیرعامل بانک صادرات ایران با هدف گرامیداشت روز پزشک با کادر درمان بیمارستان سپهر سلامت دیدار کرد و ضمن قدردانی از زحمات آنها، ارائه خدمات درمانی مناسب به شهروندان را در راستای تحقق رسالت اجتماعی مورد تاکید قرار داد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#روز_پزشک
#کادر_درمان
#سپهر_سلامت
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/458542" target="_blank">📅 19:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458541">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبا فولاد خلیج فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzGET1Yxk1ncUmq9wTO8dzOFd5Qh8VhRKbxuDAXwAFDvfKUTCIou4wMxgf_qC6io18SjPyuAWHROLTEaGtFsGs62h-4jNG75M6T9Y53Zs2ucINglCd8MseRqpYp4SfuOZmGKkNSUQHE7fIOXRMIZj6qV-kwo64Ra2VVxfN2GO42EPUUvmI1PP3bM1eyKGG4Ft1o5N1NpIRkr13jc89in71o1lHI5ArDS3KI2-VassgvEpWqXEnk-gQtGZsB_U02DOpM9GYAYgvN_vsK6JAL6PSD-3g2yi2UCE1s-uAG-dfY2joUS6K7_bkPeAwy5PbO59f5FTHbBNG9_-R32c3rUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد ۱۴۴ درصدی درآمد «فصبا» در ۸ ماه؛ فروش ۱۹ همتی با تکیه بر صادرات بریکت آهن اسفنجی
شرکت صبا فولاد خلیج فارس (فصبا)، یکی از زیرمجموعه‌های قدرتمند صندوق بازنشستگی کشوری، با انتشار گزارش عملکرد 8 ماهه منتهی به مرداد ۱۴۰۴، خبر از دستاوردهای چشمگیر و رشدی قابل توجه داد. این گزارش، تصویری روشن از موفقیت‌های عملیاتی و مالی شرکت در مسیر توسعه و سودآوری ارائه می‌دهد.</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/458541" target="_blank">📅 19:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458540">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/458540" target="_blank">📅 19:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458539">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIt9aQH2oYxWKKw43wvxvoEgVUqQLY71TVOpDpFTwR1Dv4O-742yFCP-E4vueP3vgTE7rh69TmOx2VXXC31Zy2CEjcc-o_c6FbzHeYNWkbC7Mh0iJdjPXoEU_Cg0WGOJHp-M_YuSZoRbQ2Oh31AOO30p1sBIbnaAeN9rRq0RZp5pV-W1xqghtIiywbW7rwfrkwmRlSZJNGPqhHIhaN7mERd_QeoXr5kEiXZT-wiiH-C1vZ8FF9n7W6LaHDIA1eTA2S4bTpam5a0x5lp30EjronaUY6SAIpouPhlK3jRC12Y4MW5B5Psb3hstDGyGeLcvBX4wbmhJvXLnkw0C31FatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: ایران در عمل معادلات قدرت منطقه را تغییر داد و ثابت کرد دوران بزن‌دررو، لشکرکشی از پشت اقیانوس‌ها و تهدید تمام شده است.
🔹
نمایش مضحک رسانه‌ای، واقعیت میدان و طرف پیروز را تغییر نمی‌دهد. تاریخ چندهزارسالهٔ ایران را بخوانید تا بفهمید باید با ملت ایران با زبان احترام سخن گفت‌.
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/458539" target="_blank">📅 19:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458538">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1502ec842.mp4?token=JEt6qYuEOLmjzI4XrIdssgEF1j_CgjqOU2d-0MppfprrjRVVkYB1heZKNj13nvs700glkJZMGeydC-4fNUwamHZvLSCm2OeBNaLnfCDOT1hxZ7LZTgSyCNcA9nv4bsdtNKQrfjBq4vA4MUlYHgvJSnt5mV3hwmOJz14Vk4LMeuqLUd1Yab4Tu92-ls8LGjAw1-rUeZ-60hmcMOokCDI1dHcWB7VJTfDLzqME1dYIt5kty4wnEWnwDwHy8DJlZoTU_9twVEf6ka_CGp-67K9UyYOZaxvo59ohWFXnkCT1AFMClYfki9q6oQuDPyT5ar9ztmvVfypcosMSHmWBCZSjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1502ec842.mp4?token=JEt6qYuEOLmjzI4XrIdssgEF1j_CgjqOU2d-0MppfprrjRVVkYB1heZKNj13nvs700glkJZMGeydC-4fNUwamHZvLSCm2OeBNaLnfCDOT1hxZ7LZTgSyCNcA9nv4bsdtNKQrfjBq4vA4MUlYHgvJSnt5mV3hwmOJz14Vk4LMeuqLUd1Yab4Tu92-ls8LGjAw1-rUeZ-60hmcMOokCDI1dHcWB7VJTfDLzqME1dYIt5kty4wnEWnwDwHy8DJlZoTU_9twVEf6ka_CGp-67K9UyYOZaxvo59ohWFXnkCT1AFMClYfki9q6oQuDPyT5ar9ztmvVfypcosMSHmWBCZSjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات جنگنده‌های صهیونیستی به جنوب لبنان
🔹
خبرگزاری رسمی لبنان گزارش کرد که در حملات جنگنده‌های صهیونیستی، شهرک «المنصوری» بمباران شده است. همزمان با این حملات، صهیونیست‌ها شهرک «برعشیت» در جنوب لبنان را هم هدف حملات هوایی قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/458538" target="_blank">📅 19:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttmzvDiKZqKs4g7ST59LLoe-ND2vTFjWX4kPci-_zbDbjAnRquVbrJnu-OPVGEilHRuze2bQKwZQg0COmeaOiaIMW2FVJ8gD7TAaV-uDwwFjk1yqmXJ_JLtVsGYiNyZXDu6qQN0cJqPPMgUr3s4nBV9adB4Svz8C-d_wu2lK36_CAmTGGVfwTQU0ZC_WVkdUhMEMDJE580lZQ0Hay20MNhCr-OskV6VvZWUWaczbjcDqhhCNt97NPdRYIUYXjFMTbhEKo4bueqssZ2fLenmQlKIVMHBcZ3O3HFWtd6Rt9d37k036dywL-1AxTqqLfcqaFKz3W0sqlASPMzz8YgZExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUmBqiHGLI4xxruwMw6jttvmN1IjOsjpIsFBLsVc2F8O2ClGP1ZCHe_mkPtQiVxehl3wcrLN2u06hFYUg7Dhqmswpenf9bMS7mYzxC-LbD55t9lmdwaYxKTMDFmSAw2w6bmglwzNI3kzeo0DOs36KDFr2oRf3P5wp8S6tDkikpb-oz-xbXn8XHvCnYhBpIYnJvQl9zr6-xMVHbBWTSD_-tM4t4IXLSftohfMLc66loL9FuiA-2EEW7XrGPnUsKz8waR-RWo1qH18L6_JFa4iy0cGRnW81oCWp2SQ0VQx_0KfRvSWUC432_NL_W8NHwj778DCD1qCFBvCHLBkosvMGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6UJ7tGGNRzKN5UrBPCFWHtXN-WxNpzuU_xNWVPBI2QvMU6wXZNBf9hsaIpxj3gihdUBqu-uiIt9SPocqkFAxaEr2WiTblDYg3tFXjxp5NkcdUMdOa__RoDAGpHS8sFownddh8scTlwDAVYxrYLnRBPfJrff3szIb_eciSxBZ4T7yLjHFFNWrC5B4jGfp5qBctO_47WrJdWmH-Z1s2OwIKYmDO4uZIuzsIZGElTRCPVZi9PrlVswkIu8CnrlioZRhv6Wq2C2GxtROZ-v9E4uUMWw8MDaWBDVGzMvbUYUdpBbETDm2rjyaLDcUcia3dfRULzEIU6qLMjmttSTsFCkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjZ7VCtF6NOO8dzArze2C4VMAKZhLC5BJqnLVTtQyJBuPyyEBvVZYSyGbCM71Peb14X-YoLqR7hF_PILiDr7p0x7iFkxUTRifn8ZI0SyKBJPvwS4P_RWAnS8H-FeSEzdUs1_hUfbQb2pzMIjuUR60iFFiBaFnCUjUTNOkfRsOAn0DaHA5CvKIWUCCeJRATTqdpKnfWfLpUf0u5bbiSCEHhneaHASAqO18sJ9ZOC0-_JAub6oRtmycIjmUsWl7jpHM9QV_oRiFqcQyMbLfgjvq3PkN0MJEtXJ0wTpUlRVUlOZtrYzvkVKC8bSk4PkuJQXTSFCkn3xA2eFDW9Z7bchtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsYkPAKaldm5U3qAFBB4dvYj6pMhJhHzv5oJnUadtz7tZuRbcddMBHs3KN99f7S8NkKYLepqNUlmt6SY6K2qVtn3Q4OrbrITBNSEIxi8rKf9NBtLL4pBZkVzt-uftxx74Ru3P0KqRiK7uyHAjXoKlc0qYUa9mMp9EqCLsyShr0BofHqsJH0y7Pj-lRFZmkSm8wCINQMar9NroUzTYXM1WFAbdOkjJd3EDOCHOu0YHNfBfHHDcDYO6CHg7PuGfMfu3IdOVPwvSTRJJbl_Rf5J47pLj5PZgfPg72-OVSA6gl6r-jlmSvsgSac4ww4RuC_K6skvzkdaqphjwKAg0hNKMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از دیدار وزیر خارجهٔ قطر با قالیباف  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458533" target="_blank">📅 18:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I47N4sh87khs9SLpoa3gz3bV87Wta2Anzed_sYTwjY-_wgU7s5hAEBzVw0yp1bh9JSKddWzE7EHpTQJjjp5ZfiG90um49L-gCLHQdE5KtFVwuOLPfqpf2iGMCG634KcsOfIPp-enHPqGullDicgtZzv6RUmRE01ypn24oGmBGTLe7-JFrSCDm_oWCZE6RRK7Qz2uMBnl52mZieGcMDYwNJfJtIzAVT8kuhuV1UIjp28U_7kv24dgLsxlf9kQ1grbUkKqCyG_ZC0Drf_w39ZdxaZEW4UHcDX0I9CJbEhFUpFnX9D4psHiOdSlCcQL_CEZTPts__y7RVdgROWIc3jajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCk-wiqTSZux7UF5C-9kOCwfmkX_v8sbh6r7shhnvikbi1vAfRB5YnvAohYGE-iMybchHbRvjgMd9Rb0WmFy5q03VuS5vfWhzdLgvEec7-zShl4x_AiX_3Ve-O5IquJql0xFpbdR6fZutpcUNQzkBXip8KtFKRhiM3L4ltL9JBWS7cyFNeC5uG2-hJ2sZMVOCpSptYzoRiV63rPEn_P4_pGqHwm2g3HgVSAwilYKXyuZ-JgGequM0CTBATd4ud6_pOkaF5Sy-cKnOqvi-XFEZkpANMyd61gtotUGZwTt_X6bPk5F5ft5PVVAUeX918ev-T8nzfVuerF5MTL4BEmSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UivdwTVqT-OJik0cbz3-CJ3fTJE46pxdMYZ-UiwmBmuiNekZxR3L_yK1en5VjeEtACA-LMpr1y9pcVlp1YlvlBI5YtU2QdGgyXX330-t0s_Bw-zaxvJNOOW7RFocGUzudOad0xTn3Kv0exha0GVhz5hexYtL1QCTKun6UBUAPjdrm15aMzv-1L_6yRRAbHdVIEo4nuRSuh5BE0oI1UjyKK_WdDoQkh2snCZ_hN4OpE9wg4pPWNQFtFB9mByTs-9SomnwpBiBaRPTVHcElfV5WhbXBYHg0BsmBpn85TeqZl0d3_bS82sk42O1eka3TPVEnOIuKJoo7y5oET8K_ai97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CeNK31-jOD0052pE880sFbMVPQmlZWtP-fOx9pTtl_1N1CqpHY25z-zoLUS1HKgYkGPO2SW9QpeQs7BnfAtALG9jIvN82vFoxJeLxfYHwowqIPPf0vTHBsyuKlVOJg5c9h_5x5guMfGd6lnUgRdNF-TaVa9FotykF9ZYHy3zLsMKDDeZHNz05d1JmwGPHszpG9DEyE8O97JkbSKEhvSsHO3Gbe_Z0xBTxUIBmvjLdsDz-IRlwOP1pe3DnwZIIogV5KGPhCihaAv574WjuQT3mEhj4dhjwA6mIkEu2wpv2BTfoU3XNgeh2Tpz3zn-6T-5o2VwcLeJnTrkalkl16ANgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzi3AfOx9pbsTpnp6WJ9o1sMgGNkh0HlhQF6ooFO7GpkYweqNuWXZAgPOM3FBshNacMKpKzAW2qAc9vCvSO3GRDJqn0gvDbg6zn1banoPemzQa0doErV4vUgyLkJcLbIZ1Q7CPBryzC8s25YvFV8LfMHeXkS2fFC5IIUOmPu3adFve8VLqXmUHiGVsHXdBEpXlQLeFerX9qMiovxYPmKcqTnPvViUxgrx096w0tEzhP7SdAVeH8Kok3Rp_oeCbZsyYZcdczMDzYSB_5F53aTHaRBxmUekdDV8RAz4vkRhbhWq2BTw_7rmmTeQqCQr0gpcpN--qyS1B8tr8lNZUP1qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
بیانیهٔ سازمان اطلاعات سپاه دربارهٔ ترسیم صحنهٔ سرنوشت‌ساز مبارزه با دشمن خطاب به ملت ایران
🔹
سازمان اطلاعات سپاه ضمن تبریک میلاد پیامبر اسلام و گرامی‌داشت یاد و خاطرهٔ شهدای نبردهای قهرمانانهٔ ملت ایران با آمریکای جنایت‌پیشه، بالأخص شهید خامنه‌ای(قدس سره)، بیانیهٔ خود در خصوص ترسیم صحنهٔ سرنوشت‌ساز مبارزه با دشمن شرور را خطاب به ملت شریف ایران صادر کرد.
🔹
در این بیانیه بر ارادهٔ خلل‌ناپذیر برای انتقام خون شهدای عزیز تحت رهبری زعیم عالی‌قدر و امام مسلمین، حضرت آیت‌الله سیدمجتبی خامنه‌ای(دام‌ظله‌العالی) تأکید و اعلام شده: با امام خود عهد می‌بندیم که تا آخرین قطرهٔ خون، مدافع مهم‌ترین یادگار امام شهید، یعنی «ایران قوی» بمانیم و برای پشیمان‌کردن دشمن و رفع نگرانی‌های ملت عزیز ایران لحظه‌ای درنگ نکنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/458528" target="_blank">📅 18:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458523">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nX1tociwiau3fnHXcAPVRE7lkecKOIzdS80l1k_rGwoMJyT_q42ad2Zpmw0dtYMQXHsPS85kRogiPtYNvWrop8_4xO_ROp5Gnt-Bvtr98nfwdRHLAnASnQwNH2fAyW3yjVJ4WchaRm40k2GZSnF_etirqxziKpaz_3iJoCNq_JC9bSDCdEi0vVgKNo6K2l87-gpj0VareOLUcN4IY5XeTpXzXj27C72tL-Oir88v2COonf3b5dFsymufvAFk-z9_pF58Apa1gh9fBXTBIKXNA_kmsrlFAiMeFtfBcAJZ0O0YlzPTbKqoCW7kCkLn72uOgMWS4qywanBAPrfKnPpcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuMRut3JvPyrqlr1FTGK3fvO3DeVrwRKYlH3zoP6DkN9yjrFV2x3hAnwBJI-nfopdLi91fasqgbj64IDa0hvBrKjaDt6qx-Dg-4TF8KhwFg48uUJSkLqsIOrQZRkgx9OxZst7jN0Ddj5n46Syfu0snGC6nagHglNn_Od3j-5_fCKlmPzmYiTosKTVh4sjzK0dIHjXrlOhPg0npXss-Kdy0GSZAMHxNu8VP04-yxbflvQ2fHtSPdRUR9m-as7H5y6J95nrKwOkceTqH4qGi4-CTuBNAtsQMmrRGovx31MPMyyDLSQXjzr9_1Gsha1ohi2qKVWhga-HNNY-dOw7n2FOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Omdr56eSafTJxLhQBndiWtkUrBpbRQ45tjvlIJdM3bZ4YgcP-69STknt6a4IUJZx2Luxu6Mxgn8MkI-eJDOq-s14LRb5ttH9SgNNoVjY4RHNRbT0vPiyAueZZeITkA7NhNrRbK4ZxKDsxKHvz2E9VeaZFQncuBXmDRYKVuQuulcH0Kf93W1awTKDkixgt28bPGZ--BaPn2h8xht-b2Ye-8bdELjOJUz_biInK-ItjJfT82TUbqcR8p18hrmJZZn7syr8YF5MQeb5huMj2STChvap8rp8yflRK2tGzf8QZWC6we0YVXbM_LH5w-CGWEH1Zgnc_QHjN8856DAMIfLAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJKehjM7Wn9hbNsuT_CbbnXevnyK45qQ2kiioCLkiT-e2ehd11pBPtdjjU_vriRa1qHJ4Llvxt24Trc2qYDr4nacOfo2-Xsj5pdKsKyk96WhOSI2X_1XtSACWJRGsKiTpcJSvEvrv92GKy-M_MUhf7wpxCuyALCZrU7b-zIc9NwOvV75-mX0V11ZjFOMo4_jGTdrbrcPldcL9UG4fINFZ6tMZO_GbAOxCvRtY_ZAWMLKIZvvT6oE9lHqERADBUDOZrmCPx0AJH9iWYi7V3og393xS4ymAulCmBKKFGI19GosOc20gBfLwKPYY7aAl7zRJpZs-au0jOc-eBybdaSmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7Vj1fcclhK3ib8mlEikITNxledNN7_bK9LIVgwT2XxlAP1yEtrROL3WtXaBZdx7oEWevLcNWw1q6iwGIeOuKZfvb4toCYXj1p3v7i2vJOocajnByBP1bteQRy3Or_528ImHqeZ9NC9plHUuM3IRMrTyKHxY_2hWufGtRhDxn0WVMc83ONJs0QIu9lrxAiP2MSKSn7kEnb_JSPPLi6KcPdt-dYvbfUtcWOE_bhswSSjOcGpJftXdrKjZUGptJWeBLNQKxMNQKBtcrP4lt8ncjMOt0_9N3q_URpR6UTlnVyJTnex7huWzw8o4mAhKx8zCcjk6ROB06WOqe-GSup5xyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف در دیدار با وزیر خارجهٔ قطر: ترامپ با محاسبات غلطش ناامنی دامنه‌دار در منطقه ایجاد کرده
🔹
قالیباف در دیدار با محمد عبدالرحمن آل‌ثانی با اشاره به موارد نقض عهد امریکا در اجرای یادداشت تفاهم اسلام‌آباد گفت: دولت ترامپ با اطلاعات غلط، تصمیمات غلط می‌گیرد…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/458523" target="_blank">📅 18:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458522">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3G4bQ05wZxi9P7BtQIVVLKxxKIT0Vhi-tI5RAZTftfub40mHRjK_B9JkKyx5ylDerVPlpI_z881Z3RfodH8JpfHdG2urs62ltx3E565eP7obRlsyy3K8E25jRm82RMM7UICN6isdHKR5jiY_X5OIIsZ2yw3PPTuSH2R-cnwHxrC4lhXdVTpQhCOkLwLENxK8BNkSSC0JPX0mzU5mi0sENRk2LJcBR2Um-VZnZCkCeMpLS0n0WHIaqsIQCG1rzaA0oq7y3oT3yXPrgDN8Zwtf4koqX9srgqcYW7-H8wesZcXrFH7-nci_GADVjXGjNydJ3BkAx5glVGXnHn9w6gKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایزنی وزیر خارجهٔ قطر و قالیباف دربارهٔ کاهش تنش در منطقه
🔹
وزارت خارجهٔ قطر از دیدار وزیر خارجهٔ این کشور با قالیباف دربارهٔ تلاش‌ها برای کاهش تنش و ازسرگیری گفتگوهای تهران-واشنگتن خبر داد.
🔹
وزیر خارجهٔ قطر در دیدار با قالیباف بر لزوم ازسرگیری روند دیپلماتیک…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/458522" target="_blank">📅 18:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458521">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9MG5Xi8qa2W2XBMdmcwcsRP-DHolV79T59rheHHg-Q1u3J73DixbDX1da0Qc0jSdl9ZH8Ecb62Bt2Or--wBoyf5PgiNE9nZOycEPwD9igCR0dEmFKFLeTzUcNHpjsMAiAiQNOM5eljlgBS8esbi_1-bXpjjNxyDm8pNViqbg0GlYF7eMGw4RRPJIbut5Mzp07ov6kkqzQ66yRoX09PLowi2TcOHoVI6stJ5zxCNg9sVBxXSOzrTCEJAsPSAyKyHiX-qgtFNK3jc8hSnk_bExB2VYmyH0z9k8tTR0lgsvOm16CMasTM86IWth-C9th7ExwCx752E-FB0ZyoycueGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روایت دوحه از رایزنی امروز وزیر خارجۀ قطر با عراقچی در تهران
🔹
وزارت خارجۀ قطر: آل‌ثانی با عراقچی دربارۀ تلاش‌ها برای کاهش تنش و فراهم کردن شرایط گفت‌وگو رایزنی کرد.
🔹
در این دیدار، دربارۀ مذاکرات مربوط به چارچوب موقت پیشنهادی برای ایجاد یک مسیر موقت کشتیرانی…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458521" target="_blank">📅 18:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQpVNiTR_84fZmuy95sa6EWpkx4uhzqPscy4poPcFRp06-63LevVYutY-R-xDGVzu_NlfQzkPjvnIEPUXsuqyyiY8pwVSt7mBHl3IcVPwixGHMM2RDbnYs5TCod8mwr1hVDCKEth3LVseTlN9ZsADx_nYj3MSN_TQh3w7xL0w5w59h5mZ7O0od-649vSi1XgixGmMMmqk9f-QzGbta-kI05RBiMcdhGC39M6DfuP5OF66i30sMtS4X8y_1CdEX7m4AJStVhjOEDiP4Y9-rhfd6Pn1uUiukgXN3ty4RsZO7IgQcwVxXxEn4KNHkUA_5FGTrPVcquyz0zk4DwhP9vt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چماق محاصره و هویج مذاکره؛ آمریکا از ایران «آمادگی» می‌خواهد
🔸
کاخ سفید در حالی از تداوم محاصره دریایی و فشار حداکثری اقتصادی علیه تهران خبر می‌دهد که همزمان، آمادگی ایران برای نشستن پای میز مذاکره را پیش‌شرط هرگونه گفت‌وگو اعلام کرده است.
🔹
کارولین لویت، سخنگوی کاخ سفید، امروز (پنجشنبه) در گفت‌وگو با شبکه آمریکایی فاکس‌نیوز اعلام کرد: «در حال حاضر هیچ مذاکره‌ای در جریان نیست و این وضعیت تا زمانی ادامه خواهد داشت که رئیس‌جمهور احساس کند شاید آن‌ها (ایران) بالاخره پای میز مذاکره بنشینند.»
🔹
لویت در ادامه با اشاره به ادامه محاصره دریایی ایران گفت: «رئیس‌جمهور (دونالد ترامپ) البته همچنان همه گزینه‌های ممکن را بررسی می‌کند و محاصره دریایی که بسیار مؤثر بوده، همچنان برقرار است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/458520" target="_blank">📅 17:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYwhosGxKCo7aQUjxsiymYxAzhMoKwAcKnUJ1PIpv2QOV8p771HjSPwh4xsIVpzcZP6EcM-Hrgm5fDaJE2FXTQY5bgdeHMVi9NYBfPm5uUuFQg8P67ucVDhbOMAIpVr6T3rovYSAgbeFk1J1qeXEVqACaXUGRzeXz7mviH81LzQAQi5f5R6O57cpoAXdhZClBis5_tHrSyf0vHMv_J3OUv496b-U1-ro9trMoDb0S3aEGnjEsBqE1RrUHTMV0BIEYIWS0iMV1m-yL6cyoHT7lwiwk477Sdha_qFPmxhqkbbIwfKU-t4Vm8jkNHJ_EZ5X3Q8JlJfKv6Q-d_V7lF3BzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔹
کوروش اژدهاکش، بازیکن تازه‌وارد پرسپولیس قرضی به نساجی پیوست  @Sportfars</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458519" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458518">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b8e26657.mp4?token=tZQp-UEqX4zIZU9BFlZv4oBOrGkDVzVNPNX811-fw0g1EYY0eecSOim0h6GP3H2kpiMHRH_vcsRo-n0j_mPn3W2QS_7GpJVDrvIXpfD7wi2daLu8cK2n5pyTzgeIiZMh00OYSBBAXtV2Ztawx5FJFUEDU4Ksqhm54wv8X2J0MpFBVOuSmopZLv4nXxT1BZuzkhz8GCtglpnpC4h7k4Jn07SuPUjqnSG1FxDuW9yNjttfB52bnJjyfC__6_7sWEIVgTFORBXfwNlBzJjqAvCuJPftCkUohDzqcMDFaTLSVWbz-bzDSxSotjaJ9UiFrftIrTkkQCgKV-ndxLsb8Cpyvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b8e26657.mp4?token=tZQp-UEqX4zIZU9BFlZv4oBOrGkDVzVNPNX811-fw0g1EYY0eecSOim0h6GP3H2kpiMHRH_vcsRo-n0j_mPn3W2QS_7GpJVDrvIXpfD7wi2daLu8cK2n5pyTzgeIiZMh00OYSBBAXtV2Ztawx5FJFUEDU4Ksqhm54wv8X2J0MpFBVOuSmopZLv4nXxT1BZuzkhz8GCtglpnpC4h7k4Jn07SuPUjqnSG1FxDuW9yNjttfB52bnJjyfC__6_7sWEIVgTFORBXfwNlBzJjqAvCuJPftCkUohDzqcMDFaTLSVWbz-bzDSxSotjaJ9UiFrftIrTkkQCgKV-ndxLsb8Cpyvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار و گفت‌وگوی نخست‌وزیر و وزیر خارجۀ قطر با عراقچی در تهران  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458518" target="_blank">📅 16:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458517">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2cd79445.mp4?token=h8YoXshG4ixOAUQ047zCm-G3kGlj9fWc-FnRABbKKgxcouucqnd-_pL8ynFKJx6cGeQA9fYb5_Njf4ISNiRhAW78eOtX1UT_BQP_A0sHh7hlGmkRldIMuP-H7efYYWmHf7z8GvZpHPtkvl_6zw_J8rmRpCEEKgclds_bUcudq1USLByhsTlt6rEH_C3TB5itrx5xDZyBU8_oZPuf_0HHz7HOO28ur7SUNK-LTr1efoivjhyBzxojSAQce8_C1PPPoxRLT8LlsuV185GfrU1viJmd2LMre_lz5SvYiXG_KS2Y_sev7Xixi3Ofjc9gfgz2rUxiZU2llTxh6izYJ8or31IyK3mRyGLcsb8xbXvacch2OGrGdqB5rlBBgavv5P4qgtv61SSMoCJ_XiY5sPrvLpSVF8qyX296uXbbDkBFr-j09DKWt7XUKwhWJ-W64dr0nIHc1DcQjNmpEJ17ZC4ueII4LNtIV0ONj-LUtxq_LsqFrh7tJqV5_UyPeq02zPCc3bys0viT-E-cnXwoUMHHSS-HHMKwmvABMLKEUJkXmhOqRKP_hR47nTevrn2pNQpmPfn4rtu6frvBX-BmYFB9OzqYEEDHK8Jjc-CC2pit6dw2yRODN5f-bW5yibxuKRfGe6TyWcMdjuxTCM3bzvvX-Jc6jZmiWbq2LzZlDQghc9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2cd79445.mp4?token=h8YoXshG4ixOAUQ047zCm-G3kGlj9fWc-FnRABbKKgxcouucqnd-_pL8ynFKJx6cGeQA9fYb5_Njf4ISNiRhAW78eOtX1UT_BQP_A0sHh7hlGmkRldIMuP-H7efYYWmHf7z8GvZpHPtkvl_6zw_J8rmRpCEEKgclds_bUcudq1USLByhsTlt6rEH_C3TB5itrx5xDZyBU8_oZPuf_0HHz7HOO28ur7SUNK-LTr1efoivjhyBzxojSAQce8_C1PPPoxRLT8LlsuV185GfrU1viJmd2LMre_lz5SvYiXG_KS2Y_sev7Xixi3Ofjc9gfgz2rUxiZU2llTxh6izYJ8or31IyK3mRyGLcsb8xbXvacch2OGrGdqB5rlBBgavv5P4qgtv61SSMoCJ_XiY5sPrvLpSVF8qyX296uXbbDkBFr-j09DKWt7XUKwhWJ-W64dr0nIHc1DcQjNmpEJ17ZC4ueII4LNtIV0ONj-LUtxq_LsqFrh7tJqV5_UyPeq02zPCc3bys0viT-E-cnXwoUMHHSS-HHMKwmvABMLKEUJkXmhOqRKP_hR47nTevrn2pNQpmPfn4rtu6frvBX-BmYFB9OzqYEEDHK8Jjc-CC2pit6dw2yRODN5f-bW5yibxuKRfGe6TyWcMdjuxTCM3bzvvX-Jc6jZmiWbq2LzZlDQghc9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: ۴۰ درصد ظرفیت آسیب‌دیدۀ پارس‌جنوبی به مدار تولید بازگشت
🔹
آواربرداری پارس‌جنوبی به‌طور کامل انجام شده و فرآیند بازسازی به‌صورت منظم و برنامه‌ریزی‌شده درحال دنبال‌شدن است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458517" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458516">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2111b7992.mp4?token=Y4t8PCV3SKVEXhHSC9ldZ_rUVMM1yLDu_E4F4Psw84th0aSRqzhA51MsSEe7QDDaSI25EUwXcpTY3jTiFvwZv7V6X9cKZcQICVyk_9rxDZaZqXx0Q7vZlQywnG7k5NgFXuzrL7V2HEB5puq4xYck5smNjlUk5VXx--8lz6u_mrI5TipSCws9W9pYLTWfnZ7x0_5wRa0fnfPlYMAeyqe_fMvIC77JNQwIISUZvVqY75iP8p2aBOWIuZ_jfDk3UZSfG30hYX5xDgavKbNcYOLgu9H5u15dKAIagDG8JSaKlB8_PkpbNiDIja8JT93kNj5wZSlSTXxtoy5iEKSG4bzSCZdDofOBTjoCuqPVxGgckB4_csDt2gbUikqpuFEUQUQpqiElwVZ4gHOddcjekrkAMEgakW5BBNS5ZgYZmOyvVmEWEDWU7o8l4gw056dmZMQgSRIsxbJMGBzW5yssX2AW63HAc9Hu2TAdSQH4rOa6hKpzu1SA4qUjSMrmrWtVGPDJBg1jRnxhZC1Kf7pIskcidfKqPPM0sdZh1ttUfEyREZyQFo47k146fAkUoDxGJIubZAxd2XYNgkldJaLFr0CMrapADvaMpUAFaZPksQc_2C1zFxfJ7-xnvR1l9sv9GtIyDpqnGG2suDnJBdMOvjv7mLleG6EZHraqSLFYhLsM0pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2111b7992.mp4?token=Y4t8PCV3SKVEXhHSC9ldZ_rUVMM1yLDu_E4F4Psw84th0aSRqzhA51MsSEe7QDDaSI25EUwXcpTY3jTiFvwZv7V6X9cKZcQICVyk_9rxDZaZqXx0Q7vZlQywnG7k5NgFXuzrL7V2HEB5puq4xYck5smNjlUk5VXx--8lz6u_mrI5TipSCws9W9pYLTWfnZ7x0_5wRa0fnfPlYMAeyqe_fMvIC77JNQwIISUZvVqY75iP8p2aBOWIuZ_jfDk3UZSfG30hYX5xDgavKbNcYOLgu9H5u15dKAIagDG8JSaKlB8_PkpbNiDIja8JT93kNj5wZSlSTXxtoy5iEKSG4bzSCZdDofOBTjoCuqPVxGgckB4_csDt2gbUikqpuFEUQUQpqiElwVZ4gHOddcjekrkAMEgakW5BBNS5ZgYZmOyvVmEWEDWU7o8l4gw056dmZMQgSRIsxbJMGBzW5yssX2AW63HAc9Hu2TAdSQH4rOa6hKpzu1SA4qUjSMrmrWtVGPDJBg1jRnxhZC1Kf7pIskcidfKqPPM0sdZh1ttUfEyREZyQFo47k146fAkUoDxGJIubZAxd2XYNgkldJaLFr0CMrapADvaMpUAFaZPksQc_2C1zFxfJ7-xnvR1l9sv9GtIyDpqnGG2suDnJBdMOvjv7mLleG6EZHraqSLFYhLsM0pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حیرت تلویزیون موساد از فاش شدن ضرر ۵ میلیارد دلاری ایران به تأسیسات جاسوسی آمریکا در عربستان!
🔹
شبکه اسرائیلی اینترنشنال: ایران با یک عملیات پیچیده توانست مقر یکی از دقیق‌ترین و حرفه‌ای‌ترین امکانات اطلاعاتی CIA را نابود کند!
🔹
حالا ما می‌دانیم بیست مرکز اداری فرماندهی و لجستیکی مورد هدف قرار گرفتند.
🔹
حملات ایران در محل سفارت آمریکا در ریاض انجام شده؛ جایی که در طبقه سوم آن دقیقا مقر یکی از دقیق‌ترین و حرفه‌ای‌ترین امکانات اطلاعاتی CIA بود.
🔹
عملیات به‌صورت پیچیده‌ای انجام شده و توانسته‌اند از دیوارها عبور کنند و بعد از تخریب دیوار، خود تأسیسات را نابود کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458516" target="_blank">📅 15:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458515">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTkFpcTKy9cEJE75Z5SvZGyR_lIJs3ORjoauj7TSS6rFwy-ve5ma5IDW16fKvk6KbyoDbSbIJT1d891MhOBcMIZyVljH4FnyOGx30LZiEx-Bd0DRfJ9YON2qWrrrD6XODQLG5XoFNkgQmQU7_vISoCOj1enw1LmZkJ2Ip2aMPQCNeY4VuaHggeTaTuannFyFoaImKmiiS1CHsiu0jWe0vXm89D5rB1DFEn56ajDBl0Cxw0XjyLwh7cDi3M-CNUrTYLBM4Xsf1yU_jaDO0yxhiNZcC8SNsN3ZPeyEy6Yl4vTHSm2FuM6IijVfh5Cmeuq5v9g1LXpozKKVGabXsf-uNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک محرمانۀ موشکی ایتالیا به اوکراین
🔹
طبق گزارش روزنامۀ ایتالیایی «لا رپوبلیکا» دولت جورجیا ملونی نخست‌وزیر ایتالیا مخفیانه بستۀ کمک‌های پدافندی را به اوکراین تصویب کرده است.
🔹
این بسته شامل موشک‌های پدافندی «آستر ۳۰» و همچنین رادارها می‌شود. آستر ۳۰، موشک پدافندی ساخت مشترک ایتالیا و فرانسه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458515" target="_blank">📅 15:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458514">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOx19cldsccdZf-pKCBKU0UqI5c2zNVYOhQ0vyXtEcEaQltq60XPeA8m4UuxR_anIFsoOL1jLs2Jw3In4zYxTxbybvMIr34jEQ9zIlLFTA-6VS9EKyKqQZQiVXuULBnhQsMC6ywHzQFBXpcnSqSRBOtPb1BD1ZlFjoEr2T3QHWEC5WlZo9xvMZ1Q03G8oI7tWFvbSCgkhjQe5gjKNVR0xGohiw1pj5Fqtvcnjr6zfJ2XYJj4AnaHB5BHp-kFLYKbaiukQgf47DNnPcPXGyw6v5MXSIOnmq5cV-keLiPioSgTfaU9_8N9NJTHdyufblyJiykkgaZevVaEoD7btpMn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشین، معاون رئیس جمهور : قدرت یعنی «حق انتخاب»
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، قدرت را بیش از هر چیز در داشتن «حق انتخاب» دانست و گفت: کشوری قدرتمند است که هیچ‌کس نتواند آن را در برابر یک گزینه ناگزیر قرار دهد.
🔹
حسین افشین با اشاره به تفاهم‌نامه اسلام‌آباد تأکید کرد: اسلام‌آباد برای ایران یک مقصد نبود، بلکه انتخابی عقلانی در میان گزینه‌های پیش روی کشور بود؛ انتخابی که از نگاه او، معنای واقعی قدرت ملی را نمایان می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/458514" target="_blank">📅 15:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458513">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTechnolife.com | تکنولایف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvVuQxkxI5iZRMxD_2e7CkKkkfzIKCgGfGQ_xjBYpciWMdqD5SIAu41mMNU2G-i0H3hMoKVlzCLPBkeP322WxCh693wvVpHGMlmejVnvThmMUHJzN2ngGBxFsajLsn0aXesn4ydlzYY1LtMqWE5nwM0WatdOOu1zj-kpiztflitpDG571J_2WJAk3_hVqkuINnxiNseuvisr4I7pBSy4eB7kt8HHRVKcxbwNc-qo71omxQSIy8msx25XtMD1jylgadxFc6D6k7310yBZRbKHzXKgx2RWHvt8LhmMJtifKIaI4Ambm3E5Mh97L0EY8rT76-dMOG-2D1y5l-voCCBkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یک خرید؛ شانس بردن آیفون و BMW!
✅
تا
۱۰ شهریور
، از تکنولایف با تخفیف‌های ویژه و قیمت‌های کف بازار خرید کنید و شانس بردن
آیفون ۱۷ پرومکس
رو از دست ندید.
✅
اگر پرداختتون رو از درگاه اسنپ‌پی انجام بدید، علاوه‌بر قرعه‌کشی آیفون، در قرعه‌کشی
یک دستگاه BMW
هم حضور خواهید داشت.
🚘
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/458513" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/458512" target="_blank">📅 15:14 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
