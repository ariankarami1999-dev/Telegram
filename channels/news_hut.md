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
<img src="https://cdn4.telesco.pe/file/Max4xZCaw2eu5CrsAEMtDcsIFEwbGh2jBREciEy66DkSj-2aBeNQqpcHuIcrS2VtjgqtT6BxfwJF3gPv20BVVNF-9HOiibPYeBaTWT29bsXmVl_ukHSCcTac0DCz0zWiQ6s1-Per4TVXbO0SawLoN_L2O_fvy1_WLKQiut8cE0JHPNvqyU6aRoz12InSxvVmcOo4TAXcsRJ9LRN-A6qWHdGJsS2mRJViFO9fs_obcGZlqV7yXdmWLYcQ-E4DpAJTBi5WIptMK9CNVVFAPgQNjBsv-xvQUXI0Gxi4EsYQrQ-6Lo6t5aa_W0dz7Wimk55u0hy61tdSvpo9RAeFI99ewg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0VEBoa4HupZNwW7iNEVRR1snvlC7PyN942W8Abn-mx56wgpbF-U0EhJ1Acc9IumuZKqylaC-Ija1rGq-NCOapW4_KiSH-jmChFn32mdvfw6WV9C20w7c72OrPUtO539TZu2hC7tlNV1EU9dt9m6f0T_2vOa9E2kzURptTQS2NZK1RiLRe4axL6CYaaNltIJPgfL5XTQLdbDLMQxleZ8veao-FF9XYOhBtBF-9YHzhdB1JAzwyGKkcSWrudiWlqKNH7Gijl0rQwMGDV8TqSRLYwXvsxCjCTFnb7cNPfxLMWN7JMwrpOILdze3IFs3sgh_AtOG6TdJrsNbb9QYqTdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=jJ2U36hHxM0O7IKoJXD4r9cena-Ku2BZMHvqZziC-qRGaNm_wFTH9gHtHZCXLaftItJE5aMOfba2UkImANsPT7q7SFhVDksVOUZtmr6mPjrzjnFfTN2_TGVJhT3GaVcbUlKEcGP46fiSglv3FFBShsVDHeKjz4EJvXdm9Qu9S853ZBYtMyrnqD1CrcKdYb04r3KckyWW3saC4AnAOSygemSDtuAfBGPZLHw6NdnbQzQqoFbcUNFxUh3SO2dIDUaTqnD1CwfXmJOs7uaBw-sFvoOr_WFzBYAYuNii8xJ-Xq1bg0GL1hJfWAo0J-_75cAk8DXj_YxDNGQZtOmQB5VYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=jJ2U36hHxM0O7IKoJXD4r9cena-Ku2BZMHvqZziC-qRGaNm_wFTH9gHtHZCXLaftItJE5aMOfba2UkImANsPT7q7SFhVDksVOUZtmr6mPjrzjnFfTN2_TGVJhT3GaVcbUlKEcGP46fiSglv3FFBShsVDHeKjz4EJvXdm9Qu9S853ZBYtMyrnqD1CrcKdYb04r3KckyWW3saC4AnAOSygemSDtuAfBGPZLHw6NdnbQzQqoFbcUNFxUh3SO2dIDUaTqnD1CwfXmJOs7uaBw-sFvoOr_WFzBYAYuNii8xJ-Xq1bg0GL1hJfWAo0J-_75cAk8DXj_YxDNGQZtOmQB5VYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=eHumTd4P476xchtk89T9aUAU6AYiTygSVKuJeObU6Bx5oURhRfwQ_fgEtMcfaOdO2_O2qI6z_AsPjbvOVSlaTq8uXQKbjILq_2oIylVcT-7VbCNbaaTlNPb0cNPmNsNOyNVcVP1-pAEvYITQ46VRjnACGT0yjtRYm6SeaszRGgI5ZM3ccU25e1uEVZdBMX4qJiu6Wo99ljMqsiG0aUxzR8xY_d0wEn8plPABcuut8KakawDzFiSr3FqxgJTPOXnpzVCnapGh_SQDEwMZ9RNNrYbQXrTUSpJyDyBkasb4rAEOdm5MQ9se9DIeA36r1RuSpKe8iMUbS42-82oA77bkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=eHumTd4P476xchtk89T9aUAU6AYiTygSVKuJeObU6Bx5oURhRfwQ_fgEtMcfaOdO2_O2qI6z_AsPjbvOVSlaTq8uXQKbjILq_2oIylVcT-7VbCNbaaTlNPb0cNPmNsNOyNVcVP1-pAEvYITQ46VRjnACGT0yjtRYm6SeaszRGgI5ZM3ccU25e1uEVZdBMX4qJiu6Wo99ljMqsiG0aUxzR8xY_d0wEn8plPABcuut8KakawDzFiSr3FqxgJTPOXnpzVCnapGh_SQDEwMZ9RNNrYbQXrTUSpJyDyBkasb4rAEOdm5MQ9se9DIeA36r1RuSpKe8iMUbS42-82oA77bkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=dSIb1Btb5a6fdzuRhaCd3KfteCMSL_okfJn2dTse-Xa0uUnmX_rTALfCX6_9hgJ18g61HeLp5A2fsLkYcLh8p12Df9yms_BFLlHfOrF6RE32RKBQValbMgdQzHKke_A-F8PyxfG5Wck_tcgB_qVrBk4L6Pb9wVmaddPhe3SwrMK6OY9Rb3TZs2m1CfbGCuHY5ogkLLRVq3vL1eIhWpdhZp0buXNCXke-4oXMMhxNY4yfkMp83f1ihrf8cYAP30pxXZCLEBiQxIsyeeDDzV-dvOG9KYOBzgUtUOIupsvQqCcDcuZGaIBdKG4nEwLwcFe41TGOa-9PRyx_scY67qk94Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=dSIb1Btb5a6fdzuRhaCd3KfteCMSL_okfJn2dTse-Xa0uUnmX_rTALfCX6_9hgJ18g61HeLp5A2fsLkYcLh8p12Df9yms_BFLlHfOrF6RE32RKBQValbMgdQzHKke_A-F8PyxfG5Wck_tcgB_qVrBk4L6Pb9wVmaddPhe3SwrMK6OY9Rb3TZs2m1CfbGCuHY5ogkLLRVq3vL1eIhWpdhZp0buXNCXke-4oXMMhxNY4yfkMp83f1ihrf8cYAP30pxXZCLEBiQxIsyeeDDzV-dvOG9KYOBzgUtUOIupsvQqCcDcuZGaIBdKG4nEwLwcFe41TGOa-9PRyx_scY67qk94Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=FY73p_8-8f9sLdBrQit76CXeuAbVl-cUCkHPWj0oQ69AHPKR97HqRwoBMK9mJCOIqwQmBQZKZedu5_dJBjaRtcG_jPeMVGacjTatHQ9XBQ89xePduInMnlUUATkwRSfvQJoxdqhwsYx40pIg1xQfSJkr7ga-WHz6jGtR-7yYEMfmPKsPjFUL2G3ZzxXZtFPL60r2vAmcvxrMbvZpZao-CfOiM7EvNRMBiAL3WDU6MVhYX--NG3vjen98CNfMQi4S7niE4-AEgp4oAVMt_kpiWu4GaiPV06HXuqFLwwJwQ3NwqQ0TZ_ca2XGDz1Pkzn57fLiyVyiuFTogXwcmnwWKmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=FY73p_8-8f9sLdBrQit76CXeuAbVl-cUCkHPWj0oQ69AHPKR97HqRwoBMK9mJCOIqwQmBQZKZedu5_dJBjaRtcG_jPeMVGacjTatHQ9XBQ89xePduInMnlUUATkwRSfvQJoxdqhwsYx40pIg1xQfSJkr7ga-WHz6jGtR-7yYEMfmPKsPjFUL2G3ZzxXZtFPL60r2vAmcvxrMbvZpZao-CfOiM7EvNRMBiAL3WDU6MVhYX--NG3vjen98CNfMQi4S7niE4-AEgp4oAVMt_kpiWu4GaiPV06HXuqFLwwJwQ3NwqQ0TZ_ca2XGDz1Pkzn57fLiyVyiuFTogXwcmnwWKmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=MqpKLzV03ZtHnKhJXrSzVewj5TsuGe9yIzPP5FqQW5A-sGA9vdPhfQ-D0mqXdH_qR0FKEqKhmjQ44xTy4QMbL0QWQbvAIwhsL1uyp32wu_N9p6DkO0OGk7WTGxgA7SlNeun1ZVDcnTUwy7RxcQkS-x0n9DPIZJBV2d2oR4zuHo6c-6mG96zj8U9sZdmEICchNJDEA7nhb9G9C8FYDnxqy3Kh4nPYDVygi4Ciksi30p7HZxkhZRl8HlC4g6Wjf6ueff4QOSY-H6quhWnHNZvxFNLa5h28Q85VJkTUbkpQmrZjW9OLHxLxuHpZw52VbhNjz1TjNyGvP6iu-rMoo-Pi2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=MqpKLzV03ZtHnKhJXrSzVewj5TsuGe9yIzPP5FqQW5A-sGA9vdPhfQ-D0mqXdH_qR0FKEqKhmjQ44xTy4QMbL0QWQbvAIwhsL1uyp32wu_N9p6DkO0OGk7WTGxgA7SlNeun1ZVDcnTUwy7RxcQkS-x0n9DPIZJBV2d2oR4zuHo6c-6mG96zj8U9sZdmEICchNJDEA7nhb9G9C8FYDnxqy3Kh4nPYDVygi4Ciksi30p7HZxkhZRl8HlC4g6Wjf6ueff4QOSY-H6quhWnHNZvxFNLa5h28Q85VJkTUbkpQmrZjW9OLHxLxuHpZw52VbhNjz1TjNyGvP6iu-rMoo-Pi2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=I2vCocKnxINi6GqXQo0bw3pIH13gnqN5BaJcKbLTKQVinUuCQm1Ej0rX8cmR2-fmhX7eSbvw-YuEqN-IumCt0lQZYtpq0M88hAlnuIWdTRTYIHpEuBwDHjD-MzIBT5tEjqnC8brgUVsOf4cB1Rdsvz-gwffLppncEICywViDUKr1MbFlAl0ZdoQWuZp6BdVSzJlvNSP1giAwuwYjZhwjFwBDtchnlTWy33stX2VSjW5-gfpbpaaVYSjxevZPh7vUbtQDEZJ2SPNRkDsYf57e2gCg6kD0E1OAFy4SxhJj2msmxb_LA_uapNae457H_PQ8jMA1p7L_Kr5H0hmxB5ljtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=I2vCocKnxINi6GqXQo0bw3pIH13gnqN5BaJcKbLTKQVinUuCQm1Ej0rX8cmR2-fmhX7eSbvw-YuEqN-IumCt0lQZYtpq0M88hAlnuIWdTRTYIHpEuBwDHjD-MzIBT5tEjqnC8brgUVsOf4cB1Rdsvz-gwffLppncEICywViDUKr1MbFlAl0ZdoQWuZp6BdVSzJlvNSP1giAwuwYjZhwjFwBDtchnlTWy33stX2VSjW5-gfpbpaaVYSjxevZPh7vUbtQDEZJ2SPNRkDsYf57e2gCg6kD0E1OAFy4SxhJj2msmxb_LA_uapNae457H_PQ8jMA1p7L_Kr5H0hmxB5ljtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE-zT-B1M6RiadRq8ZvBSDcnadgHnAYkvz-DqM8wQcPdThpu8kBICDJCYo-nG5q0ZG3ocGuUCaH_CqM0fPU5AQ2ZdkQnKefoZo7oAd5HkegphMh1XNhY5PXjhMMy64SXDMtBkPZxbBUlE_-lFj45DdGjhbrifNf6dvGfFdTPUlLqkEgOKBqmGPJoHgWsCBFlh_hx2pXWvLeIr8lYg24nfRuSMu7imDqE1Cf35C1IK4P25r3dK1LIr6P-Y9iuW2mfY57ymtLgdVVn4gnNOk16fWHEWs87qST_4auBlq2V6WuQ_7zhGu3_MlAYo_eBcYmRCJBXNcuYmFwHT0xWIq2DOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=VnDeahdFkX_Q2ghsSUqvxG_mhx0B1dO0E-US3LQoA7JvXQO5NcNp65WXuY-P06BG-OqmxcNyDwd6dSu0VPXuVWMw0cO643j-sQ-mMHnMcEJA69p8FrYtRrBI0n0VRYuF2S0EBDN0swppPhPWpB-T9cKd8KYeaBMx9NOLzxD0B76elChdDt9EttMaJUTn4TXDnoWjzG_8OHo2foNniYF1Kzn2TzV2UQ4moVGfcTCZmlTdd2Fb0VM3JQKEbH13vIWWBobUuvLuFATsxBKFyn0qguzJdPGjs6wm0-3MVCaFMD7kcdqXMyMC2vzVrdbZTXN7VGgyw5FDjjQmNWS7uO9c6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=VnDeahdFkX_Q2ghsSUqvxG_mhx0B1dO0E-US3LQoA7JvXQO5NcNp65WXuY-P06BG-OqmxcNyDwd6dSu0VPXuVWMw0cO643j-sQ-mMHnMcEJA69p8FrYtRrBI0n0VRYuF2S0EBDN0swppPhPWpB-T9cKd8KYeaBMx9NOLzxD0B76elChdDt9EttMaJUTn4TXDnoWjzG_8OHo2foNniYF1Kzn2TzV2UQ4moVGfcTCZmlTdd2Fb0VM3JQKEbH13vIWWBobUuvLuFATsxBKFyn0qguzJdPGjs6wm0-3MVCaFMD7kcdqXMyMC2vzVrdbZTXN7VGgyw5FDjjQmNWS7uO9c6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=TXo8YAsAOjHq4PYmd7uakw6mq-PzW81diI1ZUdZV3gNMjRv15X_VE8O53pXiKoloWvlIYTQAE-rjfh0Yfk_dYX9oJpdq7WIpcLm5SzIpPwNbPcyIEbO6JC0RzNKVADfs36rK3RDY2QyN-tthB7vXUjr_ItV3xG7XUezbSOqFVIcANCE8_EA9Tum-LBSn4p0QYwFar2TzA9lkIfN4-CVMEQljOZElZ_cDPsL8Ty4Tn1xyO_XkYy4V6jDowGppze7RwqektAkbS10BQhcjDC1tUdO1TVqs_xOPokMz2eBcn6_h0ubWu-EzOeDlwpAtYJHwfisIQgygrKN6EM65aNxdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=TXo8YAsAOjHq4PYmd7uakw6mq-PzW81diI1ZUdZV3gNMjRv15X_VE8O53pXiKoloWvlIYTQAE-rjfh0Yfk_dYX9oJpdq7WIpcLm5SzIpPwNbPcyIEbO6JC0RzNKVADfs36rK3RDY2QyN-tthB7vXUjr_ItV3xG7XUezbSOqFVIcANCE8_EA9Tum-LBSn4p0QYwFar2TzA9lkIfN4-CVMEQljOZElZ_cDPsL8Ty4Tn1xyO_XkYy4V6jDowGppze7RwqektAkbS10BQhcjDC1tUdO1TVqs_xOPokMz2eBcn6_h0ubWu-EzOeDlwpAtYJHwfisIQgygrKN6EM65aNxdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=eyBHO3KBslp8F-vXV9NXDulkMx6-WME_IXSkj3Ka1PbRMW74wFN2A22-DBlOqSaBurSs7NVGH0zPY6fWW--klKBkZ2rx-QikxVmpRjRaIjpWgs_3HtSNuydVXTqSRWNmksCwZY9R74MBbO4tbfAlHJs48kppFJ0bF5TkP28vKPfuXzu_U9tYEgpUqCKwBsGlvWzlZlcOkeUHMtiWLxRPL_chjSLAjSdg89WXFyogW8sELuz47W81ePtZuYdlP9WZTLDDHAs5PdsGZPtoVyRWdu1M0dSyxgSfG1AybGb1RDcFqwhMn8P26CkKyl6hP2GYV5qjHap8THe2wX9dLLYcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=eyBHO3KBslp8F-vXV9NXDulkMx6-WME_IXSkj3Ka1PbRMW74wFN2A22-DBlOqSaBurSs7NVGH0zPY6fWW--klKBkZ2rx-QikxVmpRjRaIjpWgs_3HtSNuydVXTqSRWNmksCwZY9R74MBbO4tbfAlHJs48kppFJ0bF5TkP28vKPfuXzu_U9tYEgpUqCKwBsGlvWzlZlcOkeUHMtiWLxRPL_chjSLAjSdg89WXFyogW8sELuz47W81ePtZuYdlP9WZTLDDHAs5PdsGZPtoVyRWdu1M0dSyxgSfG1AybGb1RDcFqwhMn8P26CkKyl6hP2GYV5qjHap8THe2wX9dLLYcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nv4eZH_RgIvdfNm2ApVA3vKrywhnnVJlKNW-dcKudEgRRkzqaKaZI_u6B8cDOd3vugH3geh1G2Hl3D911nRKbEsO2yYpHN3_PFhgdnS66Bq_Gg7R2ubmLJP0M2svvZnSTYHIZcSLBbhcOUlx_oKRHJFjBTFCtBiW29H5Zde_f73e0dQP8kiDDnXoJU83PljxGsxNHZZJ0Du57kLn9bfncRP7v2WSxS5WmdgQuUQ5vjmK7QCJWdBT5bOirfKWoHclfV3spRFvdjrzHRDxjb5T9sI2yrG7fA7afEZeL4wgzh6tgkjVQUhjaENGLuTyeg6JQq-UuD3vvQA1DhVttF_pTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=nvg13yFT1plaQNUn4azmnu7E1x9wugsQqMsT9KVj8-_lR-MweIrSLeGlomEn5i-I4Hs4WeBAsCJ3iABpbcYcg9ewgKKTsTKk-d7HRglRp1Qwg1l3_RqwBpitkU6An4yabknu4f_IPFuPezmMuzR0P8MsijqYPmQ-RKTXNBMPnarfgRSiCx83Teu8wYCGyJNXLcIPsykoRSLcNWLCfJvNj6EKbTYWertLktO6BWQ-ObL8YQbbFvoCodC9-ouAIDlDz0osL9POEv1AsAtuZvdtWcQKvWhQaGkzmB6_IEjs7npIWZq_Ch5JKpgGYnpiOMV9HEOK2bxhxrQ7yX88OnO3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=nvg13yFT1plaQNUn4azmnu7E1x9wugsQqMsT9KVj8-_lR-MweIrSLeGlomEn5i-I4Hs4WeBAsCJ3iABpbcYcg9ewgKKTsTKk-d7HRglRp1Qwg1l3_RqwBpitkU6An4yabknu4f_IPFuPezmMuzR0P8MsijqYPmQ-RKTXNBMPnarfgRSiCx83Teu8wYCGyJNXLcIPsykoRSLcNWLCfJvNj6EKbTYWertLktO6BWQ-ObL8YQbbFvoCodC9-ouAIDlDz0osL9POEv1AsAtuZvdtWcQKvWhQaGkzmB6_IEjs7npIWZq_Ch5JKpgGYnpiOMV9HEOK2bxhxrQ7yX88OnO3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBo2oJgNQUz01zVKXR0i7N_yslb6jVuKuN0leFzgw617RBWcX5SlFsc4BBjhqAC6t0tRRHq6IYS7NcNPYl_VmsXvZTFoqTAc5C_ht_5yuo6N8EFBxY_pm0IOpJK6riQerS8E4W1N5pt3f0C4W5z8ztmYmp96konlqIJ1cy1TutmUL7d3YFCem9A2-HP4te245fTFqKmXruQkFfKy5aJRhdqpUzIWdZs4ZsfkP640I8h8WFSUnCKA8oCcSAhDh87PKnlwN3cvTzgIb_mmcAeZRAUfXrXUDpOvdkEpqF13ses4kGiN3bUSnq62jgvWJSVdXUhuXUxviFjJkttL3s9afQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=Vre2NGvoZCRMEqcSqQVYx6RqVvPO8hhv2_qblukZU3cCmJX9zvkqd3y5WVJtl08w89cQqs5ZJzpNUXw1u0ddbQLOguaijNsP6LqFfPYfow2nBEDNMSddw3xkxg6TAOdt5dkZYSLEs7K9DqTOuI4EVA-hVEL4d2etcfN63f6-oNa8Fo3yWYYTwdGCFO4z_GJg9xOTh01ctiBxFMid2ZD9t3tkmcCC1mTLv-wP7RA1cGYjbDvjJnc75wSTxAubdYZsGA_Nu28nfvXpfy0iyWYfpe4S1ykWsc-LFS3iwa2GomABrPbd2JmLlJRfFRt4RjNYPWktvTdwoZ-BpC9HWM3tbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=Vre2NGvoZCRMEqcSqQVYx6RqVvPO8hhv2_qblukZU3cCmJX9zvkqd3y5WVJtl08w89cQqs5ZJzpNUXw1u0ddbQLOguaijNsP6LqFfPYfow2nBEDNMSddw3xkxg6TAOdt5dkZYSLEs7K9DqTOuI4EVA-hVEL4d2etcfN63f6-oNa8Fo3yWYYTwdGCFO4z_GJg9xOTh01ctiBxFMid2ZD9t3tkmcCC1mTLv-wP7RA1cGYjbDvjJnc75wSTxAubdYZsGA_Nu28nfvXpfy0iyWYfpe4S1ykWsc-LFS3iwa2GomABrPbd2JmLlJRfFRt4RjNYPWktvTdwoZ-BpC9HWM3tbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=ExQgfxaxXnqrBkDNyfoO4GmEoZ1WikIv7XlOSklCVDUOf4ECUFdwNBAgJ9JWCy6rUjGrc-VOyQkGKc7at1jlnb9CrRDJJiXgaiZNb8RVvbTQqNByZbSwkPQVljaMGpBZ-ZcFFjN5QiOCRfWdUgXrcJfiLp0tM3t-hyt-WC6WQQQ0A2Icyu4PuvqDYiwaaEH-WpEF30Hp4wZ2ksj2yQN-7c0d0fjn71h1Jc1nQr657bUSI2EpWj-KTtQpZYv4R5GQm27GczKvBiTtI8UWfgEkkxMASZfSU1tQJC9HaIRpVDxXTy8_IroFx3pXYVihvVHV88Vu_Mbwfc12gm2chp8OORW0VoPe0neLR2hHthmc4hpykvtOX94DPStdFPXttz64AlfOj3kxux2mCrCKQugm66oArl17jmGiKUXaez3p2MQi4Z2wFtXbNwTCktDT8EoJ50bXDnuXyUab-X0V3Exztgq2OL31egbbR_bTeZHVW5eVXTt4Ao3M4GislKpqrPXWn6XYteClzLYBR9OmOc3NYGRGJ0_0G7htbINnmgq-nf-n98DporRQtEKV5AJgg2bF9vuQf4aQyzqsgsIbDysW0nVn1HgQaO4UbuxEk3HOYUueJhYyRRUzxm8wHmr7svgaJvUzlQ8wfesdvqOq5zdUB11jJ2G_qDdNzY_s2WDSdo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=ExQgfxaxXnqrBkDNyfoO4GmEoZ1WikIv7XlOSklCVDUOf4ECUFdwNBAgJ9JWCy6rUjGrc-VOyQkGKc7at1jlnb9CrRDJJiXgaiZNb8RVvbTQqNByZbSwkPQVljaMGpBZ-ZcFFjN5QiOCRfWdUgXrcJfiLp0tM3t-hyt-WC6WQQQ0A2Icyu4PuvqDYiwaaEH-WpEF30Hp4wZ2ksj2yQN-7c0d0fjn71h1Jc1nQr657bUSI2EpWj-KTtQpZYv4R5GQm27GczKvBiTtI8UWfgEkkxMASZfSU1tQJC9HaIRpVDxXTy8_IroFx3pXYVihvVHV88Vu_Mbwfc12gm2chp8OORW0VoPe0neLR2hHthmc4hpykvtOX94DPStdFPXttz64AlfOj3kxux2mCrCKQugm66oArl17jmGiKUXaez3p2MQi4Z2wFtXbNwTCktDT8EoJ50bXDnuXyUab-X0V3Exztgq2OL31egbbR_bTeZHVW5eVXTt4Ao3M4GislKpqrPXWn6XYteClzLYBR9OmOc3NYGRGJ0_0G7htbINnmgq-nf-n98DporRQtEKV5AJgg2bF9vuQf4aQyzqsgsIbDysW0nVn1HgQaO4UbuxEk3HOYUueJhYyRRUzxm8wHmr7svgaJvUzlQ8wfesdvqOq5zdUB11jJ2G_qDdNzY_s2WDSdo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7BXkhq9Cvche5wUe76HsqbBOF9nSLkZjWVqTas5ixJEy8ooMUG4kU54lN1_EODwryFKK10XmP3r5MMcAbIMcCksIUnni_eSvHTTNFqzCRBd7NKkFovkwhUKrm77R5rC2Zeg7KiLnOYE20nk2LZwv-JqO0mGRm5hshuwDYyK8SOXhhDvuphNgshD-XlVN72S2QP-4gadTYnCK_aNY9zMLM90zUm2Pt3OJfjH-SOelhWTZn1rukoiUPYPFTrwJht9-uSe0CnhpAOGd7j-v_2yeQT5EVkYzCzFkA_MDcY31cXMWyzmBkgVFOtKWHkZXOWZhjF6Hy245FIuA4iRaxDdA0sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7BXkhq9Cvche5wUe76HsqbBOF9nSLkZjWVqTas5ixJEy8ooMUG4kU54lN1_EODwryFKK10XmP3r5MMcAbIMcCksIUnni_eSvHTTNFqzCRBd7NKkFovkwhUKrm77R5rC2Zeg7KiLnOYE20nk2LZwv-JqO0mGRm5hshuwDYyK8SOXhhDvuphNgshD-XlVN72S2QP-4gadTYnCK_aNY9zMLM90zUm2Pt3OJfjH-SOelhWTZn1rukoiUPYPFTrwJht9-uSe0CnhpAOGd7j-v_2yeQT5EVkYzCzFkA_MDcY31cXMWyzmBkgVFOtKWHkZXOWZhjF6Hy245FIuA4iRaxDdA0sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjEDzuxDijXTNOUvRzoyHmPw8wOtXF7JIZz1YBJNFdXdwAHEAgS9dB5EwqeWdr2PimX18duMGQUePHUN33Ojz7VPGRyIyvcZbeeXHLtScP9-5Clzxf-bMSJrOhv6XodG6uBJoY-JtgmFR33O6WaFESV6aON0s2xuZ8k28lVxoLY-Pul_JtsDOo6KAGwXrw2A8dKeCNsBIZ_w7TH3qnaLZCvkZ74BDEDW9ccrxgpFRciERWTRWvohxRMEFLY-HeA3yiOiciju_a4s4JUtkc3bPQ7D1Z6WagUps9V9cr9AGJvXIihf74LRGgZmU9P_Rg2hG-X-9uS-pD6CTO8KcJ0C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=cTpFijxoAsWQH5ZgOdq2XV2o0ryT7jxG8z8mrgkavLBcXbd2BWq1YCfBPGN8av74Trjynuf4TxhjUYJfW3caV7khfpoN_r24U5I4-PTc8d2DWkzWx7wO0Vq2BFQv2Zz4AMyA9qOJLaSXDMalmu7oT11T5tNQZ8x8ndA0bZpamnyPfPFIEOFmAGojVvakLZIZ9Y-NsAZ96hY9WgVe3-kAW1nYAag3CNlRyyuHTJ-EY6pL-7j65a-aZUu8pUTfuE0NpSHjPZs-pvAAp4w2ybp7pEbo-4wJMEx7G-XMtvj8U33SnP3ZJRrWgYYqBK6or1LkeYwIWRCmIsyQ4tDm_V_a8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=cTpFijxoAsWQH5ZgOdq2XV2o0ryT7jxG8z8mrgkavLBcXbd2BWq1YCfBPGN8av74Trjynuf4TxhjUYJfW3caV7khfpoN_r24U5I4-PTc8d2DWkzWx7wO0Vq2BFQv2Zz4AMyA9qOJLaSXDMalmu7oT11T5tNQZ8x8ndA0bZpamnyPfPFIEOFmAGojVvakLZIZ9Y-NsAZ96hY9WgVe3-kAW1nYAag3CNlRyyuHTJ-EY6pL-7j65a-aZUu8pUTfuE0NpSHjPZs-pvAAp4w2ybp7pEbo-4wJMEx7G-XMtvj8U33SnP3ZJRrWgYYqBK6or1LkeYwIWRCmIsyQ4tDm_V_a8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال ۱۹۵۴ بمب‌افکن B-57B Canberra نیروی هوایی آمریکا از آزمایش هسته‌ای Castle Bravo فیلم‌برداری کرد
این انفجار در آب‌سنگ مرجانی بیکینی در اقیانوس آرام با قدرت ۱۵ مگاتن انجام شد، حدود هزار برابر قوی‌تر از بمب اتمی هیروشیما.
قدرت انفجار موجب آلودگی رادیواکتیو گسترده در منطقه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73024" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVAke2EImxDSSZ6Kc896WHbaJBCXiwTmdD9n-cjyd9Pmq82iGJDy5wryoE5Xr1v3dZOz8t5nyVVowWtW9dNKVKK81MFQef7cAIdMxNorvDwvJorPdXe-vgkmXBW7HbsqJ43cirCYs8P8sz46m664n3Jp_MJjv_acNjAB2tqA_Vr_p8-mEe8Jj9UaJ2JCyhRtiXXgFZBLULBM7TVboz4sYatclTE8XMB8lx9EsHJvo4dT2YOtLKsXnRjWkyV04qB745xPmg-Z-_yOhmATWZ6vlcQJnkNp7SBoeTJKNPap9CZk85PobVa0xw8C3PlN5SPXp9NNXkQqiypKbJdYV3aW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=a-Ok8ea4Iv4mkAVXMhANMIqkuDpa86j1Ch6holdSJR5tOF3i2EoQp1yXO9FYYyVNiFT-33bdF9ybBAuppStA9hHVMP2bYWEcvsxUfuXepRCM7Tcvs2JGIhIVdZRgr6k4uHtgD5BJToBZ_mMykD5Mi8hBBzQ1NoYjaXEq_Z4l0pf3VeeIWmCJbsq63m4PftK-ekAuVfSUG5Tj0OcYq5rQt_da-RBSfOJgVGfSsrlMDttztKPfbk9E_Y3LAeSCUEUYwwhBHCXt8ryn1NOYeDrvVpcLf9Q-3xMhSGd2rC7Am3vidw2r62mty2skGcEmu065k_ksylPd5nUbBF-PXxvuzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=a-Ok8ea4Iv4mkAVXMhANMIqkuDpa86j1Ch6holdSJR5tOF3i2EoQp1yXO9FYYyVNiFT-33bdF9ybBAuppStA9hHVMP2bYWEcvsxUfuXepRCM7Tcvs2JGIhIVdZRgr6k4uHtgD5BJToBZ_mMykD5Mi8hBBzQ1NoYjaXEq_Z4l0pf3VeeIWmCJbsq63m4PftK-ekAuVfSUG5Tj0OcYq5rQt_da-RBSfOJgVGfSsrlMDttztKPfbk9E_Y3LAeSCUEUYwwhBHCXt8ryn1NOYeDrvVpcLf9Q-3xMhSGd2rC7Am3vidw2r62mty2skGcEmu065k_ksylPd5nUbBF-PXxvuzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=Joit3zuEBciySNqMIrSD7Xh86_X3FMh5I6Vmoz9yTurN4mgPoq5cvKmNQI8mDZrdK_wUC75wLh20YqiMSPwKhzysvzGHgngiSTUTVUa4I_LHjtBT0ofc62XUvqvw93ozJjQsutHerqScdIcTmi2Rmtto73brhKtgX_KbyT6748zIhQF_6n0IdkeIVMDbLstEtTinYCjugm-z-vC6PXKr2ZlNnm-C4Y0dWK3Y7cr41Jl1paLothlzHwnl4QEwZSdrkd_U_82lhHjtZ9Q7BGOSWxJWi_o25iSPTiKucCJuhYtnsMx6pxBp6lIBjXkQdujXE0undJasvGeeR6EA3YY6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=Joit3zuEBciySNqMIrSD7Xh86_X3FMh5I6Vmoz9yTurN4mgPoq5cvKmNQI8mDZrdK_wUC75wLh20YqiMSPwKhzysvzGHgngiSTUTVUa4I_LHjtBT0ofc62XUvqvw93ozJjQsutHerqScdIcTmi2Rmtto73brhKtgX_KbyT6748zIhQF_6n0IdkeIVMDbLstEtTinYCjugm-z-vC6PXKr2ZlNnm-C4Y0dWK3Y7cr41Jl1paLothlzHwnl4QEwZSdrkd_U_82lhHjtZ9Q7BGOSWxJWi_o25iSPTiKucCJuhYtnsMx6pxBp6lIBjXkQdujXE0undJasvGeeR6EA3YY6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=rAGqkrB2e66pS9TwCOwBJ-2sQGI9AziJchA0kTZOfVIv4u1WZs4E0cb47z9obHLsQ4ncPdz5eyvBS15EYRN0eLiWu_rPoGOnmK8EkW0PwTjMrlkd65CpSTtaNEYSdPeAXMYqABKPavFc7H0PiZJV-0qsm4orHIRhQweAZrUU7Ldc5HQIiEW5uwuN9t5iwIo-oacjEldwC0IFRMwUc-ozI_-8pRc7zBFUnOaxRVGHy9Xk95sHoUWScNTy5sevn-X6G5GslTjN_6WyQo18IUTwoYbPrRI0mi8ZP2ccw29bjJWzrNjdAWuLuSixviVQYGWeN8Q-xgwpqbDCqzY_iIX2Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=rAGqkrB2e66pS9TwCOwBJ-2sQGI9AziJchA0kTZOfVIv4u1WZs4E0cb47z9obHLsQ4ncPdz5eyvBS15EYRN0eLiWu_rPoGOnmK8EkW0PwTjMrlkd65CpSTtaNEYSdPeAXMYqABKPavFc7H0PiZJV-0qsm4orHIRhQweAZrUU7Ldc5HQIiEW5uwuN9t5iwIo-oacjEldwC0IFRMwUc-ozI_-8pRc7zBFUnOaxRVGHy9Xk95sHoUWScNTy5sevn-X6G5GslTjN_6WyQo18IUTwoYbPrRI0mi8ZP2ccw29bjJWzrNjdAWuLuSixviVQYGWeN8Q-xgwpqbDCqzY_iIX2Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=oXdXAMXGwWla6irUo7l5f2YQjOtdTVNaqkxg4tFopOscA1gsBiHp21Ae8PQZ7U55b9Hq2tGIRCc1cCeFprNLRAIYlEgyntQEkjzFVMESJZhZizXMQRkoGyxwMSmXwawyjQhC_qSyQW0BIxZuCrE_cEyoTdwiKk4pmWmwVFBUAkVfl5fc14Rw8NL455q6FXv2QqgrBoJOGA-CNJP0hGtLBkLvKhFIK0c_m0W6b7yU3QyCS88ETNJcR4oqWs6B96lfGgjXlTJzvH99KuFssh5HhYPRtg68BZID4YifMJTd-OP7gWgHIKrANkCaaJwzi7JzK83WgwrYuFlmLQW4xbtGDUOmNnFahbRf5OqkHYfbI0VJAS7oDUnaEaR1nqKYRbT9pMoOw6UKrUb4y_6AMKv4-Xytjz3xd5FJxeGUr0FMs4dcpKuXSIr4zqv3b2ATjEzucBwHnMOeRiTlB0P5kgaF1rks3vjA5GiUit2_TkEpwMPajHvIBH5VQvwOgVGWYNAb1MtBnGoBH78xoL8mo5quJ2RG4pIJdnn-_yCCC5ilMCjw5prdvwIYlduIXoJov9WiM7BoXMiKimmFaT7uhAHB1i62r8i_hfUxOk4M8j7ecjxaYFg0rw65WTK0r-gmU4FIohwDta_c55tsyzP_6p_Zip5BoDq6afPsx_zKQb8u3L4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=oXdXAMXGwWla6irUo7l5f2YQjOtdTVNaqkxg4tFopOscA1gsBiHp21Ae8PQZ7U55b9Hq2tGIRCc1cCeFprNLRAIYlEgyntQEkjzFVMESJZhZizXMQRkoGyxwMSmXwawyjQhC_qSyQW0BIxZuCrE_cEyoTdwiKk4pmWmwVFBUAkVfl5fc14Rw8NL455q6FXv2QqgrBoJOGA-CNJP0hGtLBkLvKhFIK0c_m0W6b7yU3QyCS88ETNJcR4oqWs6B96lfGgjXlTJzvH99KuFssh5HhYPRtg68BZID4YifMJTd-OP7gWgHIKrANkCaaJwzi7JzK83WgwrYuFlmLQW4xbtGDUOmNnFahbRf5OqkHYfbI0VJAS7oDUnaEaR1nqKYRbT9pMoOw6UKrUb4y_6AMKv4-Xytjz3xd5FJxeGUr0FMs4dcpKuXSIr4zqv3b2ATjEzucBwHnMOeRiTlB0P5kgaF1rks3vjA5GiUit2_TkEpwMPajHvIBH5VQvwOgVGWYNAb1MtBnGoBH78xoL8mo5quJ2RG4pIJdnn-_yCCC5ilMCjw5prdvwIYlduIXoJov9WiM7BoXMiKimmFaT7uhAHB1i62r8i_hfUxOk4M8j7ecjxaYFg0rw65WTK0r-gmU4FIohwDta_c55tsyzP_6p_Zip5BoDq6afPsx_zKQb8u3L4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
.
کاظمی:
در الگوی جدید بازگشایی مدارس، شرایط هر منطقه به‌صورت جداگانه بررسی می‌شود و در مناطقی که خطری دانش‌آموزان و کادر آموزشی را تهدید نمی‌کند، آموزش حضوری در اولویت خواهد بود!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73017" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#فوری
؛نحوه فعالیت مدارس هرمزگان از یکشنبه ۱۹ مهرماه ۱۴۰۵
بر اساس تصمیم جدید:
- شنبه ۱۸ مهر:
همه مقاطع در هرمزگان غیرحضوری.
از یکشنبه ۱۹ مهر به بعد:
قشم، سیریک و جاسک:
- شهرها: ترکیبی از حضوری و غیرحضوری (تعیین‌شده توسط مدیر مدرسه).
- روستاها:
حضوری اقتضایی.
بندرعباس:
- سه روز حضوری و دو روز غیرحضوری در هفته (برنامه توسط مدیر مدرسه اعلام می‌شود).
سایر شهرستان‌ها:
- حضوری.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73016" target="_blank">📅 19:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=cYUY1EfTd6VYFN_iU1ywEdZi9RFH7aOUhbQOCQeuczAZN8d55ELgJb0vi7HR_O42_wY2QbRwNtPeke7mXng9EKonRbGRHB6bzDqGMczYPl13wTn7MiR6tkYVy3o_vp61p3ibei5jDBWhGatHdDErYHL9XDHhueHoA00c4SE0nOUIS74beIe8teoocOSEZfvUaFKaM4oG8CTDNeMN_syapK1mItO3jcEjPR4Wtt11Hu4IRkJWUscTYv0ilTBWZxRvSoqHBBdsk9WcBBPxnwGJ2D0oLJjKbZxC5sNfjmngQ2UtpFWiUmH1EnokJ51MZUsBAUGQ63u0yo5q12nB2ILM9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=cYUY1EfTd6VYFN_iU1ywEdZi9RFH7aOUhbQOCQeuczAZN8d55ELgJb0vi7HR_O42_wY2QbRwNtPeke7mXng9EKonRbGRHB6bzDqGMczYPl13wTn7MiR6tkYVy3o_vp61p3ibei5jDBWhGatHdDErYHL9XDHhueHoA00c4SE0nOUIS74beIe8teoocOSEZfvUaFKaM4oG8CTDNeMN_syapK1mItO3jcEjPR4Wtt11Hu4IRkJWUscTYv0ilTBWZxRvSoqHBBdsk9WcBBPxnwGJ2D0oLJjKbZxC5sNfjmngQ2UtpFWiUmH1EnokJ51MZUsBAUGQ63u0yo5q12nB2ILM9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد دانشگاه امام صادق:
دیگه هیچی برای دفاع و حمله نداریم هرچی داشتیمو زدن؛جمهوری اسلامی هیچی نداره دیگه برای حاکمیت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73015" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxBVK_jyN9mZzDMERCYSRdyFrCISIm_US4BX4D0Z-Tp1mDriz4UR2MVpqa7F--jylZmsNbM6A4LcWC6DsbdSLbF9iPjiGL1oWyQKnwdxHkAGAZ_0HWP5cV7Bd-Vz2pJ9PoJ9EniVSv_70c1rWnpTomeWJKbrQNR-SEuLezDA6FXIXdnLzBvW7qNbOM2mCgGULiEjZ29hV2TMZvg1rz42UCMXWzKC3S83-ov_sGhmtI8_VhDiwMYlq6BpJIA3P7KdYdLQpmAAQu6Lh4_VoeeK_SBKqmrl175eSO5ulDHKEhVT8dRG8uQ0E9JXAG-Hz02G4aou0WbdEMlpmw77CdWuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y39uyOwuKZ6erS6zqrLeTijPaUYf6OpJdDP8FxVSacbOcgFf8RbrnOjFB4pzVeJACSKHCdzHDWYpsQMg5gjX8-Ufi_Gwatn51EY7WYcJYGePIYP4mo1f96Jy2NpBuiEHO3em47VijDBYnHV2ly3Xe7vO_h7ZOT0_fP0DuaeuwCmdGqMHz7hb_l_vwpTtnkwXFn13_1tJQz3ioUlylqUahuks8qyRxCdo34pTCbD2UpNCeklLIqn_Os9M_OOUQrSEKPWLWtyAI9_HeDy-293mwrku4iryIEnKcdlK3ZRJSpry8gXa30Cgs6TzkAFX66oChSxmUhpTnsfEjI-TEWNoIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=JevQX_UcRdSiv3p0hA3-JU-QouOpXd9p985V4Ja9Hc-zOCWnQyCenrl6tvPU7eMbDpoCBkGx3CO6TkCcHFCGNJF8vQxsBT8ss9CsBY1upYzisl8iECRC0BWmUVbj2tt1jk0rAa7ONkuSOrtWq6_AJ4E0aU9yNM8isjQN4hAgdBlHuBqHVrvtF4VywfIi1aYipIjrrB4DGILIBY6ivoqHSvoE_NHQCKm8LmeIvODUQyG5dNn0VHnaxjyn78YZc9JZ0o0-rVKT-Jk3pnewzXQj3WinPvLUDF4L9-uch50wOPayGGSgaHNDp2j4bvpTbfs_EnSN3BHNKKE_SBvJiCwg1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=JevQX_UcRdSiv3p0hA3-JU-QouOpXd9p985V4Ja9Hc-zOCWnQyCenrl6tvPU7eMbDpoCBkGx3CO6TkCcHFCGNJF8vQxsBT8ss9CsBY1upYzisl8iECRC0BWmUVbj2tt1jk0rAa7ONkuSOrtWq6_AJ4E0aU9yNM8isjQN4hAgdBlHuBqHVrvtF4VywfIi1aYipIjrrB4DGILIBY6ivoqHSvoE_NHQCKm8LmeIvODUQyG5dNn0VHnaxjyn78YZc9JZ0o0-rVKT-Jk3pnewzXQj3WinPvLUDF4L9-uch50wOPayGGSgaHNDp2j4bvpTbfs_EnSN3BHNKKE_SBvJiCwg1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DggzuMmU4rxI6fgR9Jpn1S8aP9cYwqjEHCfZ_lbr_IylAfOoIYwrnp_AZ0P9G3kNjHjpyvXMg8P6uIkpBGI1croXHyAxWvzkkfoBusIULg_1ALA_SCUfKbkjDEgsuBjwe4aLPf1qxoSmAGcvCNmlOM2PbTwVDpqS5Bnlg8g3hpTzCTzdWtBA0GD9V8uPUzubR2PHcvBak4bSQ44NWxyTXUDumf1s57w7A-_8wW3PglmxiMgIWe5bp957VQBjZ08lGWGm3OYhSTT4RsVbLjjtTOaAtI8Q4KGwY-VxPTYqSH6ocYWR3EwDYWjjmI4y1WEC-GIwSs8OQrnaX4zWwUL1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUtoE_qNZ60rSy4vIwfIzHNgKQ5oNsFIvgGraN9wHIYZ9NlUdtif5eSFtIth2OGHZbQBTKB_yOQmm-xVVPT_5rLPrpSrpeYjM6CQMsnQwAI1gxwqwDy-Kr3Ij1kQqHKta0ZmWf1YFFDVX4ZYC2Ixo5eLQpW4EPzIR6Clu-BMn8PoEj8DIq5EmbJCUgBwkOExP-_7hSF6FnAi7oTyWXPtrw-UWWOZ0_tmFTP2-ziWrMSzH63pTTVf0TZHRq-0h7QhXWHQqAXgKfqSfuEOhWZoh4viGwCgrtpM-3lqugNZNGeCFiYKrez_InK9kqrdKUwRRD9mMDi6eX-6MNezS2PnOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=dG1g-bPE-XjuzE0t8FCRjtfKoXRnBfRa6VA4E2IqKz9wDQNrqsyDhIf2qIjcUjQmi3T6bB_uVflHJ8VLHjljvydhfIIGgw0K06zx9JEG7OOa8vhw1NYb2w3i_FxAn30dd17gvbD7jU9_2UxjgKg8ThtRLFOQgm3i1O4dUNJxI5f1LpbiHZG8sDRODE6nXmiQ4UVXmW4Hl28-Zs7BZqq8aUWLquc70C7r7d8avjoo5jeBdTuOmeEAYZVO9Z6Z5hi16jt1_qqP3orASf6uJVENk5F66YONkfc5D-ES41HNw8RnqJiEXWCNfg8LEK8TL25r0OHxRFvk5tT-vOhrlBsg7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=dG1g-bPE-XjuzE0t8FCRjtfKoXRnBfRa6VA4E2IqKz9wDQNrqsyDhIf2qIjcUjQmi3T6bB_uVflHJ8VLHjljvydhfIIGgw0K06zx9JEG7OOa8vhw1NYb2w3i_FxAn30dd17gvbD7jU9_2UxjgKg8ThtRLFOQgm3i1O4dUNJxI5f1LpbiHZG8sDRODE6nXmiQ4UVXmW4Hl28-Zs7BZqq8aUWLquc70C7r7d8avjoo5jeBdTuOmeEAYZVO9Z6Z5hi16jt1_qqP3orASf6uJVENk5F66YONkfc5D-ES41HNw8RnqJiEXWCNfg8LEK8TL25r0OHxRFvk5tT-vOhrlBsg7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8P2SjWH4pOOlk0H_rlWsVb2QcvEVO6QlLw-U8RkBdHYxzm1RPW5Jw9cJ987RZEelAmJV2t2x07_UGf3Y4Sk5j6-h2FOcDtc925mGl3JogbFu2Xa-9dvw6pisrRmJXMf-cH5TvZb2yjfOex7X4tc7_PS47hJfs3tfTsldZd6TouGiIQZlbbZawmTC0AOfwUc2Ptl7ZKEbwk4LW_OOoVnj5d51iiWQAo2GxMmIrCmZqJE1yCnh8zFylNL3gqpaxO1Id769_PQPwDuLa9CgD9Goy7CrCgXWceg59P_5Ho4UEoIYlPeDKe_TZhEb8oEsX43TQUjfskNriq98VzLpdUi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiCI-EMo231eWBHCc5KmrmYopSv72R5BAl2_YR9NY6w08ZzDBOtu9aa_y4FYnAxLP9mPradOJOgEIbc2An9gG1TIEn0dv4iOZDCgDyXraQkNXfszSn2rVB2CSDqNYUutmpMWKgXdhUVMB30oCxMJIPjc5USHKZBZNezZ0iydgTtuTlYOWMpT9H7qxpui1DKyB3ngBSpZoQKVnL8OTX8qD34r7AT8QTpMJwayegTKuiDc35cFH2oJgP-5079hK_34Jj1oqwMdDc8RcR-E3MxkyZJepjQStXPjIQUWRVKcs0cPFckFGCv_8SC1ULF1Uet9zyUAbUVx_w4TnNt0Hp9Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=n_TA8EEMGFkgXlWi0Bep7FRorYCE9VUhn4mYAEuDQ8ryuA59tFWcZEbUV39-MNczlxgX60109HPHtB5S0dMZyDU_duElVIM4P6vAKym_3lcz-pSzPRbhkGBNfsSLCjkDCL9zMO798DEm5BkDb9z195ofoZnCgI3nd7ylTIKnbA_jjCCru4OvWUXDB0uGaVO5LlR1x27tCxcQlKnvTJEV66KKQTqdZKtcfM-2fZidl8x5KEjklnalOFb0uTOc1CN5h6ZJRSpeEyofU2jCG-Yu_cZjfbekXbZrB6chJWWb4hbqje1hTSZ_yJvGnJSAs_maUdLECPaSL80YcLd-n1Ge9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=n_TA8EEMGFkgXlWi0Bep7FRorYCE9VUhn4mYAEuDQ8ryuA59tFWcZEbUV39-MNczlxgX60109HPHtB5S0dMZyDU_duElVIM4P6vAKym_3lcz-pSzPRbhkGBNfsSLCjkDCL9zMO798DEm5BkDb9z195ofoZnCgI3nd7ylTIKnbA_jjCCru4OvWUXDB0uGaVO5LlR1x27tCxcQlKnvTJEV66KKQTqdZKtcfM-2fZidl8x5KEjklnalOFb0uTOc1CN5h6ZJRSpeEyofU2jCG-Yu_cZjfbekXbZrB6chJWWb4hbqje1hTSZ_yJvGnJSAs_maUdLECPaSL80YcLd-n1Ge9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=m0e9hZVhICLQkbuxsCn-ygoLJ1frtfja9O_8y6EBfOYvXvyvNsu3X2a-yqmK1moNLWjwaTuK1w2LO1NK67b_bWmHcfmzEIt5CAF04FaEWhmNpgEuRs50VxpIaBSiZBeAacIoaamV2t5h4FmP7NBnQANUiBY7T7YEB4-PhoKzpF4epvZRiGIGPcWt3lBK6rqJuim1Ddol8dU6aCrDbo14AR4-YOOK52yA7BFE9pCG2zPAhpXPTvmkPHBtqygY8Mg684pV-k6R5qWGGPbcw1cb9dFiiZi7mMR3R1JyOX-kmi_zyCCNJNFpR_ZvIOMFZjiBBmpP6WUgBbTdOzBLvuo4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=m0e9hZVhICLQkbuxsCn-ygoLJ1frtfja9O_8y6EBfOYvXvyvNsu3X2a-yqmK1moNLWjwaTuK1w2LO1NK67b_bWmHcfmzEIt5CAF04FaEWhmNpgEuRs50VxpIaBSiZBeAacIoaamV2t5h4FmP7NBnQANUiBY7T7YEB4-PhoKzpF4epvZRiGIGPcWt3lBK6rqJuim1Ddol8dU6aCrDbo14AR4-YOOK52yA7BFE9pCG2zPAhpXPTvmkPHBtqygY8Mg684pV-k6R5qWGGPbcw1cb9dFiiZi7mMR3R1JyOX-kmi_zyCCNJNFpR_ZvIOMFZjiBBmpP6WUgBbTdOzBLvuo4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-8M_YooesOXEx54fGV6PeC73kg-sfXi6Pyk010jno37Bw05_xOWjLK0ADdymQigZmpf5kFgy5XcFA-D1-JucrPRonxHZcQgXZwZYHaYtsXGipW1vhiN1RHg9Yn1ggPHudxDRNfbmcI5_5ks-0tm4W7CtfPyNwCxHtAeTr944ZHjOmoYmfg-qmlUSR-asL7R3s745U8_CNY_rxFNDDz9NY7Q1-brLtlGnjlsLsaySOOOotNMOlKpQ9-vmGxJvcl9u56fsXLJcnTvVyLm3BB_1YwFTYu0_ys3OcUUyacSvbkXi4Smws293rBfglSXJJ5gaUcwo99uPDumyXs8ikxHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=sTqDaeVYYb5lU8jLYj9A_DOGQvPgt8pSBTyUuHoKHGsWXal8V8XLUMj79_mw566b17dRDvgmQrn5H_2pwmoaZhyvRGF-XRY2jXIKYA94JxD9k5S1Mlmj0uhSEwpYzDGBskFfj42Nh47Gg3i0C7gG3fF6rHpYAAY8ahTeRVZMAF5kpxKCqZVO5POHyM5mu8EhRXgc2XGE8ZDy3gJFOhZawiefpIGt1WkA06YWUUZ0aG4Xd8_DohTVrdqbg7A9EkATAndKmx282U4kQT1pYjkcUwuZA6c17_vKaFHe4qAJznH7P-h-Gd8QJvLEs-dQyZYZ471ia6zhyZfUBKrtTlti4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=sTqDaeVYYb5lU8jLYj9A_DOGQvPgt8pSBTyUuHoKHGsWXal8V8XLUMj79_mw566b17dRDvgmQrn5H_2pwmoaZhyvRGF-XRY2jXIKYA94JxD9k5S1Mlmj0uhSEwpYzDGBskFfj42Nh47Gg3i0C7gG3fF6rHpYAAY8ahTeRVZMAF5kpxKCqZVO5POHyM5mu8EhRXgc2XGE8ZDy3gJFOhZawiefpIGt1WkA06YWUUZ0aG4Xd8_DohTVrdqbg7A9EkATAndKmx282U4kQT1pYjkcUwuZA6c17_vKaFHe4qAJznH7P-h-Gd8QJvLEs-dQyZYZ471ia6zhyZfUBKrtTlti4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=ZB_ytLl3TnnKHOom_94imr2bfpF1qCWuqbEbB6-l3gwcqxzLcv3OhW89pVL_TzduvcQ2oiFjAuUddodUe1KZnWzdeVvcmU-5vG_gRjwr_8eB1qhrhHjKGzVeQgFEU_JCH4IFSov-JMVnV0YS99mRL_sjcytvoBFUXsQF-V0-8XyaRiRFEPQvkNRdXxOdZOfFDaQgWwI1bC_F8Fr1CQjh7yO-RQp1AbZ89kJR9WoN0scgbQpgMb1dQ3skb50bZ7orWzWG-vD-Ku7Ioa49_WEDdx8S9-51xsLETzTNyVVXn5ECS_7NYybjbF0Akmsxq22pQCr6ttlzoyFOonzSdTudLgxvypoW3wkPHRjGTV2XbSpOBYyOWDr0bcxmrI0Nes7Z9eYwmRWU-THgG_kRtTJTmP7JwulbUP6o9lxqZpLWfaFviTQGAKsIRn91_wJ7TEvRDN_mm_z3qzJgCC39v6WbJIdAfdrFMkfQ67e3BaWiIoR3kGiny3AWs5UYiZ91XYD0fL6lX-E-PN7KgeaV0qhdWSDU5H3SLu4HmwUGuRijrqI8z2tTSFA-3QsG5Wd3m-o2F0dlHSvFF_ui9I5bi--QRGkFOvfFDqQLmf1NHLtYkkMMwir5zcxsBpHzi4mCrNKYHYV5Xk_Mr2R2_AnMbN-EtjEuocfFKVmiq-JXmKWsy4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=ZB_ytLl3TnnKHOom_94imr2bfpF1qCWuqbEbB6-l3gwcqxzLcv3OhW89pVL_TzduvcQ2oiFjAuUddodUe1KZnWzdeVvcmU-5vG_gRjwr_8eB1qhrhHjKGzVeQgFEU_JCH4IFSov-JMVnV0YS99mRL_sjcytvoBFUXsQF-V0-8XyaRiRFEPQvkNRdXxOdZOfFDaQgWwI1bC_F8Fr1CQjh7yO-RQp1AbZ89kJR9WoN0scgbQpgMb1dQ3skb50bZ7orWzWG-vD-Ku7Ioa49_WEDdx8S9-51xsLETzTNyVVXn5ECS_7NYybjbF0Akmsxq22pQCr6ttlzoyFOonzSdTudLgxvypoW3wkPHRjGTV2XbSpOBYyOWDr0bcxmrI0Nes7Z9eYwmRWU-THgG_kRtTJTmP7JwulbUP6o9lxqZpLWfaFviTQGAKsIRn91_wJ7TEvRDN_mm_z3qzJgCC39v6WbJIdAfdrFMkfQ67e3BaWiIoR3kGiny3AWs5UYiZ91XYD0fL6lX-E-PN7KgeaV0qhdWSDU5H3SLu4HmwUGuRijrqI8z2tTSFA-3QsG5Wd3m-o2F0dlHSvFF_ui9I5bi--QRGkFOvfFDqQLmf1NHLtYkkMMwir5zcxsBpHzi4mCrNKYHYV5Xk_Mr2R2_AnMbN-EtjEuocfFKVmiq-JXmKWsy4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=Q8cqWFMEN-f4BH4MZDQx2UXVRHeOAOu7pj9G_ohx8P7MLEt3VlHv9fRBYK50RX8sfd3E2PcP1ldx1kMlFOO9qeQMLANzCk47pNDn4YnxzZbr85rnYl62k1I_Gffu-kvXXHs32f5iKH3KuxU0R4U3_FZzX1oGT985DT7Y642wKbWJPSIi0cYorQtyUyePbfcByypuQ4AelMaoRjVtBXlgyOQ8jDF9hupz0kjGyRnrH7u-uovlwaq935mDChqLGrS89RtBHt907ZBMcN5fqcFfpRvyA7zsLURfke8jFtzrfcblra0d-0LK9mMV5zVeK0hJ2tF7RkQuer5KPCRB8YCQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=Q8cqWFMEN-f4BH4MZDQx2UXVRHeOAOu7pj9G_ohx8P7MLEt3VlHv9fRBYK50RX8sfd3E2PcP1ldx1kMlFOO9qeQMLANzCk47pNDn4YnxzZbr85rnYl62k1I_Gffu-kvXXHs32f5iKH3KuxU0R4U3_FZzX1oGT985DT7Y642wKbWJPSIi0cYorQtyUyePbfcByypuQ4AelMaoRjVtBXlgyOQ8jDF9hupz0kjGyRnrH7u-uovlwaq935mDChqLGrS89RtBHt907ZBMcN5fqcFfpRvyA7zsLURfke8jFtzrfcblra0d-0LK9mMV5zVeK0hJ2tF7RkQuer5KPCRB8YCQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=Dh3m7XrQ67KkUjOVtsDqTyUi3DlHr8cOACY4QJoMkrpXA_rVNM4Fvof7pezz6z1KqKq4zwIJHkHo9KdSZwuVZ-X8aV2WshNKBYBwszpX_C-lNrDA5ppnwHRGKSS_HHXnrtGH9Qnbys8e5WB81vO88O8VcTAaPixhfUYi5O-Wm-3wzjDUytdp7v-PrTYGBN3VEvohoTQPO9Ec4JVULhSEKnRuPl-DOobp9kVIaB3JzTNnYxhda8dt8Lu2R2Gmy5TrZmOsgfZ9qUCa3WBLca4lsg_1Wx7pcgZVCEj7LfQFX2xwRhsO8ZUpDgGL7nZBZjLDyg-exY9sZuz8Jn6Q1Y4Qzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=Dh3m7XrQ67KkUjOVtsDqTyUi3DlHr8cOACY4QJoMkrpXA_rVNM4Fvof7pezz6z1KqKq4zwIJHkHo9KdSZwuVZ-X8aV2WshNKBYBwszpX_C-lNrDA5ppnwHRGKSS_HHXnrtGH9Qnbys8e5WB81vO88O8VcTAaPixhfUYi5O-Wm-3wzjDUytdp7v-PrTYGBN3VEvohoTQPO9Ec4JVULhSEKnRuPl-DOobp9kVIaB3JzTNnYxhda8dt8Lu2R2Gmy5TrZmOsgfZ9qUCa3WBLca4lsg_1Wx7pcgZVCEj7LfQFX2xwRhsO8ZUpDgGL7nZBZjLDyg-exY9sZuz8Jn6Q1Y4Qzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUAtH2Fjzi8WdkKR6uIT0AExBCyzZBthyUoFIwEKuZSLvMfCWKG1k2ZbK1bpIHKewAmdkYsZAMBP1Qg7UIsUjIIWL8RcsJCyVenh_hG1tT5OzzkHpQoiniqKw8YiveY6S7yXRFV3iwahhKaRPbMevSv5yVTvFBXUT6LCwGhdFlxqPFsm1_sj4z9E0MGhYfIaydEJbMJYEDHhdjKO67HeNzg6Tm1-g62HopunO8JG0TtEQzQCqa2eGIyoJFV6JNMjKTk9wQu4OJvpkkdbkJusCYa7j6b7EYX2S1Wl3ypJQVGIKlxSrop8t08SveNF-ya0sZEgmkVrOkEdzoYH2bFtxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WHaOrbTu2GMwwgF5MqmWEmh2tPNoT4Dnh_0S0LoZynVxE2xrvWSZbibmzjOiEALfoBSIk0hULTe2J2WB_nlshu8DMEi7Q_RXN0ds4n4WEpzJyXWFrXxeoMEBvdPqEWBbwixd2G2ALdbMBElrUz4D-5ECWaSCvOJX_ac78ebmvSIX_BejZ4bPgGZaLaJBAc_4VlO-TWZaYup4Ge1NrL8n1y34AelDusPXSBqEfCSDgYgw_YbJqFDVIePyTtgXzB0YhewRjyPabWerL24fAUDcdW7TmGwD6ZLx9wsmJgQmbt7ld4Vay-iJQtPcmo-W7KTanV_RXHkaKlFIXDuuvJV1Pzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WHaOrbTu2GMwwgF5MqmWEmh2tPNoT4Dnh_0S0LoZynVxE2xrvWSZbibmzjOiEALfoBSIk0hULTe2J2WB_nlshu8DMEi7Q_RXN0ds4n4WEpzJyXWFrXxeoMEBvdPqEWBbwixd2G2ALdbMBElrUz4D-5ECWaSCvOJX_ac78ebmvSIX_BejZ4bPgGZaLaJBAc_4VlO-TWZaYup4Ge1NrL8n1y34AelDusPXSBqEfCSDgYgw_YbJqFDVIePyTtgXzB0YhewRjyPabWerL24fAUDcdW7TmGwD6ZLx9wsmJgQmbt7ld4Vay-iJQtPcmo-W7KTanV_RXHkaKlFIXDuuvJV1Pzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72994">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhIocQsNuNx136Hs9i24pKqK4Qj5tPAxY_rl0-wkkOxea8LHIt6fQ5ngAaCkkxRXhZI4HNX7gVXRiyaq53tOYUPracxtvcfzP5bzcU-KstZQzXkByf6Cx32tI7Icn7w-u3LbJtlrhUG7QHLj2a50q04ytLNuaKOeIhQMDUxRv6pU_LoKNWgT3LY5sVumHSpkDJxWsFEH0KhNabvaoGEEKn0dpld6iGUulXZ03XFaSG0PoNeuWp3zwuKo4bCpgZfNT0lRy2aox_YLYlolmlp-4Dn-r9V_ZQzGZtOe3tz_UIR9gqDTGd5Ku78xsrvtRbF1tsB1YZxkEnrSbQzZpXmCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U43prmq6JzSG2U5OtclGry3ZnnVFlhCShM-lYHxHdnba1UalLZU_T-m5W8vG3KPR6saRnxYX958G0e7purfGGBVtPsm03oy5UMPjxchGAav2QT1480EJITk2IuLH5PwGT-Wn4fXYL5yfF5CRHby7dqON0Ah7ds81vQ0L2VkEcbOKywbagrwPhhusXVz2uj-5yQ6ZpahRRnYLhwnjzRgMxbz9S6PQVjCxCqO9af5T0L7Bw2ToZebByKU9oUKP5ldyhl4chlztMm2BjDWdWEe98Klo2LlcO5AWxhg9cco3yWydP7Yl0rdQ9L8sbxAj1jQBX-Yp5PxaQxWGoGDCnYLz0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن پس از ۳۲۱ روز به خانه برگشت؛ در حالی که بدنه جزیره فرماندهی اون با نشانه‌های ثبت‌شده از اهداف منهدم‌شده در جنگ با ایران پوشیده شده.
تحلیلگران دست‌کم ۱۰۳ نماد پهپاد و ۳۴ نماد کشتی رو روی سازه بالای عرشه ناو شمردن.
گروه رزمی این ناو در جریان عملیات «خشم حماسی» (Operation Epic Fury) و محاصره بنادر ایران، ۳۶۹۳ سورتی پرواز رزمی انجام داده و ۴۵۰ موشک تاماهاوک شلیک کرده.
این گروه همچنین رکورد ۲۶۴ روز متوالی در دریا، بدون پهلو گرفتن در هیچ بندری رو ثبت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72994" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=f_u88g0shBNwaD5NeNeBue0HB3m0w9a56ALpuh7B9w1-SalP6O0SJmwGVOiw-Mo9u_3BhzzIas26x-dQvokQeYsN57ZD9JUgmVBCxUWDkDm9dq1eOxlwJnJ4rQh5rmzcSufqMPRSHfDymjXlR20a2iuxO5DuAQP6pOu3Pjg_5X7YS9XhliA9TkdjYpo-pDzIlJe43RMP6wGlpceKWzXzSu3dcEfUFfXD3tpf224q0VGiDnurmnEp8y-z70pRWdaLwVrcIzSkTSLJeLq_RzczhFbSBnW1zzuAMgAzobUrLUCd3xLbMYzGfyCU-FgQWM0Yo6D_y2YTNgqxZTPxMIGPUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=f_u88g0shBNwaD5NeNeBue0HB3m0w9a56ALpuh7B9w1-SalP6O0SJmwGVOiw-Mo9u_3BhzzIas26x-dQvokQeYsN57ZD9JUgmVBCxUWDkDm9dq1eOxlwJnJ4rQh5rmzcSufqMPRSHfDymjXlR20a2iuxO5DuAQP6pOu3Pjg_5X7YS9XhliA9TkdjYpo-pDzIlJe43RMP6wGlpceKWzXzSu3dcEfUFfXD3tpf224q0VGiDnurmnEp8y-z70pRWdaLwVrcIzSkTSLJeLq_RzczhFbSBnW1zzuAMgAzobUrLUCd3xLbMYzGfyCU-FgQWM0Yo6D_y2YTNgqxZTPxMIGPUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اسلامی، رئیس سازمان انرژی اتمی ایران:
ایران هرگز از حق غنی‌سازی اورانیوم خود صرف‌نظر نخواهد کرد و ذخایر اورانیوم خود را نیز تحویل نخواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72993" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72992">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=e8-i6obIwkMLLn7i3GNSU37uQ9ks7_psfs32KB3PWzDAbsMXjO0wPleMdZw6WquyZ3o-L-zy_HZaytt8YxRHpSwLRJe_NABKUJR8K0ZdOzTQoMSlfCvRRP7oP-FsVZLHDAqvnMyaOjEACbdWSB1gbkJIsfbjP6OroUK4BiG4wi_ABleCINL1Nq_6J-EKyfk7ZUsIGU6JewmCCSZBUIEDuRzIhG8rCFuL7mpb4w-nQ4G2dqgJub4XkR0QXApwbvjE1PCPbD-SZ8QqbFUarjCJ6u114W5VVfuQUeQljB95_JiN92g9Wjg0Gl6EYriS26NYXJHdKGEZ5C16rGrOD96IIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=e8-i6obIwkMLLn7i3GNSU37uQ9ks7_psfs32KB3PWzDAbsMXjO0wPleMdZw6WquyZ3o-L-zy_HZaytt8YxRHpSwLRJe_NABKUJR8K0ZdOzTQoMSlfCvRRP7oP-FsVZLHDAqvnMyaOjEACbdWSB1gbkJIsfbjP6OroUK4BiG4wi_ABleCINL1Nq_6J-EKyfk7ZUsIGU6JewmCCSZBUIEDuRzIhG8rCFuL7mpb4w-nQ4G2dqgJub4XkR0QXApwbvjE1PCPbD-SZ8QqbFUarjCJ6u114W5VVfuQUeQljB95_JiN92g9Wjg0Gl6EYriS26NYXJHdKGEZ5C16rGrOD96IIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران در حال آزمایش مین‌های جهنده با انفجار هوایی است؛ مین‌هایی که برای پرتاب شدن به هوا و انفجار در ارتفاع طراحی شدن.
هدف از توسعه این فناوری، جلوگیری از عملیات هلیکوپترها و سایر هواگردهای کم‌ارتفاع برای پیاده کردن نیروهاست.
@News_Hut
| C14 News</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72992" target="_blank">📅 12:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=QD5p7pnMTHUcBvxG4J9QrmCknz9R2eg2B6F3k8OBaCuw_BCRulDVLjrWblgfrIFbvDo9hDztHOPhlDdaX-GXI8ZXwr08Fj0Udf10IUDOQep473ZVclQSaiO5LNOt9d9ttTiK53YLKqdALS571ixiVOLDKfoej8UgEC5Xyjt4ibiHACQ2T0D57bQUI9XFonez-1DlxPdbM6WKAuTEXFwbU8sUSo96sA5rMZYIMhYnffwgqiVP7bTyjl53GLmwZJoRXvNLsDDRKw-gpQ-O3Oktjk2Ncuvd9WQK-EvMz0kfaVIGh2niSZ3ee6r56vWgz7G0hUFbMUTCtHZ636rMnRTcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=QD5p7pnMTHUcBvxG4J9QrmCknz9R2eg2B6F3k8OBaCuw_BCRulDVLjrWblgfrIFbvDo9hDztHOPhlDdaX-GXI8ZXwr08Fj0Udf10IUDOQep473ZVclQSaiO5LNOt9d9ttTiK53YLKqdALS571ixiVOLDKfoej8UgEC5Xyjt4ibiHACQ2T0D57bQUI9XFonez-1DlxPdbM6WKAuTEXFwbU8sUSo96sA5rMZYIMhYnffwgqiVP7bTyjl53GLmwZJoRXvNLsDDRKw-gpQ-O3Oktjk2Ncuvd9WQK-EvMz0kfaVIGh2niSZ3ee6r56vWgz7G0hUFbMUTCtHZ636rMnRTcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4atQ4yvzKTlmcB6wDv5tiH3jHLfVBSfgH2Ndg7c-KUkfkEgjPJlBmk4iJe7RZ6AOXdqaDtQ0UFYxE7XaldKBU-5rzFjnbrbMZQq6RVQ4_z1maA39_wxfPV8lGhJXs7XCE-dA2Emzkboduhl26FPEqpc9LM3GLEozoGBStmO7zxBffRtMElILIxl4UaUUOuSy3q33nH9-PTWtD0xpWWrIdM6yzLR9wwdP6LuVFnWmpCWGAHS8vgFTe9LM7w-sOKwHR8Vi0TZqZAPWqUMuc4gom17GZs92hx5dNMlimnYIv86pX4p0DvCVScnGn298Q4j4gW5YZ2HNytie30mbudqRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbaok1lGV05eIdiSs-LygiGkYxzOvT5u7rW6OjoKT844tDHs8DEhD2C71JI8dhV9tDJLTcwkXKsZ2xb__I5_y50zVH8SeqtiMRCf9CXRXPsKswDGCSeKUwEMyHxsF_rvfwgPhSE0N-zsl_zazYS6KjpmmUSxlSLF9DqfG8xejGF9O9X-P3MQt0Syu4K45JSWIOWXttum4Wmr6d4CFZdOTmd-pKHbfrO4xJXBhYIOe8b613opkhRqnk9i45p1kEGczTda_RcdF3TLOTumoyY1BogOJyefjfzckN5ljpLeZKX-T1kdYycWmaqsv7ZuInExOCqqk7n_ejaafDJmZ8I8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aR6urAFPF9lDUusu-oLYq9Ya3nkObkT5NCT3OFGqUVA6sHDs5haBVOdOMON6lxIZ23Ne1QhisDGAEp9KWf2pKiGD4MEBU_ldrwX1HiajlA9UlOsHojuT5F81ShqXfA7vYXPZtkoYYqOmXEFFnKfkuv5b1Vfb_gmIVvnx-_sNSVdeZO-Jcfp7pL5tp4gXDstJcZoENjoxug5JbnC9zzkgI08f7yhEkPQRf4RJUi5TBXZd3hs0HlX-6LcOp4vaRDeuadok1iAZVPB-lEMKEqLdbo-n7Zy8NfByXZZoS4LqVlI9IITXNLTcgp_N63yWDiSevVmnXQTikH5Ax30ntDpJeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=MJ9OrbX7HlHgYhsltBjAFUK--Cz1kb3pvWYIJPyQWcIicJPkayHeQkadUH--dYlKL8BLAVKCeP5z5Wc6Aa4MNQVWZ4c9juH6ziGcVZ4Kwmj8HS-6p942wBC3H-tvly9ua8Ss_y1wABWbox6q4mW-fWFGgDBWr4Qrpp_nQQyUZC1Pr58wtqQ9Z2JjoXfS8kdbSbyNzD5hq4_L6eDASUv3iHpLX_SjWpUzw3EVm9sNsXgD9gCqLgJ4KcrPBDuQLf5eDsdo0Ng7t-iUk2ubbz5PrFOtp_d4JljS2K8av9VmvageOc2xNi3xu52gTvIUJMgd8nHY_ahXrHklnuOXcN7X9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=MJ9OrbX7HlHgYhsltBjAFUK--Cz1kb3pvWYIJPyQWcIicJPkayHeQkadUH--dYlKL8BLAVKCeP5z5Wc6Aa4MNQVWZ4c9juH6ziGcVZ4Kwmj8HS-6p942wBC3H-tvly9ua8Ss_y1wABWbox6q4mW-fWFGgDBWr4Qrpp_nQQyUZC1Pr58wtqQ9Z2JjoXfS8kdbSbyNzD5hq4_L6eDASUv3iHpLX_SjWpUzw3EVm9sNsXgD9gCqLgJ4KcrPBDuQLf5eDsdo0Ng7t-iUk2ubbz5PrFOtp_d4JljS2K8av9VmvageOc2xNi3xu52gTvIUJMgd8nHY_ahXrHklnuOXcN7X9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1cjIWjTY41Y-jGuCXKJlfvqfoAyaxrnq7jOFe8oMse4D_IKt1WwV4W6rFuko00vkxfo_9-uAWO1krpCJdx5TI5VLoRkwVyd_N78kSrho-t3PtJIJnJ-cxwvTT997yS0KZFHGOVU_6LurzZW3MMtju9T9eQWAU_15Plk0Gw76wY1h_NFtBKinJKI0t-E4p3AamwIMpHZWtR959Xqnb1RLbXpDgp2cl_6E_NXK7ccJmvqZXydTndkS3PU3PXFdjxFdAM1sOeSk9RbbXbMUqs3KZghBhSOYE4cpvK1dtthiUjlHv4Wf3DsnCiSiyOiupAQC04q6AYPGvLRhuIlrA_vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=kB_B7eTLJX0rJiEtZBlW4XcNooQyrlaVu4V4Qa0D5GgtZ2RSUWEl2C8lF97RRZwgnYK_7mk_pA4gRqLwkOwsaVJtkfG1BbhZkCtqTqtQvTZgQqJTpHzHBSHZCRHJFr8GlKReZGAZ7_AVLGuazz-jf3LkSibG7ezd7RFb-riLw2QT8zQg07VokrwAXSCf_75lr7_A1arv_eBRXLRB3nPkTp5qn0cL8oErNv85aE0ZCXFMFjUK4rPEfdzxzW5We6dR1Hd6L1oyYWjnTI_rrkDEYMBru4O3pfWVjb6vXWm02dZBwvMD9mnmBvZfrMDjJB_7JoQhj-DZfAu9L3yBBKvAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=kB_B7eTLJX0rJiEtZBlW4XcNooQyrlaVu4V4Qa0D5GgtZ2RSUWEl2C8lF97RRZwgnYK_7mk_pA4gRqLwkOwsaVJtkfG1BbhZkCtqTqtQvTZgQqJTpHzHBSHZCRHJFr8GlKReZGAZ7_AVLGuazz-jf3LkSibG7ezd7RFb-riLw2QT8zQg07VokrwAXSCf_75lr7_A1arv_eBRXLRB3nPkTp5qn0cL8oErNv85aE0ZCXFMFjUK4rPEfdzxzW5We6dR1Hd6L1oyYWjnTI_rrkDEYMBru4O3pfWVjb6vXWm02dZBwvMD9mnmBvZfrMDjJB_7JoQhj-DZfAu9L3yBBKvAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=fyTYBd_6sVXsaKpYj7J8i69MJoymNoMZIYuYj2BHkDpQf49o3iHjCQR8TqkFYvBAM2_jf7VTDPvnj7blp5dJkUT-zS4rfxQGggZRLE7skaKtWGaT9eotzz22ocrn2ZqH--HVcngu2GFwnJZHF6fWIvhKXWAk6b0_mzvmj5fjP6OLiA3WOFtpuLnoonyA4-O8Ase98m8heXhsOT1lA0eGj-YYNKgLrGKrQfrLFfcsL6YaFXS4dC94V4U3iQvwhdYtzo_A4TqYyyCPzWR71dxFD2xDTmjjLwvg1eBO3898aCGuAcVVx1dkonn6ns6lhlf3SEJ9VgbYnySQe-MHBlb_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=fyTYBd_6sVXsaKpYj7J8i69MJoymNoMZIYuYj2BHkDpQf49o3iHjCQR8TqkFYvBAM2_jf7VTDPvnj7blp5dJkUT-zS4rfxQGggZRLE7skaKtWGaT9eotzz22ocrn2ZqH--HVcngu2GFwnJZHF6fWIvhKXWAk6b0_mzvmj5fjP6OLiA3WOFtpuLnoonyA4-O8Ase98m8heXhsOT1lA0eGj-YYNKgLrGKrQfrLFfcsL6YaFXS4dC94V4U3iQvwhdYtzo_A4TqYyyCPzWR71dxFD2xDTmjjLwvg1eBO3898aCGuAcVVx1dkonn6ns6lhlf3SEJ9VgbYnySQe-MHBlb_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=RhVl1LZ63_LlX82A6Drs6krSGVvsZ4uWHa_BPp5-aZM7_f1thFNmMrFnRhC9fFuztnE_Wp81QtwYfBcCwfDXGz4Bfd-rywMfjQKdb1CQrvyuYBGItWqvb34FZr9fgssth6EEHsEbv0sT1Y2BfoIb6tAO8yg9jewk9wdC3RY32_tV5UQhfgdb4syGDyXouLKWljveZH1RSO9seVQrOztEIh_pVZ1r4J93nMNOaHSVvMMWLhaE7Ib8IeQvb607HSb1JRlIbxS-q_-jNk_ta_IyjjvkCz-3vUXm-tYQ7omP8ZSbH1C1FCu8g-ZT17OQQ3r3kl9AB2Y7CoPyjBDGrjvJV1buC5K1ndGUfcIrf-AJRs5gIOORyX7ejVQDIJ7OpCk9kPa8wCwuUmRT6Em9IfcqpDV4XWJJ5kRhlCLZUHS-x7y_0RQKYZGwr_KDgDK1TxrOwbKMwL5qbjtlO3h1VCBSEmvOiffOvfr8L41fpIJcL7mePdnI_sJYeFeyusJI51dYiVG9DnBrE1E1fNq7etB01KVIexothR8dEm-zUmgGq-hPTRUru0O-UzlkdcX1B_H4al768JfHewWHrmyHLb_AxgPK-abUldyuteWk9su0Jqgczy1DynnCWBlEaLntHtZez9BCTj1_CeR72OlUl7zP3QE6Vrw2VJ1F46kJwg8vVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=RhVl1LZ63_LlX82A6Drs6krSGVvsZ4uWHa_BPp5-aZM7_f1thFNmMrFnRhC9fFuztnE_Wp81QtwYfBcCwfDXGz4Bfd-rywMfjQKdb1CQrvyuYBGItWqvb34FZr9fgssth6EEHsEbv0sT1Y2BfoIb6tAO8yg9jewk9wdC3RY32_tV5UQhfgdb4syGDyXouLKWljveZH1RSO9seVQrOztEIh_pVZ1r4J93nMNOaHSVvMMWLhaE7Ib8IeQvb607HSb1JRlIbxS-q_-jNk_ta_IyjjvkCz-3vUXm-tYQ7omP8ZSbH1C1FCu8g-ZT17OQQ3r3kl9AB2Y7CoPyjBDGrjvJV1buC5K1ndGUfcIrf-AJRs5gIOORyX7ejVQDIJ7OpCk9kPa8wCwuUmRT6Em9IfcqpDV4XWJJ5kRhlCLZUHS-x7y_0RQKYZGwr_KDgDK1TxrOwbKMwL5qbjtlO3h1VCBSEmvOiffOvfr8L41fpIJcL7mePdnI_sJYeFeyusJI51dYiVG9DnBrE1E1fNq7etB01KVIexothR8dEm-zUmgGq-hPTRUru0O-UzlkdcX1B_H4al768JfHewWHrmyHLb_AxgPK-abUldyuteWk9su0Jqgczy1DynnCWBlEaLntHtZez9BCTj1_CeR72OlUl7zP3QE6Vrw2VJ1F46kJwg8vVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=KvVNC05E4VzVKRPvobYFvG29Ywq4iBuJAgGo9nIvW8kXppIkjl2PALaO-6bYSme-Ok7xyzjJyOROTHhtH_I1grpSmLQ5aLFKmwAojcE6fR4xTe4DiUnabBQ7JSGy5UciHA9h2g9UZ2yXsS50JDtfduMcOzr57HhVhIPV7KajFVqdNtlve5nT5Q_yDf1vNP9vTLNmvyVHhbWdJyRaukk6463sv62ft-ASVbgjc3KsIhsshoqmvEwLwrRAiSkm5VsMw3ov3o-XK8kQQjCf8ZnnksIIqDqTYhCrgzhQ2i7b3qyCm973daEqezxydNpKq209vzc5q_V2HR5dcB00sQGmww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=KvVNC05E4VzVKRPvobYFvG29Ywq4iBuJAgGo9nIvW8kXppIkjl2PALaO-6bYSme-Ok7xyzjJyOROTHhtH_I1grpSmLQ5aLFKmwAojcE6fR4xTe4DiUnabBQ7JSGy5UciHA9h2g9UZ2yXsS50JDtfduMcOzr57HhVhIPV7KajFVqdNtlve5nT5Q_yDf1vNP9vTLNmvyVHhbWdJyRaukk6463sv62ft-ASVbgjc3KsIhsshoqmvEwLwrRAiSkm5VsMw3ov3o-XK8kQQjCf8ZnnksIIqDqTYhCrgzhQ2i7b3qyCm973daEqezxydNpKq209vzc5q_V2HR5dcB00sQGmww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhsSfeQQnG0CyiG8arYA8R7D5hGZa67R71vRwl3qzQBB5xsIuVDm0PjubRRqf14pwJBQueybdK0sJwzrL9mPFwfbXqG-Dm6GoknAGGNVcJRHgBlgthXQxcWKUlor89gTQSpujkB0YXWy7hsUofNmAOCrmIm7hG_ARxmjokCFu58RvDInmy4bknjy07Ag4-DmLxmHDj6pG6FTDYz6dY25CGgEUG_9LCEt8peunfA0CD10BzkbBFgDxJJeSTK-dbbGsGHNDj_54hNGE6Fccs0tZn-WQfdxJcWSJQBeJI_kAHNGnU4LWqxlXASH0s_r3yIVvMgpywE9F7_41Dxc4CsMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7UPIGqU67b8ck5hQGq7ncj4UWAzMeVRyyCpXA36VE0jUyg0McRGsaHbX1Oa5gpSgcBNhZDXTwQzQ5C3IqsjcWygQNeScPa2F9273TF2xj58KVdpgUWX7CXvOyBQt8rxu9m9WQS23H2ksAeolNBNre3nJKTMYkKO1UCfKZuCf84AYqIYpiNNdZQ686bwilPeAmmaQAzQBpwjt_6Sv2AWeUaiILwh2IiE4D-CXWXbld5nKDVeHbvvHHheynZLE1ILfaW-aiWjdwrKeKY335-RqIlcQEwj5FaeNgLfcJpMUKYWW6eaChrPiqirgV_EgNC7s3a35UEkbIERFk_-arz8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVYfoSI0Dk1V6l9NANhfH-oIoN_f1csQq_PhrIH7DkciLH0ggqm4IUTmPpfWFttCS35Z--J9ltwT2m3JnLXibwFX6eTEubJO9gNkCqJVR6lEEgtNKcNSdPjQfuFMm-IqhYFSQgUI0WKsV60DWMVBBpzfMnGh40thSl6G4hmM6AfSKu7orTvBAxedsrR4zGl294dqIQWLCx8q8up1G6ZV3sA_q0-1KXHiaerIl-JndU7mb56MZr8b9kNSp8qRw_NVGbfRxqDpPAMddA8KKNdoSk2Biso9U-3x6etXSVdeNV07zlIW6Ba1UCHFjzXjCMgcrDz93iDmxRkbSQTT6faDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJMXv-ePhR6oKh6LXx39tZDSWrDmgrtpJnjvI59Mov9f1DbfKssMX0y7jFNuvpXSJhGPO20BAToE3h6iKs0ps4EL6jAdN-J4h2ffIi6409u_Dr3CH8y112o5zIb7I17GfslSyaNybHx36suIpxLb-PU7zZtiv-cX4R3pRTxdyQPD_UyuOT35wOlOScMoixehcKZrwIaFT3mKLv2ehWksuEl9euRTeEgnSPneP3kAgcYe8mX7-UdKjoVxNvxjneJ8TjS-C8FzADGvNMQwze5m4B-YLpxp0P7ozyjHyPRrp93m3RTTb51ytLib0sU6mvEC-6Jh0GxHuSnN62zf8nWiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5wbLmanTkQIUdJgXR_XUyJd5QYMFdOZx7Pc5cMU8Ez9M9UkHYpgOe1v9BqFdt1FSL9txXv7z-7ZMuUwPdCaW5nWPAz5kh247eANLh4Itn8M-rHT5H7GF9mMtSxcWCR6udVA62E-gdtgJ3vnG5f2x1Cz02su00915Pc7sEURw5JWcCaZa7zbrQQVNf9fiuj04_RJs9XNqLRj2IcA7br8TErpUqpKusnGoMA0eBapJ8l-GjpIS_hRDneS7bUZ55qJMmsYx6z0iTeM_tCWoj3cSnvNHySV4roVbRz4wEN0jJ_PTiAOndEauec9E_Vx2TIrLgtoOmeVDEoj-Lc7MlxiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2d_1qtKhwAd770iSlO-0aLTNltrDNbowHe469QpGA0YEyfZT2RMWn3aMsOy9_f5XmVnNy6QgrwsD66OtpSdE6qCiMNo_iaqXBKiXQmLEzc5i23qkBr7dilVRv2TsCc44HpzX0lI9xpJAlhNOEgffu313o87iR9HiBG0-x7a4X2XUxt46QtowIZOPgwOsAcVc9nEXLI28kJzI6YhEupLx8U5oa3K0KiEtUSvkXW5dV27uHEzCK_WV08QA3QpvohaBu7JQ9F2Osm1B9aPh0D2vbDJvOIbecI4lzNsoa9IckwiKTxuOiDCYoxQKntDz0NWKs-JXkme9jiDyBwaKsVVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=Y3PWPrxGk9yZ3NFxqG-qzcAwbBrN3LI4MDmr7uEUBU2xhiesmxsEN7wIYgrnM_MxqvlI4w4uUEtCQc4w_uAaUqMmTeAyEQ-qxL3SrvH-_rKlBO_QOReL01pVvVe9WPjv7440v4nlRjC72Y6nu5rPVPhIx_RdTqfYUrY14tOrESX2AXmR4KUrEvC5RRP50zCW6bjRbo75RrMVdSBg_QgPp8yMKFMCsHN_9Ka3JE16WIi103j8BTW_pgPFG2Mr9hIQf-H4SeydQW-sLD8G8gVnM5eD_VLgQnv1w4F9CD2yOc4xkrzkXYdAL070lPMgmSvie4gdnj3qewE4yDwl6O5gZaiRwZfIzFjNBy7H3DfmGKwWj7hYQfsOAPPdgtbo_9G922pH-bh22yjQl65UInAEaULapK3zqB5FeITdGICEJiP6z1WJVALjlZxEOkf7hfJiEbnzXd1y6eOPV3Pyt0KDrl--oduYOuetgICyxtTkBPdDr-6WLbOmU6RlGpvakqSRwTZ1UzEadK8bt9kXTzBRRvQr-1R2nzkz-C3bvaVLvpUeq6ZIZiKwBA6_EB_UUYR8Hdw6VMRCgkUfcYy1bBpM7dnulMXBI_dHX5Td3u-d5H6SlLN8JmHd1-auuSVvJl0-vpQQxaXc8AQat8qNs6hLQVGS5uOu8yikt36Nz1bEwkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=Y3PWPrxGk9yZ3NFxqG-qzcAwbBrN3LI4MDmr7uEUBU2xhiesmxsEN7wIYgrnM_MxqvlI4w4uUEtCQc4w_uAaUqMmTeAyEQ-qxL3SrvH-_rKlBO_QOReL01pVvVe9WPjv7440v4nlRjC72Y6nu5rPVPhIx_RdTqfYUrY14tOrESX2AXmR4KUrEvC5RRP50zCW6bjRbo75RrMVdSBg_QgPp8yMKFMCsHN_9Ka3JE16WIi103j8BTW_pgPFG2Mr9hIQf-H4SeydQW-sLD8G8gVnM5eD_VLgQnv1w4F9CD2yOc4xkrzkXYdAL070lPMgmSvie4gdnj3qewE4yDwl6O5gZaiRwZfIzFjNBy7H3DfmGKwWj7hYQfsOAPPdgtbo_9G922pH-bh22yjQl65UInAEaULapK3zqB5FeITdGICEJiP6z1WJVALjlZxEOkf7hfJiEbnzXd1y6eOPV3Pyt0KDrl--oduYOuetgICyxtTkBPdDr-6WLbOmU6RlGpvakqSRwTZ1UzEadK8bt9kXTzBRRvQr-1R2nzkz-C3bvaVLvpUeq6ZIZiKwBA6_EB_UUYR8Hdw6VMRCgkUfcYy1bBpM7dnulMXBI_dHX5Td3u-d5H6SlLN8JmHd1-auuSVvJl0-vpQQxaXc8AQat8qNs6hLQVGS5uOu8yikt36Nz1bEwkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLo1XeERXtodet_62pGwrr_1qVLQwjrkvKCZwBqgFivWvXSyNBrHihVax2wFDgRgWS8iyMI9uVRLR5Qet1h59JxCYBNGoXLQeryyZeK9fDSyZ2BbLkWFGQDbyz1GhyQNSPnE6h3J-HOolxwFCGKLNCvHfXaWyjHwKf9pSmNYT4Cw-9BB0wO2AV1pkyB-a-wGk5XtYrVXA4EZg0XEogfm93NCedSrMe7QJAqp7qXhOWjd_LWm111TTN-s9BZhdi4g_EuW30oOmqOtGwonV935BRemJf7_IoNpCSvNM56uFr69siT71aKYuWboJUEYFNWilini7K1RM1g9ak0BvnrM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJu-p_zFZRAn7I3P2b3TBKRhOEItTxbviyJLoEKvwTgR-PM2xm0w7gU2NT8JBihKg61zzjIPRnb70qpMieaun09VyWg39O_KxcAzPOM4q0M7edTYN69cBZ9wwbETpDniXnPoZPTOieLT0SkfgQJnjwWzBOz_Ul3LaiXShny_wzEpJVmMf8Z9fMM82lbHqTtOi1JufWzNgasbQXpb9QdVZQsy-33WlB17SfPZ1zcPkXidesYDU2TKj2-u_46p5HTs0mO53TDG1ErHZeDJUk1iZrvhfZ7IQu9_icVJnmmFED0BMl10GgIntttq79V6Clp7kTI6CzSGdpTX1kDOsRczsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=jd9YAnn0RKTkiE6Sdr4XoXSJ9PPFySp95_ZTaWxo46xb72l8ZSDQl0D8Ehhx7IdxlU_CF8dml_eCZ5gHmfAg-_WL2VQj60ziB3xCAqY1z4GgWcf603ii7UwwLZZoXJkzwxvEE7O21Ihuvr07dw_dcbHvTj7Iz5zYIK9NZMqgQTvwHo3oQglhK76kipv31nxVVXs2L0lODW9SxbxmA8ScPYM6TJus4KVBpOcisTG2kIHWjlB9fZCdvUbVyskJeLis3Qx4G5neui0QLXc976xttQp2TtvCnW-BdMomdHQIyue6OkWiQlF2OLgLdYnRsvqjFKAKZmDrBXzwp76js5Dj_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=jd9YAnn0RKTkiE6Sdr4XoXSJ9PPFySp95_ZTaWxo46xb72l8ZSDQl0D8Ehhx7IdxlU_CF8dml_eCZ5gHmfAg-_WL2VQj60ziB3xCAqY1z4GgWcf603ii7UwwLZZoXJkzwxvEE7O21Ihuvr07dw_dcbHvTj7Iz5zYIK9NZMqgQTvwHo3oQglhK76kipv31nxVVXs2L0lODW9SxbxmA8ScPYM6TJus4KVBpOcisTG2kIHWjlB9fZCdvUbVyskJeLis3Qx4G5neui0QLXc976xttQp2TtvCnW-BdMomdHQIyue6OkWiQlF2OLgLdYnRsvqjFKAKZmDrBXzwp76js5Dj_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=EvTvsht_AJIXPg1GSu4aHjH6pUHLgNb9CneqsyRUgevWlwPz4VX_taxexxjcnKGpUQ2AVGR8sAFXfg1-x_jRgBYn_EHmep_VGaeswE79dNZl866BcPADjdcug6nvtpxB4nD6U4r0EnHe3ls8MrOIG-DJW19UrhCqfu2nozqcCoXRJ4g-2TeAvxUfpMt9obkIdK5d4zpn0NDSnsznUTb0RBFnYrGinHXVE216eczrWYEZBvMowkLz3QKy8YsH0PtlQiVh8Rjm4hcLhln4TuJ2uCILEUUVqkPaWMK58CQWc_46sjY5-VRL-VKljbtl-vS_qow3W0duc1po5qIcW52XUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=EvTvsht_AJIXPg1GSu4aHjH6pUHLgNb9CneqsyRUgevWlwPz4VX_taxexxjcnKGpUQ2AVGR8sAFXfg1-x_jRgBYn_EHmep_VGaeswE79dNZl866BcPADjdcug6nvtpxB4nD6U4r0EnHe3ls8MrOIG-DJW19UrhCqfu2nozqcCoXRJ4g-2TeAvxUfpMt9obkIdK5d4zpn0NDSnsznUTb0RBFnYrGinHXVE216eczrWYEZBvMowkLz3QKy8YsH0PtlQiVh8Rjm4hcLhln4TuJ2uCILEUUVqkPaWMK58CQWc_46sjY5-VRL-VKljbtl-vS_qow3W0duc1po5qIcW52XUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=WOCgXX4kGhC4SCI5xEp1RnkRT0I9HqLMw_7-6k9ItQbLLEg0UyFjhLo9PAKLYS7L0wyks9MbcNTJsJHJfVnOKHSbxiDfEe7wrov5CJQxPvTQL2TgINCi8PcHEAL7Dj53dUXZLOB2Flf-NjT0tOgMjQy7gp4lYW9hbO-bLGPA1oqE4i49Exrt9gU9HTGLsgmezZ3ZRoe__jM8hc11qK8iyB3tTmzJ3Cu0cLHdMhqEsw7h80u6A7QLmB54Od4nH6qm_1XQnWMM8_U4mjsF4KNv8cazwC86MJ5WqVV-p7qxfhjH4_O4rejphPmBwsqnQAxlYf6VCAiNsJHFhG7IG1yeuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=WOCgXX4kGhC4SCI5xEp1RnkRT0I9HqLMw_7-6k9ItQbLLEg0UyFjhLo9PAKLYS7L0wyks9MbcNTJsJHJfVnOKHSbxiDfEe7wrov5CJQxPvTQL2TgINCi8PcHEAL7Dj53dUXZLOB2Flf-NjT0tOgMjQy7gp4lYW9hbO-bLGPA1oqE4i49Exrt9gU9HTGLsgmezZ3ZRoe__jM8hc11qK8iyB3tTmzJ3Cu0cLHdMhqEsw7h80u6A7QLmB54Od4nH6qm_1XQnWMM8_U4mjsF4KNv8cazwC86MJ5WqVV-p7qxfhjH4_O4rejphPmBwsqnQAxlYf6VCAiNsJHFhG7IG1yeuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=Rm3PE47qPz3C5Fza6rgGXWvPADplqp6F8L21kN1ULKabLI4DCAEhgs_0EMYSjNNNPURu1AA6mfS4YHdfHwyLzathNT0z_V05k2R063fIB_XJ2bW7DYAI0rP2eLIX2axrTsqo-esYt1EEEqYGprzbCSquIjkt4FVWF8TNfR74uWwUEMwpMweYlXxaZT3moto2dZ1CXPji4HgqI6CwD6YFkc_YUaqBta1zs86PgT6NwmuVyYQKYFBU1LTcMJTPOO9qqLg76LgEX5xblWGGGB-8Ndkx9XEpp3AstGDapH2wwar8tHlBC1WXsgZiyyATy_QH5J8MSqbJbsIMSRAp1k6YYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=Rm3PE47qPz3C5Fza6rgGXWvPADplqp6F8L21kN1ULKabLI4DCAEhgs_0EMYSjNNNPURu1AA6mfS4YHdfHwyLzathNT0z_V05k2R063fIB_XJ2bW7DYAI0rP2eLIX2axrTsqo-esYt1EEEqYGprzbCSquIjkt4FVWF8TNfR74uWwUEMwpMweYlXxaZT3moto2dZ1CXPji4HgqI6CwD6YFkc_YUaqBta1zs86PgT6NwmuVyYQKYFBU1LTcMJTPOO9qqLg76LgEX5xblWGGGB-8Ndkx9XEpp3AstGDapH2wwar8tHlBC1WXsgZiyyATy_QH5J8MSqbJbsIMSRAp1k6YYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=i4j8oEc8Jt39Uvj6aGJ87lDD7w1B160yOYoae0psCzJcF5zAr5N4wOowtyYRPYSIRpOw-zyVqqA3fmiiwib5kyE7oPoysll17EfYW_88hK13ox6NRSpKTOrOKt-tYY6xpzX5-cAKbl3HO0tm0dY3vwdgk_3aG9DwqNtEcdO7reV0yBx4fnNEnZDQBOTrwYoxioph9gu-SDaWXuqSfXYfttL2gF4FD934IaS2gy6g8G0cGIrPrStieV7u8QFkWgT2y5yJpDMVxWFhogtmwAIIDYCKEIKUUcmN6qMNSSPIs0nXm4nHAG1yPgz9tPO2n3z1ml9xM2G_xciWCEZUSf1iqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=i4j8oEc8Jt39Uvj6aGJ87lDD7w1B160yOYoae0psCzJcF5zAr5N4wOowtyYRPYSIRpOw-zyVqqA3fmiiwib5kyE7oPoysll17EfYW_88hK13ox6NRSpKTOrOKt-tYY6xpzX5-cAKbl3HO0tm0dY3vwdgk_3aG9DwqNtEcdO7reV0yBx4fnNEnZDQBOTrwYoxioph9gu-SDaWXuqSfXYfttL2gF4FD934IaS2gy6g8G0cGIrPrStieV7u8QFkWgT2y5yJpDMVxWFhogtmwAIIDYCKEIKUUcmN6qMNSSPIs0nXm4nHAG1yPgz9tPO2n3z1ml9xM2G_xciWCEZUSf1iqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=n1VkR3SKPJyj3hgAg2kOdyqTt2JkyjZzzvLmqnkpPdL3m9XrtMNvKcvYd3gAhSWOsvtSMdKLq8Dk64YIdzodzF1JkHTD0NWphSCw8hUrmhT8bJ5uSBVaPYBC6RoywjDtHKj8ugfH2v_Os3LcDAxS4Oo12CMhAHhPzp3mRTbb0Xik_5_wbbQMh7aOOVXJpXPEDAeLuNPw5-yKIl-nWQghnKoF0sJsETCbpInnG6ykUzIhbxUt8gN84xuASkr4QWu8--s_wVWAf0tjWoCFb7UtKWEdKmM4BHCCjuXBRseL88KZ8DiePpLI9-jx8MQ1BIzOmkGuOSzAGhokpzjr7WvNVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=n1VkR3SKPJyj3hgAg2kOdyqTt2JkyjZzzvLmqnkpPdL3m9XrtMNvKcvYd3gAhSWOsvtSMdKLq8Dk64YIdzodzF1JkHTD0NWphSCw8hUrmhT8bJ5uSBVaPYBC6RoywjDtHKj8ugfH2v_Os3LcDAxS4Oo12CMhAHhPzp3mRTbb0Xik_5_wbbQMh7aOOVXJpXPEDAeLuNPw5-yKIl-nWQghnKoF0sJsETCbpInnG6ykUzIhbxUt8gN84xuASkr4QWu8--s_wVWAf0tjWoCFb7UtKWEdKmM4BHCCjuXBRseL88KZ8DiePpLI9-jx8MQ1BIzOmkGuOSzAGhokpzjr7WvNVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv5NXT-HJ_mSGDjbL-PC54-UQv7VmL2WINyb5wuJYMRRJK7P6PmcFj-Q5CPF4Vx996asCVw25TTX66mg2TullPa2Ln5eRFBueJ1S3lllEh2Zb5jo4piOg9_MuBbg-Z631tSM7qPXul0_vZz6JnCPuht7Zhw9le4Wj3IzBE5kyvH0kEdAwTsA2FhIPdb5wRdjL6gHRNjbSGgGz44tnm64ADHd9tG6lOZkIx1B-30pWyKGe1YhpYb7V26btW1wXc0MygUR35yIMzRQkD1qtvdfNe7eIO7Sp6E2YNXSpGVe8nEbaxD0VpnKd4HyWlRZYDc-7EyO4w0pdKcrZUa2ubF2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=LDM2GIfKO_kPUot07pk1N4MFqU7B087uiwJxO2yTrWaZWkx7-Lx57KFBcUooqtfheHKuzfzG5gk18QIEhR6ilF_fihlTJ3A3fe9wXXr2KlVN4z1jEImKkevwu3PTA-627Ty7R85csfeGX8lTT_KmUtbuBjXJS3cJ1TMiRr8baz7zXDcJmcXAZdRtFVLx9Mqjj30SP46Y3OKG7ItBVQsL4npivo1rdpY5YDe6msNfsvV7v1XxUqEEk4wzSyE7XvWrXCQADJEW9ARah6pa7aHxzPMTTnUrYKLbAuP89C3_-PnZfcwwEBpbiAPD0m57gJ-pQpk3aKJut5I0-Tfm0zqE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=LDM2GIfKO_kPUot07pk1N4MFqU7B087uiwJxO2yTrWaZWkx7-Lx57KFBcUooqtfheHKuzfzG5gk18QIEhR6ilF_fihlTJ3A3fe9wXXr2KlVN4z1jEImKkevwu3PTA-627Ty7R85csfeGX8lTT_KmUtbuBjXJS3cJ1TMiRr8baz7zXDcJmcXAZdRtFVLx9Mqjj30SP46Y3OKG7ItBVQsL4npivo1rdpY5YDe6msNfsvV7v1XxUqEEk4wzSyE7XvWrXCQADJEW9ARah6pa7aHxzPMTTnUrYKLbAuP89C3_-PnZfcwwEBpbiAPD0m57gJ-pQpk3aKJut5I0-Tfm0zqE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkr4_v5o10p4fzp785jWjiymzT4XHwCi6so71SfuPmbS9ykaqqvRzB0HrsI0KDBHbT85VLZckbyhrecH11ZebLA2w9ZlE-AS9nyAL7eRsHClnMmDjGjf-vJGZOvcBNzwrGoysvGzRiieN4fv9ua-dpN6Y4QFgFXFyJ8SWopXssDKtc4DDizEybIa5ZiZqlrRtfZgXQPBFXYkmn4JD_qHk1iMs0xRssUxJXj-q7bcZjDYyOKJp4VL_C4MR3TSjM3YkxRGt-0NedAON9z_u-pDJb50raKqndK4zO6Bq2H5U19zZjgzgLzIjwvnNgzxWkF0HDdRZccN0mYiqf06xl9eAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WugM4ME1VcSWO1d09lesGnO7nVsGn0y5BTcYFQii5V40OQV2Wj9iySXqc0RzEjqVtnIus8p-GNFUgJ9MIS2AS4DQ78Dy7pJrsyfkiwFkTkbxWebJCLGmM74KLpdqRyM_Z2FNGV2Ns6JW_fQSAaU2cAqfOTh0xDVZv3jW3gaK7OrMZitk15sYMWacUNg55T-X3llbuiWaktFkH18BBiJUFUGdPFNROFqCYsFqPwOcmq9RhxAauFUHtP4czOy6X_jj4F14Gho8T73JGCDZk4s6r_B75DQBEJaINXQQp93dN8DxbHSRnbDqAZTV4xpK4nq_P-0RAyGW3NyVkA-xzOlJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=Iwz6nVjMokqufIdQiko0b4deqscqtsY3-UMMsHXlhtoURVsnkASzEA8JqKAvJ9B0JeX-8TSWn6ockUJTHG25zL6Ycwo5PNeHRD3zShac5al5fobmgDTDqNZrhExzpSKib6M4q4MF_O_YHalYrWGv9BLI7ETPlwaVmksyU8oglk_KTDEgQGH12gvmE1cUiHUZTQH8QjbL1ILI_Q-t52GHvCUUR9Te6xuRK-3ZdiBPUMhVSwngMDKsXs-ONTiRdbZUx74dtFzepFSUweWpbsmGUXvwiRT18GpkE2TlwyraBFon8Ot35FL5XFpIm2PCBO1Wp66NJ1PjfMkqaFBAcXJsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=Iwz6nVjMokqufIdQiko0b4deqscqtsY3-UMMsHXlhtoURVsnkASzEA8JqKAvJ9B0JeX-8TSWn6ockUJTHG25zL6Ycwo5PNeHRD3zShac5al5fobmgDTDqNZrhExzpSKib6M4q4MF_O_YHalYrWGv9BLI7ETPlwaVmksyU8oglk_KTDEgQGH12gvmE1cUiHUZTQH8QjbL1ILI_Q-t52GHvCUUR9Te6xuRK-3ZdiBPUMhVSwngMDKsXs-ONTiRdbZUx74dtFzepFSUweWpbsmGUXvwiRT18GpkE2TlwyraBFon8Ot35FL5XFpIm2PCBO1Wp66NJ1PjfMkqaFBAcXJsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=Dp399iRHvUAUKZHBXJr8zp0PZr3vCbsCcMV1kU14fWVjVfxU1Sb9kw9rhP8QmjXHcdak4NkMqbcdKQhWnIESl22aw8TPLnnwxtDnTJrdccQcccW-Zp8O9v6K5FJfe9G8VyynUl5UsiZIAv4ZM4O8g5oPnbhshfUi5J6LeR_Wfs73RKvkfWl4qSFWC8VHbmpQIbWWhQgX9a6xT8OIlnznMq4A9JN49ToBwAfbjAEm-XbVm2n4w5xgxXlUoAyCVHRckMMDYVD9qME5udgIo0wHrOcBDvKY3RO0EqDbm5c6JnpydXJQveNUt85vZPP09-bGfG9OdG8Zxd972-YlMaoFzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=Dp399iRHvUAUKZHBXJr8zp0PZr3vCbsCcMV1kU14fWVjVfxU1Sb9kw9rhP8QmjXHcdak4NkMqbcdKQhWnIESl22aw8TPLnnwxtDnTJrdccQcccW-Zp8O9v6K5FJfe9G8VyynUl5UsiZIAv4ZM4O8g5oPnbhshfUi5J6LeR_Wfs73RKvkfWl4qSFWC8VHbmpQIbWWhQgX9a6xT8OIlnznMq4A9JN49ToBwAfbjAEm-XbVm2n4w5xgxXlUoAyCVHRckMMDYVD9qME5udgIo0wHrOcBDvKY3RO0EqDbm5c6JnpydXJQveNUt85vZPP09-bGfG9OdG8Zxd972-YlMaoFzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=jHWhfw6Vn7_4v5yBZh1gMpM6qXzvoH2ofH6RAmCLyAPwotsD3LRUA5dxDBvpoKBc0GBIAUjChNtfWUv9NTCT8nm0BkSdaS4t3mCAI4NHU_lYIP0W4PDpoAWhzKzlv7qQZVamp8RB_MSHkTd2DLxZLglf5L06Lfj5pGwHV3gdvkmyX-dK-hhPmaw_TDcy1Mr4eamMzbS2t0cgVygApTLryzmyKCoMi_sYeqNmNQlG9gMTfbi5JfOAqXpRHS0YEBe7DP8osuuM5V_e9Sgf2tHkFNmYejSRMO3oRFUaMBofllYDF_ep5XFf-fr32PSucHKoMWYeW0UGmtl6C_x1zLnffw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=jHWhfw6Vn7_4v5yBZh1gMpM6qXzvoH2ofH6RAmCLyAPwotsD3LRUA5dxDBvpoKBc0GBIAUjChNtfWUv9NTCT8nm0BkSdaS4t3mCAI4NHU_lYIP0W4PDpoAWhzKzlv7qQZVamp8RB_MSHkTd2DLxZLglf5L06Lfj5pGwHV3gdvkmyX-dK-hhPmaw_TDcy1Mr4eamMzbS2t0cgVygApTLryzmyKCoMi_sYeqNmNQlG9gMTfbi5JfOAqXpRHS0YEBe7DP8osuuM5V_e9Sgf2tHkFNmYejSRMO3oRFUaMBofllYDF_ep5XFf-fr32PSucHKoMWYeW0UGmtl6C_x1zLnffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=vBF5XXWt56APxpF-g5U4ajrB4RTvmhmdYLt4qrFLZ_hBH7DlIhmvHUWO-oGEWspcv4KxvHks-WB5QvZ6zt-G0uamH7DqR6R6U40-fgTMmWvdEqm1rGAB6VIGqRETXadi1QYD_NQEHP7IrkazBnzQjW9IeKHZ5xRUmWrQP_l7s4yF5wfcpEK5N15zMXMHwYU4F3wYWgERFhh94dlOd6SwtrV5Mih-vmgKJnAs7FMZShM6Enivb6wVQWupA5mWbohKb9WUYEPseKLQVGQQXpj_nzc7rcowoxTv6ftNPXhcMxAEej_A_61FSEqKJyrM103qHWX_NLB1ZgVM463i47m1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=vBF5XXWt56APxpF-g5U4ajrB4RTvmhmdYLt4qrFLZ_hBH7DlIhmvHUWO-oGEWspcv4KxvHks-WB5QvZ6zt-G0uamH7DqR6R6U40-fgTMmWvdEqm1rGAB6VIGqRETXadi1QYD_NQEHP7IrkazBnzQjW9IeKHZ5xRUmWrQP_l7s4yF5wfcpEK5N15zMXMHwYU4F3wYWgERFhh94dlOd6SwtrV5Mih-vmgKJnAs7FMZShM6Enivb6wVQWupA5mWbohKb9WUYEPseKLQVGQQXpj_nzc7rcowoxTv6ftNPXhcMxAEej_A_61FSEqKJyrM103qHWX_NLB1ZgVM463i47m1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=r0Z0JDP6S6dY3AIYMZXFg9SBKQIhlXFwbull0c9bCVId43OaBfLeW6t2moVxcTDNFmlmjkPTX1kllFtpQ-Wqqi62TX9XmjDNU3ceR48UlmmsBu5PS3bqJkI7Lnhb-XWNxUvh20X3ADCfJfqoNiiUdSH1Nc3NSVIHyf3oXwboa0rwFoXaRIftqXjcd0VCHG9b13e35YUJoUpJ0jfLSByyBsdStuMSBnyxnJZbbMJZrMKZCmt4z5vC5o5EzGdgbPWjtIYN9vaJlXCUnm10KFKfqxbkh9O7ISBadLGvf8MlZ14whiOn7ag4oH-pfG_AapSWZXBuojqIai97oHtWKrSauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=r0Z0JDP6S6dY3AIYMZXFg9SBKQIhlXFwbull0c9bCVId43OaBfLeW6t2moVxcTDNFmlmjkPTX1kllFtpQ-Wqqi62TX9XmjDNU3ceR48UlmmsBu5PS3bqJkI7Lnhb-XWNxUvh20X3ADCfJfqoNiiUdSH1Nc3NSVIHyf3oXwboa0rwFoXaRIftqXjcd0VCHG9b13e35YUJoUpJ0jfLSByyBsdStuMSBnyxnJZbbMJZrMKZCmt4z5vC5o5EzGdgbPWjtIYN9vaJlXCUnm10KFKfqxbkh9O7ISBadLGvf8MlZ14whiOn7ag4oH-pfG_AapSWZXBuojqIai97oHtWKrSauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=TJvjktKumVkS3Hzd5giMYT_-RS-BMFMMguov34k6VXe8keKemAn5DnH17-GRJZIfTz1tSGqoN63xVcexC8G4IRBXOPoexG-R3WGQB1ha7BWX-y8INwaInd-J_EUtZZo9LNlc4lCa9-JbMQCHaN3fkrgEYeIORg-OZo_rlNijfSt0Znu3T10NdXdXepYFhiL7RB2J7IXaEhn3sm7Gd_nMscGSsYuC96-vIJIjt2CEEfNZ4Ram9igjzn8d7cFJ0B4-3wXeoLQM9ZsanwcQusraFMgUhtmmhE0-M0pQ6rAmDOlblHeI-pjPs3HTrfoVkOlklpWMRguBGZpm1Zp8pq5bLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=TJvjktKumVkS3Hzd5giMYT_-RS-BMFMMguov34k6VXe8keKemAn5DnH17-GRJZIfTz1tSGqoN63xVcexC8G4IRBXOPoexG-R3WGQB1ha7BWX-y8INwaInd-J_EUtZZo9LNlc4lCa9-JbMQCHaN3fkrgEYeIORg-OZo_rlNijfSt0Znu3T10NdXdXepYFhiL7RB2J7IXaEhn3sm7Gd_nMscGSsYuC96-vIJIjt2CEEfNZ4Ram9igjzn8d7cFJ0B4-3wXeoLQM9ZsanwcQusraFMgUhtmmhE0-M0pQ6rAmDOlblHeI-pjPs3HTrfoVkOlklpWMRguBGZpm1Zp8pq5bLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxBBNrsRHBO6P3r2ZhtbSJJjP8wsCtrs6AY4NftyvGFPAE9RYPhUj9AKweMqs_aiXUW_xC5n8wELesFsC_kjXVa0AjBxcdOs80niHD28_h8M_ioWy7A5C1r4nSWDOdTqRv25JtVXoHv9iPUqHZZKUggJHZjbO7um7_zWIIR939QSOuj2NAbSUfxpIlft5egJhC3a4NPViSb6MBThUX6TEUvLwamlUuD4GeiuUHxYtlPEGl0oHdOlm5vRySwapJ2QwyJnzlsHgEg71TfJFiblRJ3HEo8ZPUSTusxq87R2lNEqOcZ5DdqQJmfFhA46PyBAzarMv3a3I6Lfne78EommhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=t3I155Ug9raNlpWEu9tXGC5PvKpEt0iZR63B30k2zAuw12IMkSFxILIsoPLqNtGylsbpugFtmaawX5Tz0JovNL9Rdk_Lnl1WbzGOtxgD85gbDa7RBnsGhHAge6GTzfDRk2zYT9Uu3z6mYG-8Pia7cskDln2v1oLCZrozMQ8WcsVu69QlgqLdiSxCtk4HU-iHGhvYoTxjNKqpqn97yTU0irY6trT0r5NpR6nVC_zW5Ff1sj7BYWLI-pO2OOcQaizHlwO5xZ5wC8eltHRrd60aqm3e-7k0nO73P-_NpVjTUfJEeQnA1hy7my7S349OqsMQvdFOZIq9P-JUflBaD0qTkGpm2qBIntdx2Gpbl15zo7v46yZMZACWjEVegIJxOEhJE03EcOgI_FptqB2HyKsdXimI8dT-x059H0slUdsd8OS5ctflfMhHi-JNvuVNYb9M1AtYv7SOcPE_CWD0unN35p9NMkULYyt4BxYr2dONsfliK3gnBHzFMpALJNPe2sSIU-GY9fc6PrJsxAq14DLEMFKpgGbPRpmWuRbrBgNkC8oqGER5Q6ePR7fqtmgx5tKxVcv_5W_f8rK7xhT3leWwTj6Y0t8n0nI617kmkazg6Be5JJ8lBD-92fzkVcxqh-2nDi1BVE1eg7RhkECzPhHtUQzDxWhPV8tNglWvthNYc6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=t3I155Ug9raNlpWEu9tXGC5PvKpEt0iZR63B30k2zAuw12IMkSFxILIsoPLqNtGylsbpugFtmaawX5Tz0JovNL9Rdk_Lnl1WbzGOtxgD85gbDa7RBnsGhHAge6GTzfDRk2zYT9Uu3z6mYG-8Pia7cskDln2v1oLCZrozMQ8WcsVu69QlgqLdiSxCtk4HU-iHGhvYoTxjNKqpqn97yTU0irY6trT0r5NpR6nVC_zW5Ff1sj7BYWLI-pO2OOcQaizHlwO5xZ5wC8eltHRrd60aqm3e-7k0nO73P-_NpVjTUfJEeQnA1hy7my7S349OqsMQvdFOZIq9P-JUflBaD0qTkGpm2qBIntdx2Gpbl15zo7v46yZMZACWjEVegIJxOEhJE03EcOgI_FptqB2HyKsdXimI8dT-x059H0slUdsd8OS5ctflfMhHi-JNvuVNYb9M1AtYv7SOcPE_CWD0unN35p9NMkULYyt4BxYr2dONsfliK3gnBHzFMpALJNPe2sSIU-GY9fc6PrJsxAq14DLEMFKpgGbPRpmWuRbrBgNkC8oqGER5Q6ePR7fqtmgx5tKxVcv_5W_f8rK7xhT3leWwTj6Y0t8n0nI617kmkazg6Be5JJ8lBD-92fzkVcxqh-2nDi1BVE1eg7RhkECzPhHtUQzDxWhPV8tNglWvthNYc6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=uHr-sUni7sae41D9D0akqDhAFd6f9_R_Q9BaFjMGP5nt-ebbO4XR3sqAtVKu7hkUQHA9o5OWw0mAl9inqi0dD2Fkp42TjtWAERVHZhg7hvYLdowINPFttJ6FHtKNknXsVUZRixWr0-SMEv25BsCFO5Xo3NuWGs7jSrW_uQA9ASTvlCX9_Gn6MPJv5G2xDAcLofy-lXhXIKl59lOBiN06AtizllfH8Awy04u8E5Lcuz5Dso58mas9DUEiIl2QrPdlbHfrNvxGqGtz04u9z4uTLmbKkM2CtOGcOGaPviaEHXFbAassmRIGcawe7sarxVAPDnbOAM0g1K9yWWhxSlOQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=uHr-sUni7sae41D9D0akqDhAFd6f9_R_Q9BaFjMGP5nt-ebbO4XR3sqAtVKu7hkUQHA9o5OWw0mAl9inqi0dD2Fkp42TjtWAERVHZhg7hvYLdowINPFttJ6FHtKNknXsVUZRixWr0-SMEv25BsCFO5Xo3NuWGs7jSrW_uQA9ASTvlCX9_Gn6MPJv5G2xDAcLofy-lXhXIKl59lOBiN06AtizllfH8Awy04u8E5Lcuz5Dso58mas9DUEiIl2QrPdlbHfrNvxGqGtz04u9z4uTLmbKkM2CtOGcOGaPviaEHXFbAassmRIGcawe7sarxVAPDnbOAM0g1K9yWWhxSlOQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=g0Arv9x_k-7VP-qPTH2T4ocUADQ-iUSMLoZre9ECrZNst7d4ZihoMyCO0BnZ8kJ7FDjFrCfLaa_hbUYoRu8lLRvlzJ-sQLXpp11tvYhQkC4aW3cTJQdU97bXqCWLqSk2HErMtvBzw5v4LChK_O8IGBDPGG-mGyYIFIml0ERKl7jK5lgxmI-iu91a7XSf7_ekk4SMMEaZCpnbakNZNeyXeh3sIY9cznWEMcIvjmmUbvcTJil5pE-eP-gX45yhgcRSWFI3jjBknzvBcqRaq0vYZUoc673EYAjY8gjAW_zDwMwrOZ7CmGaIKpptSQOJgI4UITi3bcEscxSAaU-CFCNpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=g0Arv9x_k-7VP-qPTH2T4ocUADQ-iUSMLoZre9ECrZNst7d4ZihoMyCO0BnZ8kJ7FDjFrCfLaa_hbUYoRu8lLRvlzJ-sQLXpp11tvYhQkC4aW3cTJQdU97bXqCWLqSk2HErMtvBzw5v4LChK_O8IGBDPGG-mGyYIFIml0ERKl7jK5lgxmI-iu91a7XSf7_ekk4SMMEaZCpnbakNZNeyXeh3sIY9cznWEMcIvjmmUbvcTJil5pE-eP-gX45yhgcRSWFI3jjBknzvBcqRaq0vYZUoc673EYAjY8gjAW_zDwMwrOZ7CmGaIKpptSQOJgI4UITi3bcEscxSAaU-CFCNpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=hbN7hE-phsm_lPahEbr5697HAkEevuCtGicG9cYWu5n6HUsBnsV9c6btfZJidiobOgtMYkbnZi5lYOIT-TDn0Rj4ta0L6tW8vsWMl3AJet8skwJRAHHjhHLCAz25WOOs1xaFSLthj9wHzJjraAqEJAZMlf9jA9w2Nv4aONh3zokwFUUuOnaGYPszYm7rXzUvdX4_KOOQPM-6uZsWjKy9tflqgJPzkmWaFkrsdL7-kKRWLgsLJfT37EnmveWdj7IYYTkG3F3XJnPG7uCt_qtCRBDs6I-o6EXugle473Qsnahf7Y9xZqRdc4wHxCz6X8bfKSgPHp2NYWMrLu2x24LjyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=hbN7hE-phsm_lPahEbr5697HAkEevuCtGicG9cYWu5n6HUsBnsV9c6btfZJidiobOgtMYkbnZi5lYOIT-TDn0Rj4ta0L6tW8vsWMl3AJet8skwJRAHHjhHLCAz25WOOs1xaFSLthj9wHzJjraAqEJAZMlf9jA9w2Nv4aONh3zokwFUUuOnaGYPszYm7rXzUvdX4_KOOQPM-6uZsWjKy9tflqgJPzkmWaFkrsdL7-kKRWLgsLJfT37EnmveWdj7IYYTkG3F3XJnPG7uCt_qtCRBDs6I-o6EXugle473Qsnahf7Y9xZqRdc4wHxCz6X8bfKSgPHp2NYWMrLu2x24LjyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=Rg0C5dP3_-sZu0g3wtY4nHqODVgsvH6EGgZ6ZkbQOchr2QEW-39mQYd2xXI36h3e6r5syBSGxUzmFCubl73qDg8jBh7FR3yLqQj1K_oDvpkKgUefivb3ftkJqNc5QHyHsYEwxf_FWABS1AU_gRlEm5QHaEF1SGwuZmmEfrLkcEp4O-D5QK_pCQQ86hBFtl666mdurBr7Cfn3CnwmC69F9PMcwpvSCJM5Z5JBA2_4F56mfHfo6W986uihjkmYBgreVtFcmQ7888M4J5KsoSKGayCemqI9U0MKnItt14UKCX_lM2UlDgHsN1wcvFxeICtf52JTz4mRulJSmc5qBhLOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=Rg0C5dP3_-sZu0g3wtY4nHqODVgsvH6EGgZ6ZkbQOchr2QEW-39mQYd2xXI36h3e6r5syBSGxUzmFCubl73qDg8jBh7FR3yLqQj1K_oDvpkKgUefivb3ftkJqNc5QHyHsYEwxf_FWABS1AU_gRlEm5QHaEF1SGwuZmmEfrLkcEp4O-D5QK_pCQQ86hBFtl666mdurBr7Cfn3CnwmC69F9PMcwpvSCJM5Z5JBA2_4F56mfHfo6W986uihjkmYBgreVtFcmQ7888M4J5KsoSKGayCemqI9U0MKnItt14UKCX_lM2UlDgHsN1wcvFxeICtf52JTz4mRulJSmc5qBhLOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=k53s7t_OlT6dLd9s__hOBWhmMX8NEZ_jTwAes8bGQRXAWIUdDF8AfUiCpf_VSqrvS_FtfB-FgLVCosYqJMCKlvI8yMN5f-dMzt2OamX6jPPhWCnGMJ5-CtfXv3D-Wws_m5H_EHWoJOKq0wAh6bcloXrqawpZRXJFYwpLhMxveeo9qB5TOXiUuDVE36yLUSK3tvbSVzfRQBwYm6J6yJkZgZti1d8k3BVYeIp9ByCZybNp9vuRlMMI7GdwZkFJLNzKz0D82Eu66z3FSitnxa1gmB34LK5XiRR2Y-n7CFJzXNLQY9-KDM1lkN8MTD3bYiRA5Mf1lRcbWgigK2y0n7AeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=k53s7t_OlT6dLd9s__hOBWhmMX8NEZ_jTwAes8bGQRXAWIUdDF8AfUiCpf_VSqrvS_FtfB-FgLVCosYqJMCKlvI8yMN5f-dMzt2OamX6jPPhWCnGMJ5-CtfXv3D-Wws_m5H_EHWoJOKq0wAh6bcloXrqawpZRXJFYwpLhMxveeo9qB5TOXiUuDVE36yLUSK3tvbSVzfRQBwYm6J6yJkZgZti1d8k3BVYeIp9ByCZybNp9vuRlMMI7GdwZkFJLNzKz0D82Eu66z3FSitnxa1gmB34LK5XiRR2Y-n7CFJzXNLQY9-KDM1lkN8MTD3bYiRA5Mf1lRcbWgigK2y0n7AeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=JH0i5E3bL_7u2hnSJ5SBIXJTSnghCQmeuIhOBUGXIb8s_a4Xz3e8GySBuz_U6GpHzQvAoY5EVhK1BbUBfBCn9uWQj2vQZu-kG9-MAOlaQzrtTGi9TD9Ek13_n8UTk2AUmq6MAIdw7E7g_iNgNVt9hFe6ak01H--GFGO-lzX654qk9LnrpXEtHFU3G78ljDH87oeFuhtu3W1SwAcPYFH6v9j9nTE9738NCDLVeZR9TtkJHdnduaB6jN-dcG06i-WDow1Fi3vPJEMskD5s6nbplrWTlMn5_GzZwrVt5tcy__-erYAEHk6_93KemU7DdAR9URtuJ3dWLigFw_4kGwPczQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=JH0i5E3bL_7u2hnSJ5SBIXJTSnghCQmeuIhOBUGXIb8s_a4Xz3e8GySBuz_U6GpHzQvAoY5EVhK1BbUBfBCn9uWQj2vQZu-kG9-MAOlaQzrtTGi9TD9Ek13_n8UTk2AUmq6MAIdw7E7g_iNgNVt9hFe6ak01H--GFGO-lzX654qk9LnrpXEtHFU3G78ljDH87oeFuhtu3W1SwAcPYFH6v9j9nTE9738NCDLVeZR9TtkJHdnduaB6jN-dcG06i-WDow1Fi3vPJEMskD5s6nbplrWTlMn5_GzZwrVt5tcy__-erYAEHk6_93KemU7DdAR9URtuJ3dWLigFw_4kGwPczQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=ZPtVvrJe80YeWbKPLXlQFCumbahFwtUVfUo56HnFkKF3c1TpEvvmRjFZffYSPElqzZtvn8mK9-84zrfEF2d94GmG_LpIom0vYVt7kWDqPF7RuksMEsdONE1_aEk7ug3z-nrdJv_QuBqiMOO-5n9QZUHgkwlmplXrolsBmRgQxHEQiy_4teD9tkBXV-65ofBGoCIzXPCkoo-UPysKQNVYZfwtrwMkC6OJl4HiuzKxRXcNXVHdIa4WmQFXwS3tt84klOTv2t-rEZUCn27sB725PTKXr9WPqbl5KW-fA1JV34nfoqg0zqZ19k2BwJyJs-1WQcEzeaVJpuMzZBbyvRovxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=ZPtVvrJe80YeWbKPLXlQFCumbahFwtUVfUo56HnFkKF3c1TpEvvmRjFZffYSPElqzZtvn8mK9-84zrfEF2d94GmG_LpIom0vYVt7kWDqPF7RuksMEsdONE1_aEk7ug3z-nrdJv_QuBqiMOO-5n9QZUHgkwlmplXrolsBmRgQxHEQiy_4teD9tkBXV-65ofBGoCIzXPCkoo-UPysKQNVYZfwtrwMkC6OJl4HiuzKxRXcNXVHdIa4WmQFXwS3tt84klOTv2t-rEZUCn27sB725PTKXr9WPqbl5KW-fA1JV34nfoqg0zqZ19k2BwJyJs-1WQcEzeaVJpuMzZBbyvRovxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=vSPbDz1BNOEBS6uz5vUHhU6B0nB7pxKDI7NLoGW25XSPrU_yqouU4uqP5imv0A55NxmUFYu1pfbZckdZEn9Z6iifqUna6OQHDr2VunbYp1PPsE-K62qFswVteaCJogZ4-p8HCOwi7OluzozoIm1E1Vd05fWgjzHlGJQNDTvk2DJiUIZMIgrgc04jVoAIAlg7zWZJgfcHgMIZVFyOWIUn8qFgYhqrC5jeOGhOrDZy1hqmKVKx-NX8IXlNvTJ5iROfbQF31OyFo_fT2-jEFk0bjGif_rd1kBxXzDYq2Xf6ZlRjT5lixHe1AXIA1sQBuPgWHOmI01tQwV0Unbwxj75ZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=vSPbDz1BNOEBS6uz5vUHhU6B0nB7pxKDI7NLoGW25XSPrU_yqouU4uqP5imv0A55NxmUFYu1pfbZckdZEn9Z6iifqUna6OQHDr2VunbYp1PPsE-K62qFswVteaCJogZ4-p8HCOwi7OluzozoIm1E1Vd05fWgjzHlGJQNDTvk2DJiUIZMIgrgc04jVoAIAlg7zWZJgfcHgMIZVFyOWIUn8qFgYhqrC5jeOGhOrDZy1hqmKVKx-NX8IXlNvTJ5iROfbQF31OyFo_fT2-jEFk0bjGif_rd1kBxXzDYq2Xf6ZlRjT5lixHe1AXIA1sQBuPgWHOmI01tQwV0Unbwxj75ZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=eLZT7lxz0wPtfVwXWo_LqcNFTidJYgkmEyeav1zgglEXPxxmkZfwDlLfclFyZqXs-JRAeIV8N7KLnEQkQ2kFzOYlFxHehDSk0-tOk9BlM6qNqLY7WDuofmErEjPUN0VA_uawQbt2Zq_ccXRNlMCRDUGRMcmqI_cVPmHaPYz7suoArPnGpRsJ3Y8Wkmod5E0t9gPpWUYX1b7yC8ifxVhgJRYnOLwnlATt82nvlpH0AFZm8MMLow9OBIW3bugTLFGL3r5I-YJmcrW5SZkHK1gzMLaijOluepW33yBWsYy7DQzx0FLCavPRVp4KcVH1yXV1R2cFFjgnu5WZpArzs66Spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=eLZT7lxz0wPtfVwXWo_LqcNFTidJYgkmEyeav1zgglEXPxxmkZfwDlLfclFyZqXs-JRAeIV8N7KLnEQkQ2kFzOYlFxHehDSk0-tOk9BlM6qNqLY7WDuofmErEjPUN0VA_uawQbt2Zq_ccXRNlMCRDUGRMcmqI_cVPmHaPYz7suoArPnGpRsJ3Y8Wkmod5E0t9gPpWUYX1b7yC8ifxVhgJRYnOLwnlATt82nvlpH0AFZm8MMLow9OBIW3bugTLFGL3r5I-YJmcrW5SZkHK1gzMLaijOluepW33yBWsYy7DQzx0FLCavPRVp4KcVH1yXV1R2cFFjgnu5WZpArzs66Spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhymef75dHJeZLgKwxamhJ7EfXSV1MA1Cgz-R_9UxO4wwhEJXdZhuuFmSMk2HrOLjHq0vYt1_2gYgHcpkh3b0sbv14WCe-uLKhV5kzcWgc4UtahOv47om5AM1XMmYLCHEJzogdCDDIozk1MwVKo77houIjLturBP8N9-VqI_gySQNvFl9zaOfjWJhiie4bkLPJRFq2NnC5l-BgMf9avcLSf6HqjjxjJ5VNCPc7jIkB2upSB6gzjgGtFHan8RvlTzldOpBXNHnyD27y-fDy0AD1vgpBwEHBk1SoIMhj0qeoGYlw8B9I4giCH2_A1Is5Gfi4wxpYQ4JorQ3TyOA28ePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
